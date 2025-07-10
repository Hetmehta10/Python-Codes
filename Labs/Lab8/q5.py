# Create multiple suitable exceptions for a file handling program.
try:
    # Opening a file that does not exist
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found!")

try:
    # Trying to write to a file without proper permissions
    with open("random.txt", "r") as file:
        file.write("This is a test.")

except:
    print("Unable to write to file.")

try:
    # Opening a file with an invalid mode
    with open("random.txt", "xyz") as file:
        content = file.read()

except ValueError:
    print("Invalid file mode specified!")

try:
    # Performing an operation on a closed file
    file = open("random.txt", "r")
    file.close()
    file.read()

except ValueError:
    print("I/O operation on closed file!")