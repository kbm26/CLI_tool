import subprocess
from collections. abc import Mapping
from rich import print as rprint
import sys
import typer
from PyInquirer import prompt, print_json, Separator

app = typer.Typer()

def main():
    """
    Handles user's input and executes the appropriate commands
    """
    
    user_inputs = sys.argv
    command = command_validator(sys.argv[0])
    arguments = argument_validator(sys.argv[1:])
    
    match command:
        case "make":
            pass
            
    
    
def make(args:list) :
    if (len(args)==2):
        
        match args[0] :
            case "file":
                return subprocess.run(["touch",f"{args[1]}"])
            case "folder":
                return subprocess.run(["mkdir",f"{args[1]}"])
            case "repo":
                return make_repo(args[1])
            
    else:
        print("INVALID ARGUMENT")
                
def make_repo(repo_name:str) -> None:
    subprocess.run(["mkdir",f"{repo_name}"])
    
    
                
    
def command_validator(command:str) -> str:
    command_list = ["find","make","delete","dev"]
    if(command.lower() in command_list):
        return command
    else:
        return "invalid"
        

def argument_validator(args:list) -> list:
    return [arg for arg in args if arg != '']
        
        
    
@app.command()
def say_hi(name):
    print(f"hi {name}")

if __name__ == "__main__":
    app()    
