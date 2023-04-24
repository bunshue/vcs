import os

def main():

    filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'
    foldername = 'C:/_git/vcs/_4.cmpp/_python_test/data'
   
    # Display the size
    try:
        print(getSize(foldername), "bytes")
    except:
        print("Directory or file does not exist")

def getSize(path):
    size = 0 # Store the total size of all files

    if not os.path.isfile(path):
        lst = os.listdir(path) # All files and subdirectories
        for subdirectory in lst:
            size += getSize(path + "\\" + subdirectory) 
    else: # Base case, it is a file
        size += os.path.getsize(path) # Accumulate file size 

    return size

main() # Call the main function
