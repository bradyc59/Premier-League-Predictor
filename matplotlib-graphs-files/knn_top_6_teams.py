import matplotlib.pyplot as plt

actual_table = {'City': 1,
                'Liverpool': 2,
                'Chelsea': 3,
                'Tottenham': 4,
                'Arsenal': 5,
                'United': 6}

predicted_table = {'Liverpool': 1,
           'Chelsea': 2,
           'City': 3,
           'United': 4,
           'Tottenham': 5,
           'Arsenal': 6
           }

fig, ax = plt.subplots()

x1, y1 = zip(*actual_table.items())
ax.scatter(x1, y1, c='red', label='Actual Table')

x2, y2 = zip(*predicted_table.items())
ax.scatter(x2, y2, c='blue', label='Predicted Table')

ax.set_xlabel('KNN Top 6 Teams')
ax.set_ylabel('Position in Table')
ax.set_title('Premier League Tables')

ax.legend()

plt.show()