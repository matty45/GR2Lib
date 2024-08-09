"""This loads a granny file and prints out all of its info."""
from gr2_dll_funcs import granny_get_file_info, granny_get_grn_section_array, granny_read_entire_file
from gr2_format import GrannyFile
from gr2_size_test import check_granny_struct_sizes

def print_file_stats(granny_file : GrannyFile):
    """This prints internal file statistics. """
    section_array = granny_get_grn_section_array(granny_file.contents.header)
    print("Granny file contains " + str(granny_file.contents.section_count) + " sections.")

    #Iterate through granny file sections and check if they are compressed or not.
    for section_index in range(granny_file.contents.section_count):
        if granny_file.contents.sections[section_index]:
            print("Section " + str(section_index) + " is present.")

            if section_array[section_index].data_size == section_array[section_index].expanded_data_size:
                 print("Section " + str(section_index) + " is uncompressed.")
            else:
                print("Section " + str(section_index) + " is compressed.")
        else:
            print("Section " + str(section_index) + " is empty or freed from memory.")

def print_file_info_stats(granny_file : GrannyFile):
    """This prints file info statistics. """
    file_info = granny_get_file_info(granny_file)
    if file_info:
        print(file_info)
    else:
        print("Could not get granny file information.")
    

#Make sure we implemented the structs correctly or so help me god.
check_granny_struct_sizes()

FILE_PATH = "test_fbx_mongoose_render.gr2"

#Ctypes requires a full path to the file, idk how to do relative lol.
file = granny_read_entire_file(FILE_PATH)

if file:
    print_file_stats(file)
    print_file_info_stats(file)
else:
    print("Could not open " + FILE_PATH)



