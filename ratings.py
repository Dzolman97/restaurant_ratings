"""Restaurant rating lister."""


# put your code here

dictionary = {}

file_opener = open("scores.txt")

def getScores():
   for line in file_opener:
      line = line.rstrip()
      key, value = line.split(":")
      dictionary[key] = int(value)


def add_rest_rate():
   print("Please add your favorite restaurant!")
   restaurant = input("Restaurant > ")
   rating = int(input("Rating out of 5 > "))

   dictionary[restaurant] = rating


def print_sorted(dictionary):
   dictionary = dict(sorted(dictionary.items()))

   for line, rate in dictionary.items():
      print(line, rate)


getScores()
add_rest_rate()
print_sorted(dictionary)