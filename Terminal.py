from  Cliente import Cliente
class Terminal:
    def __init__(self):
        self.__cliente=None
    def __set_cliente(self,cliente:Cliente):
        self.__cliente=cliente
    def __login(self,email,password,nickname):
        self.__set_cliente(Cliente(email,password,nickname))
        print(f"Client set: {self.__cliente}")
    def __send_email(self,email,subject,message):
        if self.__cliente is not None:
            self.__cliente.send_email(subject,message,email)
        else:
            print("No client set. Please set a client first.")

    def start(self):
        while True:
            print(f"{self.__cliente}>",end="")
            input_str = input()
            parts = input_str.split("-")
            if input_str.lower() == "exit":
                print("Exiting terminal.")
                break
            if parts[0].lower() == "login" and len(parts) == 4:
                    email = parts[1]
                    password = parts[2]
                    nickname = parts[3]

                    self.__login(email, password, nickname)
            elif parts[0].lower() == "send" and len(parts) == 4:
                    email = parts[1]
                    subject = parts[2]
                    message = parts[3]
                    self.__send_email(email, subject, message)
            elif self.__cliente is None:
                print("No client set. Please set a client first.")  
if __name__ == "__main__":
    terminal = Terminal()
    terminal.start()