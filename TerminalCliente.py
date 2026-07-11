
class ClienteTerminal:
    def __init__(self, name):
        self.name = name
    def authenticate(self, email, password):
        self.email = email
        self.password = password
    def send_email(self, subject, message, recipient_email):
        self.subject = subject
        self.message = message
        self.recipient_email = recipient_email
        
    def run(self):
        while True:
            print(f"Welcome to {self.name} Terminal")
            print("1. Authenticate")
            print("2. Send Email")
            print("4. list Emails")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                self.authenticate(email, password)
                print(f"Authenticated as {self.email}")
            elif choice == '2':
                if not hasattr(self, 'email') or not hasattr(self, 'password'):
                    print("Please authenticate first.")
                    continue
                subject = input("Enter the subject: ")
                message = input("Enter the message: ")
                recipient_email = input("Enter the recipient's email: ")
                self.send_email(subject, message, recipient_email)
                print(f"Email sent to {self.recipient_email}")
            elif choice == '3':
                if not hasattr(self, 'email') or not hasattr(self, 'password'):
                    print("Please authenticate first.")
                    continue
                # Placeholder for listing emails
                print("Listing emails...")
            elif choice == '4':
                print("Listing emails...")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

