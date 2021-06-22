# Controle-de-Estoque
 


Controle de estoque desenvolvido em:

1. HTML
2. CSS
3. PYTHON/DJANGO
4. MySQL

Ferramentas utilizadas: 

1. Visual Studio Code 
2. MySql Workbench

Comandos para MySql 

 create database controleEstoque ;
 use controleEstoque; 
 create table cEstoque (
 cod_produto int auto_increment primary key not null,
	nome_pr varchar(50) not null unique,
 	qtde_pr int not null,
 	valor_pr decimal(10,2)
 );

 create table cUser (
 	cod_user int auto_increment primary key not null,
 	nome_user varchar(50) not null unique,
 	email_user varchar(50) not null,
 	senha_user varchar(50) not null,
 	dn_user date not null,
  sexo_user varchar (9) not null,
  end_user varchar(80) not null,
  end_n_user int not null,
	est_user varchar(10) not null
 );
 
 