
def myfunc(str_to):
    even_str = ""
    odd_str = ""
    for j in range(0,len(str_to)):
        if j % 2 == 0 :
            even_str = even_str + str_to[j]
        else:
            odd_str = odd_str + str_to[j]
    final_str = even_str + " " + odd_str
    print final_str

t = int(raw_input())
for i in range(0,t):
    str_to_test = raw_input()
    myfunc(str_to_test)