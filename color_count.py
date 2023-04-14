'''At a fun fair, a street vendor is selling different colours of balloons. He sells N number of different colours of balloons (B[]). The task is to find the colour (odd) of the balloon which is present odd number of times in the bunch of balloons. '''

balloons = ['red', 'blue', 'green', 'red', 'green', 'green', 'blue']
color_counts = {}
# Count the number of balloons of each color
for color in balloons:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    
# Find the color that appears an odd number of times
for color, count in color_counts.items():
        if count % 2 == 1:
            print(color)
        else:
            print(None)
