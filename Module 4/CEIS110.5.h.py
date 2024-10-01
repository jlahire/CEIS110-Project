

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    dollar_cost = (driven_miles / miles_per_gallon) * dollars_per_gallon
    return dollar_cost

if __name__ == '__main__':
    miles_per_gallon= float(input()) 
    dollars_per_gallon= float(input())
    
    print('{:2f}'.format(driving_cost(10.0, miles_per_gallon, dollars_per_gallon)))
    print('{:2f}'.format(driving_cost(50.0, miles_per_gallon, dollars_per_gallon)))
    print('{:2f}'.format(driving_cost(400.0, miles_per_gallon, dollars_per_gallon)))

    
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    cost = driven_miles * (1.0/miles_per_gallon) * dollars_per_gallon
    return cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    print("{:.2f}".format(driving_cost(10.0, miles_per_gallon, dollars_per_gallon)))
    print("{:.2f}".format(driving_cost(50.0, miles_per_gallon, dollars_per_gallon)))
    print("{:.2f}".format(driving_cost(400.0, miles_per_gallon, dollars_per_gallon)))



