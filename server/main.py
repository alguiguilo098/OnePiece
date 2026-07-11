from fastapi import FastAPI
import server.EmailService as EmailService
from dto.LoginDTO import LoginDTO
from dto.SenderDTO import SenderDTO
from server.PyPostgres import PyPostgres
from dotenv import load_dotenv
import os

app = FastAPI()
cliente =EmailService.EmailService("","")
load_dotenv()

pyconn = PyPostgres(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", 5432)),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DB"))

pyconn.create_table()

@app.post("/login")
def login(login_dto: LoginDTO):
    global cliente
    cliente = EmailService.EmailService(login_dto.email, login_dto.password)
    return {"message": f"Client set: {cliente}"}

@app.post("/send_email")
def send_email(sender_dto: SenderDTO):
    if cliente is not None:
        cliente.send_email(sender_dto.subject, sender_dto.message, sender_dto.email)
        pyconn.insert_email(sender_dto.subject, sender_dto.message, sender_dto.email)        
        return {"message": "Email sent."}
    else:
        return {"error": "No client set. Please set a client first."}
    
@app.get("/emails")
def get_emails():
    emails = pyconn.fetch_emails()
    return {"emails": emails}

