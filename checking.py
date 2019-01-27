answersFile = open("set_test", 'r')
answers = []
for line in answersFile:
    ans = line[0]
    answers.append(ans)

answersFile.close()

guessedFile = open("guessed", 'r')
guessed = []
for line in guessedFile:
    if line == "1":
        guessed.append("1")
    elif line == "0":
        guessed.append("0")
    else:
        guess = float(line)
        if guess < 0.5:
            guessed.append("0")
        else:
            guessed.append("1")

guessedFile.close()

print("ANSWERS:", answers)
print("GUESSED:", guessed)
l = len(answers)
correct = 0
for i in range(l):
    if guessed[i] == answers[i]:
        correct += 1

accuracy = (correct * 100) / l
print("ACCURACY:", accuracy, "%")
