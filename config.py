import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'postgres'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'admin'),
    'port': os.getenv('DB_PORT', '5432')
}

# Schema do banco
SCHEMA = 'dsp_sauter'

# Caminhos
DATA_PATH = 'data/twitchdata.csv'