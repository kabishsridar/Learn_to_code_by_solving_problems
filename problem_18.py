def clean(address):
    address = address.lower()
    at = address.find('@') # we need to remove characters before @ symbol so we need to find it first
    before_at = address[:at] # after finding the index of @ , we seperated it as before_at and after_at to remove before_at and add after_at
    after_at = address[at:]

    plus = before_at.find('+') # afer the + is not required, so we should remove them . for that we need to find +
    if plus != -1:
        before_at = before_at[:plus] # this is the unwanted string to be removed

    cleaned_before_at = ''
    i = 0
    while i < len(before_at):  # repeat for each character before the @ symbol
        if before_at[i] != '.':  # If the character is not a dot, add it to the cleaned string
            cleaned_before_at += before_at[i]
        i += 1  # Move to the next character

    cleaned = cleaned_before_at + after_at
    return cleaned 

n = int(input("The no. of email addresses(1 - 100,000): "))
addresses = set()

for i in range(n):  # Loop each email address
    address = input("Enter email address: ")
    addres = clean(address)
    addresses.add(addres)

print("The no. of unique email address in which you have entered is")
print(len(addresses))
