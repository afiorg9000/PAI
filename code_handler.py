import os

def extract_code(response):
    code_start_index = response.find("```")
    code_end_index = response.rfind("```") + 3
    code_only = response[code_start_index + 3:code_end_index]
    return code_only


def save_to_file(code, file_extension):
    folder_name = input("Do you want to save the file in a folder? (yes/no): ")

    if folder_name.lower() == "yes":
        folder_name = input("Enter the name of the folder: ")
        folder_path = os.path.join("filebase", folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    else:
        folder_path = "filebase"

    filename = generate_filename(folder_path, file_extension)

    with open(filename, "w") as file:
        file.write(code)

    print("Output code saved to", filename)


def generate_filename(folder_path, file_extension):
    user_input = input("Enter a file name: ")
    filename = user_input.replace(" ", "_") + file_extension
    return os.path.join(folder_path, filename)


def get_file_extension(user_input):
    file_extension = ".txt"  # Default file extension if not specified

    if "py" in user_input.lower():
        file_extension = ".py"
    elif "html" in user_input.lower():
        file_extension = ".html"
    elif "css" in user_input.lower():
        file_extension = ".css"
    elif "js" in user_input.lower():
        file_extension = ".js"

    return file_extension
