
from functions.run_python import run_python

def main():

    print('\nRunning main.py.......')
    print(run_python("calculator", "main.py"))

    print('\nRunning main.py", ["3 + 5"].......')
    print(run_python("calculator", "main.py", ["3 + 5"]))

    print('\nRunning tests.py.......')
    print(run_python("calculator", "tests.py"))

    print('\nRunning ../main.py.......')
    print(run_python("calculator", "../main.py"))

    print('\nRunning nonexistent.py.......')
    print(run_python("calculator", "nonexistent.py"))
    
    print("\nRunning lorem.txt.......")
    print(run_python("calculator", "lorem.txt")+'\n')
    
if __name__ == "__main__":

    main()

