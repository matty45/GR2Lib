"""This triggers all the tests to make sure things work correctly."""

# Make sure we implemented the structs correctly or so help me god.
from tests.extended_data_check_test import extended_data_check_test
from tests.basic_load_test import load_test
from tests.struct_size_test import check_granny_struct_sizes


check_granny_struct_sizes()

test_file_path = "any idle.gr2"

load_test(test_file_path)

extended_data_check_test(test_file_path)