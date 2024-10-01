
# 1 step = 2.5 feet
steps = 0

def feet_to_steps(feet):
    global steps
    steps = feet / 2.5
    steps = int(steps)
    return steps

if __name__ == '__main__':
    feet_walked = float(input('Enter feet walked >> '))
    feet_to_steps(feet_walked)
    print(steps)
