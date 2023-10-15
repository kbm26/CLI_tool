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
    input = input("Name the file you want to create (with an extension eg. .txt)")
    local.make_file(input)
    
def delete_file():
    input = input("Name the file you want to delete (with an extension eg. .txt)")
    local.delete_file(input)

def create_directory():
    pass
    
    
def delete_directory():
    pass

    
    

if __name__ == "__main__":
    git()
