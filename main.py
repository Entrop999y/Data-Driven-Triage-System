# set the date
from datetime import datetime
import datetime as dt  # create dates etc
from patient_file import PatientFile
from triage_score_cal import TriagedPatient
from list_management import PatientWalkInListManagement
from list_management import PatientHasSeenNurseManagement
from list_management import PatientHasSeenDoctorListManagement
from list_management import PatientHasSeenDoctorListManagement

from database_waiting_list_service import SQLService
from List_and_node import LinkedList
from remediedpatient import RemediedPatient

import sqlite3

# ***************************************import Modules section Above***********************

# reminder:fname,lname,dob,ppsn,address,n_o_kin,
#                  mob,presenting_symptoms
patient_1 = PatientFile("Neil", "Sewell", "10/05/1970", "12345F", "34 Whats Another year Avenue", "Ethel"
                        , "087999666", "chest pain", ("2021-12-15 10:29:23.141923"),
                        ("2021-12-15 11:39:23.141923"))
patient_2 = PatientFile("John", "Maher", "14/2/1945", "12345M", "43 Birch Avenue", "Mary",
                        "087999666", "chest pain", "2021-12-15 14:39:23.141923", "2021-12-15 14:39:23.141923")

patient_3 = PatientFile("Clifford", "Diamond", "25/6/68", "12346F", "24 Georgian Village ", "Grace ",
                        "087999664", "chest pain", "2021-12-15 13:36:24.141923", "2021-12-15 19:36:24.141923")

patient_4 = PatientFile("Frances", "Ormonde", "23/02/1991", "32314F", "12 Boiroimhe Lawns",
                        "Miriam", "0898723421", "Asthma Attack", ("2021-12-15 13:36:24.141923"),
                        ("2021-12-15 13:36:24.141923"))
patient_5 = PatientFile("Pat ", "Leahy", "13/10/2000", "233432M", "Tara Hills ", "Winnie",
                        "0867893412", "Got a bad hiddin", ("2021-12-11 13:40:24.141923"),
                        ("2021-12-15 13:40:24.141923"))

# *******************example data  three patients with similar presentation "Chest pain" for triage*******

# reminder : ,patient_object,on_oxygen,systolicBP,resp_rate,heart_rate,Sp_O_2,patient_cat,triage_cat
triage_2 = TriagedPatient(patient_2, "N", "143", "17", "100", "96", "6", "Yellow")
# the clinical algorithm suggests this patient with chest pain is relatively stable after Nurse assessment
# triage_2.patient_object.displayPatient() # test did it form right ....works ok !

triage_3 = TriagedPatient(patient_3, "Y", "110", "23", "113", "92", "11", "Red")
# this patient also presented with "chest pain" but because her requires oxygen, has high heart rate,
# still breathing with difficulty


# ***************sample triaged patients to populate the doctors list***********
# add hardwired patients to database


# ****************hardwired objects for development purposes above******************************************
waiting_list = SQLService('waiting_list.db')  # instantiating the hardcopy database
waiting_list.createDB()  # create the table headings and the mastercopy table of all interactions/procedures/tests
waiting_list.createWRLTable()  # create the second table for waiting room
waiting_list.createTPTable()  # create 3rd table for triaged patients only
waiting_list.createRPTable()  # 4th table for patients who have seen doctor, had procedure done or in ward or discharged

# basic insertion to master list table below
waiting_list.insert_patient_waiting(patient_1)
waiting_list.insert_patient_waiting(patient_2)
waiting_list.insert_patient_waiting(patient_3)
waiting_list.insert_patient_waiting(patient_4)
waiting_list.insert_patient_waiting(patient_5)  # and adding all 5 patients

# insertion of demo patients to Waiting Room Table
# basic insertion to master list table below
waiting_list.insert_patient_WRL(patient_1)
waiting_list.insert_patient_WRL(patient_2)
waiting_list.insert_patient_WRL(patient_3)
waiting_list.insert_patient_WRL(patient_4)
waiting_list.insert_patient_WRL(patient_5)  # and adding all 5 patients

# insert demo patients that have been triaged for demonstration purposes
waiting_list.insert_patient_triaged(triage_2)
waiting_list.insert_patient_triaged(triage_3)

ssl_1 = LinkedList()  # SLL_1 List holds queue of walk in patients waiting to see Triage Nurse
patients_in_waiting_room = PatientWalkInListManagement(ssl_1)  # pass the sll list to the patient list manager class
# add pre-loaded waiting room patients
patients_in_waiting_room.addPatientwalkinList(patient_4)  # add the walk in patients (sample data ) to them
patients_in_waiting_room.addPatientwalkinList(patient_5)  # add the walk in patients (sample data ) to them

