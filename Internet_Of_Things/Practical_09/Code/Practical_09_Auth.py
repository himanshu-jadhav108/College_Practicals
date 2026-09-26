# Practical 9: Password-Protected Smart Sensor System Using SHA-256
import hashlib
import random

STORED_HASH = hashlib.sha256("IoT@123".encode()).hexdigest()
MAX_ATTEMPTS = 3

def read_sensor():
    return {"temperature": round(random.uniform(26, 31), 1),
            "humidity": round(random.uniform(50, 65), 1)}

def authenticate_and_read(attempts_passwords):
    print(f"Stored SHA-256 hash: {STORED_HASH[:32]}...")
    print("=== Smart Sensor Login ===")
    attempts_left = MAX_ATTEMPTS
    for pw in attempts_passwords:
        print(f"Enter password: {pw}")
        pw_hash = hashlib.sha256(pw.encode()).hexdigest()
        if pw_hash == STORED_HASH:
            print("Access Granted")
            print("Sensor Data:", read_sensor())
            return
        else:
            attempts_left -= 1
            print(f"Access Denied ({attempts_left} attempts left)")
            if attempts_left == 0:
                print("Account locked: too many failed attempts")
                return

if __name__ == "__main__":
    print("--- Test Run 1: Successful Auth ---")
    authenticate_and_read(["wrong1", "admin", "IoT@123"])
    print("
--- Test Run 2: Lockout ---")
    authenticate_and_read(["abc", "xyz", "12345"])
