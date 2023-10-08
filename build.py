import os

package_directory = "package"
os.chdir(package_directory)

while True:
    answer = input(
'''1: install library
2: uninstall library
3: build
4: upload to test.pypi.org
5: upload to pypi.org
6: run test.py here
7: run test.py on CMD

>''')

    if answer == '1':
        os.system("pip install chromaconsole")
    elif answer == '2':
        os.system("pip uninstall chromaconsole")
    elif answer == '3':
        os.system("py -m build")
    elif answer == '4':
        os.system("py -m twine upload --repository testpypi dist/*")
    elif answer == '5':
        os.system("py -m twine upload --repository pypi dist/*")
    elif answer == '6':
        os.system("py ../test.py")
    elif answer == '7':
        os.system(f'start cmd /k python ../test.py')
    else:
        print("Invalid choice. Please select a valid option.")