patients_in_waiting_room.who_s_in_the_waiting_room()  # test to see if adding patients

# patient_walk_in_list.addPatientwalkinList(patient_1)
# test to see if can be displayed


patient_triaged_list = LinkedList()  # SLL_2List holds queue of triaged patients waiting to see Doctor
patient_triaged_list = PatientHasSeenNurseManagement(patient_triaged_list)
waiting_list.insert_patient_triaged(triage_2)  # inserting hardwired patients for demo
waiting_list.insert_patient_triagedPL(triage_2)  # insert to sepearate table for the demo
waiting_list.insert_patient_triaged(triage_3)  # inserting hardwired patients for demo
waiting_list.insert_patient_triagedPL(triage_3)  # insert to sepearate table for the demo

# create entry in tables to add the triage data for each patient object
patient_triaged_list.addPatienttriageList(triage_2)  # inserting hardwired patients for demo
patient_triaged_list.addPatienttriageList(triage_3)  # inserting hardwired patients for demo

patient_has_seen_doctor_list = LinkedList()  # SLL_3  holds queue of doctor assessed patients waiting to go ward/theatre or discharged
# instantiate the list_management object - I used the same name I realise now confusingly !

patient_has_seen_doctor_list = PatientHasSeenDoctorListManagement(patient_has_seen_doctor_list)

# ***********************************List Instantiating Area Above *************************************************

# *************** login *************section********code********


now = datetime.now()

print("*************************************************************************")
print("****************" + (now.strftime("%Y-%m-%d %H:%M:%S")) + "********************")

print("Welcome to HSE Frasier Crane Memorial A+E  ")
print("*************************************************************************")


# ******password menu *****function************************************************
def passwordMenu():
    print("Login Required to proceed: >> >>")
    print(" Type your UserID and Password  and press Return")
    login_details = ["User", "Password"]
    usr_ID = input("Input your user ID >> >>")
    paswrd = input("Input your Password")

    login_attempt = [usr_ID, paswrd]  # concatenate for search strategy
    print(login_attempt)
    if login_attempt[0] == login_details[0] and login_attempt[1] == login_details[1]:

        print("Success! Thank you for not hacking our system today")
        waiting_list = SQLService('waiting_list.db')
        waiting_list.createDB()
        # waiting_list.insert_patient_waiting(patient_1)  # append new entry to hard copy database
        # now the sll version of this list for the waiting room

        menuMain()
    else:
        print("Wrong User or password !\n Better try an obvious combination (hint)")


# ************** LOGIN MENU ABOVE ***********************************************************************


# ************************************ Background Processes Section  Above********************************
def enter_vitals():
    # apply the Copenhagen Triage Algorithm to prioritise each patient according to simple vital physiological measurements
    # blood pressure e.g. too low indicates bleed/shock; heart rate- too high indicates bleed
    # on oyxgen, SpO2 and breathes per minute indicate if respiratory failure will occur soon

    patient_score = 0  # create a variable int to store the patients score by default = 0
    # declare the physiological variables as global to allow instantiation of TriagedPatient in main

    # begin with respiratory vitals
    global systolic_blood_pressure

    global heart_rate

    global minute_ventilation

    global pulse_oximetry

    global is_the_patient_on_oxygen

    is_the_patient_on_oxygen = input("Is the patient requiring Oxygen currently (type Y/N)?>>>>")
    is_the_patient_on_oxygen = is_the_patient_on_oxygen.capitalize()  # make sure in capital

    if is_the_patient_on_oxygen == "Y":
        patient_score = patient_score + 4  # add 4 points to the patients score as requires oxygen mask
    else:
        patient_score = patient_score + 0

    pulse_oximetry = int(input("What is the patient's SpO2 level (Normal Range 94%-98% "
                               "on Room Air)>>>>"))
    if pulse_oximetry <= 94:
        patient_score = patient_score + 2  # add 2 points to the patient score as in danger of desaturating
    else:
        patient_score = patient_score + 0
    minute_ventilation = int(input("What is the patient's respiratory rate per minute?"
                                   "(Normal Range <22 per minute)>>>>"))
    if minute_ventilation >= 22:

        patient_score = patient_score + 3  # add 3 points to patient score as
    else:
        patient_score = patient_score + 0
        # enter cardiovascular vitals
    heart_rate = int(input("What is the patient's heart rate per minute?"
                           "(Normal Range <110 per minute)>>>>"))
    if heart_rate >= 110:
        patient_score = patient_score + 2  # add 2 points to score if heart rate is trying to compensate
    else:
        patient_score = patient_score + 0

    systolic_blood_pressure = int(input("Enter the Systolic (Upper) Reading from "
                                        "the Sphymanometer"
                                        "(Normal Range >100 mmHG)>>>>"))
    if systolic_blood_pressure <= 100:
        patient_score = patient_score + 3  # add 3 points for falling BP
    else:
        patient_score = patient_score + 0

    print(f"The patient score so far is {patient_score}")

    print(" You may also apply clinical judgement of your own to revise the patient category")

    # allows nurse apply clinical judgement to alter Green vs Yellow vs Orange vs Red status
    # append this information to the patient_object by instantiating a new revised patient object the triaged_patient

    patient_category(patient_score)  # pass onto the next function which interprets the patient score clinically

    return patient_score, systolic_blood_pressure, heart_rate, minute_ventilation, pulse_oximetry, is_the_patient_on_oxygen


