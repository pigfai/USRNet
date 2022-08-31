import os
file_path = "./trainsets/trainH/"
list_all = os.listdir(file_path)
print(list_all)


for i in list_all:
    print(i)
    used_name = file_path + i
    fix_name_png = file_path + i[:-3] + "png"
    print(used_name, fix_name_png)
    os.rename(used_name, fix_name_png)
