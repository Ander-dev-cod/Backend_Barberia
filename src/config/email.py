import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Cargar variables desde el archivo .env
load_dotenv()

def send_email(to_email: str, subject: str, template_id: str, content: str, data: dict) -> bool:
   
    message = Mail(
        from_email=os.getenv("MAIL_FROM"),  #  correo 
        to_emails=to_email, # destinatario
        subject=subject,  # asunto
        html_content=content     # contenido del correo 
    )
    
    # se pueden con plantillas ingresando a samgrid y creandolas
   
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code == 202
    except Exception as e:
        print(f"[ERROR] Falló el envío a {to_email}: {e}")
        return False
