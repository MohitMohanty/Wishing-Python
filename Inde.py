import os

def list_text_files():
    text_files = [f for f in os.listdir() if f.endswith('.txt')]
    return text_files

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())  # Print each line of the file
    except FileNotFoundError:
        print("File not found")

def display_options(text_files):
    print("Welcome to the Cat Program:-")
    print("Select your wish number from the cat:")
    for i, file_name in enumerate(text_files, 1):
        print(f"{i}. {file_name}")
    print(f"{len(text_files) + 1}. Quit")

def main():
    text_files = list_text_files()
    while True:
        display_options(text_files)
        #option = input("Enter your choice: ")
        option = sys.argv[1]

        if option.isdigit():
            option = int(option)
            if 1 <= option <= len(text_files):
                file_name = text_files[option - 1]
                read_file(file_name)
            elif option == len(text_files) + 1:
                print("Quitting program...")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            file_name = option.strip() + '.txt'  # Append .txt extension
            if file_name in text_files:
                read_file(file_name)
            elif option.lower() == 'quit':
                print("Quitting program...")
                break
            else:
                print("File not found. Please try again or enter 'quit' to exit.")

if __name__ == "__main__":
    main()
