import os
import subprocess
from string import Template

if __name__ == '__main__':
    with open("program_input.txt",'r') as inp:
        with open("program_out.txt",'w') as out:
            lang = input().lower()
            # Python  
            if lang=="py":
                proc=subprocess.run(["python","python.py"], stdin=inp,stdout=subprocess.PIPE)

            # Javascript
            elif lang=="js":
                proc=subprocess.run(["node","javascript.js"], stdin=inp,stdout=subprocess.PIPE)
            
            # PHP
            elif lang=="php":
                proc=subprocess.run(["php","php.php"], stdin=inp,stdout=subprocess.PIPE)

            # C Program
            elif lang=="c":
                subprocess.call(["gcc", "c.c"])
                tmp=subprocess.call("a", stdin = inp)
                os.remove("a.exe")

            # C++ Program
            elif lang=="cpp":
                subprocess.call(["g++", "cpp.cpp"]) 
                tmp=subprocess.call("a", stdin = inp) 
                os.remove("a.exe")

            # Java Program
            elif lang=="java":
                subprocess.call(["javac", "Main.java"]) 
                tmp=subprocess.call("java Main", stdin = inp) 
                os.remove("Main.class")

            else:
                print("Incorrect Lang")
                
            # Output
            if lang=="c" or lang=="cpp" or lang=="java":
                print(tmp)
                
            else:
                val={"output":Template(proc.stdout.decode("utf-8"))}
                print(val["output"].template)
