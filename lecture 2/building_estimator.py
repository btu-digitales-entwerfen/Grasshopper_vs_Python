
height = input('what height?')
height = float(height)
level_height = 4.0
max_height = 200.0
site_area = float(input('what area'))
pro_person = float(input('how much pro person'))

if(height <= max_height):
    level_number = height/level_height
    level_number = round(level_number)
    print(level_number)
    total_area = level_number*site_area
    total_ppl = total_area/pro_person
    total_ppl = round(total_ppl)
    print('total people',total_ppl)
else:
    print("your building is too high")

    

