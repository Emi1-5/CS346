# auth_script.py
import requests
import passwords  # Import the passwords.py module

# Use the credentials from passwords.py
username = passwords.username
password = passwords.password

# URL for HTTP Basic Authentication (Replace with the correct URL you are working with)
url = "http://localhost:9090/basic-auth/user/pass"

# Send the request with authentication
response = requests.get(url, auth=(username, password))

# Check the response status
if response.status_code == 200:
    print("Authentication successful!")
else:
    print(f"Failed to authenticate: {response.status_code}")

