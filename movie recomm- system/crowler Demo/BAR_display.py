import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3]

# heights of bars
height = [89.9, 44.55555, 6]

# labels for bars
tick_label = ['Positive', 'Nagetive', 'Nutral']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['green', 'red','blue'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title(' Movie Review bar chart!')

# function to show the plot
plt.show()