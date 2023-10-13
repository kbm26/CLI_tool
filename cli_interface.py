from InquirerPy import prompt
from InquirerPy.validator import NumberValidator
from InquirerPy import get_style
from InquirerPy import inquirer

def get_message(result):
    return f"Hi {result['confirm_name']}, enter your age:"
style = get_style({"checkbox": "#ffffff", "answer": "#000000"}, style_override=True)

result = inquirer.confirm(message="Confirm?", style=style).execute()
questions = [
    {
        "type": "input",
        "message": "Name:",
        "name": "name",
    },
    {
        "type": "input",
        "message": "Confirm Name:",
        "name": 'confirm_name',
        "default": lambda result: result["name"],   # inline lambda to make the code shorter
    },
    {
        "type": "input",
        "message": get_message,   # use a named function for more complex logic
        "name": 'age',
        "validate": NumberValidator(),
    },
]

result = prompt(questions)