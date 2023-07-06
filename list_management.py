from patient_file import PatientFile # need to access methods from

from List_and_node import LinkedList
from List_and_node import Node
from datetime import datetime
#from SLL import SLL


class PatientWalkInListManagement:
    def __init__(self,sll_1):
        #self.patient_object=patient_object
        self.patient_walk_in_list=sll_1 # will prioritise vs time of walk in



    def addPatientwalkinList(self, patient_object):
        self.patient_walk_in_list.append(patient_object)  # append the contact object to the list
        # will have method to display patients in the waiting room who have walked in




    def who_s_in_the_waiting_room(self):  # display waiting room list
        global tmp_patient
        current_size = self.patient_walk_in_list.size()
        counter = 1
        while counter <= current_size:
            tmp_node = self.patient_walk_in_list.get_node(counter)
            tmp_patient = tmp_node.get_obj()
            tmp_patient.displayPatient()
            counter = counter + 1
        return tmp_patient

    def see_the_next_patient(self):
        try:# need a method os avoiding crash as the sll is empty but the function in main has called it
            # not really a priority list more of a stack where we pop from the bottom (those longest in waiting room)
            tmp_node = self.patient_walk_in_list.get_node(1)  # in this case, the patients in the waiting room are
            # triaged according to the time they arrived and so we access node 1
            priorty_patient = tmp_node.get_obj()  # we get the patient details from the node so nurse can triage and
            # pass onto the patient triaged list
            priorty_patient.displayPatient()  # we show the priority patient to the nurse to read
        except:
            print("No more patients in waiting room")


        return priorty_patient # transfer the patient data to the nurse for triage

    def remove_triaged_patient(self):
        self.patient_walk_in_list.pop_front()  # then remove the priority patient from the first node position








#************************************************** Above Class to record basic walkin patient list & methods

class PatientHasSeenNurseManagement:
    def __init__(self, SLL_2):
        self.patient_triaged_list = SLL_2  # will prioritise vs patient_category score from the algorithm

    def addPatienttriageList(self,triaged_patient):
        # add triaged patient to the SLL list
        self.patient_triaged_list.append(triaged_patient)



    def who_s_waiting_to_see_Doctor(self):#display triaged patients list
        current_size=self.patient_triaged_list.size()
        counter=1
        while counter <=current_size:
            tmp_node=self.patient_triaged_list.get_node(counter)
            tmp_patient=tmp_node.get_obj()
            tmp_patient.patient_object.displayPatient()

            counter=counter+1


    def choose_priority_patient_for_doctor(self):
        doctor_priority_patient=None # create variable to store priority patient
        # priority patient = with highest patient_cat score
        position_of_dpp=0 # start off counter for position of priority patient

        current_size = self.patient_triaged_list.size()
        counter = 1
        while counter <= current_size:# while the linked list is being traversed from start to finish
            tmp_node=self.patient_triaged_list.get_node(counter)
            tmp_doc_priority_pat=tmp_node.get_obj() # extract the data from each node

            if doctor_priority_patient == None:

                doctor_priority_patient = tmp_doc_priority_pat
                position_of_dpp=1

            else:

                if int(tmp_doc_priority_pat.patient_cat)>int(doctor_priority_patient.patient_cat):# if I don't add int
                    # it compares as string only!

                    doctor_priority_patient=tmp_doc_priority_pat
                    position_of_dpp=counter
            counter = counter + 1
        self.patient_triaged_list.pop_any(position_of_dpp) #### remove from triage list as part of method using SLL


        return doctor_priority_patient

#********************************Above a Class to manage triaged patients sll list and methods********************

class PatientHasSeenDoctorListManagement:
    def __init__(self,SLL_3):

        self.patient_has_seen_doctor_list=SLL_3

    def addPatientdoctorSeen(self,triaged_patient):
        # method to add patient to third list category
        self.patient_has_seen_doctor_list.append(triaged_patient)

    def who_s_seen_the_Doctor(self): #display ward waiting list/discharged list

        current_size=self.patient_has_seen_doctor_list()
        counter=1
        while counter <=current_size:
            tmp_node=self.patient_has_seen_doctor_list.get_node(counter)
            tmp_patient=tmp_node.get_obj()
            tmp_patient.displayPatient()
            counter=counter+1




#****************************above a class to manage patients who have seen the doctor as a sll list*****************