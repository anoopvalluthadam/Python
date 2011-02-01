demo_list = ['"', "Hello", "Anoop", "How", "are", "you", '"', "asdf", "ert4", "'", "Second", "Third", "'", "asdfasdf", "123123"]
list2 = []
string_l = []
string_constant = ""
i = -1
for value in demo_list:
    if value == "\"" and i!=0:
        i = 0
        continue
    if i == 0 and value == "\"":
        i = 2
        print string_constant
        string_constant = ''
        continue
    if i == 0:
        string_constant = string_constant + ' ' + value
        continue
    else:
        list2.append(value)

print string_l 
