"""This loads a granny file and prints out more detailed info."""

from gr2_dll_funcs import granny_get_file_info, granny_read_entire_file
from gr2_format import GrannyFile


def print_file_model_stats(granny_file : GrannyFile):
    """This prints file model statistics. """
    file_info = granny_get_file_info(granny_file)
    for model_index in range(file_info.contents.model_count):
        model = file_info.contents.models[model_index]
        print(f"Model name: {model.contents.name}")

def adv_load_gr2_test(file_path : str):
    #Ctypes requires a full path to the file, idk how to do relative lol.
    file = granny_read_entire_file(file_path)
    if file:
        print_file_model_stats(file)
    else:
        print(f"\nCould not open {file_path}")