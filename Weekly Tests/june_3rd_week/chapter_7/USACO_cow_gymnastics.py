fin = open('Weekly Tests//june_3rd_week//gymnasticsin.txt') # open the input file
fout = open('gymnasticsout.txt', 'w') # create or open the file

line = fin.readline().split() # read first line for k, n
k = int(line[0]) # num of practice sessions
n = int(line[1]) # num of cows

# need to find the number of consistent pairs
sessions = []
for session in range(k):
    line = fin.readline().split()
    rankings = []
    for item in line:
        rankings = (int(item))
    sessions.append(rankings)
    print(sessions)
