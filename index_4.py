# Banco de Dados:

  # Um banco de dados relacional é um tipo de banco de dados que organiza e armazena informações em tabelas que têm relações entre si. Cada tabela é composta por colunas e linhas, onde cada coluna representa um atributo específico e cada linha representa um registro de dados. Os bancos de dados relacionais seguem o modelo relacional, que é baseado na teoria matemática das relações. Esse modelo utiliza chaves primárias e chaves estrangeiras para estabelecer conexões entre diferentes tabelas. Aqui estão alguns 
  # conceitos-chave de bancos de dados relacionais:
 
  # 1. **Tabelas**: São usadas para armazenar os dados. Cada tabela possui um nome único e é composta por colunas e linhas.2. **Colunas**: Representam os atributos dos dados a serem armazenados. Cada coluna possui um tipo de dado específico, como texto, números, datas, etc.

  # 3. **Linhas**: Também chamadas de registros, são instâncias individuais de dados que são armazenadas nas tabelas.

  # 4. **Chave Primária**: É um campo ou conjunto de campos que identifica exclusivamente cada registro em uma tabela. Garante a unicidade dos registros.

  # 5. **Chave Estrangeira**: É um campo que estabelece uma relação entre duas tabelas. Geralmente, a chave estrangeira em uma tabela é uma referência à chave primária em outra tabela.

  # 6. **Normalização**: É o processo de organizar os dados em várias tabelas para eliminar a redundância e manter a integridade dos dados.

  # 7. **SQL (Structured Query Language)**: É a linguagem usada para manipular e consultar bancos de dados relacionais. Comandos SQL permitem criar, modificar, inserir e recuperar dados das tabelas.

  # Exemplos de sistemas de gerenciamento de banco de dados relacionais incluem MySQL, PostgreSQL, Microsoft SQL Server e Oracle Database.

  # Esses bancos de dados são amplamente utilizados em várias aplicações, desde sistemas de gerenciamento de conteúdo até sistemas de finanças, devido à sua capacidade de estruturar e relacionar os dados de forma eficiente.



## Indtrodução a Biblioteca Pandas:
  
  ## Pandas é um pacote em Python que fornece estruturas de dados projetados para facilitar o trabalho com dados estruturados (tabelas) e de séries temporais.

## Pandas possui duas estruturas de dados que são as principais para a análise / manipulação de dados: Series e o DataFrame.

# ex: 01

import pandas as pd

pd.Series(data=5)

lista_nomes = 'Kayke Luiza Marcos Pedro Renata'.split()

pd.Series(lista_nomes) # Criar uma series com o valor a lista_nomes = 'Kayke Luiza Marcos Pedro Renata' .split()

dados = {
    'nome_1': 'Kayke',
    'nome_2': 'Luiza',
    'nome_3': 'Marcos',
    'nome_4': 'Pedro',
    'nome_5': 'Renata',
}

pd.Series(dados) # Criar uma series com um dicionário