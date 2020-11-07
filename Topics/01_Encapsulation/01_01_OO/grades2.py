
def get_average(grades):
    count = len(grades)

    i = 0
    total = 0
    
    while i<count:    
        v = grades[i]
        total = total + v
        i = i + 1    
        
    avg = total / count
    
    return avg
    
jan = [100,100,80,95,100,90,92,84,98,100]
bobby = [75,66,84,90,92,100,38,73,22,95]

result = get_average(bobby)

print(result)