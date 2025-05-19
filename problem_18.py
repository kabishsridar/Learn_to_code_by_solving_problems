def clean(address): # define a function named clean(address)
    address = address.lower() # convert it to lowercase a=for consistency
    at = address.find('@') # we need to remove characters before @ symbol so we need to find it first, for that we use find 
    before_at = address[:at] # after finding the index of @ , we seperated it as before_at and after_at to remove before_at and add after_at
    after_at = address[at:]

    plus = before_at.find('+') # afer the + is not required, so we should remove them, for that we need to find +
    if plus != -1: # if plus symbol is not at last before_at should be the string before at and after plus
        before_at = before_at[:plus] # this is the unwanted string to be removed

    cleaned_before_at = '' # initiate cleaned_before_at as an empty string
    i = 0 # initiate i to 0
    while i < len(before_at):  # repeat for each character before the @ symbol
        if before_at[i] != '.':  # If the character is not a dot, add it to the cleaned string
            cleaned_before_at += before_at[i] # the before_at will be added to cleaned_before_at
        i += 1  # Move to the next character

    cleaned = cleaned_before_at + after_at # it is the correct email address named cleaned
    return cleaned

n = int(input("The no. of email addresses(1 - 100,000): ")) # prompt the user for number of email addresses
addresses = set() # initiating an empty set named addresses

for i in range(n):  # Loop each email address
    address = input("Enter email address: ") # prompt for email address
    addres = clean(address) # calling our user defined function clean(address)
    addresses.add(addres) # add cleaned address to the empty set named addresses

print("The no. of unique email address in which you have entered is")
print(len(addresses)) # display the output for for number of unique addresses
