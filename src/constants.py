import dotenv
import os

dotenv.load_dotenv()

LB_NAME=os.getenv("LB")
MB_NAME=os.getenv("MB")

LB_DOB=os.getenv("LB_DOB")
MB_DOB=os.getenv("MB_DOB")

LB_EMAIL_ADDRESS=os.getenv("LB_EMAIL_ADDRESS")
LB_EMAIL_PASS=os.getenv("LB_EMAIL_PASS")

MB_EMAIL_ADDRESS=os.getenv("MB_EMAIL_ADDRESS")
MB_EMAIL_PASS=os.getenv("MB_EMAIL_PASS")

CHEMIST_EMAIL_ADDRESS=os.getenv("CHEMIST_EMAIL_ADDRESS")
CHEMIST_NAME=os.getenv("CHEMIST_NAME")

ADDRESS=os.getenv("ADDRESS")
