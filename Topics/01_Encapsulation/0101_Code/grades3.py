
def get_average(grades):
    # Code here
    return 75.5

def get_number_fails(grades):
    # Code here
    return 3

def get_highest_grade(grades):
    # Code here
    return 90

def get_grade(grades, index):
    return grades[index]

def set_grade(grades, index, value):
    grades[index] = value

jan = [100,100,80,95,100,90,92,84,98,100]    
bobby = [75,66,84,90,92,100,38,73,22,95]

print( get_average(jan) )

print( get_highest_grade(jan) )

v = get_grade(jan, 8)
set_grade(bobby, 8, v)

set_grade(bobby, 7, get_grade(jan, 7))

print( get_grade(bobby, 8) )

print( get_number_fails(bobby) )