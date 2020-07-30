import os

#The Main function of the moudlue.
#Can Delete String in one file or run on all files in folders and delete a string inside.
def Delete():

    print("Delete Script Activated:\n")

    File_Name = input("Enter file name to be deleted or press * for whole files in folder:")
    StringToBeDelted = input("Enter the string you want to delete:")


    #Test for which operation: change on file or running on all files.
    operation = File_Name.find('*')
   


    #Case delete a string in one file
    if( operation == -1 ):

        #check if there is a file with this name in the folder.
        file_located = os.path.isfile(File_Name)

        if(file_located == False):
            print("File not Found.\n")
            exit()

        #if file located or the target is to run and delete string in all files
        ChangeSingleFile(File_Name,StringToBeDelted)
        

    #if file located or the target is to run and delete string in all files
    else:
        RunOnAllFile()
        




def RunOnAllFile():
    print("RunOnAllFile Function Activated.\n")
    
    


def ChangeSingleFile(file_name,StringToBeDelted):
        print("ChangeSingleFile Function Activated on {}.\n".format(file_name))
        test_if_string_exists_and_delete(file_name,StringToBeDelted)



def test_if_string_exists_and_delete(file_name,StringToBeDelted):
    print("Test if string exsists:\n")

    with open(file_name) as target_file:
     if file_name in target_file.read():
         print("string exsists\n")
    



if __name__ == "__main__":
    Delete()