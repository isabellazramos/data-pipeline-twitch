
# Data Pipeline - Análise de Dados do Twitch

<p align="center">
  <img alt="Principal linguagem do projeto" src="https://img.shields.io/github/languages/top/isabellazramos/data-pipeline?color=56BEB8">
  <img alt="Quantidade de linguagens utilizadas" src="https://img.shields.io/github/languages/count/isabellazramos/data-pipeline?color=56BEB8">
  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/isabellazramos/data-pipeline?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-pré-requisitos">Pré-requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-começando">Começando</a> &#xa0; | &#xa0;
  <a href="#file_folder-estrutura-do-projeto">Estrutura</a> &#xa0; | &#xa0;
  <a href="https://github.com/isabellazramos" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

Este projeto implementa um pipeline de dados completo para coleta, processamento e análise de dados dos principais canais da Twitch. Os dados são obtidos do Kaggle e incluem métricas como tempo de visualização, seguidores, visualizações e outras informações relevantes sobre streamers.

O pipeline é dividido em três etapas principais seguindo a arquitetura de medalhão:
- **Bronze**: Coleta e ingestão dos dados brutos
- **Silver**: Limpeza, transformação e processamento dos dados
- **Gold**: Análise e geração de insights finais

## :rocket: Tecnologias ##

As seguintes ferramentas foram usadas na construção do projeto:

- **Python**: Linguagem principal para scripts e notebooks
- **Jupyter Notebook**: Para análise de dados e visualizações
- **PostgreSQL**: Banco de dados para armazenamento dos dados
- **Apache Airflow**: Orquestração do pipeline de dados
- **Pandas**: Manipulação e análise de dados
- **Psycopg2**: Conector PostgreSQL para Python

## :white_check_mark: Pré-requisitos ##

Antes de começar, você precisa ter instalado em sua máquina:

- [Git](https://git-scm.com)
- [Python](https://www.python.org/) (versão 3.8 ou superior)
- [PostgreSQL](https://www.postgresql.org/)
- [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

## :checkered_flag: Começando ##

```bash
# Clone este repositório
$ git clone https://github.com/isabellazramos/data-pipeline

# Entre na pasta do projeto
$ cd data-pipeline

# Instale as dependências Python
$ pip install -r requirements.txt

# Configure as variáveis de ambiente
# Copie o arquivo .env.example para .env e preencha com suas credenciais
$ cp .env.example .env

# Configure o banco de dados PostgreSQL
# Execute o script SQL para criar o schema e tabela
$ psql -U postgres -f "bronze/script.sql"

# Execute o notebook de inserção de dados
# Abra o Jupyter e execute: bronze/insert_data.ipynb

# Configure e execute o Airflow para processamento
# Execute o script de preparação: silver/move_table.py

# Para análise, abra o notebook: gold/analise_twitchdata.ipynb
```

## :file_folder: Estrutura do Projeto ##

```
data-pipeline/
├── README.md
├── requirements.txt          # Dependências Python
├── config.py                 # Configurações e credenciais
├── .env.example             # Exemplo de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── bronze/
│   ├── insert_data.ipynb    # Notebook para inserção de dados no PostgreSQL
│   └── script.sql           # Script SQL para criação do schema e tabela
├── silver/
│   └── move_table.py        # Script Airflow para processamento dos dados
├── gold/
│   └── analise_twitchdata.ipynb  # Análise exploratória dos dados do Twitch
└── data/
    └── twitchdata.csv       # Dataset original do Kaggle
```

## 📊 Dataset ##

O dataset utilizado contém informações sobre os principais canais da Twitch, incluindo:

- Nome do canal
- Tempo de visualização (minutos)
- Tempo de transmissão (minutos)
- Pico de visualizações
- Média de visualizações
- Seguidores atuais e ganhos
- Visualizações ganhas
- Status de parceria
- Conteúdo maduro
- Idioma do canal

**Fonte**: [Kaggle - Twitch Data](https://www.kaggle.com/aayushmishra1512/twitchdata)

## 🔒 Segurança e Boas Práticas

Este projeto implementa as seguintes boas práticas:

- **Variáveis de ambiente**: Credenciais armazenadas em arquivo `.env` (não versionado)
- **Tratamento de erros**: Try-except blocks em todas as operações críticas
- **Logging**: Logs estruturados para monitoramento e debugging
- **Idempotência**: Operações que podem ser executadas múltiplas vezes sem efeitos colaterais
- **Arquitetura em camadas**: Separação clara entre Bronze (bruto), Silver (processado) e Gold (análise)
- **Validação de dados**: Verificações de integridade e limpeza de dados inconsistentes

---

Feito com :heart: por <a href="https://github.com/isabellazramos" target="_blank">Isabella M. Ramos</a>

&#xa0;

<a href="#top">Voltar para o topo</a>
