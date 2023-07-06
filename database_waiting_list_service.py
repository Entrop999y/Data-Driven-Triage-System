import sqlite3
from patient_file import PatientFile
from triage_score_cal import TriagedPatient
from list_management import PatientWalkInListManagement


class SQLService:  # control db using class methods
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()

    def createDB(self): # master copy - all entries
        self.c.execute("CREATE TABLE IF NOT EXISTS patients (\n"
                       "                     fname text,\n"
                       "                     lname text,\n"
                       "                     dob text,\n"
                       "                     ppsn text,\n"
                       "                     address text,\n"
                       "                     n_o_kin text,\n"
                       "                     mob_phone text,\n"
                       "                     presenting_symptoms text,\n"
                       "                     date_created text,\n"
                       "                     date_accessed text,\n"
                       "                     on_oxygen text,\n"
                       "                     systolicBP text,\n"
                       "                     resp_rate text,\n"
                       "                     heart_rate text, \n"
                       "                     Sp_O_2 text,\n"
                       "                     patient_cat text,\n"
                       "                     triage_category text,\n"
                       "                     impression_diagnosis text,\n "
                       "                     action, \n "
                       "                     outcome"
                       "                    )")
        # creates the basic table for data persistance. All possible fields added
        # placeholder to create table headings
        # fname,lname,dob,ppsn,address,n_o_kin, mob,presenting_symptoms,date_created,
        # date_accessed on_oxygen,systolicBP,resp_rate,heart_rate,Sp_O_2,triage_category

        self.conn.commit()  # commit to file

    def insert_patient_waiting(self, patient_object):
        with self.conn:
            self.c.execute("""INSERT OR IGNORE INTO patients VALUES (:fname,:lname,:dob,:ppsn, :address,:n_o_kin ,:mob_phone,
                           :presenting_symptoms,:date_created,:date_accessed,:on_oxygen,:systolicBP,
                           :resp_rate,:heart_rate, :Sp_O_2, :patient_cat, :triage_category,:impression_diagnosis,
                           :action,:outcome)"""
                           ,
                           {'fname': patient_object.first_name, 'lname': patient_object.last_name,
                            'dob': patient_object.date_of_birth, 'ppsn': patient_object.ppsn,
                            'address': patient_object.address, 'n_o_kin': patient_object.next_of_kin,
                            'mob_phone': patient_object.mobile_no,
                            'presenting_symptoms': patient_object.presenting_symptoms,
                            'date_created': patient_object.date_created,
                            'date_accessed': patient_object.date_updated,
                            'on_oxygen': None,
                            'systolicBP': None,
                            'resp_rate': None,
                            'heart_rate': None,
                            'Sp_O_2': None,
                            'patient_cat': None,
                            'triage_category': None,
                            'impression_diagnosis':None,
                            'action':None,
                            'outcome':None
                            })
            # populates the database table using the dictionary format.
            # uses the dot notation corresponding to patient object to add persistant data to the columns.
            # fields corresponding to the triaged patient are marked None corresponding to null in database
            self.conn.commit()

    # placeholder to create table headings
    # fname,lname,dob,ppsn,address,n_o_kin, mob,presenting_symptoms,date_created,
    # date_accessed on_oxygen,systolicBP,resp_rate,heart_rate,Sp_O_2,triage_category
    def insert_patient_triaged(self, triaged_patient):
        with self.conn:
            self.c.execute("""INSERT OR IGNORE INTO patients VALUES (:fname,:lname,:dob,:ppsn, :address,:n_o_kin ,:mob_phone,
                           :presenting_symptoms,:date_created,:date_accessed,:on_oxygen,:systolicBP,
                           :resp_rate,:heart_rate,:Sp_O_2, :patient_cat, :triage_category,:impression_diagnosis,
                           :action,:outcome)"""
                           ,
                           {'fname': triaged_patient.patient_object.first_name,
                            'lname': triaged_patient.patient_object.last_name,
                            'dob': triaged_patient.patient_object.date_of_birth,
                            'ppsn': triaged_patient.patient_object.ppsn,
                            'address': triaged_patient.patient_object.address,
                            'n_o_kin': triaged_patient.patient_object.next_of_kin,
                            'mob_phone': triaged_patient.patient_object.mobile_no,
                            'presenting_symptoms': triaged_patient.patient_object.presenting_symptoms,
                            'date_created': triaged_patient.patient_object.date_created,
                            'date_accessed': triaged_patient.patient_object.date_updated,
                            'on_oxygen': triaged_patient.is_the_patient_on_oxygen,
                            'systolicBP': triaged_patient.systolic_blood_pressure,
                            'resp_rate': triaged_patient.minute_ventilation,
                            'heart_rate': triaged_patient.heart_rate,
                            'Sp_O_2': triaged_patient.pulse_oximetry,
                            'patient_cat': triaged_patient.patient_cat,
                            'triage_category': triaged_patient.vitals_nurseclinical_judgement,
                            'impression_diagnosis':None,
                            'action': None,
                            'outcome':None

                            })
            # populates the database table using the dictionary format.
            # uses the dot notation corresponding to patient object to add persistant data to the columns.
            # fields corresponding to the triaged patient are marked None corresponding to null in database
            self.conn.commit()
    def createWRLTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS WaitingRoom (\n"
                       "                     fname text,\n"
                       "                     lname text,\n"
                       "                     dob text,\n"
                       "                     ppsn text,\n"
                       "                     address text,\n"
                       "                     n_o_kin text,\n"
                       "                     mob_phone text,\n"
                       "                     presenting_symptoms text,\n"
                       "                     date_created text,\n"
                       "                     date_accessed text,\n"
                       "                     on_oxygen text,\n"
                       "                     systolicBP text,\n"
                       "                     resp_rate text,\n"
                       "                     heart_rate text, \n"
                       "                     Sp_O_2 text,\n"
                       "                     patient_cat text,\n"
                       "                     triage_category text,\n"
                       "                     impression_diagnosis text,\n "
                       "                     action, \n "
                       "                     outcome"
                       "                    )")
        # seperate  table for those in weighting room "static copy" of that aspect of care only
        self.conn.commit()

    def createTPTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS TriagedPatients (\n"
                       "                     fname text,\n"
                       "                     lname text,\n"
                       "                     dob text,\n"
                       "                     ppsn text,\n"
                       "                     address text,\n"
                       "                     n_o_kin text,\n"
                       "                     mob_phone text,\n"
                       "                     presenting_symptoms text,\n"
                       "                     date_created text,\n"
                       "                     date_accessed text,\n"
                       "                     on_oxygen text,\n"
                       "                     systolicBP text,\n"
                       "                     resp_rate text,\n"
                       "                     heart_rate text, \n"
                       "                     Sp_O_2 text,\n"
                       "                     patient_cat text,\n"
                       "                     triage_category text,\n"
                       "                     impression_diagnosis text,\n "
                       "                     action, \n "
                       "                     outcome"
                       "                    )")

        self.conn.commit()

        # separate  table for those who have been triaged "static copy" of that aspect of care only
    def createRPTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS RemediedPatients (\n"
                       "                     fname text,\n"
                       "                     lname text,\n"
                       "                     dob text,\n"
                       "                     ppsn text,\n"
                       "                     address text,\n"
                       "                     n_o_kin text,\n"
                       "                     mob_phone text,\n"
                       "                     presenting_symptoms text,\n"
                       "                     date_created text,\n"
                       "                     date_accessed text,\n"
                       "                     on_oxygen text,\n"
                       "                     systolicBP text,\n"
                       "                     resp_rate text,\n"
                       "                     heart_rate text, \n"
                       "                     Sp_O_2 text,\n"
                       "                     patient_cat text,\n"
                       "                     triage_category text,\n"
                       "                     impression_diagnosis text,\n "
                       "                     action, \n "
                       "                     outcome"
                       "                    )")
        # separate  table for those who have been triaged "static copy" of that aspect of care only
        self.conn.commit()


    def insert_patient_WRL(self, patient_object):# separate copy to Waiting room list
        with self.conn:
            self.c.execute("""INSERT OR IGNORE INTO WaitingRoom  VALUES (:fname,:lname,:dob,:ppsn, :address,:n_o_kin ,:mob_phone,
                           :presenting_symptoms,:date_created,:date_accessed,:on_oxygen,:systolicBP,
                           :resp_rate,:heart_rate, :Sp_O_2, :patient_cat, :triage_category,:impression_diagnosis,
                           :action,:outcome)"""
                           ,
                           {'fname': patient_object.first_name, 'lname': patient_object.last_name,
                            'dob': patient_object.date_of_birth, 'ppsn': patient_object.ppsn,
                            'address': patient_object.address, 'n_o_kin': patient_object.next_of_kin,
                            'mob_phone': patient_object.mobile_no,
                            'presenting_symptoms': patient_object.presenting_symptoms,
                            'date_created': patient_object.date_created,
                            'date_accessed': patient_object.date_updated,
                            'on_oxygen': None,
                            'systolicBP': None,
                            'resp_rate': None,
                            'heart_rate': None,
                            'Sp_O_2': None,
                            'patient_cat': None,
                            'triage_category': None,
                            'impression_diagnosis':None,
                            'action':None,
                            'outcome':None
                            })
            # populates the database table using the dictionary format.
            # uses the dot notation corresponding to patient object to add persistant data to the columns.
            # fields corresponding to the triaged patient are marked None corresponding to null in database
            self.conn.commit()


    def insert_patient_triagedPL(self, triaged_patient):# separate copy to triaged table
        with self.conn:
            self.c.execute("""INSERT OR IGNORE INTO TriagedPatients VALUES (:fname,:lname,:dob,:ppsn, :address,:n_o_kin ,:mob_phone,
                           :presenting_symptoms,:date_created,:date_accessed,:on_oxygen,:systolicBP,
                           :resp_rate,:heart_rate,:Sp_O_2, :patient_cat, :triage_category,:impression_diagnosis,
                           :action,:outcome)"""
                           ,
                           {'fname': triaged_patient.patient_object.first_name,
                            'lname': triaged_patient.patient_object.last_name,
                            'dob': triaged_patient.patient_object.date_of_birth,
                            'ppsn': triaged_patient.patient_object.ppsn,
                            'address': triaged_patient.patient_object.address,
                            'n_o_kin': triaged_patient.patient_object.next_of_kin,
                            'mob_phone': triaged_patient.patient_object.mobile_no,
                            'presenting_symptoms': triaged_patient.patient_object.presenting_symptoms,
                            'date_created': triaged_patient.patient_object.date_created,
                            'date_accessed': triaged_patient.patient_object.date_updated,
                            'on_oxygen': triaged_patient.is_the_patient_on_oxygen,
                            'systolicBP': triaged_patient.systolic_blood_pressure,
                            'resp_rate': triaged_patient.minute_ventilation,
                            'heart_rate': triaged_patient.heart_rate,
                            'Sp_O_2': triaged_patient.pulse_oximetry,
                            'patient_cat': triaged_patient.patient_cat,
                            'triage_category': triaged_patient.vitals_nurseclinical_judgement,
                            'impression_diagnosis':None,
                            'action': None,
                            'outcome':None

                            })
            # populates the database table using the dictionary format.
            # uses the dot notation corresponding to patient object to add persistant data to the columns.
            # fields corresponding to the triaged patient are marked None corresponding to null in database
            self.conn.commit()

    def insert_patient_RemediedPL(self, remedied_patient_object):# separate copy to triaged table
        with self.conn:
            self.c.execute("""INSERT OR IGNORE INTO RemediedPatients VALUES (:fname,:lname,:dob,:ppsn, :address,:n_o_kin ,:mob_phone,
                           :presenting_symptoms,:date_created,:date_accessed,:on_oxygen,:systolicBP,
                           :resp_rate,:heart_rate,:Sp_O_2, :patient_cat, :triage_category,:impression_diagnosis,
                           :action,:outcome)"""
                           ,
                           {'fname': remedied_patient_object.patient_object.patient_object.first_name,
                            'lname': remedied_patient_object.patient_object.patient_object.last_name,
                            'dob': remedied_patient_object.patient_object.patient_object.date_of_birth,
                            'ppsn': remedied_patient_object.patient_object.patient_object.ppsn,
                            'address': remedied_patient_object.patient_object.patient_object.address,
                            'n_o_kin': remedied_patient_object.patient_object.patient_object.next_of_kin,
                            'mob_phone': remedied_patient_object.patient_object.patient_object.mobile_no,
                            'presenting_symptoms': remedied_patient_object.patient_object.patient_object.presenting_symptoms,
                            'date_created':remedied_patient_object.patient_object.patient_object.date_created,
                            'date_accessed': remedied_patient_object.patient_object.patient_object.date_updated,
                            'on_oxygen': remedied_patient_object.patient_object.is_the_patient_on_oxygen,
                            'systolicBP': remedied_patient_object.patient_object.systolic_blood_pressure,
                            'resp_rate': remedied_patient_object.patient_object.minute_ventilation,
                            'heart_rate': remedied_patient_object.patient_object.heart_rate,
                            'Sp_O_2': remedied_patient_object.patient_object.pulse_oximetry,
                            'patient_cat': remedied_patient_object.patient_object.patient_cat,
                            'triage_category': remedied_patient_object.patient_object.vitals_nurseclinical_judgement,
                            'impression_diagnosis':remedied_patient_object.diagnosis,
                            'action': remedied_patient_object.remedy,
                            'outcome':remedied_patient_object.conclusion

                            })
            # populates the database table using the dictionary format.
            # uses the dot notation corresponding to patient object to add persistant data to the columns.
            # fields corresponding to the triaged patient are marked None corresponding to null in database
            self.conn.commit()