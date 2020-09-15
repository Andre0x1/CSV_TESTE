import csv


row_list = [["SN", "Name", "Contribution"],
             [1, "Lis Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]


cars = [["Ford"], ["Volvo"], ["BMW"]]

with open('Test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cars)

