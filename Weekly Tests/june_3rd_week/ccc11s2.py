# the first line contains the number of questions(n)
# the next n lines choice chosen by student
# the next n lines are corrrect options
# need to check the result

n = int(input())
chosen_lst = []
correct_lst = []
result = 0
for questions in range(n):
    chosen = input()
    chosen_lst.append(chosen)
for answers in range(n):
    answer = input()
    correct_lst.append(answer)
for i in range(n):
    if chosen_lst[i] == correct_lst[i]:
        result +=1

print(result)