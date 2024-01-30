mysql> CREATE TABLE etage(    
    -> id int auto_increment,
    -> nom varchar(255),
    -> numero int,
    -> superficie int,
    -> primary key (id)
    -> );

mysql> CREATE TABLE salle(
    -> id int auto_increment,
    -> nom varchar(255),      
    -> id_etage int,
    -> capacite int,
    -> primary key (id)       
    -> );

# Creation des tables avec les collones demandée