"""This triggers all the tests to make sure things work correctly."""

from tests.basic_modify_test import basic_modify_test
from tests.extended_data_check_test import extended_data_check_test
from tests.basic_load_test import load_test
from tests.extended_data_parse_test import parse_extended_data_test
from tests.file_creation_test import file_creation_test
from tests.vertex_modify_test import vertex_modify_test
from tests.vertex_type_parse_test import vertex_type_parse_test
from tests.struct_size_test import check_granny_struct_sizes

#Start a timer
import time
start_time = time.time()

# Make sure we implemented the structs correctly or so help me god.
print("Checking granny struct sizes.")
check_granny_struct_sizes()

test_file_path = "house_render.gr2"
test_file_creation_path = "some_shitty_file.gr2"

print("\nTriggering load test.")
if load_test(test_file_path):
    print("\nLoad test completed successfully!")

print("\nTriggering extended data check test.")
if extended_data_check_test(test_file_path):
    print("\nExtended data check test completed successfully!")

print("\nTriggering extended data parse test.")
if parse_extended_data_test(test_file_path):
    print("\nExtended data parse test completed successfully!")

print("\nTriggering vertex type parse test.")
if vertex_type_parse_test(test_file_path):
    print("\nVertex type parse test completed successfully!")

print("\nTriggering basic file modification test.")
if basic_modify_test(test_file_path):
    print("\nBasic file modification test completed successfully!")

print("\nTriggering file creation test.")
if file_creation_test(test_file_creation_path):
    print("\nfile creation successfully!")

print("\nTriggering vertex file modification test.")
if vertex_modify_test(test_file_path):
    print("\nVertex file modification test completed successfully!")

print("ALL TESTS DONE! --- Tests took %s seconds total" % (time.time() - start_time))