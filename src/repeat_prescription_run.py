from src.repeat_prescripton import RepeatPrescription

def run():

    patient_initials = "LB"

    presciption  = RepeatPrescription(patient_initials)
    presciption.get_patient_details()
    presciption.get_medication_list()
    presciption.contruct_email_body()
    presciption.send_email()


