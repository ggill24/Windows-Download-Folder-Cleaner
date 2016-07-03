import os
import getpass
import datetime


# list of all the files in the download folder
file_paths = list()

def main():

    get_files()

    if len(file_paths) > 0:
        assess_file()
    else:
        print("Download folder is empty")


#Get all the files in the Download Folde
def get_files():

    os.chdir(download_directory())

    #all items in the downloads folder
    items = os.listdir(os.getcwd())

    #credits: http://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    for path, subdirs, files in os.walk(download_directory()):
        for name in files:
            #desktop.ini is a file we don't want to delete!
            if(name == "desktop.ini"):
                continue
            #Only want to assess files that have not been used for at least a week or in the current month
            if(os.path.exists(name)):
                if(is_file_one_week_old(name)):
                    file_paths.append(os.path.join(path, name))

#Checks if the file can be deleted and deletes it
def assess_file():

    for item in file_paths:
        if(os.path.exists(item) and os.path.isfile(item)):
            if(prompt_delete(item)):
                delete_file(item)
                print()

def is_file_one_week_old(file):

    date_accessed = datetime.datetime.fromtimestamp(os.path.getmtime(file))

    if (datetime.datetime.utcnow().month != date_accessed.month) or \
                    (datetime.datetime.utcnow().day - date_accessed.day) > 7:
        return True
    else:
        return False


def prompt_delete(file):
   
    user_answer = None
    print("0 = NO & 1 = YES")

    while user_answer not in ["0", "1"]:
        user_answer= raw_input("Do you want to delete " + file + "?")

     if(user_answer == "0"):
        return False
    if(user_answer == "1"):
        return True



def delete_file(path):
     if(os.path.isfile(path)):
         os.remove(path)
         print(os.path.basename(path) + "deleted.")
     else:
         print("unable to delete: " + os.path.basename(path))

def download_directory():

    username = getpass.getuser()
    return "C:/Users/" + username + "/Downloads"


if __name__ == "__main__":
    print("two.py is being run directly")
    main()



