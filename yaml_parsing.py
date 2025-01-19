import yaml

# print(dsata['operations']

def load_ops():
    file = "associations.yaml"
    with open(file) as f:
        data = yaml.safe_load(f)
    return data

def rando_levels():
    no_ht, ht, multiop = list(), list(), list()
    file = "associations.yaml"
    with open(file) as f:
        data = yaml.safe_load(f)
    for i in range(0, len(data['operations'])):
        print(i)
        print(data['operations'][i]['rando'])
        match data['operations'][i]['rando']:
            case 1:
                no_ht.append(data['operations'][i]['name'])
                print(no_ht)
                # break
            case 2:
                ht.append(data['operations'][i]['name'])
                print(ht)
                # break
            case 3:
                multiop.append(data['operations'][i]['name'])
                print(multiop)
                # break
            case _:
                print(data['operations'][i]['rando'], data['operations'][i]['rando'] == 2)
                print("non recognised flag, exiting")
                exit()
            
    return no_ht, ht, multiop
            


def load_ops_rando():
    file = "associations.yaml"
    randomise = list()

    with open(file) as f:
        data = yaml.safe_load(f)
    for i in range(0, len(data['operations'])):
        # print(data['operations'][i]['rando'], "\n")
        if data['operations'][i]['rando'] == True:
            randomise.append(data['operations'][i]['name'])
    return randomise
