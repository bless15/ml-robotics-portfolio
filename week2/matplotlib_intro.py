"""import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 40]

plt.plot(x, y, marker="o", markersize="10")

plt.title("My First Graph")
plt.xlabel("Time")
plt.ylabel("Value")

plt.show()"""

"""import matplotlib.pyplot as plt
students = ['John', 'Mary', 'Love']
scores = [10, 50, 30]

plt.scatter(students, scores)
plt.title("My Scatter Plot")
plt.xlabel("students")
plt.ylabel("scores")

plt.show()"""


'''import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.subplot(1, 2, 1)
plt.plot(x, y)

plt.subplot(1, 2, 2)
plt.bar(x, y)

plt.show()'''


'''import matplotlib.pyplot as plt
x = [10, 25, 17, 13, 32]
y = [2, 7, 5, 1, 6]

plt.plot(x, y, marker = "o", markersize = 10)

plt.title("Part of my Exercises")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid()

plt.show()'''



import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
sales = [20, 35, 25, 45, 50]

plt.plot(days, sales)
plt.plot(days, sales, marker = "o", markersize = 10)
plt.title("Personal Exercise")
plt.xlabel("Days Side")
plt.ylabel("Sales Section")
plt.grid()
plt.show()