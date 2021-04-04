class RotatedArraySearch(object):
    def __init__(self) -> None:
        """Constructor.
        """
        pass

    def main(self: object, input_list: list, target: int) -> int:
        """Find the index by searching in a rotated sorted array in O(log n) time.

            Parameters
            ----------
            input_list : list, required
                List to search for the number.
            target : int, required
                Number to get the index for.
            
            Returns
            ----------
            int
                Returns the index of the number if exists otherwise -1.
        """

        if not input_list or len(input_list) == 0:
            return -1
        elif len(input_list) == 1 and  input_list[0] == target:
            return 0
        else:
            return self.search(input_list, target, 0, len(input_list)-1)

    def search(
        self: object,
        input_list: list,
        target: int,
        start_index: int,
        end_index: int) -> int:

        """Search helper method.

            Parameters
            ----------
            input_list : list, required
                List to search for the number.
            target : int, required
                Number to get the index for.
            start_index : int, required
                Start index within the list.
            end_index : int, required
                End index within the list.
            
            Returns
            ----------
            int
                Returns the index of the number if exists otherwise -1.
        """

        if start_index > end_index:
            return -1

        middle_index: int = (start_index + end_index) // 2

        if input_list[middle_index] == target: # middle is target
            return middle_index
        elif input_list[start_index] <= input_list[middle_index]: # left array is sorted
            if target >= input_list[start_index] and target <= input_list[middle_index]:
                return self.search(input_list, target, start_index, middle_index-1)
            else:
                return self.search(input_list, target, middle_index+1, end_index)
        else: # right array is sorted
            if target >= input_list[middle_index] and target <= input_list[end_index]:
                return self.search(input_list, target, middle_index+1, end_index)
            else:
                return self.search(input_list, target, start_index, middle_index-1)