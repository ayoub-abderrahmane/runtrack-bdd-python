mysql> INSERT INTO etage (nom ,numero ,superficie)
    -> VALUES
    -> ('RDC' ,0 ,500),
    -> ('R+1' ,1 ,500);


mysql> INSERT INTO salle (nom ,id_etage ,capacite)
    -> VALUES
    -> ('Lounge' ,1 ,100),  
    -> ('Studio son' , 1 ,5), 
    -> ('Broadcasting' ,2 ,50), 
    -> ('Bocal Peda' ,2 ,4),  
    -> ('Coworking' ,2 ,80), 
    -> ('Studio Video' ,2 ,5); 

# Ajout des informations demandée dans les tables