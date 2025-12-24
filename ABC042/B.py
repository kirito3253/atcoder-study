import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
l = int(input_data[1])
data = input_data[2:2+n]

text = ''
for x in sorted(data):
    text = text + x
print(text)