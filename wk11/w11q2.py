text = input("Enter a string: ")

histogram = {}

for char in text:
    histogram[char] = histogram.get(char, 0) + 1

print("Histogram:", histogram)
