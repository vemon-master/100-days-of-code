import random
list_name=input("enter a list of names sepaerated by a , and space\n")
names=list_name.split(", ")#its for splitting the entities in a list 

len(names) #collects the number of lists entered 
payee= random.randint(0, len(names)-1)
payer=names[payee]#to reference the number chosen by the rundom module
print (f"its {payer} who will pay the bill")