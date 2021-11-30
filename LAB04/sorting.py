import random




def sort_func(randomlist):
    new_list = []
    for item in randomlist:
        if len(new_list) == 0:
            new_list.append(item)
        else:
            for idx, elem in enumerate(new_list):
                if item <= elem:
                    new_list.insert(idx, item)
                    break
                elif idx == len(new_list) -1:
                    new_list.append(item)
                    break
                continue
    return new_list

def sort_reverse_func(randomlist):
    new_list = []
    for item in randomlist:
        if len(new_list) == 0:
            new_list.append(item)
        else:
            for idx, elem in enumerate(new_list):
                if item >= elem:
                    new_list.insert(idx, item)
                    break
                elif idx == len(new_list) -1:
                    new_list.append(item)
                    break
                continue
    return new_list              


if __name__ == '__main__':
    randomlist = random.sample(range(0, 100), 50)
    
    if sort_func(randomlist) == sorted(randomlist):
        print('True')
    else:
        print('False')