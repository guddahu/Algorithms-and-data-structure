from typing import List, Tuple, Any


class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['key', 'value']

    def __init__(self, k: Any, v: Any):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0}, {1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityQueue:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        function for the length
        :return: length of the queue
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        checks if the queue is empty
        :return: if the queue is empty
        """
        return len(self.data) == 0

    def top(self) -> Node:
        """
        gets the root element
        :return: the root node in min heap
        """
        if len(self.data) == 0:
            return
        return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
        gets the index left children of min heap
        :param index: the parent node index
        :return: the left children index
        """
        if 2 * index + 1 < len(self.data):
            return 2 * index + 1

    def get_right_child_index(self, index: int) -> int:
        """
        gets the index right children of min heap
        :param index: the parent node index
        :return: the right children index
        """
        if 2 * index + 2 < len(self.data):
            return 2 * index + 2

    def get_parent_index(self, index: int) -> int:
        """
        gets the parent for the child node
        :param index: child node index
        :return: parent for the child node
        """
        if self.data[index] == self.top():
            return
        if len(self.data) > (index - 1) / 2 >= 0:
            return (index - 1) // 2

    def push(self, key: Any, val: Any) -> None:
        """
        Adds the element to the queue
        :param key: key for inserion
        :param val: value of element
        :return: None
        """
        self.data.append(Node(key, val))
        self.percolate_up(len(self.data) - 1)

    def pop(self) -> Node:
        """
        pops the last element in queue
        :return: last node in queue
        """
        if len(self.data) == 0:
            return
        self.swap(0, len(self.data) - 1)  # put minimum item at the end
        item = self.data.pop()  # and remove it from the list;
        self.percolate_down(0)  # then fix new root
        return item

    def get_min_child_index(self, index: int) -> int:
        """
        gets the index for the smallest node
        :param index: index to search from
        :return: smallest node (index)
        """
        if len(self.data) == 0 or (
                self.get_left_child_index(index) is None and
                self.get_right_child_index(index) is None):
            return
        if self.get_left_child_index(index) is None:
            return self.get_right_child_index(index)
        elif self.get_right_child_index(index) is None:
            return self.get_left_child_index(index)

        if self.data[self.get_left_child_index(index)] < \
                self.data[self.get_right_child_index(index)]:
            return self.get_left_child_index(index)
        else:
            return self.get_right_child_index(index)

    def swap(self, i, j):
        """
        swaps two nodes
        :param i: first node
        :param j: second node
        :return: None
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def percolate_up(self, index: int) -> None:
        """
        Helper function for push, maintains min heap properties
        :param index: index of node to push up
        :return: None
        """
        parent = self.get_parent_index(index)
        if index > 0 and self.data[index] < self.data[parent]:
            self.swap(index, parent)
            self.percolate_up(parent)  # recur at position of parent

    def percolate_down(self, index: int) -> None:
        """
        Helper function for pop, maintains min heap properties
        :param index: index of node to push down
        :return: None
        """
        if self.get_left_child_index(index) is not None:
            left = self.get_left_child_index(index)
            small_child = left  # although right may be smaller
            if self.get_right_child_index(index) is not None:
                right = self.get_right_child_index(index)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[index]:
                self.swap(index, small_child)
                self.percolate_down(small_child)  # recur at position of small child


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = PriorityQueue()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        if the queue is empty
        :return: bool if queue is empty
        """
        return len(self.data) == 0

    def top(self) -> int:
        """
        gets the root element in max heap implementation
        :return: the root node in min heap
        """
        if self.data.top() is None:
            return
        return self.data.top().value

    def push(self, key: int) -> None:
        """
        Adds the element to the queue in max heap implementation
        :param key: key for inserion
        :param val: value of element
        :return: None
        """
        self.data.push(-key, key)

    def pop(self) -> int:
        """
        pops the last element in queue in max heap
        :return: last node in queue
        """
        return self.data.pop().value


def heapify_helper(array, length, index):
    """
    Helper function for heap sort
    :param array: array to sort
    :param length: length of array
    :param index: index of node to heapify from
    :return:
    """
    largest_val = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < length and array[left_child] > array[largest_val]:
        largest_val = left_child

    if right_child < length and array[right_child] > array[largest_val]:
        largest_val = right_child

    if largest_val != index:
        array[index], array[largest_val] = array[largest_val], array[index]
        heapify_helper(array, length, largest_val)


def heap_sort(array):
    """
    Heap sort an array in place
    :param array: array to be sorted
    :return: sorted array
    """
    length = len(array)
    for i in range(length // 2 - 1, -1, -1):
        heapify_helper(array, length, i)

    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_helper(array, i, 0)
    return array


def find_ranking(rank, results: List[Tuple[int, str]]) -> str:
    """
    Finds the data with the particular rank
    :param rank: rank to be found
    :param results: list with team wins and losses
    :return: the team
    """
    final_queue = PriorityQueue()

    for i in range(len(results)):
        final_queue.push(results[i][0], results[i][1])

    for i in range(len(final_queue)):
        popped = final_queue.pop()

        if popped is not None and i + 1 == rank:
            return popped.value
