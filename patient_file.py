

class PatientFile:
    def __init__(self,fname,lname,dob,ppsn,address,n_o_kin,
                 mob,presenting_symptoms,date_created,date_accessed):

        self.first_name= fname
        self.last_name=lname
        self.date_of_birth=dob
        self.ppsn=ppsn
        self.address=address
        self.next_of_kin=n_o_kin
        self.mobile_no = mob
        self.presenting_symptoms=presenting_symptoms
        self.date_created = date_created
        self.date_updated = date_accessed


    def displayPatient(self):
        print(f"-------- {self.ppsn} ----------")
        print(f"Firstname: {self.first_name}")
        print(f"Lastname: {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.mobile_no}")
        print(f"Next of Kin: {self.next_of_kin}")
        print(f"Presenting Symptoms: {self.presenting_symptoms}")
        print(f"Date Created: {self.date_created}")
        print(f"Date Last accessed: {self.date_updated}")
        print(f"------------------------")




