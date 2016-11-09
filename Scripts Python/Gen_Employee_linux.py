#!/usr/bin/python
#
# coding: utf8 
#
# Generate employes file                                                                                                                 
# File will be of the format :                                                                                                         
# first_name | last_name | IP                                                                                            
#                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                      
import random                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                 
def generate_employe(size, name, first, second):      

    	with open("employe.txt", "a") as fich:
    
    		employes = names(size)

		for name, numero in employes.iteritems():
			fich.write(unicode(name + " | " + random_patronyme() + " | " + random_ip(first, second))+ "\n")
	fich.close()
                                                                                                                                      
def WeightedPick(d):                                                                
    r = random.uniform(0, sum(d.itervalues()))  
    s = 0.0                 
    for k, w in d.iteritems():           
        s += w                               
        if r < s: return k                     
    return k                                                     
                                                                                                                                                                                                                                                         
def names(size):         
    names = {'Adolphe':1.72, 'Adrien':6.31, 'Adrienne':2.01, 'Alain':20.36, 'Albertine':4.08,'Alexandrie':5.54,'Alphonse':8.16,'Amaury':6.75,
'Ambre':3.76,'Ambroise':1.59, 'Anatole':5.22,'Annette':1.37,'Anselme':1.08,'Antoine':46.70,'Antoinette':9.37,'Apollinaire':4.14, 'Armand':30.71,'Arnaud':9.24,'Aude':6.31,'Auguste':20.36,'Augustin':5.86, 'Aurore':11.02,'Baptiste':4.81,'Basile':1.02,'Bastien':2.29,
'Bernadette':1.15,'Berthe':6.69,'Blaise':2.17,'Camille':4.87,'Carole':5.93, 'Cerise':2.45, 'Charlot':2.96,'Christophe':13.86,'Claire':49.67,'Clarisse':7.93,'Claudine':4.17,'Colette':3.79,
'Colombe':3.89,'Cyrille':1.15,'Damien':4.01, 'Delphine':2.84,'Didier':1.66,'Dominique':7.30,
'Edmond':3.47,'Edouard':13.89,'Elise':2.36,'Elodie':4.84,'Emile':12.14,'Etienne':10.58, 'Eustache':2.01,'Fabienne':2.07, 'Fernand':7.58,'Fernande':1.31,'Fiacre':2.23,'Fifi':3.66,'Flavie':2.45,'Franck':11.82,'Gaspard':2.23,'Gaston':9.37,'Gautier':2.71,
'Georges':35.90,'Georgette':1.75,'Germain':16.31,'Germaine':5.32,'Gervais':1.98,'Gilberte':5.48,'Gilles':8.76,'Guillaume':15.32,'Gustave':6.31,
'Henri':119.43,'Henriette':1.50,'Hercule':2.61,'Hilaire':5.13,'Hortense':2.39,'Ignace':1.37,'Jacques':81.97,'Jeanne':15.13,'Jeannette':4.91,'Jeannot':7.61,
'Jolie':28.77,'Josette':14.72,'Jourdain':3.12,'Julien':134.02,'Julienne':2.96,'Juliette':16.25,'Juste':167.03,'Laure':6.02,'Laurent':28.80,'Lazare':4.43,
'Loup':17.01,'Luc':20.80,'Luce':1.88,'Lucie':18.80,'Lucien':25.49,'Lucienne':7.07,'Lucille':6.63,'Manon':2.68,'Marc':19.37,'Marceline':4.36,'Marcelle':1.31,
'Marguerite':28.29,'Marie':122.52,'Mariette':4.08,'Marine':40.49,'Martine':2.68,'Mathieu':3.35,'Mathilde':4.71,'Maxime':3.92,'Maximilien':3.12,
'Micheline':3.50,'Mignon':4.71,'Mireille':3.03,'Modeste':22.71,'Monique':5.93,'Nadine':21.19,'Narcisse':1.18,'Nathalie':10.42,'Nazaire':2.01,'Nicolas':51.04,
'Odette':4.59,'Odile':3.60,'Olivier':123.64,'Olympe':1.56,'Pascal':34.34,'Paule':25.87,'Paulette':2.29,'Philibert':1.75,'Philippe':66.23,'Pierre':177.41,
'Placide':3.38,'Pons':1.24,'Raoul':5.77,'Raymonde':1.15,'Reine':36.80,'Renaud':1.85,'Reynaud':3.06,'Roch':1.18,'Rochelle':2.80,'Rodolphe':1.40,
'Romain':15.32,'Romaine':12.97,'Rosette':8.09,'Sacha':1.53,'Serge':10.29,'Solange':28.96,'Suzanne':27.14,'Sylvain':1.31,'Sylvestre':2.77,'Sylviane':1.88,
'Sylvie':17.33,'Thibault':2.04,'Thierry':5.35,'Toussaint':2.17,'Urbain':17.14,'Victoire':63.40,'Vienne':30.61,'Violette':8.25,'Virginie':35.71,'Vivienne':1.47,
'Yves':3.41,'Yvette':2.20, 'Yvonne':12.30 }                      
    results = {}                  
    for x in xrange(size):                                                             
        p = unicode(WeightedPick(names))   
        results[p] = results.get(p, 0) + 1 
    return results                          

def random_patronyme():
    	with open("Patronymes.txt", "r") as f:
   		x = random.randrange(0, 400)
		lines = f.readlines()
    		patronyme = lines[x]
		print(patronyme)
		f.close()
   	return patronyme
        
    
def random_ip(first, second):                                                           
                                                                                                                                      
    	ip = ".".join([unicode(first),unicode(second),                                               
   	unicode(random.randrange(1,256)),unicode(random.randrange(1,256))])                        
    
	return ip
                                                                                                                                                                                                                                                     

def generate_first():
    not_valid = [10,127,169,172,192]                                                
    first = random.randrange(1,256) 
                                                           
    while first in not_valid:                                                         
        first = random.randrange(1,256)

    return first

def main():                                                                           
    first = generate_first()
    seconds = [11, 16, 40, 56]
    name_service = ["Compta", "Informatique", "R&D", "RH"]
    
    for i in range(0,4):
        size_service = random.randrange(500, 1000)
        generate_employe(size_service, name_service[i], first, seconds[i])                 
                                                            
                                                                                                                                      
if __name__ == "__main__":                     
    main()                                                                 
            
