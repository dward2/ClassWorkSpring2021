import logging
from datetime import datetime


def fibonacci(fib_list):
    next_number = fib_list[-1] + fib_list[-2]
    logging.info("{} + {} = {}".format(fib_list[-1], fib_list[-2], next_number))
    fib_list.append(next_number)
    if next_number < 100:
        fibonacci(fib_list)
    else:
        logging.warning("Reached end of list")
    return fib_list
    
    
def main():
    x = [0, 1]
    answer = fibonacci(x)
    print(answer)
    
    
if __name__ == "__main__":
    in_file = open("counter.txt", "r")
    counter = int(in_file.readline().strip("\n"))
    in_file.close()
    log_name = "fiblog_{}.txt".format(counter)
    counter += 1
    out_file = open("counter.txt", "w")
    out_file.write(str(counter))
    out_file.close()
    logging.basicConfig(filename=log_name, level=logging.INFO,
                        filemode="w")
    main()
    