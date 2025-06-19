# Epidemology
# P = number of people have/ had disease
# N = number of people who have the disease on Day 0
# R = infected on very next day
p = int(input())
n = int(input())
r = int(input())

days = 0
current_infected = n
total_infected = n

while total_infected <= p: # breaks if total_infected is equal to total people have disease
    days += 1 # increment number of days for each loop
    current_infected = current_infected * r # calculate infected persons
    total_infected += current_infected # add to the total_infected
print(days) # return number of days