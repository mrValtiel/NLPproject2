import re

answers = []
results = []

set_answers = open("set_test_with_answers", 'r')
for line in set_answers:
    x = str(line[0])
    answers.append(x)
set_answers.close()

set_test = open("set_test", 'r')
l = len(answers)
success = 0
spam = 0
i = 0
for line in set_test:
    x = "0"
    if re.search("free", line) or re.search("money", line):
        x = "1"
        spam += 1
    else:
        x = "0"

    if x == answers[i]:
        success += 1

    i += 1

set_test.close()

accuracy = (success * 100) / l

print("Mails checked: ", l)
print("Mails detected as SPAM: ", spam)
print("Mails successfully detected: ", success)
print("Accuracy: ", accuracy, "%")
