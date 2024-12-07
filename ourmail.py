import os
from dotenv import load_dotenv
from mailjet_rest import Client

load_dotenv()

api_key = os.getenv("MAIL_API_KEY")
api_secret = os.getenv("MAIL_SECRET_KEY")

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

from_mail = os.getenv("FROM_MAIL")
to_email = os.getenv("TO_MAIL")

def send_mail(name, cName, email, phNo, service, sMessage):
    
    subject = f"Inquiry from {name} Regarding {service}"
    text_content = f"""\
    Hello,

    You have received a new inquiry through your website's mailing system. Below are the details:

    **Name:** {name}  
    **Company Name:** {cName}  
    **Email:** {email}  
    **Phone Number:** {phNo}  
    **Service Interested In:** {service}  

    **Message:**  
    {sMessage}


"""

    message = {
    'Messages': [
            {
                "From": {
                    "Email": from_mail,  
                    "Name": "Luminare Digital"
               },
                "To": [
                    {
                        "Email": to_email
                    }
                ],
                "Subject": subject,
                "TextPart": text_content
            }
        ]
    }

    result = mailjet.send.create(data=message)

    if result.status_code == 200:
        print("Mail sent successfully!")
    else:
        print(f"Failed to send email. Status code: {result.status_code}")
        