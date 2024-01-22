import os
import pyfiglet


ascii_banner = pyfiglet.figlet_format("File Management Tool", font = "digital")



def crtDir(dirName):
    print("Creating a new Directory")
    try:
        os.mkdir(dirName)
        print(f"Directory '{dirName}' created successfully.")
    except FileExistsError:
        print(f"Directory '{dirName}' already exists.")
    except IOError:
        print("Permission denied.")
    except FileNotFoundError:
        print("The system cannot find the path specified")
    except Exception as error:
        print("An error occurred: ",error)




# we'll create a file management tool that allows the user to list files, create directories, and delete files or directories.


def delFile(fileName):
    try:
        if os.path.isfile(fileName):
            os.remove(fileName)
            print("File deleted successfully.")
            
        else:
            print("File or directory not found.")
    except FileNotFoundError:
        print("No such file or directory.")
    except IOError:
        print("Permission denied.")
    except Exception as error:
        print("An error occurred: ",error)
        


def delDir(dirName):
    try:
        if os.path.isdir(dirName):
                os.rmdir(dirName)
                print("Directory deleted successfully.")
        else:
                print("File or directory not found.")
    except FileNotFoundError:
        print("No such file or directory.")
    except IOError:
        print("Permission denied.")
    except Exception as error:
        print("An error occurred: ",error)



def listDirCont(dir):
    try:
        files = os.listdir(dir)
        if(len(files)>0):
            for file in files:
                print(file)
        else:
            print("this directory is empty.")
    except FileNotFoundError:
        print("Directory not found.")
    except IOError:
        print("Permission denied.")
    except Exception as error:
        print("An error occurred: ",error)


def crtFile(fileName):
    print("Create a new file with optional content.")
    with open(fileName, 'w') as file:
        pass
    print(f"File '{fileName}' created successfully.")


def clear_screen():
    if(os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')






while True:
    clear_screen()
    print(ascii_banner)
    print("1. List Files in the current \n2. Create a new Directory \n3. Delete File  \n4. Delete Directory \n5. Create an empty file \n6. End of program")
    num=input("Enter number of operation to run: ")


    if num == "1":
        dir = input("Enter directory path (default is current directory): ")
        listDirCont(dir)
    elif num == "2":
        dirName = input("Enter the name of the directory to create: ")
        crtDir(dirName)
    elif num == "3":
        name = input("Enter the name of the file to delete: ")
        delFile(name)
    elif num == "4":
        name = input("Enter the name of the directory to delete: ")
        delDir(name)
    elif num == "5":
        fileName = input("Enter file name to create: ")
        crtFile(fileName)
    elif num== "6":
        print("end the script.")
        break
    else:
        print("Invalid number operation. Please enter a number between 1 and 6.")

    input("\n \n Press Enter to continue")

















































# os.system("shutdown /r /t 0")

# os.system("sudo shutdown -r now")



