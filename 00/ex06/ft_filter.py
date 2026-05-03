import sys

def ft_filter(fofo, lop):
    def __doc__():
        """
        This function takes a function and a list, and yields elements from the list that satisfy the
        condition defined by the function. If the function is None, it yields all non-false elements from the list.
        """
    for i in lop:
        if fofo is None:
            if i:
                yield i
        else :
            if fofo(i):
                yield i


def main():
    def __doc__():
        """
        This function demonstrates the use of the ft_filter function by creating a sample list and applying the filter to it.
        """
    pass


if __name__ == "__main__":
    main()