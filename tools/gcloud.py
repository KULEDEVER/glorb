import subprocess
import sys

print("⚡ Welcome to Glorb for Google Cloud. Type 'glorbexit' to leave. ⚡")

while True:
    try:
        # Get user command
        user_input = input("Google Cloud> ").strip()
        
        # Exit condition
        if user_input.lower() == "glorbexit":
            print("Goodbye!")
            break
            
        # Skip empty inputs
        if not user_input:
            continue
            
        # Combine 'git' with user arguments and run it
        full_command = f"gcloud {user_input}"
        subprocess.run(full_command, shell=True)
        
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
