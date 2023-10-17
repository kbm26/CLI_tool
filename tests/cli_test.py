import unittest
import main as cli

class My_testcase(unittest.TestCase):
    
    def test_command_validator(self):
        """
        tests correct and incorrect commands
        """
        
        output1 = cli.command_validator("")
        output2 = cli.command_validator("make")
        self.assertEqual("invalid",output1,"The error output is not working.")
        self.assertEqual("make",output2,"This should work")
        
    def test_argument_validator(self):
        """
        tests correct and incorrect arguments
        """
        
        output1 = cli.argument_validator([""])
        output2 = cli.argument_validator(["textfile","repo"])
        self.assertEqual([],output1,"The error output is not working.")
        self.assertEqual(["textfile","repo"],output2,"This should work")
        
    
        
if __name__ == '__main__':
    unittest.main()