"""
http_status_codes.py
Author: ITP 150 Ashlee Raya
Date Created: July 7, 2026
This program uses Python's match structure to set a description for an
HTTP server status code. The user enters the status code and a short description
indicates if the request for the resource succeeded or failed for the following
status codes. An unknown status code results in an Unknown description.
200 (OK): The request has succeeded.
201 (Created): Request has been fulfilled and a new resource has been created.
301 (Moved Permanently): Requested resource was permanently moved to a new URL.
302 (Found): Requested resource was temporarily moved to a different URL.
404 (Not Found): The server cannot find the requested resource.
"""

status_code = int(input('Please enter the status code:'))
# determines description of HTTP status code or "Unknown" if not found.
match status_code:
case 200:
    description = "(OK): The request has succeeded."
case 201:
    description = ("(Created): Request has been fulfilled and a new "
                  "resource has been created.")
case 301:
    description = ("(Moved Permanently): Requested resource was "
                    "permanently moved to a new URL.")
     case 302:
        description = ("(Found): Requested resource was temporarily moved to a"
                       "different URL.")
    case 404:
        description = ("(Not Found): The server cannot find the requested "
"resource.")
    case _:
        description = "Unknown" # Default case

print(f"Status Code: {status_code}, Description: {description}")