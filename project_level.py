def input_levels():
    """
    the function creates Prompts(input of the levels) the user to input seawater levels one by one.
    Continues until an empty line is entered.
    :return: list of float: A list containing all valid seawater level inputs.
    """
    levels = []
    for i in range(1000):
        line = input()
        if line == "":
            break
        try:
            value = float(line)
            levels.append(value)
        except ValueError:
            print("Error: Please enter a valid number!")
    return levels

def minimum(levels):
    """
    this function returns the minimum value in the list.
    :param levels: The seawater level values.
    :return:The smallest value in the list
    """
    return min(levels)

def maximum(levels):
    """
    this function returns the maximum value in the list.
    :param levels: The seawater level values.
    :return: The highest value in the list
    """
    return max(levels)

def median(levels):
    """
    this function calculate the median value in the list.
    :param levels: The seawater level values.
    :return: The median(middle) value in the list
    """
    order = sorted(levels)
    count = len(order)
    if count % 2 == 0:
        return (order[count // 2 - 1] + order[count // 2]) / 2
    else:
        return order[count // 2]

def mean(levels):
    """
    this function calculates the mean value in the list.
    :param levels: The seawater level values.
    :return: The mean(average) value in the list
    """
    mean_value = sum(levels) / len(levels)
    return mean_value

def standard_deviation(levels):
    """
    this function Calculates the standard deviation of the values.
    :param levels: The seawater level values.
    :return: The standard deviation of the values in the list
    """
    mean_value = mean(levels)
    variance_value = sum((x - mean_value) ** 2 for x in levels) / (len(levels)-1)
    standard_dev = variance_value ** 0.5
    return standard_dev


def main():
    """
    Main function that runs the program:
    :return: Prompts user input
    - Validates minimum input count
    - Calculates and prints the required summary statistical results
    """
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")
    levels = input_levels()
    if len(levels) < 2:
        print("Error: At least two measurements must be entered!")
    else:
        print(f"Minimum: {minimum(levels):.2f} cm")
        print(f"Maximum: {maximum(levels):.2f} cm")
        print(f"Median: {median(levels):.2f} cm")
        print(f"Mean: {mean(levels):.2f} cm")
        print(f"Deviation: {standard_deviation(levels):.2f} cm")

if __name__ == "__main__":
    main()
