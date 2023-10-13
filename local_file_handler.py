import subprocess
import sys
import git_remote_handler as git
       
def make_repo(repo_name:str) -> None:
    auth = git.git_login()
    git.create_repository(auth,repo_name)
    repo = git.find_repo(auth,repo_name)
    subprocess.run(["mkdir",f"{repo_name}"])
    subprocess.run(["git","init",f"./{repo_name}"])
    subprocess.run(["git", "branch","-M","main"])
    subprocess.run(["git","remote","set-url","origin",f"{repo.clone_url}"])
    subprocess.run(["git","push","-u","origin","main"])
    
def make_file(file_name:str) -> None:
    subprocess.run(["touch",f"{file_name}"])
    
def delete_file(file_name:str) -> None:
    subprocess.run(["rm",f"{file_name}"])
    
def delete_folder(folder_name:str) -> None:
    subprocess.run(["rmdir",f"{folder_name}"])
            
def make_folder(folder_name:str) -> None:
    subprocess.run(["mkdir",f"{folder_name}"])
    

            

if __name__ == "__main__":
    make_repo("TEST_CLI2")
