"""Basic Granny file creation test"""

from ctypes import POINTER, Structure, byref, c_char_p, c_void_p, cast, pointer
from granny_dll_funcs import granny_begin_file_data_tree_writing, granny_write_data_tree_to_file
from granny_dll_vars import GrannyFileInfoType, GrannyGRNFileMV_ThisPlatform
from granny_formats import GrannyDataTypeDefinition, GrannyFileArtToolInfo, GrannyFileExporterInfo, GrannyFileInfo, GrannyMaterial

def create_basic_art_tool_info() -> GrannyFileArtToolInfo:
    tool_info = GrannyFileArtToolInfo()
    tool_info.art_tool_name = b'Python Script'
    tool_info.units_per_meter = 100
    tool_info.origin[:] = [0, 0, 0]
    tool_info.right_vector[:] = [1, 0, 0]
    tool_info.up_vector[:] = [0, 0, 1]
    tool_info.back_vector[:] = [0, -1, 0]
    return tool_info

def create_basic_exporter_tool_info() -> GrannyFileExporterInfo:
    exporter_info = GrannyFileExporterInfo()
    exporter_info.exporter_name = b'Python Script'
    return exporter_info


def create_test_material(file_info : GrannyFileInfo):
    materials = []
    materials.append(GrannyMaterial(name=b"Test Material"))

    Array = POINTER(GrannyMaterial) * len(materials)
    granny_materials = Array()
    
    for i, mat in enumerate(materials):
            granny_materials[i] = pointer(mat)
            
    file_info.material_count = len(materials)
    file_info.materials = granny_materials

class CustomExtendedData(Structure):
    """ Custom extended data, ditto """
    _pack_ = 1
    _fields_ = [
                ('test_string',c_char_p)]

def add_custom_data_to_test_material(file_info: GrannyFileInfo):

    CustomExtendedDataType = (GrannyDataTypeDefinition * 2)()
    CustomExtendedDataType[0] = GrannyDataTypeDefinition(member_type=8,name = b"TestString")
    CustomExtendedDataType[1] = GrannyDataTypeDefinition(member_type=0)

    file_info.materials.contents.contents.extended_data.type = CustomExtendedDataType
    
    crap = CustomExtendedData(test_string = b"lol")

    file_info.materials.contents.contents.extended_data.object = cast(pointer(crap), c_void_p)



def create_empty_granny_file(file_path : str):

    # Create empty file_info
    file_info = GrannyFileInfo()
    
    #Create art tool info with some basic data inside
    file_info.art_tool_info = pointer(create_basic_art_tool_info())

    #Create exporter tool info with some basic data inside
    file_info.exporter_tool_info = pointer(create_basic_exporter_tool_info())

    file_info.file_name = file_path.encode()

    #Add a test material with custom extended data
    create_test_material(file_info)
    add_custom_data_to_test_material(file_info)

    # Write file

    data_tree_writer = granny_begin_file_data_tree_writing(GrannyFileInfoType,pointer(file_info),0,0)

    if data_tree_writer:
        file_write_success = granny_write_data_tree_to_file(data_tree_writer,0x80000037,GrannyGRNFileMV_ThisPlatform,file_path,1)
        if file_write_success:
            return True
    
    return False


def file_creation_test(file_path : str) -> bool:
    """This will create an empty granny file and save it somewhere."""
    file = create_empty_granny_file(file_path)
    if file:
        print(f"\nManaged to create file: {file_path}")
        return True
    else:
        print(f"\nCould not create file: {file_path}")
        return False