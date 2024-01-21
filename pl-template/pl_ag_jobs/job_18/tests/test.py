#! /usr/bin/python3

import cgrader
import random

class QuestionGrader(cgrader.CGrader):


    def tests(self):
        # Executable strings and usage strings for autograding
        executable_string = "./helloworld"
        expected_string = "Hi! My name is "

        self.test_compile_file("helloworld.c",
                                "helloworld",
                                name="Compilation Test",
                                points=0)
                                
        
        self.test_run(executable_string, 
                    name="Using Write() Test",
                    reject_symbols=["printf(", "fwrite(", "puts("])
        
        self.test_run(executable_string, 
                    name="Functionality Test",
                    exp_output=expected_string)
        
        #Compile program again with memory leak tests
        self.compile_file("helloworld.c",
                                "helloworld",
                                enable_asan=True)

        self.test_run(executable_string,
                    name="Memory Leak Test",
                    reject_output=['AddressSanitizer'],)
                    
g = QuestionGrader()
g.start()