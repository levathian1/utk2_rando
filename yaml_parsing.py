import yaml

# print(dsata['operations']

def load_ops():
    file = "associations.yaml"
    with open(file) as f:
        data = yaml.safe_load(f)
    return data

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
