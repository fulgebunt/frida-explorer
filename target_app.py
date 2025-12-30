# target_app.py
import time
import sys

def check_license():
    """
    This is the function we will hook.
    It's supposed to return False, but we will force it to return True.
    """
    print("[App] Checking license server... (This is the real function)")
    return False

def main():
    print("[App] Application starting...")
    is_licensed = check_license()

    if is_licensed:
        print("[App] SUCCESS: License is valid. Welcome, Premium User!")
    else:
        print("[App] FAILURE: License is invalid. Running in limited mode.")
        sys.exit(1) # Exit with an error code

    print("[App] Doing premium work...")
    time.sleep(2)
    print("[App] Work finished.")

if __name__ == "__main__":
    main()