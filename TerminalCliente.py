import os
from dotenv import load_dotenv
import requests
class ClienteTerminal:
    def __init__(self):
        load_dotenv()
        self.__host = os.getenv("serverip", "localhost")
        self.__port = int(os.getenv("port", 8000))
    def __sendmanyemail(self, subject, message, recipient_email):
        for email in recipient_email:
            requests.post(f"http://{self.__host}:{self.__port}/send_email", 
                            json={"subject": subject, "message": message, "email": email})
    def __authenticate(self, email, password):
        requests.post(f"http://{self.__host}:{self.__port}/login",
                      json={"email": email, "password": password})
        print(f"Authenticated with email: {email}") 
    def __send_email(self, subject, message, recipient_email):
        requests.post(f"http://{self.__host}:{self.__port}/send_email", 
                            json={"subject": subject, "message": message, "email": recipient_email})
    def  __list_emails(self):
        response = requests.get(f"http://{self.__host}:{self.__port}/emails")
        emails = response.json().get("emails", [])
        for i in range(len(emails)):
            email = emails[i]
            print(f"Email {i+1}:")
            print(f"  Subject: {email['subject']}")
            print(f"  Message: {email['message']}")
            print(f"  Recipient Email: {email['recipient_email']}")
            print()
    def run(self):
        while True:
            print("1. Authenticate")
            print("2. Send Email")
            print("3. List Emails")
            print("4. Exit")
            print("5. Send Many Emails")
            print()
            choice = input("Enter your choice: ")
            if choice == '1':
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                self.__authenticate(email, password)
            elif choice == '2':
                subject = input("Enter the subject: ")
                message = input("Enter the message: ")
                recipient_email = input("Enter the recipient's email: ")
                self.__send_email(subject, message, recipient_email)
                print(f"Email sent to {recipient_email} with subject: {subject}")
            elif choice == '3':
                self.__list_emails()
            elif choice == '4':
                print("Exiting...")
                break
            elif choice == '5':
                subject = input("Enter the subject: ")
                message = input("Enter the message: ")
                recipient_emails = input("Enter the recipient's emails (comma-separated): ").split(",")
                self.__sendmanyemail(subject, message, recipient_emails)
                print(f"Emails sent to {recipient_emails} with subject: {subject}")
            else:
                print("Invalid choice. Please try again.")
    
        
if __name__ == "__main__":
    terminal = ClienteTerminal()
    terminal.run()