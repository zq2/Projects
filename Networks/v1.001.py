import random
import time

# Database simulation
students = {
    "student1": {"name": "Alice", "ip": "192.168.1.10", "otp": None},
    "student2": {"name": "Bob", "ip": "192.168.1.11", "otp": None},
    "student3": {"name": "Charlie", "ip": "192.168.1.12", "otp": None}
}

# Simulating the correct network IP for the campus
campus_network_ip = "192.168.1.0/24"

def generate_otp():
    """Generates a random 6-digit OTP."""
    return random.randint(100000, 999999)

def is_on_campus(ip_address):
    """Verifies if the student is on the campus network."""
    return ip_address.startswith("192.168.1.")

def send_otp(student_id):
    """Sends OTP to the student's registered device."""
    otp = generate_otp()
    students[student_id]['otp'] = otp
    print(f"OTP for {students[student_id]['name']} is {otp}")

def verify_otp(student_id, entered_otp):
    """Verifies the entered OTP against the one stored for the student."""
    return students[student_id]['otp'] == entered_otp

def mark_attendance(student_id, ip_address):
    """Marks attendance if the student is on campus and OTP is valid."""
    if is_on_campus(ip_address):
        print(f"{students[student_id]['name']} is on campus. Sending OTP...")
        send_otp(student_id)
        otp_input = input("Enter the OTP sent to your device: ")
        
        if verify_otp(student_id, int(otp_input)):
            print(f"Attendance marked for {students[student_id]['name']}.")
        else:
            print("Invalid OTP. Attendance not marked.")
    else:
        print(f"{students[student_id]['name']} is not on campus. Attendance not marked.")

# Example usage
ip_address_input = input("Enter your IP address: ")
student_id_input = input("Enter your student ID (e.g., student1, student2): ")
mark_attendance(student_id_input, ip_address_input)
