csv_file = 'NewsSource.csv'
txt_file = 'News Source'

text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        print(line)
        print('\n\n')

        line = line.split(",", 2)
        text_list.append("".join(line))
        text_list.append('\n\n')


with open(txt_file, "w") as my_output_file:
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
