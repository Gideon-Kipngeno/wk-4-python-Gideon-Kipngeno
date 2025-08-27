"""
Error Handling Lab
- Asks the user for a filename
- Reads and prints its content
- Handles errors if file does not exist
"""

filename = input("Enter the filename to read: ")

try:
    # Use the filename provided by the user
    file = open(filename, "r")
    content = file.read()
    print("\nFile Content:\n")
    print(content)
    file.close()  
except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: Permission denied for '{filename}'.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
