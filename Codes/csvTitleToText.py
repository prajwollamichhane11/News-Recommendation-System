csv_file = 'title.csv'
txt_file = 'News Title'

text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        print(line)
        print('\n\n')

        line = line.split(",", 2)
        text_list.append("".join(line))
        text_list.append('\n\n')


with open(txt_file, "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