def patient_category(patient_score):
    # this function interprets the triage score above,categorises it into clinical "intervals", red, green etc
    # then allows the nurse an opportunity to modify this score producing triage_cat final int variable
    # It then instantiates a new TraiagedPatient Object and adds to its corresponding list

    global patient_triaged, clinical_judgement
    global patient_cat
    # an attempt to access these variables in main in the if loops below but proved easier
    # to perform tasks within this function

    if patient_score <= 1:  # green category (can only be 0 if true)

        print("This patient is a category Green Patient:\n "
              "This means their condition is stable,\n"
              "non urgent and they required re-evaluation every 180 minutes.\n "
              "As Triage Nurse you may apply \n clinical judgement to raise their triage"
              " score by 3 points(up one level) \nor by 6 points (up two levels)")
        try:
            clinical_judgement = int(
                input("Please indicate your choice by inputting\n "
                      "0 (stay same level),\n"
                      " 3 (move up one level)\n"
                      "or 6 (move up two levels)\n"))
        except:
            print('You have entered an invalid value.')


        patient_cat = int(patient_score + clinical_judgement)
        # we need to produce a triaged patient category for
        # the triaged patient object to update the status after nurse assessment
        if patient_cat <= 1:
            patient_triaged = "Green"
        elif 2 <= patient_cat <= 3:
            patient_triaged = "Yellow"

        elif 4 <= patient_cat <= 7:
            patient_triaged = "Orange"
        elif 8 <= patient_cat <= 14:
            patient_triaged = "Red"
        print(f" The final category for the patient is {patient_triaged}")

        # return patient_triaged, patient_cat  # blank string to hold
        # final category red vs orange vs yellow vs green
    elif 2 <= patient_score and patient_score <= 3:
        # choosing range for category yellow and delivering the protocol advice before nurse adds clinical judgement

        print("This patient is a category Yellow Patient:"
              " This means their condition is potentially unstable, urgent and "
              " they required re-evaluation every 60 minutes. As Triage Nurse"
              " you may apply clinical judgement to raise their triage score by 3 points(up one level)"
              " or by 6 points (up two levels) or decrease by one level by adding -3")
        try:
            clinical_judgement = int(
                input("Please indicate your choice by inputting:\n"
                      " 0 (stay same level),\n"
                      " 3 (move up one level)\n"
                      "or 6 (move up two levels) or \n"
                      "-3 (downgrade patient category by one level"))

        except:
            print('You have entered an invalid value.')


        patient_cat = int(patient_score) + int( clinical_judgement)
        # we need to produce a triaged patient category for
        # the triaged patient object to update the status after nurse assessment
        if patient_cat <= 1:
            patient_triaged = "Green"
        elif 2 <= patient_cat <= 3:
            patient_triaged = "Yellow"

        elif 4 <= patient_cat <= 7:
            patient_triaged = "Orange"
        elif 8 <= patient_cat <= 14:
            patient_triaged = "Red"
        print(f" The final category for the patient is {patient_triaged}")


    elif 4 <= patient_score and patient_score <= 7:
        # choosing range for category orange (4-7)
        # and delivering the protocol advice before nurse adds clinical judgement
        print("This patient is a category Orange Patient:\n"
              " This means their condition is Emergent\n"
              " and they are critically ill:they required re-evaluation every 15 minutes.\n"
              " As Triage Nurse"
              " you may apply clinical judgement \n to raise their triage score by 3 points(up one level)"
              " or decrease by one level by adding -3")
        try:# error handling for non int input
            clinical_judgement = int( input("Please indicate your choice by inputting:\n"
                      " 0 (stay same level),\n "
                      "3 (move up one level to Red) or\n "
                      "-3 (downgrade patient category by one level to Yellow"))

        except:
            print('You have entered an invalid value.')

        patient_cat = int(patient_score + clinical_judgement)

        # we need to produce a triaged patient category for
        # the triaged patient object to update the status after nurse assessment

        if patient_cat <= 1:
            patient_triaged = "Green"
        elif 2 <= patient_cat <= 3:
            patient_triaged = "Yellow"

        elif 4 <= patient_cat <= 7:
            patient_triaged = "Orange"
        elif 8 <= patient_cat <= 14:
            patient_triaged = "Red"
        print(f" The final category for the patient is {patient_triaged}")





    elif 8 <= patient_score and patient_score <= 14:

        # choosing range for category Red
        # but this time Nurse can't apply judgement as the physiological measurements indicate likely will
        # die if not brought to resuss room

        print("This patient is a category Red Patient: \n"
              "This means their condition is Life-threatening\n"
              "Please transfer to Resuss Immediately\n and bleep the intensivest on-call")
        # the vital signs prohibit the nurse from altering the Copenhagen Score

        patient_cat = int(patient_score)
        patient_triaged = "Red"

    priority_patient = patients_in_waiting_room.see_the_next_patient()  # access the method to obtain the head node
    # of sll1
    # print(priority_patient)
    patients_in_waiting_room.remove_triaged_patient()

    triaged_patient = TriagedPatient(priority_patient, is_the_patient_on_oxygen, systolic_blood_pressure
                                     , minute_ventilation
                                     , heart_rate, pulse_oximetry, patient_cat, patient_triaged)
    print(f" The final category for the patient is {patient_triaged}")
    # pass the patient object to triaged patient object adding the vital stats to instantiate

    # display a summary of what has been changed so far before asking to commit to database

    print(f"The following Information was updated after Triage for\n"
          f"{triaged_patient.patient_object.first_name} {triaged_patient.patient_object.first_name}:"
          f" \n {triaged_patient.displayTriagedPatient()}")

    waiting_list.insert_patient_triaged(triaged_patient)
    waiting_list.insert_patient_triagedPL(triaged_patient)
    # create entry in tables to add the triage data for each patient object
    patient_triaged_list.addPatienttriageList(triaged_patient)  # add to the SLL2 list

    # TriagedPatient.displayTriagedPatient()
    # placeholder...now ask if they want to commit this to the database
    # now remove the triaged
    # patient from the initial patient list and transfer to the triaged patient list

    return patient_triaged, patient_cat

    # print(patient_cat)


