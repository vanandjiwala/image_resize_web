from PIL import Image
import os

#returns true if landscape and returns false if portrait  mode
#determined by the width and height of the image
def get_image_orientation(image):
    (width,height) = image.size
    if (width > height):
        return True
    else:
        return False

#Downscales and stores image in output folder
def downscale_images(input_image_path_list,output_dir_path):
    print("downscale")
    for image_path in input_image_path_list:
        image = Image.open(image_path)
        output_file_name = os.path.basename(image_path)
        if(get_image_orientation(image)):
            desired_size = (1920,1080)
            resized_image = image.resize(desired_size,Image.ANTIALIAS)
            resized_image.save(os.path.join(output_dir_path,output_file_name),"JPEG")
        else:
            desired_size = (1080, 1920)
            resized_image = image.resize(desired_size, Image.ANTIALIAS)
            resized_image.save(os.path.join(output_dir_path, output_file_name), "JPEG")
