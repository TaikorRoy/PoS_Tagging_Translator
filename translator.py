__author__ = 'Taikor'


import json

json_path = "PoS_tagging_dict.json"   # json file storing the tagging dictionary

def translating(input):
    with open(json_path, 'r', encoding='utf-8') as f:
        json_string = f.read()
    tagging_dict = json.loads(json_string)
    taggings = input.split(' ')

    result = list()
    for tagging in taggings:
        result.append(mapping(tagging, tagging_dict))
    output = ' '.join(result)
    print(output)
    return output

def mapping(tagging_abbr, dict):
    capital = tagging_abbr[0]
    try:
        sub_dict = dict[capital]
    except:
        return 'Level 1_Tagging_Not_Found'
    try:
        return sub_dict[tagging_abbr]
    except:
        return 'Level_2_Tagging_Not_Found'

""" Example Code!!
input = 'ag an ad a e ng nr ns nt nz nx n q r s tg vg vd vn v y z'
translating(input)
"""