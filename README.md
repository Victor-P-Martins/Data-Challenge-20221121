# Data-Challenge-20221121
This is a challenge by Coodesh

Desafio de dados focado em fazer uma análise exploratória de duas bases de dados disponibilizadas em formato csv.

- Lista de filmes da Netflix: netflix_titles.csv

- Lista de filmes da Amazon Prime: amazon_prime_titles.csv

## Descrição dos dados

show_id - Unique ID for every Movie / Tv Show

type - Identifier - A Movie or TV Show

title - Title of the Movie / Tv Show

director - Director of the Movie

cast - Actors involved in the movie / show

country - Country where the movie / show was 
produced

data_added - Date it was added on Netflix or 
Amazon Prime 

release_year - Actual Release year of the move / show

rating - TV Rating of the movie / show 

duration - Total Duration - in minutes or number of seasons

## Filtro de dados

Nessa etapa você poderá exibir os dados por meio de uma REST API ou no Colab, Jupyter Notebook ou similar. Exiba as seguintes informações:

1 - Top 10 atores/atrizes considerando todos os dados;

2 - Top 5 países produtores de conteúdos considerando todos os dados e comparando as duas plataformas;

3 - Mês no qual há mais adições de filmes na plataforma Netflix;

4 - Quantidade de filmes listados como comédia.

5 - Lista de todos os gêneros de filmes.

6 - A frequência de "TV Show" de todos os dados e comparativamente em relação as duas plataformas

7 - A frequência de "Movies" de todos os dados e comparativamente em relação as duas plataformas

## Tecnologias utilizadas

Para desenvolver esse desafio foram utilizadas as seguintes tecnologias:
    - Python -> Linguagem de programação para desenvolvimento das análises tratamentos e API.
    - Docker -> Sistema de containers para execução da aplicação.
    - Git/Github -> Sistema de versionamento 

Na linguagem python foram utilizadas as seguintes bibliotecas, frameworks e ferramentas:

    - Pandas -> Biblioteca de análise e transformação de dados tabulares para python. Foi escolhida por ser extremamente simples, rápida e versátil, principalmente para volume de dados pequeno como o do desafio proposto.

    - FastApi -> Biblioteca de python para criação de APIs. Extremamente poderosa e simples de utilizar.

    - Jupyter Notebook -> Ambiente para execução de códigos em forma de blocos facilitando a visualização de dados em projetos análicos.

## Etapas do processo

### Transformação e tratamento de dados

1 - Junção das duas bases de dados separadas (Netflix + Prime)

2 - Tratamento das colunas Country, Cast e Date Added onde os valores não estavam normalizados. Cada uma dessas colunas continha múltiplas informações separadas por vírgulas, porém, na mesma coluna. Foi feito o tratamento de quebra das informações por delimitador e separados em outras colunas ou criando mais linhas dependendo do caso.

3 - Remoção de valores vazios em determinadas colunas.

## Análise de dados

Os resultados podem ser vistos no diretório notebooks no arquivo analysis.ipynb

## Extra

Para consumo de alguns dos dados fiz uma api utilizando a biblioteca de python FastApi

Métodos disponíveis:

    - /top10actors -> Retorna o top 10 atores com mais produções por empresa.
    - /top5countrys -> Retorna os top 5 países produtores de filmes. 
    - /listgenres -> Retorna a lista completa de gêneros de filmes.
    - /docs -> Documentação da api


## Executando a API

Para executar a api será preciso ter o docker e o docker-compose instalados na máquina.
Para rodar o sistema será preciso fazer um clone do repositório para a máquina local. Iniciar o terminal no repositório clonado
e executar o comando: 

docker-compose up -d

Este comando inicializará o sistema no localhost na porta 8000




