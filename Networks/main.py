import requests # Import the requests library for making HTTP requests

def check_ip_address(desired_ip):
    try:
        # Get the current IP address from a public API
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status() # Raise an exception for non-200 status codes

        current_ip = response.json()['ip'] # Extract the current IP address from the JSON response

        if current_ip == desired_ip: # Compare the current IP with the desired IP
            return True
        else:
            return False
    # Handle potential errors during the request
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return False

# Test usage
desired_ip = '143.60.76.30'  # IP of mcs.uvawise.edu
if check_ip_address(desired_ip):
    print("The current IP address matches the desired IP address.")
else:
    print("The current IP address does not match the desired IP address.")