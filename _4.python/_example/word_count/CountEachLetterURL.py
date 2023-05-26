import urllib.request

# Count each letter in the string 
def countLetters(s): 
    counts = 26 * [0] # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts

print('統計一個檔案內每個英文字母出現的字數')

url = 'https://android.googlesource.com/kernel/msm/+/android-7.1.0_r0.2/Documentation/ioctl/cdrom.txt'
infile = urllib.request.urlopen(url)
s = infile.read().decode() # Read the content as string 

counts = countLetters(s.lower())
    
# Display results
for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i])
          + (" time" if counts[i] == 1 else " times"))


