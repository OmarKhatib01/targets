import csv

file = csv.reader(open('data.csv', 'r'))


def popDict(input_file):
    target_dict = {}
    for idx, row in enumerate(input_file):
        name = row[0].split(' ')
        handle = row[1]
        if idx == 0:
            continue
        elif name[-1] in target_dict.keys():
            full_name = "_".join(name)
            target_dict[full_name] = {'fn': name[0], 'ln': " ".join(name[1:]), 'handle': handle}
            print(full_name)
        else:
            target_dict["_".join(name[1:])] = {'fn': name[0], 'ln': " ".join(name[1:]), 'handle': handle}
    return target_dict

targets = popDict(file)
print(targets)
