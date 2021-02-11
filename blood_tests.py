def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total Cholesterol")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()


def HDL_driver():
    HDL = get_generic_input("HDL")
    analysis = analyze_HDL(HDL)
    output_generic("HDL", HDL, analysis)


def get_generic_input(test_name):
    HDL = input("Enter {} result: ".format(test_name))
    return int(HDL)


def analyze_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"


def output_generic(test_name, test_value, analysis):
    print("The {} entered was {}".format(test_name, test_value))
    print("This value is {}".format(analysis))


def LDL_driver():
    LDL = get_generic_input("LDL")
    analysis = analyze_LDL(LDL)
    output_generic("LDL", LDL, analysis)


def analyze_LDL(LDL):
    if LDL >= 190:
        return "Very high"
    elif 160 <= LDL < 190:
        return "High"
    elif 130 <= LDL < 160:
        return "Borderline high"
    else:
        return "Normal"


def analyze_total_cholesterol(total):
    if total < 200:
        return "Normal"
    elif 200 <= total < 240:
        return "Borderline high"
    else:
        return "High"


def total_driver():
    total_chol = get_generic_input("Total cholesterol")
    analysis = analyze_total_cholesterol(total_chol)
    output_generic("Total cholesterol", total_chol, analysis)


if __name__ == "__main__":
    interface()
