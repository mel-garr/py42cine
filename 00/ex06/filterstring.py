import sys
from ft_filter import ft_filter

def main():
    def __doc__():
        """
        This function demonstrates the use of the ft_filter function by creating a sample list and applying the filter to it.
        """
    try:
        assert len(sys.argv) == 3
        text = sys.argv[1].split(" ")
        num = int(sys.argv[2])

        print(list(ft_filter(lambda ss: len(ss) > num, text)))


    except (AssertionError, ValueError):
        print(f"AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()