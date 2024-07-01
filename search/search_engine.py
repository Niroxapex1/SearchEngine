import os

input_list = []

find_text = input('What do You Want To Find:👉 ')
sorter = input('How do You want to sort the list ? \nLower to Upper ->(ltu) or by there first indext ->(first indext) ? :👉')
input_list.append(find_text)
last_text = input_list[0] = f' {find_text} '

directory_path = 'dickens'
file_list = os.listdir(directory_path)

if sorter == 'ltu':
    file_list.sort(key=lambda x: len(x))


def find():
    found = False
    search_result = open('saerch_result.txt','w')
    search_sim = open('search_sim.txt','w')
    for filename in file_list:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r', errors='ignore') as file:
            for line_num, line in enumerate(file, start=0):
                if last_text in line:
                    search_result.write(f'{filename}:{line_num}'f' ---> {line}')
                    found = True
                else:
                    if find_text in line:
                        search_sim.write(f'{filename}:{line_num}'f' ---> {line}')
 
    if not found:
        print('nop, no one is here')
        
find()