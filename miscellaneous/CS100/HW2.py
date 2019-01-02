#Problem 1 

def file_copy(in_file, out_file):
    inF = open(in_file,'r+')
    outF = open(out_file,'w+')
    outF.write(inF.read())
    inF.close()
    outF.close()

file_copy('created_equal.txt', 'copy.txt')
open_f = open('copy.txt')
equal_f = open('created_equal.txt')
equal_f.read()


#Problem 2
def file_stats(input_file):
    lines=0
    words=0
    characters=0
    inF = open(input_file,'r')
    for line in inF:
            lines += 1
            words += len(line.split())
            characters += len(line)
    print("lines",lines)
    print("words",words)
    print("characters",characters)
file_stats('created_equal.txt')

#problem 3

def repeat_words(input_file):
     f = open(input_file, 'r')
     for line in f:
        list=[]
        list=line.split()
        j=0
        words=[]
        for i in list:
            words.append(''.join(e for e in i if e.isalnum()))
        for i in words:
            words[j]=i.lower()
            j=j+1
        duplicates = [x for n, x in enumerate(words) if x in words[:n]]
        if(len(duplicates)>0):
           for i in duplicates:
               print (i,end=" ")
           print("")
           
repeat_words("testfile.txt")
    
