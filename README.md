# Grupo6-TheWitcher

<div align="center"><img src= "https://i.imgur.com/9MHMuCL.png" height="230" width="auto"/></div>

## Alunos

|Nome|Matrícula|Github|
|--|--|--|
|Amanda Emilly Muniz de Menezes|150116136|[@AmandaMuniz](https://github.com/AmandaMuniz)|
|Caio César de Almeida Beleza|150078692|[@Caiocbeleza](https://github.com/Caiocbeleza)|
|Francisco Heronildo Sousa Santos|160006210| [@FranciscoHeronildo](https://github.com/FranciscoHeronildo)|
|Ricardo de Castro Loureiro|200043111|[@castroricardo1](https://github.com/castroricardo1)|
|Paulo Batista|180054554|[@higton](https://github.com/higton)|

## Sobre

<div align="center"><img src= "https://i.imgur.com/FqupKBz.png" height="100" width="auto"/></div>

Este repositório é destinado ao apredizado sobre o conteúdo ministrado na disciplina de Sistemas de Bancos de dados 1 na da Universidade de Brasília - Gama, durante o período 2021/2.

## Como Rodar o Jogo

<div align="center"><img src= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia1.tenor.com%2Fimages%2Fe4d1876e4e989151dd88705e71172071%2Ftenor.gif%3Fitemid%3D18933836&f=1&nofb=1" height="" width="auto"/></div>


### Clonar o Repositório
```
git clone https://github.com/SBD1/Grupo6-TheWitcher
```

### Abrir a pasta onde foi clonado

```
$ cd Grupo6-TheWitcher
```

### Abrir a pasta Game
```
$ cd Game
```

### Adicionar as dependências

```
$ pip install psycopg2
```
#### ou

```
$ pip3 install psycopg2
```

### Crie um novo database no seu postgresql com o nome "thewitcher"

#### Abrir o arquivo conn.py e colocar o usuário de senha do seu postgresql em conexão com o localhost em `user="usuário"` e `password="senha"`.*


#### * Se não tiver um usuário no postgres:

`https://www.postgresql.org/docs/8.0/sql-createuser.html`

*Para facilitar aqui, utilize "postgres" tanto para o usuário quanto para a senha

#### Para dar acesso do novo usuário ao banco do jogo

```
$ su - postgres
```

```
postgres=# grant all privileges on database thewitcher to user_name;
```  


### Ainda na pasta Game, para rodar o jogo via terminal:

```
$ python main.py
```

### ou

```
$ python3 main.py
```
