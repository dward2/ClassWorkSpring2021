# calculator.py


def sqrt(n): 

    # We are using n itself as 
    # initial approximation This 
    # can definitely be improved  
        x = n 
        y = 1
          
        # e decides the accuracy level 
        e = 0.000001
        while(x - y > e): 
      
            x = (x + y)/2
            y = n / x 
      
        return x 

def calc_input():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    a = int(a)
    b = int(b)
    print("The numbers you entered are {} and {}".format(a, b))
    return a, b


def add(a, b):
    print("Add")
    answer = a + b
    print("{} + {} = {}".format(a, b, answer))
    return answer


def subtract(a, b):
    print("Subtract")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))
    return answer


def multiply(a, b):
    print("Multiply")
    answer = a * b
    print("{} * {} = {}".format(a, b, answer))
    return answer


def divide(a, b):
    print("Name of calculator is {}".format(__name__))
    print("Divide")
    answer = a / b
    print("{} * {} = {}".format(a, b, answer))
    return answer


def overall_function(a, b):
    c = add(a, b)
    d = subtract(a, c)
    e = multiply(c, d)
    return e


def run_my_program():
    a = input("Get First number:")
    b = input("Get Second Number:")
    c = add(a, b)
    d = subtract(a, c)
    e = multiply(c, d)
    print("The answer is {}".format(e))

def math_command(a, b):
    c = input("Enter a command: ")
    if c == "a":
        add(a, b)
    elif c == "s":
        subtract(a, b)
    elif c == "m":
        multiply(a, b)
    elif c == "d":
        divide(a, b)
    else:
        print("{} is not a valid command".format(c))
        

def math_api(a, b, sign):
    if sign == "a":
        answer = add(a, b)
    elif sign == "s":
        answer = subtract(a, b)
    elif sign == "m":
        answer = multiply(a, b)
    elif sign == "d":
        answer = divide(a, b)
    else:
        return False
    return answer





if __name__ == "__main__":
    x, y = calc_input()
    math_command(x, y)

    print("Finished")
