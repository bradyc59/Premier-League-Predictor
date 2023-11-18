import matplotlib.pyplot as plt

actual_table = {'City': 1,
                'Liverpool': 2,
                'Chelsea': 3,
                'Tottenham': 4,
                'Arsenal': 5,
                'United': 6,
                'West Ham': 7,
                'Leicester': 8,
                'Brighton': 9,
                'Wolves': 10,
                'Newcastle': 11,
                'Palace': 12,
                'Brentford': 13,
                'Villa': 14,
                'Southampton': 15,
                'Everton': 16,
                'Leeds': 17,
                'Burnley': 18,
                'Watford': 19,
                'Norwich': 20}

predicted_table = {'City': 1,
           'Liverpool': 2,
           'Chelsea': 3,
           'Arsenal': 4,
           'Tottenham': 5,
           'United': 6,
           'West Ham': 7,
           'Southampton': 8,
           'Palace': 9,
           'Brighton': 10,
           'Wolves': 11,
           'Leicester': 12,
           'Villa': 13,
           'Brentford': 14,
           'Newcastle': 15,
           'Everton': 16,
           'Leeds': 17,
           'Watford': 18,
           'Burnley': 19,
           'Norwich': 20
           }

fig, ax = plt.subplots()

x1, y1 = zip(*actual_table.items())
ax.scatter(x1, y1, c='red', label='Actual Table')

x2, y2 = zip(*predicted_table.items())
ax.scatter(x2, y2, c='blue', label='Predicted Table')

ax.set_xlabel('Teams')
ax.set_ylabel('Position in Table')
ax.set_title('Premier League Tables')

ax.legend()

plt.show()
