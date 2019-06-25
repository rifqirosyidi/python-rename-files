import os
def rename_file():
	# Get file names to be renamed from folder
	file_list = os.listdir("/home/rief/Documents/Coding - Python/Renaming Code/img")
	original_path = os.getcwd()

	# Change directory to the image Location
	os.chdir("{}/img".format(os.getcwd()))

	# For each file, rename filename
	for file_name in file_list:
		new_file_name = file_name.translate(str.maketrans("", "", "1234567890"))
		os.rename(file_name, new_file_name)

	os.chdir(original_path)

rename_file()