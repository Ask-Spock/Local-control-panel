import os

#The Main function of the moudlue.
#Can Update String in one file or run on all files in folders and Update a string inside.
def Update():

    print("Update Script Activated:\n")

    File_Name = "test.html" #input("Enter file name to be Updated or press * for whole files in folder:")
    StringToBeDelted = "Thomas" #input("Enter the string you want to Update:")
    New_Updateted_String = "Hey Hey I am new here" #input("Enter the new string:")

    #Test for which operation: change on file or running on all files.
    operation = File_Name.find('*')
   


    #Case Update a string in one file
    if( operation == -1 ):

        #check if there is a file with this name in the folder.
        file_located = os.path.isfile(File_Name)

        if(file_located == False):
            print("File not Found.\n")
            exit()

        #if file located or the target is to run and Update string in all files
        ChangeSingleFile(File_Name, StringToBeDelted, New_Updateted_String)
        

    #if file located or the target is to run and Update string in all files
    else:
        RunOnAllFile()
        




def RunOnAllFile():
    print("RunOnAllFile Function Activated.\n")
    
    


def ChangeSingleFile(file_name, StringToBeDelted, New_Updateted_String):
        print("ChangeSingleFile Function Activated on {}.\n".format(file_name))
        test_if_string_exists_and_Update(file_name, StringToBeDelted, New_Updateted_String)



def test_if_string_exists_and_Update(file_name, StringToBeDelted, New_Updateted_String):

    does_string_exsists = False
    

    print("Test if string exsists:\n")

    with open(file_name) as target_file:
     if StringToBeDelted in target_file.read():
        print("string_exsists.\n")
        does_string_exsists = True
    
    if(does_string_exsists):
        #read input file
        fin = open(file_name, "rt")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace(StringToBeDelted, New_Updateted_String)
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open(file_name, "wt")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()
        print("Text Updated.\n")

    else:
        print("Text does not exsist in file, program exit.\n")
        exit()


        




if __name__ == "__main__":
    Update()