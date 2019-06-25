import os
def rename_file():
	# Get file names from folder
	file_list = os.listdir("/home/rief/Documents/Coding - Python/Renaming Code/img")
	print(file_list)


	# For each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))


rename_file()