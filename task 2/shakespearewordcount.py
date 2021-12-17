
  

import string


text = open("shakespeare.txt", "r")
  

d = dict()
  

for line in text:
    
    line = line.strip()
  
    line = line.lower()

    line = line.translate(line.maketrans("", "",  string.punctuation))
  
    # splits the word
    words = line.split(" ")
  
    # Iterate through each line to to act
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
#turn dictionary into tuple to sort by freq
dw=sorted(d.items(), key=lambda x: x[1], reverse=True)

print(dw)


