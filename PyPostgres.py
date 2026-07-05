import psycopg2
class PyPostgres:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Exception as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return None
    def create_table(self):
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS emails (
                id SERIAL PRIMARY KEY,
                s44ubject TEXT NOT NULL,
                message TEXT NOT NULL,
                recipient_email TEXT NOT NULL
            );
            '''
            cursor.execute(create_table_query)
            connection.commit()
            cursor.close()
            connection.close()
    def insert_email(self, subject, message, recipient_email):
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            insert_query = '''
            INSERT INTO emails (subject, message, recipient_email)
            VALUES (%s, %s, %s);
            '''
            cursor.execute(insert_query, (subject, message, recipient_email))
            connection.commit()
            cursor.close()
            connection.close()
    def fetch_emails(self):
        list_emails = []
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            fetch_query = 'SELECT * FROM emails;'
            cursor.execute(fetch_query)
            emails = cursor.fetchall()
            for email in emails:
                print(f"ID: {email[0]}, Subject: {email[1]}, Message: {email[2]}, Recipient Email: {email[3]}")
                list_emails.append({
                    "id": email[0],
                    "subject": email[1],
                    "message": email[2],
                    "recipient_email": email[3]
                })
            cursor.close()
            connection.close()
            return list_emails
        return []