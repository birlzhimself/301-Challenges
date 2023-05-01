#!/usr/bin/python3

#Script:   Ops Challenge: Class 12 - Python Collections 
#Purpose:  Prompt the user to type a string input as the variable for your destination URL.
#Why:      Learn how to print information to the screen depending on if the condition is met.import requests

# Prompt the user to enter a destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP method
http_method = input("Select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the entire request to the screen and ask for confirmation
print(f"Sending {http_method} request to {url}")
confirmation = input("Confirm? (y/n): ").lower()

if confirmation == "y":
    # Perform the HTTP request using the requests library
    response = requests.request(http_method, url)

    # Print the plain terms of the status code
    status_code = response.status_code
    if status_code == 200:
        status = "OK"
    elif status_code == 201:
        status = "Created"
    elif status_code == 204:
        status = "No Content"
    elif status_code == 400:
        status = "Bad Request"
    elif status_code == 401:
        status = "Unauthorized"
    elif status_code == 403:
        status = "Forbidden"
    elif status_code == 404:
        status = "Site not found"
    elif status_code == 500:
        status = "Internal Server Error"
    else:
        status = "Unknown"
    print(f"Status code: {status_code} ({status})")

    # Print the response headers to the screen
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
else:
    print("Request cancelled.")
