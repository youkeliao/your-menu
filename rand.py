import random
import json


def func(n: int):
    files = [random.sample(staple_food, 1), random.sample(food2, n), random.sample(food3, 1), random.sample(food4, 2),
             random.sample(breakfast, 1)]
    return files


with open("result.json", "r+", encoding="utf8") as f:
    temp = json.load(f)
    staple_food = temp["菜谱"]["主食"]
    food2 = temp["菜谱"]["家常菜"]
    food3 = temp["菜谱"]["汤与粥"]
    food4 = temp["菜谱"]["甜品"]
    breakfast = temp["菜谱"]["早餐"]
    # print(random.choice(staple_food))
    # print(random.sample(food2, 3))
    # print(random.choice(food3))
    # print(random.choice(food4))
    # print(f"早餐：{breakfast}")
