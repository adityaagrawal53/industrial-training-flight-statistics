import matplotlib.pyplot as plt
import csv

x = [70, 80, 93, 75, 60, 70, 80, 75, 93, 75]
y = [60, 70, 80, 60, 70, 80, 93, 60, 93, 75]

plt.scatter(x, y)
plt.title('Student Marks')
plt.xlabel('Subjects')
plt.ylabel('Marks')

plt.show()

with open('addresses.csv', mode='r') as csv_file:
    my_input = []
    print(my_input)
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f'First name: {row["first name"]} Last name: {row["last name"]} Address: {row["city"]} {row["city acronym"]} {row["post"]}')
        my_input.append(row["first name"])
        line_count += 1
    print(my_input)
    print(f'Processed {line_count} lines.')