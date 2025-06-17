# error
ORDER = ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red']
HANDFUL_SIZE = 7
TIME_PER_HANDFUL = 13
TIME_PER_RED = 16

color_counts = {}
for color in ORDER:
    color_counts[color] = 0
try:
    while True:
        line = input().strip()
        if line == 'end of box':
            total_time = 0

            for i in range(len(ORDER)):
                color = ORDER[i]
                count = color_counts[color]

                if color == 'red':
                    total_time += count * TIME_PER_RED
                else:
                    handfuls = (count + HANDFUL_SIZE - 1) // HANDFUL_SIZE
                    total_time += handfuls * TIME_PER_HANDFUL

            print(total_time)

            for color in ORDER:
                color_counts[color] = 0

        elif line in color_counts:
            color_counts[line] += 1

except EOFError:
    pass