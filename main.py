file = open('/Users/kirill/Documents/txt_projeckt/Perepis.txt', 'r')

def task_a(file):
    count_more=0
    for i in file:
        listik=i.split()
        if int(listik[3].split('.')[2])<1978:
            print(str(listik[0]))
            count_more+=1
    print(count_more)

def task_b(file, st, end):
    for i in file:
        listik=i.split()
        if st < int(listik[3].split('.')[2]) and int(listik[3].split('.')[2])<end :
            print(str(listik))
task_b(file,1900,1990)
task_a(file)



