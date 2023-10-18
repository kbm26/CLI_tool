import subprocess
import git_remote_handler as git

def make_remote_and_local_repo(repo_dir:str,repo_name:str) -> None:
    auth = git.git_login()
    
    make_remote_repo(repo_name)
    
    repo = git.find_repo(auth,repo_name)

    path = f"{repo_dir}{repo_name}"


    
    make_local_repo(f"{repo_dir}{repo_name}")
    make_file(f"{repo_dir}{repo_name}/text.txt")
    subprocess.run([f"git -C {path} add ."],shell=True)
    subprocess.run([f"git -C {path} branch -M main"],shell=True)
    subprocess.run([f"git -C {path} commit -m \"first commit\""],shell=True)
    subprocess.run([f"git -C {path} remote add origin {repo.clone_url}"],shell=True)
    subprocess.run([f"git -C {path} push -u origin main"],shell=True)
    
def make_remote_repo(repo_name:str) -> None:
    auth = git.git_login()
    git.create_repository(auth,repo_name)
    
def make_local_repo(repo_name:str) -> None:
    make_folder(repo_name)
    subprocess.run([f"git init {repo_name}"],shell=True)
    
def make_file(file_name:str) -> None:
    print(f"this is the path: {file_name}")
    subprocess.run([f"touch {file_name}"],shell=True)
    
def delete_file(file_name:str) -> None:
    subprocess.run(["bash","-c",f"rm {file_name}"])
    
def delete_folder(folder_name:str) -> None:
    subprocess.run(["bash","-c",f"rm -r {folder_name}"])
            
def make_folder(folder_name:str) -> None:
    print (f"THIS IS THE DIRECTORY: {folder_name}")
    subprocess.run([f"mkdir {folder_name}"],shell=True)
    
def find_files_and_directories(directory) -> list:
    bytes = subprocess.run(["bash","-c",f"ls {directory}"], capture_output=True).stdout.strip()
    table = [ [word] for word in bytes.decode("utf-8").split("\n") ]
    return table
    


if __name__ == "__main__":
    make_remote_and_local_repo("~/","deathMarch")