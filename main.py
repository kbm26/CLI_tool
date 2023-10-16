import local_file_handler as local
import git_remote_handler as remote
import cli_interface as ui

def main():
    mode = ui.mode_selector()
    match mode:
        case "Create":
            pass
        case "Delete":
            pass
        case "View":
            pass
        case "Git (GitHub)":
            pass
        
def git():
    if(not remote.credentials_validator()):
        remote.create_credentials()
    else:
        choice = ui.git_mode()
        match choice:
            case "Change/Insert Token":
                pass
            case "View":
                pass
            case "Create":
                pass
            case "Delete":
                pass
            
            
def create_file():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        file = input("Name the file you want to create (with an extension eg. .txt)")
        local.make_file(f"{path}{file}")
    else:
        print("Directory not selected")
    
def delete_file():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        file = input("Name of the file you want to delete (with an extension eg. `.txt`)")
        local.delete_file(file)
    else:
        print("Directory not selected")


def create_directory():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        Directory = input("Name the Directory you want to create")
        local.make_folder(Directory)    
    else:
        print("Directory not selected")

    
    
def delete_directory():
    path = ui.directory_inquirer()
    if [*path][-1] == "/":
        Directory = input("Name of the empty Directory you want to delete")
        local.delete_folder(Directory)   
    else:
        print("Directory not selected")


    

if __name__ == "__main__":
    create_file()
