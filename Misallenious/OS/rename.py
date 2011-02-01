import os
import os.path
import sys

rename_counter = 1

def group_rename(dir_path, file_path, filtering_string, new_name):
    """ Renames the files """
    global rename_counter
    final_file_path = dir_path + '/' + file_path
    final_rename_path = dir_path + '/' + new_name + str(rename_counter) + filtering_string
    os.rename(final_file_path, final_rename_path)
    print 'Converting \o' + final_file_path + '\'' + '[to]' + '\''+ final_rename_path + '\''
    rename_counter += 1

contents = os.listdir(sys.argv[1])
contents.sort()
print contents

#Holds the name of files
filtering_string = sys.argv[2]
filtered_contents = filter(lambda x:x.endswith(filtering_string),contents)
#The list which holds the the filtered elements according to the users choice
new_name = sys.argv[3]
for file_path in filtered_contents:
    group_rename(sys.argv[1],file_path, filtering_string, new_name)
