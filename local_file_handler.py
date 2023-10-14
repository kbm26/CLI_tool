import subprocess
import sys
import git_remote_handler as git
       
def make_remote_and_local_repo(repo_name:str) -> None:
    auth = git.git_login()
    
    make_remote_repo(repo_name)
    
    repo = git.find_repo(auth,repo_name)
    git_dir = f"--git-dir=./{repo_name}/.git/"
    work_dir = f"--work-tree=./{repo_name}"
    
    make_local_repo(repo_name)
    
    subprocess.run(["touch",f"./{repo_name}/text.txt",])
    subprocess.run(["git",git_dir,work_dir,"add","."])
    subprocess.run(["git",git_dir,work_dir,"commit","-m","first commit"])
    subprocess.run(["git",git_dir,work_dir,"branch","-M","main"])
    subprocess.run(["git",git_dir,work_dir,"remote","add","origin",f"{repo.clone_url}"])
    subprocess.run(["git",git_dir,work_dir,"push","-u","origin","main"])
    
def make_remote_repo(repo_name:str) -> None:
    auth = git.git_login()
    git.create_repository(auth,repo_name)
    
def make_local_repo(repo_name:str) -> None:
    subprocess.run(["mkdir",f"{repo_name}"])
    subprocess.run(["git","init",f"./{repo_name}"])
    
def make_file(file_name:str) -> None:
    subprocess.run(["touch",f"{file_name}"])
    
def delete_file(file_name:str) -> None:
    subprocess.run(["rm",f"{file_name}"])
    
def delete_folder(folder_name:str) -> None:
    subprocess.run(["rmdir",f"{folder_name}"])
            
def make_folder(folder_name:str) -> None:
    subprocess.run(["mkdir",f"{folder_name}"])
    

            

if __name__ == "__main__":
    make_repo("k")
