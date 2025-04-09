# This script demonstrates basic file handling in Python.
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
            print("Error: File not found.")
except IOError:
            print("Error: Cannot read the file.")
finally:
    print("Operation completed.")


# Modify the content and write to a new file
new_filename = "modified_sample.txt"
try: 
    with open('modified_sample.txt', 'w') as file:
        file.write("This is the modified content of the file.")
        print(f"Content written to {new_filename} successfully.")
except IOError:
    print(f"Error: Cannot write to {new_filename}.")