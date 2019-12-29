import os
import glob
import uuid

#validate if directory exists or does not exist.
#returns true if directory exists
#returns false if diretory does not exist
def validate_dir_path(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        return False

#function to get the number of images in the input folder which need to be resized
#function will check for all the supported file formats and count the total number of images
def get_number_of_images(dir_path,supported_format_list):
    image_count = 0
    for format in supported_format_list:
        search_pattern = os.path.join(dir_path, "*."+format)
        image_count += len(glob.glob(search_pattern))
    return image_count

#Get full path of images having supported file format
def get_path_of_images(dir_path,supported_format_list):
    image_paths = []
    for format in supported_format_list:
        search_pattern = os.path.join(dir_path, "*."+format)
        searched_result = glob.glob(search_pattern)
        if len(searched_result) > 0:
            image_paths.extend(searched_result)
    print(image_paths)
    return image_paths

#get root directory for project
def get_project_root_dir():
    return os.getcwd()

#create a directory if already not present
def create_directory(dir_root_path,dir_name):
    full_path = os.path.join(dir_root_path,dir_name)
    print("Images will be store at {} ".format(full_path))
    os.makedirs(full_path,exist_ok=True)
    return full_path

#Generate unique name for the folder
def generate_unique_name():
    unique_name = str(uuid.uuid4())
    return unique_name