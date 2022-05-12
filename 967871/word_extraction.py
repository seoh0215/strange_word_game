import os

file_list = os.listdir('.')
text_files = [file for file in file_list if file.endswith('txt')]
dict_files = []

for file in text_files:
    dict_files.append(open(file, 'r', encoding='UTF-8'))
    
words = []

for dict_file in dict_files:
    content = dict_file.readlines()
    for idx in range(1, len(content)):
        if content[idx-1] == '#00\n':
            words.append(content[idx].replace('-', '').replace(' ', '').replace('ㆍ', '').replace('^', ''))
        
f = open('dict.txt', 'wt', encoding='UTF-8')
f.writelines(words)
f.close()

    