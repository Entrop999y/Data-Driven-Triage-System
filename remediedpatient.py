
class RemediedPatient:

    def __init__(self,triaged_patient,impression_diagnosis,action,outcome):
        self.patient_object=triaged_patient
        self.diagnosis=impression_diagnosis
        self.remedy=action
        self.conclusion=outcome


    def displayRemediedPatient(self):
        print(f"--------Handover/Discharge Summary----------\n\n")
        print(f"--------Clinical Notes------------------- ----------")
        print(f"Patient {self.patient_object.patient_object.first_name}  {self.patient_object.patient_object.last_name}"
              f"was seen by me after presenting on {self.patient_object.patient_object.date_created} "
              f"with the following presenting symptoms :{self.patient_object.patient_object.presenting_symptoms} ")

        print(f" My impression was that the presentation and clinical findings were consistent with a diagnosis of:"
              f"{self.diagnosis}")
        print(f"Accordingly, we administered the following treatment:\n {self.remedy}")
        print(f"and we report the patient outcome as :{self.conclusion}")
        print(f"--------****************************************  ----------")
