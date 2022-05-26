# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        data=f.read().split()
    return data
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    d = {}
    #loop through each line of the file
    for line in text:
        #remove the leading spaces and newline character
        line = line.strip()
        #convert to lowercase
        line = line.lower()
        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("","", string.punctuation))


        #split lines into words
        words = line.split(" ")

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])

    print(d)


count_words()
    
