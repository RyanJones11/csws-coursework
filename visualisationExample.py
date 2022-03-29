import matplotlib.pyplot as plt

names = ["Mercedes", "Redbull"]
points = [613.5, 585.5]

fig, axs = plt.subplots()

axs.set_title("Bar plot")
axs.bar(names, points)

input_values = [1, 2, 3, 4, 5]
value1 = [1, 30, 60, 40, 25]
value2 = [1, 8, 27, 64, 125]
fig, ax = plt.subplots()
ax.plot(input_values, value1, 'mD:')
ax.plot(input_values, value2, 'ro--')

plt.show()

fig, ax = plt.subplots()

ax.set_title("Bar plot")
ax.bar(resultNames, resultValues)
ax.set_yticks(range(0,100,10))
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()