"""This loads a granny file and prints out some of its info."""
from granny_dll_funcs import granny_get_file_info, granny_get_grn_section_array, granny_read_entire_file
from granny_formats import GrannyFile, GrannyFileInfo

def print_file_stats(granny_file : GrannyFile):
    """This prints internal file statistics. """
    section_array = granny_get_grn_section_array(granny_file.contents.header)
    print(f"\nGranny file contains {granny_file.contents.section_count} sections.")

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

def print_file_info_stats(file_info : GrannyFileInfo):
    """This prints file info statistics. """    
    #Get source file used to make the granny file if applicable.
    if file_info.contents.file_name:
        print(f"\nSource file name: {file_info.contents.file_name.decode("UTF-8")}")

    # Get art tool info
    if file_info.contents.art_tool_info:
       info_data = file_info.contents.art_tool_info.contents
       print("\nArt tool info:")
       print(f'File was made using \'{info_data.art_tool_name.decode("UTF-8")}\' Version: ({info_data.art_tool_major_revision}.{info_data.art_tool_minor_revision})')

       print("\nArt tool coordinate info:")
       print(f"Units per meter: {info_data.units_per_meter}")
       print(f"Right vector: {info_data.right_vector[0]} {info_data.right_vector[1]} {info_data.right_vector[2]}")
       print(f"Up vector: {info_data.up_vector[0]} {info_data.up_vector[1]} {info_data.up_vector[2]}")
       print(f"Back vector: {info_data.back_vector[0]} {info_data.back_vector[1]} {info_data.back_vector[2]}")
    else:
        print ("No art tool info, this might break some granny dll functions.")

    # Get exporter info
    if file_info.contents.exporter_info:
       export_info = file_info.contents.exporter_info.contents
       print("\nExporter tool info:")
       print(f'File was exported using \'{export_info.exporter_name.decode("UTF-8")}\' Version: ({export_info.exporter_major_revision}.{export_info.exporter_minor_revision}.{export_info.exporter_build_number}.{export_info.exporter_customization})')
    else:
        print ("No exporter tool info, this might break some granny dll functions.")

    #Get item counts
    print("\nObject counts:")
    print(f"Textures: {file_info.contents.texture_count}")
    print(f"Materials: {file_info.contents.material_count}")
    print(f"Skeletons: {file_info.contents.skeleton_count}")
    print(f"Vertex datas: {file_info.contents.vertex_data_count}")
    print(f"Tri topologies: {file_info.contents.tri_topology_count}")
    print(f"Meshes: {file_info.contents.mesh_count}")
    print(f"Models: {file_info.contents.model_count}")
    print(f"Track Groups: {file_info.contents.track_group_count}")
    print(f"Animations: {file_info.contents.animation_count}")

def load_test(file_path : str):
    file = granny_read_entire_file(file_path)
    if file:
        print("\nPrinting out basic granny file stats:")
        print_file_stats(file)
        
        file_info = granny_get_file_info(file)
        if file_info.contents is None:
            print("Could not get file info..")
            return

        print("\nPrinting out basic granny file info stats:")
        print_file_info_stats(file_info)
    else:
        print(f"\nCould not open {file_path}")



