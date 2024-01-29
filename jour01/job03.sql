mysql> CREATE TABLE etudiant (
    -> id int not null auto_increment,
    -> nom varchar(255) not null,
    -> prenom varchar(25) not null,
    -> age int not null,
    -> email varchar (255) not null,
    -> primary key (id)
    -> );

mysql> SHOW TABLES;