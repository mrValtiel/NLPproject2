import os

listSPAM = os.listdir("database/spam")
print("SPAM files: ", len(listSPAM))
listNotSPAM = os.listdir("database/notspam")
print("NotSPAM files: ", len(listNotSPAM))

spamFile = open("spam", 'w+')

for file in listSPAM:
    fileName = "database/spam/" + file
    #print(fileName)
    f = open(fileName, 'r')
    content = f.read()
    f.close()
    #print(content)
    content = str(content)
    content = content.replace("b\'", "")
    content = content.replace("\n", " ")
    content = content.replace("Subject: ", "")
    content = "1 | " + content + "\n"
    spamFile.write(content)

spamFile.close()
print("SPAM file created")

notspamFile = open("notspam", 'w+')

for file in listNotSPAM:
    fileName = "database/notspam/" + file
    #print(fileName)
    f = open(fileName, 'r')
    content = f.read()
    f.close()
    #print(content)
    content = str(content)
    content = content.replace("b\'", "")
    content = content.replace("\n", " ")
    content = content.replace("Subject: ", "")
    content = "0 | " + content + "\n"
    notspamFile.write(content)

notspamFile.close()
print("notSPAM file created")
