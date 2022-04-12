
import math 
PI = math.pi

"""
    This function calculates the factorial of a given integer
    :param n: the integer to be calculated
    :type n: int
"""  

def factorial(n):
    if n == 0: 
        return 1
    return n * factorial(n - 1)

"""
    This function calculates the minimal n required for the reminder of the answer to be as as small as needed
    :param number: the number to be calculated
    :type n: float
    :param accuracy: the accuracy the user has chosen
    :type n: float
    :return: the smallest n required, -1 if there was something unusual
    :rtype: int
"""  
def find_minimun_n(number, accuracy):
    calculated_reminder = 0
    for n in range(1, 100):
        if (n + 1) % 2 == 1:
            calculated_reminder = pow(number , 2 * n + 3) / factorial(2 * n + 3)
            if calculated_reminder < accuracy:
                return n
    return -1

"""
    This function calculates the sin value of a specified number, with the given accuracy

    First of all, by using the fact that the nth derivative of sin(x) is cos(x)/sin(x)/-cos(x)/-sin(x),  we know that the nth derivative of any c in [0, x] is smaller than 1
    So, we can say that the Lagrange remainder has to be smaller than "pow(number , 2 * n + 3) / factorial(2 * n + 3)"
    if we find the minimal n which satisfies the inequality "pow(number , 2 * n + 3) / factorial(2 * n + 3)" < accuracy,
    we can say that that the Lagrange remainder is smaller than the accuracy as well, which means the found n is the minimal one
    then, once we find the minimal n, we calculate the Taylor polynomial of the found n, and its the answer.


    :param number: the number to be calculated
    :type n: float
    :param accuracy: the accuracy the user has chosen
    :type n: float
    :return: the sin value of the given number
    :rtype: float
""" 
def calc_sin(number, accuracy):
    number = number % (2 * PI) #since sin is a periodic function, we can take 2pi from the number as many times as we want 
    smallest_n = find_minimun_n(number , accuracy)
    if smallest_n == -1:
        return 
    
    calculated_value = 0
    for i in range(smallest_n + 1):
        calculated_value += (pow(-1, i) * (pow(number, 2 * i + 1)) / factorial(2 * i + 1))
    
    return calculated_value

"""
    This function calculates the cos value of a specified number, with the given accuracy
    :param number: the number to be calculated
    :type n: float
    :param accuracy: the accuracy the user has chosen
    :type n: float
    :return: the cos value of the given number
    :rtype: float
""" 
def calc_cos(number, accuracy):
    return calc_sin(PI / 2 - number, accuracy)


def main():
    number = float(input("Please enter what number u want to calculate: (dagrees) "))
    number = number * PI/180 #converting into radians
    answer_accuracy = int(input("Please enter whats the accuracy you want to program to calculate (10^-x when x is your input)"))
    function_index = int(input("Please enter which trigonometric function you want to use:\n\t1 : sin(x)\n\t2 : cos(x)\n"))

    if function_index == 1:
        print("The calculated answer is: " + str(calc_sin(number, 1 / (10 ** answer_accuracy))))
    elif function_index == 2:
        print("The calculated answer is: " + str(calc_cos(number, 1 / (10 ** answer_accuracy))))
    else:
        print("Invalid number\nrestarting the program...")
        main()

if __name__ == "__main__":
    main()