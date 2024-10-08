"""Basic Granny file modification test"""

from granny_dll_funcs import granny_begin_file_data_tree_writing, granny_get_file_info, granny_read_entire_file, granny_write_data_tree_to_file
from granny_dll_vars import GrannyFileInfoType, GrannyGRNFileMV_ThisPlatform
from granny_formats import GrannyFileInfo


def modify_some_stuff(file_info : GrannyFileInfo):
    file_info.contents.art_tool_info.contents.art_tool_name = b'Some random art tool idk, go away.'
    file_info.contents.art_tool_info.contents.units_per_meter = 666666666
    file_info.contents.exporter_info.contents.exporter_name = b"What are you looking at?"
    file_info.contents.exporter_info.contents.exporter_build_number = 666
    file_info.contents.exporter_info.contents.exporter_customization = 66643345345
    file_info.contents.exporter_info.contents.exporter_major_revision = 435
    file_info.contents.exporter_info.contents.exporter_minor_revision = 43

    data_tree_writer = granny_begin_file_data_tree_writing(GrannyFileInfoType,file_info,0,0)

    if data_tree_writer:
        test_file_name = "modified_gr2_test_result.gr2"
        file_write_success = granny_write_data_tree_to_file(data_tree_writer,0x80000037,GrannyGRNFileMV_ThisPlatform,test_file_name,1)
        if file_write_success:
            print(f"Managed to edit and write a file to {test_file_name}!")

def basic_modify_test(file_path : str) -> bool:
    """This will load a gr2 file, modify it and save it as a different file."""
    file = granny_read_entire_file(file_path)
    if file:
        file_info = granny_get_file_info(file)
        
        if file_info.contents is None:
            print("Could not get file info..")
            return False

        modify_some_stuff(file_info)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False