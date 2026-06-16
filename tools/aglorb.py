import subprocess
import sys

print("⚡ Welcome to Glorb for ADB. Type 'glorbexit' to leave. ⚡")

while True:
    try:
        # Get user command
        user_input = input("ADB> ").strip()
        
        # Exit condition
        if user_input.lower() == "glorbexit":
            print("Goodbye!")
            break
            
        # Skip empty inputs
        if not user_input:
            continue
            
        # Combine 'git' with user arguments and run it
        full_command = f"adb {user_input}"
        subprocess.run(full_command, shell=True)
        
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
