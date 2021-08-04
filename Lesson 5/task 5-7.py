import json

dict_profit = {}
dict_lesion = {}
my_list = []

with open("task5-7.txt", encoding="utf-8") as file:
    lines = file.readlines()
    profit_list = []
    for line in lines:
        name, _, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            profit_list.append(profit)
            dict_profit.update({name: profit})
        elif profit < 0:
            dict_lesion.update({name:profit})
    my_list.append(dict_profit)
    my_list.append(dict_lesion)
    my_list.append({"Средняя прибыль": sum(profit_list) / len(profit_list)})
print(my_list)
with open("task5-7json", "w", encoding="utf-8") as file_json:
    json.dump(my_list, file_json)

