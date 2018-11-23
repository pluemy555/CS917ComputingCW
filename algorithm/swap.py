with open ('morse.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        line = line.replace('\n','').replace(' ', '')
        line = line.split(':')
        swap = [line[1], line[0]]
        print(':'.join(swap), end=",\n")
