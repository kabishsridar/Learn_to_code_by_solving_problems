total_paint = int(input()) # total amount of paint James has (in liters)
paint_per_badge = int(input()) # how much paint is used for one badge
badge_price = int(input()) # price of each badge

badges = total_paint // paint_per_badge # number of bages
leftover_paint = total_paint % paint_per_badge # paint left after making badges

total_money = (badges * badge_price) + leftover_paint
print(total_money) # display total money