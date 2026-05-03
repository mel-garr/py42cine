import sys
try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) < 2:
        sys.exit()

    arg = sys.argv[1]
    try:
        a = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if a % 2:
        print("I'm Odd")
    else:
        print("I'm Even") 
except AssertionError as e:
    print(f"AssertionError: {e}")
