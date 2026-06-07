import typer


def main(num1: float, num2: float, divide: bool = False, add: bool = False, subtract: bool = False, multiply: bool = False):
    """
    A Simple Calculator. Input one number, a space, and then another, followed by your operation flag.
    """
    if add:
        print(num1 + num2)
    elif subtract:
        print(num1 - num2)
    elif divide: 
        print(num1 / num2)
    elif multiply:
        print(num1 * num2)
    else:
        print("Please add flag")

if __name__ == "__main__":
    typer.run(main)