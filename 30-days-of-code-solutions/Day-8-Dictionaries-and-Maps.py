# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())

ph_book = {}
for i in range(n):
    #pass key value to insert to a function
    entry = raw_input().split(" ")
    ph_book[str(entry[0])] = int(entry[1])

inp = raw_input()
while inp != "":
    try:
        if inp in ph_book:
            print inp+"="+str(ph_book[inp])
        else:
            print 'Not found'
        inp = raw_input()
    except (EOFError):
        break