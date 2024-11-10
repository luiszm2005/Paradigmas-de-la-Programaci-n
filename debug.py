import pdb  # We import the pdb module, which is the Python debugger.

def calculate_rectangle_area(width, high):
    # We can set a breakpoint here to inspect variables
    pdb.set_trace()  # This command will stop the execution and open the interactive debugger.

    # Calculate the area of the rectangle
    area = width * high
    return area

def main():
    width = 5  # We assign a value to the width
    high = 10  # We assign a value to the high

    # We call the function to calculate the area
    area = calculate_rectangle_area(width, high)

    # We print the result
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()