def clean(address):
    address = address.lower()
    at = address.find('@')
    before_at = address[:at]
    after_at = address[at:]

    plus = before_at.find('+')
    if plus != -1:
        before_at = before_at[:plus]

    cleaned_before_at = ''
    i = 0
    while i < len(before_at):
        if before_at[i] != '.':
            cleaned_before_at += before_at[i]
        i += 1

    cleaned = cleaned_before_at + after_at
    return cleaned

n = int(input("The no. of email addresses(1 - 100,000): "))
addresses = set()

for i in range(n):
    address = input("Enter email address: ")
    addres = clean(address)
    addresses.add(addres)
print("The no. of unique email address in which you have entered is")
print(len(addresses))