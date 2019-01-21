import os

#creating two separate files
listSPAM = os.listdir("database/spam")
print("SPAM files: ", len(listSPAM))
listNotSPAM = os.listdir("database/notspam")
print("NotSPAM files: ", len(listNotSPAM))

spamFile = open("spam", 'w+')
listStrSpam = []

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
    listStrSpam.append(content)
    spamFile.write(content)

spamFile.close()
print("SPAM file created")

notspamFile = open("notspam", 'w+')
listStrNotSpam = []

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
    listStrNotSpam.append(content)
    notspamFile.write(content)

notspamFile.close()
print("notSPAM file created")

#creating mixed files
listStrSpamLen = len(listStrSpam)
listStrNotSpamLen = len(listStrNotSpam)

a = min(listStrSpamLen, listStrNotSpamLen) #mniejszy set
b = max(listStrSpamLen, listStrNotSpamLen) #wiekszy set
diff = b - a #roznica

a_main, a_test = a * 9/10, a * 1/10
b_main, b_test = b * 9/10, b * 1/10
diff_main, diff_test = diff * 9/10, diff * 1/10
a_main = int(a_main)
a_test = int(a_test)
b_main = int(b_main)
b_test = int(b_test)
diff_main = int(diff_main)
diff_test = int(diff_test)

print("Main set (min - notspam): ", a_main)
print("Test set (min - notspam): ", a_test)
print("Main set (max - spam): ", b_main)
print("Test set (max - spam): ", b_test)

print("Creating mixed files with 50/50 spam/notspam")
x = 0
set_main = open("set_main", 'w+')

for i in range(a_main):
    lineSpam = str(listStrSpam[i])
    lineNotSpam = str(listStrNotSpam[i])
    set_main.write(lineSpam)
    x += 1
    set_main.write(lineNotSpam)
    x += 1

set_main.close()
print("Main set (90%) created")
print("Mails: ", x)
y = 0
set_test = open("set_test", 'w+')

for i in range(a - a_test, a):
    lineSpam = str(listStrSpam[i])
    lineNotSpam = str(listStrNotSpam[i])
    set_test.write(lineSpam)
    y += 1
    set_test.write(lineNotSpam)
    y += 1

set_test.close()
print("Test set (10%) created")
print("Mails: ", y)
print("All mails: ", str(x + y))
