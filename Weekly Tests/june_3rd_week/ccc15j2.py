happy = ":-)"
sad = ":-("
prompt = input()
happy_count = prompt.count(happy)
sad_count = prompt.count(sad)

if happy_count > sad_count:
    print("happy")
elif happy_count < sad_count:
    print("sad")
elif happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")