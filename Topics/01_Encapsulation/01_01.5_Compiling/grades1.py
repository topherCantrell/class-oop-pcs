
grades = [75,66,84,90,92,100,38,73,22,95]
count = 10

i = 0
total = 0
while True:
    if i >= count:
        break
    v = grades[i]
    total = total + v
    i = i + 1
    
    
avg = total / count

print(avg)