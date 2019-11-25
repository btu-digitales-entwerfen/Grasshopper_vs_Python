# main file





# importing module from the same directory as the main script

import useful2





# importing of modules from external folder
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'E:/Documents/GitHub/Grasshopper_vs_Python/lecture 5/1')
import useful
filetemp = useful.some_function()

print(useful.some_function())





# nested lists

grid = [
    [1,2,3], #0  #0,1,2
    [4,5,6], #1  #0,1,2
    [7,8,9,'a','b','c']  #2  #0,1,2,3,4,5
]

print(grid[2][3])






# error handling

try:
    var = 2
    var2 = "asd"
    var/var2
except ZeroDivisionError:
    print("you can't divide by zero")
except TypeError:
    print("you can't divide num by text")   
except:
    print("other error")






# working with files

# mode = 'r'  # read
# mode = 'w'  # write, can create files if it's not existing
# mode = 'a'  # append only 
# mode = 'r+' # read & write


filename = "e:/Documents/GitHub/Grasshopper_vs_Python/lecture 5/some_file.txt" #place here you filename 
f = open(filename,'w')
#line = f.readline()
#print(line)
#for line in f.readlines():
#    print(line)


text_to_write = "pineapple"
f.write('\n'+text_to_write)


class Building():
    variable1 = 1
    variable2 = 2
    variable3 = True
    windows_number = 0

    # initializing function
    def __init__(self,levels_num):
        self.levels = levels_num
    # regular function
    def Area(self):
        area = 100
        #temptemp = self.levels*area
        return self.levels*area

    # regular function
    def Function(self,something):
        something = something + 2
        # ---
        # ---
        # ---
        return something
        
temp = Building(5)
temp2 = Building(10)
print(temp2.Area())
temp.windows_number = 50
print(temp.windows_number)
print(temp.levels)