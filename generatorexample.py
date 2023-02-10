mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = create_generator() # create a generator

print(mygenerator)

for i in mygenerator:
    print(i)