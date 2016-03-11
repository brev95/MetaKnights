import csv

global_addresses = []
global_animal_names = []

Global_Address_Class_List = []
Global_Animal_Class_List = []
Global_Relation_Class_List = []

class Address:
	name = ''
	animal_names = []
	def init(self):
		self.data = []
	
class Animal:
	name = ''
	assoc = []
	def init(self):
		self.data = []
	
class Assoc:
	name = ''
	num = 0
	def init(self):
		self.data = []
		
class Relation:
	animal = ''
	address = ''
	def init(self):
		self.data = []

#with open('file_internal_external_noHeader.csv', 'rb') as csvfile:
#with open('file-02_filtered.csv', 'rb') as csvfile:
#with open('file-03_filtered.csv', 'rb') as csvfile:
#with open('file-04_filtered.csv', 'rb') as csvfile:
with open('file-05_filtered.csv', 'rb') as csvfile:
#with open('combined_file.csv', 'rb') as csvfile:
	# Read csv file
	spamreader = csv.reader(csvfile, delimiter=',')
	
	# Variables for animal name and address
	address = ''
	animal_name = ''

	
	# Load global animal names and addresses
	for name in spamreader:
		if name[1] not in global_addresses:
			global_addresses.append(name[1])
			
		if name[0] not in global_animal_names:
			global_animal_names.append(name[0])
	
		relation = Relation()
		relation.animal = name[0]
		relation.address = name[1]
		
		if relation not in Global_Relation_Class_List:
			Global_Relation_Class_List.append(relation)
		
	
	# Sort and print all addresses and animal names
	global_addresses.sort()
	global_animal_names.sort()


	for address_name in global_addresses:
		address = Address()
		address.name = address_name
		Global_Address_Class_List.append(address)
		
		
	for animal_name in global_animal_names:
		animal = Animal()
		animal.name = animal_name
		Global_Animal_Class_List.append(animal)
		
	for address in Global_Address_Class_List:
		address.animal_names = []
		for relation in Global_Relation_Class_List:
			if ((relation.address == address.name) and (relation.animal not in address.animal_names)):
				address.animal_names.append(relation.animal)
				
	for animal in Global_Animal_Class_List:
		animal.assoc = []
		for address in Global_Address_Class_List:
			if len(address.animal_names) < 4: # and len(address.animal_names) < 4:
				if animal.name in address.animal_names:
					for animal_name in address.animal_names:
						used = False
						for association in animal.assoc:
							if animal_name == association.name:
								association.num += 1
								used = True
						if used == False:
							newAssoc = Assoc()
							newAssoc.name = animal_name
							newAssoc.num += 1
							animal.assoc.append(newAssoc)
		
# Print lists		
#	for address in Global_Address_Class_List:
#		print address.name
#		print address.animal_names

#	for animal in Global_Animal_Class_List:
#		print animal.name
		
#	for relation in Global_Relation_Class_List:
#		print relation.animal
#		print relation.address

	for animal in Global_Animal_Class_List:
		if len(animal.assoc) > 1:
			print animal.name
			for association in animal.assoc:
				if association.num > 2:
					print "    " + association.name + " " + str(association.num)
			print '\n'

		
	print "0"	
		
		
		
		

	
	
#def main():

		
#		name_file.write(name[0])
#		name_file.write("\n")
		
		# Print external IPs
#		ext_file.write(name[1])
#		ext_file.write("\n")
	