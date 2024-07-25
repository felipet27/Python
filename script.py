import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Configuración
SERVER_URL = 'https://example.com/'
SENDGRID_API_KEY = 'TU_SENDGRID_API_KEY'
FROM_EMAIL = 'tu-email@ejemplo.com'
TO_EMAIL = 'destinatario@ejemplo.com'

def servidor(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"El servidor {url} está funcionando correctamente.")
            return True
        else:
            print(f"El servidor {url} presento una comunicacion inesperada: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Error al intentar conectarse con el servidor {url}: {e}")
        return False

def notificacion(api_key, from_email, to_email, subject, content):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f"Notificación enviada y el estado: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar la notificación: {e}")

if __name__ == "__main__":
    if not servidor(SERVER_URL):
        notificacion(
            SENDGRID_API_KEY,
            FROM_EMAIL,
            TO_EMAIL,
            "Servidor web caído",
            f"El servidor {SERVER_URL} no está respondiendo correctamente, se seguirá monitoreando."
        )
