# distinct years
# should check the next num is distinct using for loop
def check_distinct(year): # function to check whether it is distinct
    checked = []
    for digit in year: #  loop through each number
        if digit in checked:
            return False # if the digit is in checked, then return FAlse
        checked.append(digit) # if not presented, append it to checked
    return True

def next_distinct_year(year):
    year_int = int(year) # converting to integer, to increment
    while True:
        year_int += 1 # increments for each loop
        if check_distinct(str(year_int)): # checking thorugh converting to string
            print(year_int)
            break # after checked completely, breaks

if __name__ == "__main__": # should start at first
    year = input() # get the year
    next_distinct_year(year) # calling the function