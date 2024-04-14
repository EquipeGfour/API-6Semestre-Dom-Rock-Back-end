# API-6Semestre-Dom-Rock-Back-end


## Requisitos para executar o projeto
Para que consiga rodar o projeto é necessario instalar estás tecnologias abaixo

- Python
- MySql

## Execução do projeto
### Windows

#### 1. Criação do ambiente virtual.
Abra um terminal dentro da pasta do projeto e execute o comando abaixo.
```bash
python -m venv .venv
```

#### 2. Ativando o ambiente virtual.
Para ativar o ambiente virtual execute o comando abaixo.
```bash
.\.venv\Scripts\activate
```

#### 3. Instalação das dependencias.
Para instalar todas as dependencias do projeto execute o comando abaixo.
```bash
pip install -r requirements.txt
```

#### 4. Arquivo de configurações
Crie um arquivo chamado `config.ini` na raiz do projeto, copie o conteudo do arquivo `config.default.ini` para o arquivo criado e preencha os campos faltantes.


#### 5. Execução do projeto.
```bash
python .\src\main.py
```