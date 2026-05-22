with open("data\\sample.txt", "r") as file:
    print(file.read(5))  # Reads first 5 characters
    print(file.tell())   # Outputs: 5
    print(file.read(5))  # Reads first 5 characters
    print(file.tell())   # Outputs: 10
    file.seek(0)         # Resets cursor back to the start
    print(file.read(5))  # Reads first 5 characters
    print(file.tell())   # Outputs: 5
