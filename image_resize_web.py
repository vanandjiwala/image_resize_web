import sys
import Utils.imageUtils as imgUtils
import Utils.pathUtils as pathUtils

#list of all available argument options
available_flags = ["-h","-d","-i","-o"]
#list of supported file formats
supported_file_formats = ["jpeg","jpg"]


print(sys.argv)

#if required argument is not passed then raise an exception
if(not(("-h" in sys.argv) or ("-i" in sys.argv))):
    raise Exception('There should be at least 1 valid argument passed. -h or -i')

#process with -h option and exit the program after printing help information
if "-h" in sys.argv:
    print("-h : HELP  print all available arguments for the script")
    print("-d : DPI  SET dpi for the output image")
    print("-o : Set output directory path for the resized images")
    print("-i : Set input directory path for images that needs to be resized")
    exit()

#process with -i flag
if "-i" in sys.argv:
    #Obtain the index of -i
    input_index = sys.argv.index("-i")

    #if value is not provided for -i option then give proper error message to user and exit the script
    try:
        input_folder_path = sys.argv[input_index + 1]
    except IndexError:
        print("There is something wrong with the argument, please refer to the usage section of documentation")
        exit()


    input_exists = pathUtils.validate_dir_path(input_folder_path)
    #print("value of input_exists is {}".format(input_exists));

    #raise eception if input directory does not exist.
    if not(input_exists):
        raise Exception("Input directory {} used is not a valid directory".format(input_folder_path))

    num_of_files = pathUtils.get_number_of_images(input_folder_path,supported_file_formats)

    if not(num_of_files > 0):
        raise Exception("Input directory {} used does not contain any supported file. Please refer to the documentation for supported file formats".format(input_folder_path))

    # TODO: Handle case with -o option
    if "-o" in sys.argv:
        print("output directory given")
    else:
        output_path = pathUtils.create_directory(pathUtils.get_project_root_dir(), pathUtils.generate_unique_name())
        imgUtils.downscale_images(pathUtils.get_path_of_images(input_folder_path,supported_file_formats),output_path)


    #pathUtils.get_path_of_images(input_folder_path,supported_file_formats)