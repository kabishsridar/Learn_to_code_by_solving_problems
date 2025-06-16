# Finding Mama bear bowls
bowl1 = int(input()) # get the inputs
bowl2 = int(input())
bowl3 = int(input())

lst = [bowl1, bowl2, bowl3] # converting to list to use max and min
papa = max(lst)
baby = min(lst)
for bowl in lst:
    if bowl != papa and bowl != baby: # if the bowl is not max and min, then return the output
        print(bowl)