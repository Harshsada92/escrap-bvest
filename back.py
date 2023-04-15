from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import mysql.connector
from mysql.connector import Error

# Function to check if a user exists in the database
def check_user(username, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='harsh',
            user='root',
            password='1234'
        )
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            # Execute the SQL query
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            # Check if the user exists in the database
            if cursor.fetchone() is not None:
                return True
            else:
                return False
        else:
            print("Could not connect to database")
            return False
    except Error as e:
        print("Error while connecting to database", e)
        return False
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Define the HTTP request handler class
class MyHandler(BaseHTTPRequestHandler):
    
    # Function to handle GET requests
    def do_GET(self):
        # Parse the URL and extract the query parameters
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        # Check if the user is trying to log in
        if 'username' in params and 'password' in params:
            # Get the username and password from the query parameters
            username = params['username'][0]
            password = params['password'][0]
            # Check if the user exists in the database
            if check_user(username, password):
                # Return a success page
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Login successful</h1></body></html>')
            else:
                # Return an error page
                self.send_response(401)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Invalid username or password</h1></body></html>')
        else:
            # Return the login page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Login</h1><form method="get" action="/"><label>Username:</label><input type="text" name="username"><br><label>Password:</label><input type="password" name="password"><br><input type="submit" value="Log in"></form></body></html>')
            
# Create an HTTP server and bind it to a port
port = 8080
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)
print(f'Starting server on port {port}...')
httpd.serve_forever()