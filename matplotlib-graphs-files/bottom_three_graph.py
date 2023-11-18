import matplotlib.pyplot as plt

actual_table = {
                'Burnley': 18,
                'Watford': 19,
                'Norwich': 20}

predicted_table = {
           'Watford': 18,
           'Burnley': 19,
           'Norwich': 20
           }

fig, ax = plt.subplots()

x1, y1 = zip(*actual_table.items())
ax.scatter(x1, y1, c='red', label='Actual Table')

x2, y2 = zip(*predicted_table.items())
ax.scatter(x2, y2, c='blue', label='Predicted Table')

ax.set_xlabel('Relegated Teams')
ax.set_ylabel('Position in Table')
ax.set_title('Premier League Tables')

ax.legend()

plt.show()
