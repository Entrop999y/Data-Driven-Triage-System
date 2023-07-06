from patient_file import PatientFile

class TriagedPatient():
    # pass the original patient class to it to allow inheritance of attributes

    # uses a simple triage scoring system the Copenhagen Triage System
    # https://sjtrem.biomedcentral.com/articles/10.1186/s13049-016-0312-6/figures/1?fbclid=IwAR25oSJ5I3YvZQ5fqBV3Qupgsye
    # MvfeiCKwmyDPjKWf9Os6oBxQGfdFfvaY

    def __init__(self,patient_object,on_oxygen,systolicBP,resp_rate,heart_rate,Sp_O_2,patient_cat,triage_cat):

        self.patient_object=patient_object
        self.is_the_patient_on_oxygen = on_oxygen
        self.systolic_blood_pressure = systolicBP
        self.minute_ventilation = resp_rate
        self.heart_rate = heart_rate
        self.pulse_oximetry = Sp_O_2
        self.patient_cat=patient_cat
        self.vitals_nurseclinical_judgement= triage_cat

    def set_triage_cat(self,pat_cat):
        self.vitals_nurseclinical_judgement=pat_cat



    def displayTriagedPatient(self):
        print(f"Patient name: {self.patient_object.first_name} {self.patient_object.last_name}")
        print(f"--------Clinical Measurements  ----------\n\n")
        print(f"--------Respiratory Function  ----------")

        print(f"Oxygen Required: {self.is_the_patient_on_oxygen}")
        print(f"Respiratory Rate per minute: {self.minute_ventilation}")
        print(f"SpO2: {self.pulse_oximetry}")
        print(f"--------****************  ----------")
        print(f"--------Cardiovascular Function  ----------")
        print(f"Heart Rate : {self.heart_rate}")
        print(f"Systolic Blood pressure: {self.systolic_blood_pressure}")

        #print(f"Date Last accessed: {patient_file.self.date_updated}")
        print(f"--------Patient Triage Category  ----------")
        print(f" Patient Triage Score:{self.patient_cat} ----------")
        print(f"Patient Status : {self.vitals_nurseclinical_judgement}")
        print(f"------------------------")







