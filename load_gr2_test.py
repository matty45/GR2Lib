"""This loads a granny file and prints out all of its info."""
from gr2_dll_funcs import granny_get_file_info, granny_get_grn_section_array, granny_read_entire_file
from gr2_format import GrannyFile
from gr2_size_test import check_granny_struct_sizes

def print_file_stats(granny_file : GrannyFile):
    """This prints internal file statistics. """
    section_array = granny_get_grn_section_array(granny_file.contents.header)
    print(f"Granny file contains {granny_file.contents.section_count} sections.")

    #Iterate through granny file sections and check if they are compressed or not.
    for section_index in range(granny_file.contents.section_count):
        if granny_file.contents.sections[section_index]:

            print(f"\nSection {section_index} is present.")

            if section_array[section_index].data_size == section_array[section_index].expanded_data_size:
                 print(f"Section {section_index} is uncompressed.")
            else:
                print(f"Section {section_index} is compressed.")
        else:
            print(f"Section {section_index} is empty or freed from memory.")

def print_file_info_stats(granny_file : GrannyFile):
    """This prints file info statistics. """
    file_info = granny_get_file_info(granny_file)
    if file_info == 0:
        print("Could not get granny file information.")
        return
    
    # Get art tool info
    if file_info.contents.art_tool_info:
       info_data = file_info.contents.art_tool_info.contents
       print("\nArt tool info:")
       print(f'File was made using \'{info_data.art_tool_name.decode("UTF-8")}\' Version: ({info_data.art_tool_major_revision}.{info_data.art_tool_minor_revision})')

       print(f"Units per meter: {info_data.units_per_meter}")

       print(f"\nRight vector: {info_data.right_vector[0]} {info_data.right_vector[1]} {info_data.right_vector[2]}")
       print(f"Up vector: {info_data.up_vector[0]} {info_data.up_vector[1]} {info_data.up_vector[2]}")
       print(f"Back vector: {info_data.back_vector[0]} {info_data.back_vector[1]} {info_data.back_vector[2]}")
    else:
        print ("No map tool info, this might break some granny dll functions.")

    #Get item counts
    print(f"\n Textures: {file_info.contents.texture_count}")
    print(f"Materials: {file_info.contents.material_count}")
    print(f"Skeletons: {file_info.contents.skeleton_count}")
    print(f"Vertex datas: {file_info.contents.vertex_data_count}")
    print(f"Tri topologies: {file_info.contents.tri_topology_count}")
    print(f"Meshes: {file_info.contents.mesh_count}")
    print(f"Models: {file_info.contents.model_count}")
    print(f"Track Groups: {file_info.contents.track_group_count}")
    print(f"Animations: {file_info.contents.animation_count}")

    

#Make sure we implemented the structs correctly or so help me god.
check_granny_struct_sizes()

FILE_PATH = "test_fbx_mongoose_render.gr2"

#Ctypes requires a full path to the file, idk how to do relative lol.
file = granny_read_entire_file(FILE_PATH)

if file:
    print_file_stats(file)
    print_file_info_stats(file)
else:
    print(f"Could not open {FILE_PATH}")