# ************************************ Functional Section  Above********************************

def menuMain():
    while True:
        now = datetime.now()
        print(
            "*********************************************************************************************************")
        print("****************" + (now.strftime("%Y-%m-%d %H:%M:%S")) + "**************************************"
                                                                         "********************************")
        print(
            "*********************************************************************************************************")
        print("***************              Access Granted       "
              "****************************************************************\n")

        print(
            "                                 Main Menu                                                 \n \n         ")

        print(" 1.Record Patient details at Reception (before triage)"
              " \n 2. A+E Nurse Triage \n 3. Doctor Treatment/ Referral \n 4. "
              "View Waiting List Priority   ")

        choice = eval(input("Enter your choice (1->4) or 'Exit' and press return"))
        if (choice == 1):  # Hi, let me take your details first
            print("************ New Patient Details: Add Patient***********************************************   ")
            # reminder:fname,lname,dob,ppsn,address,n_o_kin,
            #                  mob,presenting_symptoms

            last_name = input(" Please enter the new patients's Last name :\n")
            first_name = input(" Please enter the new patient's First name :\n")
            date_of_birth = input(" Please enter the new patient's Date of Birth DD/MM/YYYY :\n")
            address = input(" Please enter the new patient's home Address   :\n")
            ppsn = input(" Please enter the new patient's PPSN No.:\n")
            phone_mobile = input(" Please enter the new patient's Mobile Phone Number :\n")
            next_of_kin = input(" Enter Patients Next of Kin  :\n")
            presenting_symptoms = input(" Enter Patients presenting symptoms in their pwn words e.g. 'chest pain'  :\n")
            date_created = now.strftime("%Y-%m-%d %H:%M:%S")
            date_last_accessed = now.strftime("%H:%M:%S")  # "%Y-%m-%d %H:%M:%S"
            # order of instatiation:fname,lname,dob,ppsn,address,n_o_kin,
            #                  mob,presenting_symptoms,date_created,date_accessed
            # instantiate the new patient object
            n_patient = PatientFile(first_name, last_name, date_of_birth, ppsn, address, next_of_kin,
                                    phone_mobile, presenting_symptoms, date_created,
                                    date_last_accessed)
            waiting_list.insert_patient_waiting(n_patient)  # append new entry to hard copy database
            waiting_list.insert_patient_WRL(n_patient)  # append to Waiting List Room Hard Copy Table

            patients_in_waiting_room.addPatientwalkinList(n_patient)  # insert new atient to SLL

            n_patient.displayPatient()

        elif (choice == 2):  # the nurse is calling you !
            print(" The following patient has waited the longest to be triaged and is up next")
            try:
                patients_in_waiting_room.see_the_next_patient()  # return the first patient with method
                # priority_patient=patients_in_waiting_room.choose_priority_patient_WaitingRoom()
                # apply method to patients in waiting room according to who arrived first and has not been triaged

                # print(f"The following Information was gathered on admission for "
                # f"this patient: {patient_1.displayPatient()}")
                # print(" Please enter the patient's vitals in order to triage this patient")
                # above is test with sample patient
                # **************************** indicate patient longest in waiting room to Triage Nurse****
                enter_vitals()
            except:
                print("No more patients to triage")






        elif (choice == 3):  # "you're next to see the doctor"
            try:
                doctor_priority_patient = patient_triaged_list.choose_priority_patient_for_doctor()
                print(f" The following patient has has been assessed as the priority patient and is up next\n"
                      f"{doctor_priority_patient.patient_object.first_name}  "
                      f"{doctor_priority_patient.patient_object.last_name}")

                remedy_1 = input("Having taken the history of the presenting complaint and examined the patient\n"
                                 "what is your impression or provisional diagnosis?")  # mimics the situation where the
                # doctor has suppossedly performed a clinical examination and made a diagnosis albeit provisional
                remedy_2 = input(" Summarise the action taken (e.g. transferred to theatre for emergency operation)\n"
                                 "by you for patient treatment >>> >>>")  # expected reply something
                # like "sent to plaster room for
                # cast" type of stuff or "found a bed on St. Theresas ward" or "sent for angioplasty and stenting"
                remedy_3 = input("Briefly summarise the patient outcome \n 1. Admitted to ward for observation\n"
                                 "2. discharged home with prescription\n "
                                 "3. Passed away ,\n"
                                 " 4. Sent to theatre for emergency procedure>>> >>> ")
                # instantiate the final patient object
                remedied_patient = RemediedPatient(doctor_priority_patient, remedy_1, remedy_2, remedy_3)

                # add to the patient_has_seen_the_doctor SLL_3 list
                patient_has_seen_doctor_list.addPatientdoctorSeen(remedied_patient)

                # add to the hard copy tables
                # waiting_list.insert_patient_waiting(remedied_patient)
                waiting_list.insert_patient_RemediedPL(remedied_patient)

                # display summary for patient
                remedied_patient.displayRemediedPatient()
            except:
                print("No more patients to triage !")

                # write to the database hard copy









        elif (choice == 4):
            print("*********Priority Queues Frasier Crane Memorial A &E *******************")
            print("****************" + (now.strftime("%Y-%m-%d %H:%M:%S")) + "********************")
            choose=choice = eval(input(" Choose from the following Menu Options:\n "
                           "1. People waiting to see nurse \n"
                           "2. People waiting to see the doctor\n"
                           " Please type 1 or 2 as appropriate and press return\n>>> >>"))
            if (choose == 1):



                patients_in_waiting_room.who_s_in_the_waiting_room()
            elif (choose == 2):
                print("The following Patients have been triaged: \n")
                print(patient_triaged_list.who_s_waiting_to_see_Doctor())

                print("And the next patient to see the doctor will be: \n")



                patient=patient_triaged_list.choose_priority_patient_for_doctor()
                print(patient.displayTriagedPatient())
            else:
                print("Please choose an option by inputting a number")
        else:# program exits if any key other than a number 1-4 is picked

            break

    # *******************************Main menu display above ********************


# *********************MAIN MENU ABOVE ************************************
passwordMenu()

# *********** CALL FUNCTIONS MENU ABOVE*****************************************
