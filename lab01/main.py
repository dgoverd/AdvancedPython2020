data = list(map(float, input().split()))

for i in range(len(data)):
    data[i] = data[i]**2
data.sort()
data_str = [str(elem) for elem in data]
print(" " . join(data_str))
