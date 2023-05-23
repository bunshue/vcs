def main():
    while True:
        try:
            filename = 'C:/_git/vcs/_1.data/______test_files1/article2.txt'
            infile = open(filename, "r") # Open the file
            break 
        except IOError:
            print("File " + filename + " does not exit. Try again")

    counts = 26 * [0] # Create and initialize counts
    for line in infile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears  " + str(counts[i])
              + (" time" if counts[i] == 1 else " times"))

    infile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

print('統計一個檔案內每個英文字母出現的字數')
main()


