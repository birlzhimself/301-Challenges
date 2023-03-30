#!/usr/bin/python3

#Script:   Ops Challenge: Class 13 - Python Collections 
#Purpose:  Evaluate how a web server responds to outside requests.
#Why:      Lear to communicate with web servers to create the interactive web sites

import requests

# Prompt user for URL and HTTP method
url = input("Enter URL: ")
method = input("Enter HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Prompt user for authentication credentials
username = input("Enter username: ")
password = input("Enter password: ")

# Confirm request with user
print(f"\nSending {method} request to {url}\n")
confirmation = input("Press Y to confirm or any other key to cancel: ")
if confirmation.lower() != "y":
    print("Request cancelled.")
    exit()

# Send request with authentication using requests library
response = requests.request(method, url, auth=(username, password))

# Print response status code and reason
print(f"\nResponse Status Code: {response.status_code} ({response.reason})")

# Translate status codes to plain terms
status_codes = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}
if response.status_code in status_codes:
    print(f"Status: {status_codes[response.status_code]}")
else:
    print("Status: Unknown")

# Print response headers
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
