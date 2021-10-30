largest = None;
smallest = None;
while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break;
    try :
        fnum = int(num)
        if smallest is None :
            smallest = fnum
        if largest is None:
            largest = fnum
        if fnum < smallest :
            smallest = fnum
        if fnum > largest :
            largest = fnum
    except :
        print('invalid input')
        continue;
print('Maximum is', largest)
print('Minimum is', smallest)
