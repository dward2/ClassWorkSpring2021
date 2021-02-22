class Patient:
    
    def __init__(self, first_name, last_name, age=None, state="NC"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)
        
    def output_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
        
        
def main():
    patient_1 = Patient("Ann", "Ables")
    patient_2 = Patient("Bob", "Boyles")
    # patient_1.first_name = "Ann"
    # patient_1.last_name = "Ables"
    patient_3 = Patient("Celia", "Chou", 45)
    
    
    print(patient_1)
    print(patient_1.first_name)
    print(patient_1.last_name)
    print(patient_1.age)
    print(patient_2)
    print(patient_2.first_name)
    print(patient_2.last_name)
    print(patient_2.age)
    print(patient_1.output_full_name())
    print(patient_3.age)
    
    
if __name__ == "__main__":
    main()
    
        
    