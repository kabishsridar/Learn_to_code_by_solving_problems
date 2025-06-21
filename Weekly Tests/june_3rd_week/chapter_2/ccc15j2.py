happy = ":-)"
sad = ":-("
prompt = input() # get input
happy_count = prompt.count(happy) # count number of happy
sad_count = prompt.count(sad) # count number of sad

if happy_count > sad_count: # return the result as which is greater
    print("happy")
elif happy_count < sad_count:
    print("sad")
elif happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")