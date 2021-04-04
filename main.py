from tests.tests_rotated_array_search import TestCasesRotatedArraySearch
from solution.rotated_array_search import RotatedArraySearch

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_rotated_array_search: TestCasesRotatedArraySearch = TestCasesRotatedArraySearch()

    tests_rotated_array_search.input_list_is_none_return_minus_one()
    tests_rotated_array_search.input_list_is_empty_return_minus_one()
    tests_rotated_array_search.input_list_has_one_element_nonmatching_return_minus_one()
    tests_rotated_array_search.input_list_has_one_element_matching_return_zero()

    tests_rotated_array_search.input_list_with_multiple_elements_no_pivot_nonmatching_even_return_minus_one()
    tests_rotated_array_search.input_list_with_multiple_elements_no_pivot_matching_even_return_index()
    tests_rotated_array_search.input_list_with_multiple_elements_no_pivot_nonmatching_odd_return_minus_one()
    tests_rotated_array_search.input_list_with_multiple_elements_no_pivot_matching_odd_return_index()

    tests_rotated_array_search.input_list_with_multiple_elements_pivot_nonmatching_even_return_minus_one()
    tests_rotated_array_search.input_list_with_multiple_elements_pivot_matching_even_return_index()
    tests_rotated_array_search.input_list_with_multiple_elements_pivot_nonmatching_odd_return_minus_one()
    tests_rotated_array_search.input_list_with_multiple_elements_pivot_matching_odd_return_index()

    tests_rotated_array_search.input_list_with_multiple_elements_pivot_matching_edge_cases_return_index()

    ###################################
    # Demo
    ###################################
    rotated_array_search: RotatedArraySearch = RotatedArraySearch()

    input_list_0: list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    target_0: int = 6
    result_0: int = rotated_array_search.main(input_list_0, target_0)
    print(result_0) # 0

    input_list_1: list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    target_1: int = 1
    result_1: int = rotated_array_search.main(input_list_1, target_1)
    print(result_1) # 5

    input_list_2: list = [6, 7, 8, 1, 2, 3, 4]
    target_2: int = 8
    result_2: int = rotated_array_search.main(input_list_2, target_2)
    print(result_2) # 2

    input_list_3: list = [6, 7, 8, 1, 2, 3, 4]
    target_3: int = 1
    result_3: int = rotated_array_search.main(input_list_3, target_3)
    print(result_3) # 3

    input_list_4: list = [6, 7, 8, 1, 2, 3, 4]
    target_4: int = 10
    result_4 = rotated_array_search.main(input_list_4, target_4)
    print(result_4) # -1