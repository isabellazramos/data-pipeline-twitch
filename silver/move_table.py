import os
import sys
sys.path.append('..')  # Para importar config

from datetime import datetime, timedelta
import logging

import psycopg2 as db
import pandas as pd
from config import DB_CONFIG, SCHEMA

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def print_context(ds, **kwargs):
    """Função de contexto para logging"""
    logger.info(f"Executando tarefa em: {ds}")
    return "Contexto definido"

def run_transformation(**context):
    """
    Executa transformação dos dados: limpeza e cópia para tabela silver
    """
    conn = None
    try:
        # Conectar ao banco
        conn = db.connect(**DB_CONFIG)
        logger.info("Conexão com o banco estabelecida.")

        # Query para ler dados da bronze
        source_table = f"{SCHEMA}.twitchdata"
        target_table = f"{SCHEMA}.twitchdata_clean"

        # Criar tabela silver se não existir
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {target_table} (
            id SERIAL PRIMARY KEY,
            channel TEXT,
            watch_time BIGINT,
            stream_time BIGINT,
            peak_viewrs BIGINT,
            average_viewers BIGINT,
            followers BIGINT,
            followers_gained BIGINT,
            views_gained BIGINT,
            partnered BOOLEAN,
            mature BOOLEAN,
            lang TEXT,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        with conn.cursor() as cur:
            cur.execute(create_table_query)
            conn.commit()
            logger.info(f"Tabela {target_table} criada/verificada.")

        # Ler dados da bronze
        df = pd.read_sql(f"SELECT * FROM {source_table}", conn)
        logger.info(f"Lidos {len(df)} registros da tabela bronze.")

        # Transformações básicas (silver layer)
        # Remover duplicatas
        df_clean = df.drop_duplicates(subset=['channel'])
        
        # Tratar valores nulos
        df_clean = df_clean.fillna({
            'watch_time': 0,
            'stream_time': 0,
            'peak_viewrs': 0,
            'average_viewers': 0,
            'followers': 0,
            'followers_gained': 0,
            'views_gained': 0
        })
        
        # Filtrar registros inválidos (exemplo: canais sem nome)
        df_clean = df_clean[df_clean['channel'].notna() & (df_clean['channel'] != '')]
        
        logger.info(f"Após limpeza: {len(df_clean)} registros.")

        # Inserir na tabela silver
        with conn.cursor() as cur:
            # Limpar tabela antes de inserir (para idempotência)
            cur.execute(f"TRUNCATE TABLE {target_table}")
            
            # Inserir dados
            for _, row in df_clean.iterrows():
                insert_query = f"""
                INSERT INTO {target_table} 
                (channel, watch_time, stream_time, peak_viewrs, average_viewers, 
                 followers, followers_gained, views_gained, partnered, mature, lang)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cur.execute(insert_query, tuple(row))
            
            conn.commit()
            logger.info(f"Inseridos {len(df_clean)} registros na tabela silver.")

    except Exception as e:
        logger.error(f"Erro na transformação: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()
            logger.info("Conexão fechada.")

default_args = {
    "owner": "DSP",
    "depends_on_past": False,
    "start_date": datetime(2019,11,26),
    "email": ["sauter_ds@sauter.digital"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG("move_table", default_args = default_args, schedule_interval = "0 22 * * *", catchup = False)

t_set_context = PythonOperator(
    task_id = "t_set_context", 
    provide_context= True, 
    python_callable=print_context, 
    dag = dag)

t_move_table = PythonOperator(
    task_id="moveTable", 
    python_callable=run_transformation, 
    provide_context=True,
    dag=dag)

t_set_context >> t_move_table