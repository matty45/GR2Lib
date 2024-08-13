"""This triggers all the tests to make sure things work correctly."""

from tests.basic_modify_test import basic_modify_test
from tests.extended_data_check_test import extended_data_check_test
from tests.basic_load_test import load_test
from tests.struct_size_test import check_granny_struct_sizes

# Make sure we implemented the structs correctly or so help me god.
print("Checking granny struct sizes.")
check_granny_struct_sizes()

test_file_path = "test_fbx_mongoose_render.gr2"

print("\nTriggering load test.")
if load_test(test_file_path):
    print("\nLoad test completed successfully!")

print("\nTriggering extended data check test.")
if extended_data_check_test(test_file_path):
    print("\nExtended data check test completed successfully!")

print("\nTriggering basic file modification test.")
if basic_modify_test(test_file_path):
    print("\nBasic file modification test completed successfully!")