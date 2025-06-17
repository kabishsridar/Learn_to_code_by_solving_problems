ORDER = ['orange', 'blue', 'green', 'yellow', 'pink', 'violet', 'brown', 'red'] # order of smarties

# Constants based on problem description
HANDFUL_SIZE = 7            # Max number of Smarties per handful
TIME_PER_HANDFUL = 13 # Time in seconds to eat any handful (non-red)
TIME_PER_RED = 16 # Time taken to eat one red Smartie

# Dictionary to track how many Smarties of each color we have
color_counts = {}
for color in ORDER:
    color_counts[color] = 0

try:
    while True:
        line = input().strip()

        if line == 'end of box':
            total_time = 0

            for color in ORDER: # Loop through colors in order
                count = color_counts[color]

                if color == 'red': # Red Smarties eaten one at a time
                    total_time += count * TIME_PER_RED
                else:
                    handfuls = (count + HANDFUL_SIZE - 1) // HANDFUL_SIZE
                    total_time += handfuls * TIME_PER_HANDFUL

            print(total_time) # Output total time for current box

            # Reset color counts
            for color in ORDER:
                color_counts[color] = 0

        elif line in color_counts:
            color_counts[line] += 1

except EOFError:
    pass
