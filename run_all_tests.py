"""This triggers all the tests to make sure things work correctly."""

#from tests.adv_load_gr2_test import adv_load_gr2_test
from tests.struct_size_test import check_granny_struct_sizes
from tests.basic_load_test import load_gr2_test

# Make sure we implemented the structs correctly or so help me god.
check_granny_struct_sizes()

test_file_path = "test_fbx_mongoose_render.gr2"

# Extract basic information from a gr2 file.
load_gr2_test(test_file_path)
#adv_load_gr2_test(test_file_path)