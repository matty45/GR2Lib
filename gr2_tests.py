"""This triggers all the tests to make sure things work correctly."""

from gr2_size_test import check_granny_struct_sizes
from load_gr2_test import load_gr2_test

# Make sure we implemented the structs correctly or so help me god.
check_granny_struct_sizes()

# Extract basic information from a gr2 file.
load_gr2_test("test_fbx_mongoose_render.gr2")