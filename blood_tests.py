def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        
def HDL_driver():
    HDL = get_HDL_input()
    analysis = analyze_HDL(HDL)
    output_HDL(HDL, analysis)
    
def get_HDL_input():
    HDL = input("Enter HDL Level: ")
    return int(HDL)
    
def analyze_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"

def output_HDL(HDL, analysis):
    print("The HDL entered was {}".format(HDL))
    print("The HDL level is {}".format(analysis))
    
def LDL_driver():
    pass
    
interface()

