
def analyze(fileName):
 #get file that is going to be read
 myFile = open(fileName, "r")
 wordCounter = {} #dictionary to keep track of word count
 
#get a list containing all the words
 data = myFile.read()
 words = data.split()
 
 #for each word in the file, check if its in the dictionary
 #if it is, addd to it's current count
 #if it's not, then add it to dictionary w/ a count of 1 
 for word in words:
  if word == "i":
   word = "I"
  if word in wordCounter:
   wordCounter[word]+=1
  else:
   wordCounter[word] = 1

 sortedCounter = sorted(wordCounter.items(), key = lambda x:(-x[1], x[0]))
 sortedCounter = dict(sortedCounter)

 print()

 i = 0 
 for word, counter in sortedCounter.items():
  print(f"{word}: {counter}", end = "\n")
  i+=1
  if(i == 5):
   break
def main():
 analyze("document.txt")

main()
