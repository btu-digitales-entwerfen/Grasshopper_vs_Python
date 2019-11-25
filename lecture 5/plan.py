w

#import stuff
#little bit about general stuff

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['a','b','c','d']
]
'''
try:
    asdasd
except dividedbyzero
except invalidvalue
'''
##########
'''
mode = 'r' # read
# mode = 'w' # write, can create files
# mode = 'a' # append only 
# mode = 'r+'# read & write


f = open("file",mode)

f.readline()
f.readlines()

for line in f.readlines():
    print(line)

f.close()

f.write("\nasdasd")



'''
#classes

#str,num,boolean

class Building:

    #lvl = None




    def __init__(self, levels, name):
        self.lvl = levels


a = Building(10,"aa")

a.lvl