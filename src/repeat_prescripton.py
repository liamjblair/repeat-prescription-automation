from src import constants
import os
import smtplib
import dotenv
from src import logger

dotenv.load_dotenv()

class RepeatPrescription:

    def __init__(self, initials) -> None:
        self.initials = initials

    def get_patient_details(self):
        env_vars = dict(os.environ)
        # pull all patient details (eg name, address, email...) from environ variables based on intitials
        patient_details = {k: v for k,v in env_vars.items() if k.startswith(f"{self.initials}_")}

        self.name = patient_details.get(f"{self.initials}_NAME")
        self.dob = patient_details.get(f"{self.initials}_DOB")
        self.address = patient_details.get(f"{self.initials}_ADDRESS")
        self.email_address = patient_details.get(f"{self.initials}_EMAIL_ADDRESS")
        self.email_pass = patient_details.get(f"{self.initials}_EMAIL_PASS")

    def get_medication_list(self) -> list:
        env_vars = dict(os.environ)
        # pull medication list from environ variables based on intitials
        self.meds_list = [v for k,v in env_vars.items() if k.startswith(f"MED_{self.initials}_")]

    def contruct_email_body(self) -> str:
        chemist_name = constants.CHEMIST_NAME
        # format into a vertical list and indented for the email body
        formatted_meds_list = "\n            ".join(self.meds_list)

        self.email_body = f"""

            {self.name}    
            {self.dob}    
            {self.address}
                
            Hi, could I please have
                
            {formatted_meds_list}
            
            For {chemist_name}
                
            Thank you
            {self.name.split()[0]}

        """
        
    def send_email(self):

        # SMTP server configuration
        smtp_server = constants.SMTLIB_SERVER
        smtp_port = constants.SMTLIB_PORT

        sender_email = self.email_address
        sender_password = self.email_pass
        subject = "Prescription"
        receiver_email = constants.CHEMIST_EMAIL_ADDRESS

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            
            email_content = f"Subject: {subject}\n\n{self.email_body}"

            server.sendmail(sender_email, receiver_email, email_content)
            server.quit()

        except smtplib.SMTPAuthenticationError as e:
            logger.error(f"Authentication error: {e}")
        except smtplib.SMTPException as e:
            logger.error(f"An error occurred while sending the email: {e}.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}.")



