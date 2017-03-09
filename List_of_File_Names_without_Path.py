#List_of_File_Names.py

import os
from fnmatch import fnmatch

my_path = '[pathName]'
pattern_list = ['*.py', '*.msg', '*.pdf' ,'*.htm', '*.docx' , '*.xls', '*.tif', '*.xlsx', '*.doc' , '*.oft'
                , '*.xml', '*.thmx']
my_text_file_path = '[pathName']
duplicate_text_file_path = '[pathName]'
#_____________________________________________________________________________________________________________
def create_list_of_file_names(path, file_extensions):
	"""Creates list of all the files in a folder and the subfolders"""
	list_of_file_names = []
	for path, subdirs, files in os.walk(path):
		for name in files:
			for extension in file_extensions:
				if fnmatch(name, extension):
					list_of_file_names.append(name)
	return list_of_file_names
	
	
def alphabetize(list_of_file_names):
	"""sorts list into alpabetical order"""
	list_of_file_names.sort()
	return list_of_file_names


def create_text_file(text_file_path, list_of_file_names):
	"""creates the text file that contains the names of the files"""
	text_file = text_file_path
	with open(text_file, 'w') as f:
		for i in list_of_file_names:
			f.write(i + '\n')
		f.close()	
	return text_file
	
def count_number_of_duplicates(my_list):

	count_duplicate = 0
	duplicate_list =[]
	for i in range(len(my_list)):
		current_position = i 
		if i > 0:
			previous_position = current_position - 1
			if my_list[current_position] == my_list[previous_position]:
				count_duplicate = count_duplicate + 1
				duplicate_list.append(my_list[i])
			else:
				pass
		else:
			pass
	return count_duplicate
	
	
def file_list_duplicates(my_list):

	count_duplicate = 0
	duplicate_list =[]
	for i in range(len(my_list)):
		current_position = i 
		if i > 0:
			previous_position = current_position - 1
			if my_list[current_position] == my_list[previous_position]:
				count_duplicate = count_duplicate + 1
				duplicate_list.append(my_list[i])
			else:
				pass
		else:
			pass
	return duplicate_list
		

	

	

#______________________________________________________________________________________________________________
#Variables to input: path, file_extensions, text_file_path

def master_plan(path, file_extensions, text_file_path, duplicate_path):
	list_of_file_names = create_list_of_file_names(path, file_extensions)
	list_of_file_names = alphabetize(list_of_file_names)
	
	text_file = create_text_file(text_file_path, list_of_file_names)
	
	length_of_list = len(list_of_file_names)
	c_dup = count_number_of_duplicates(list_of_file_names)
	f_dup_list = file_list_duplicates(list_of_file_names)
	
	save_f_dup = create_text_file(duplicate_path, f_dup_list)
	
	
	
	
	print 'Total duplicates in folder is %s' % c_dup
	print 'Total files in Folder is %s' % length_of_list
	
	
	
master_plan(my_path, pattern_list, my_text_file_path, duplicate_text_file_path)

	


















