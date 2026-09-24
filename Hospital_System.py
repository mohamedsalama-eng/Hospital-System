MAX_SECTIONS = 20
MAX_PATIENT = 5

class Hostpital:
    no_of_patient = 0
    def __init__(self):
        self.sections = {i: [] for i in range(1, MAX_SECTIONS + 1)}

    def addPatient(self,section , name , status):
        if section > 20:
            print("Invalid Section [1 - 20]")
            return
        
        lst = self.sections[section]

        if len(lst) >= MAX_PATIENT:
            print("Sorry we can't add more patients")
            return
        
        if status == 0:
            lst.insert(0,(name , status))
        elif status == 1:
            lst.append((name , status))
        return lst

    def show_patients(self):
        for section , patients in self.sections.items():
            if patients:
                print(f"section {section}")
                for name , status in patients:
                    x = ["regular" if status == 0 else "Urgent"]
                    print("--" + name + " " + x[0])

    def pickup_patient(self, section):
        if not self.sections[section]:
            print("No patients , Take rest Dr")
        else:
            print(f"Please go to the Dr's Room Mr {self.sections[section][-1][0]}")
            self.sections[section].pop()
        

if __name__ == "__main__":
    h = Hostpital()
    while True:
        n = int(input("Enter your choice:  \n1) Add new patient \n2) Print all patient \n3) Get next patient \n4) Exit\n"))

        
        if n == 1:
            sec = int(input("Enter the section: "))
            name = str(input("Enter the name: "))
            status = int(input("Enter the status: "))

            h.addPatient(sec , name , status)

        elif n == 2:
            h.show_patients()

        elif n == 3:
            sec = int(input("Enter the section:"))
            h.pickup_patient(sec)
        elif n == 4:
            break

        else:
            print("Invalid number [1 - 4]")



        