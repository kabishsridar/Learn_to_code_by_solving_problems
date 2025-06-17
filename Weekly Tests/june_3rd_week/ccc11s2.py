# the first line contains the number of questions(n)
# the next n lines choice chosen by student
# the next n lines are corrrect options
# need to check the result

n = int(input()) # get input for number of questions 
chosen_lst = []
correct_lst = []
result = 0
for questions in range(n): # read first n lines and store it as chosen_lst
    chosen = input()
    chosen_lst.append(chosen) # read next n lines and store it as correct_lst
for answers in range(n):
    answer = input()
    correct_lst.append(answer)
for i in range(n):
    if chosen_lst[i] == correct_lst[i]: # if chosen answer is same as correct answer, then increment one mark
        result +=1

print(result)