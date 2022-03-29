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