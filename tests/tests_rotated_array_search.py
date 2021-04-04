import unittest
from solution.rotated_array_search import RotatedArraySearch


class TestCasesRotatedArraySearch(unittest.TestCase):
    def input_list_is_none_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = None
        target: int = 1

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)
    
    def input_list_is_empty_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = []
        target: int = 1

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)

    def input_list_has_one_element_nonmatching_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [2]
        target: int = 1

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)
    
    def input_list_has_one_element_matching_return_zero(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [2]
        target: int = 2

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, 0)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_with_multiple_elements_no_pivot_nonmatching_even_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [1,4,5,8,23,50]
        target: int = 15

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)
    
    def input_list_with_multiple_elements_no_pivot_matching_even_return_index(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [1,4,5,8,23,50]
        target: int = 23

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, 4)

    def input_list_with_multiple_elements_no_pivot_nonmatching_odd_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [1,4,5,8,23,50,51]
        target: int = 15

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)
    
    def input_list_with_multiple_elements_no_pivot_matching_odd_return_index(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [1,4,5,8,23,50,51]
        target: int = 23

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, 4)
    
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_with_multiple_elements_pivot_nonmatching_even_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [6,8,23,50,-10,-8,0,1,4,5]
        target: int = 15

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)

    def input_list_with_multiple_elements_pivot_matching_even_return_index(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [6,8,23,50,-10,-8,0,1,4,5]
        target: int = 1

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, 7)

    def input_list_with_multiple_elements_pivot_nonmatching_odd_return_minus_one(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [6,8,23,50,-10,-8,0,1,4]
        target: int = 15

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, -1)

    def input_list_with_multiple_elements_pivot_matching_odd_return_index(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list: list = [6,8,23,50,-10,-8,0,1,4]
        target: int = 1

        # Act
        index: int = rotated_array_search.main(input_list, target)

        # Assert
        self.assertEqual(index, 7)
    
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_with_multiple_elements_pivot_matching_edge_cases_return_index(self: object) -> None:
        # Arrange
        rotated_array_search: RotatedArraySearch = RotatedArraySearch()
        input_list_0: list = [-8,0,1,4,6,8,23,50,-10]
        input_list_1: list = [50,-10,-8,0,1,4,6,8,23]
        target: int = 1

        # Act
        index_0: int = rotated_array_search.main(input_list_0, target)
        index_1: int = rotated_array_search.main(input_list_1, target)

        # Assert
        self.assertEqual(index_0, 2)
        self.assertEqual(index_1, 4)