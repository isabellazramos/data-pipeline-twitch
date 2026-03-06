#!/usr/bin/env python
"""
Script de teste para validar a estrutura do projeto
"""
import os
import sys
from pathlib import Path

def test_structure():
    """Testa se a estrutura do projeto está correta"""
    print("=" * 60)
    print("🧪 TESTANDO ESTRUTURA DO PROJETO")
    print("=" * 60)
    
    base_path = Path(".")
    
    # Arquivos esperados na raiz
    root_files = {
        "config.py": "Arquivo de configuração",
        "README.md": "Documentação do projeto",
        "requirements.txt": "Dependências Python",
        ".env.example": "Exemplo de variáveis de ambiente",
        ".gitignore": "Arquivo git ignore"
    }
    
    print("\n✓ Verificando arquivos raiz:")
    all_exist = True
    for file, desc in root_files.items():
        exists = (base_path / file).exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {file:<20} - {desc}")
        all_exist = all_exist and exists
    
    # Estrutura de pastas
    print("\n✓ Verificando pastas:")
    folders = {
        "bronze": {
            "insert_data.ipynb": "Notebook de coleta",
            "script.sql": "Script SQL de criação"
        },
        "silver": {
            "move_table.py": "Script de transformação ETL"
        },
        "gold": {
            "analise_twitchdata.ipynb": "Notebook de análise"
        },
        "data": {}
    }
    
    for folder, files in folders.items():
        folder_path = base_path / folder
        exists = folder_path.exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {folder}/")
        
        for file, desc in files.items():
            file_path = folder_path / file
            exists = file_path.exists()
            status = "   ✓" if exists else "   ✗"
            print(f"  {status} {file:<30} - {desc}")
    
    # Testar imports
    print("\n✓ Verificando imports:")
    try:
        import config
        print("  ✓ config.py pode ser importado")
    except ImportError as e:
        print(f"  ✗ Erro ao importar config.py: {e}")
        all_exist = False
    
    # Verificar conteúdo de arquivos importantes
    print("\n✓ Verificando conteúdo dos arquivos:")
    
    # Requirements.txt
    try:
        with open("requirements.txt") as f:
            reqs = f.read()
            has_pandas = "pandas" in reqs
            has_psycopg = "psycopg2" in reqs
            has_airflow = "airflow" in reqs
            status = "✓" if (has_pandas and has_psycopg and has_airflow) else "✗"
            print(f"  {status} requirements.txt contém dependências essenciais")
    except Exception as e:
        print(f"  ✗ Erro ao ler requirements.txt: {e}")
    
    # Config.py
    try:
        with open("config.py") as f:
            config_content = f.read()
            has_db_config = "DB_CONFIG" in config_content
            has_schema = "SCHEMA" in config_content
            status = "✓" if (has_db_config and has_schema) else "✗"
            print(f"  {status} config.py contém configurações esperadas")
    except Exception as e:
        print(f"  ✗ Erro ao ler config.py: {e}")
    
    # .env.example
    try:
        with open(".env.example") as f:
            env_content = f.read()
            has_db_host = "DB_HOST" in env_content
            has_db_user = "DB_USER" in env_content
            status = "✓" if (has_db_host and has_db_user) else "✗"
            print(f"  {status} .env.example contém variáveis de ambiente")
    except Exception as e:
        print(f"  ✗ Erro ao ler .env.example: {e}")
    
    print("\n" + "=" * 60)
    print("✅ TESTES CONCLUÍDOS COM SUCESSO!" if all_exist else "⚠️  ALGUNS TESTES FALHARAM")
    print("=" * 60)

if __name__ == "__main__":
    test_structure()
