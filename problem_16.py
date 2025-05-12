a = open('wordin.txt', 'r')
b = open('wordout.txt', 'w')

l = a.readline().split()
k = int(l[1])  # Max characters per line
word = a.readline().split()

line = ''
char_on_line = 0

for i in word:
    if char_on_line + len(i) <= k:
        line += i + ' '
        char_on_line += len(i) + 1
    else:
        b.write(line[:-1] + '\n')
        line = i + ' '
        char_on_line = len(i) + 1 
b.write(line[:-1] + '\n')

a.close()
b.close()
