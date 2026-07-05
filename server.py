from fastapi import FastAPI
import Cliente
from dto.LoginDTO import LoginDTO
from dto.SenderDTO import SenderDTO
app = FastAPI()
cliente =Cliente.Cliente("","")


@app.post("/login")
def login(login_dto: LoginDTO):
    global cliente
    cliente = Cliente.Cliente(login_dto.email, login_dto.password)
    return {"message": f"Client set: {cliente}"}

@app.post("/send_email")
def send_email(sender_dto: SenderDTO):
    if cliente is not None:
        cliente.send_email(sender_dto.subject, sender_dto.message, sender_dto.email)
        return {"message": "Email sent."}
    else:
        return {"error": "No client set. Please set a client first."}

