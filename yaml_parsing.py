import yaml

# TODO: rearange yaml organisation to clean up reading process

def load_ops():
    file = "associations.yaml"
    with open(file) as f:
        data = yaml.safe_load(f)
    return data

def rando_levels():
    """_summary_: Retrieve randomiser flagged operations in association.yaml and sort into corresponding list

    Returns:
        _type_: List: 3 lists containing each type of randomiser flagged operation as defined in operation_classification.py
    """
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
            
