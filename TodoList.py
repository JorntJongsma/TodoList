from datetime import datetime, date
import itertools
import json


class Todolis():

    with open("todo_data.json" ,'r') as r_file:
        r = json.load(r_file)

    lastkey = list(r.keys())[-1]
    id = itertools.count(int(lastkey)+1)

    # auto update

    def __init__(self, name, end_date,priority ):
        self.id =  next(self.id)
        self.name = name
        self.start_date = datetime.now()
        self.end_date = end_date
        self.priority = priority

todo = Todolis("plassen", date(2024, 7, 1), 3)

item = {
    todo.id:[todo.name ,str(todo.start_date), str(todo.end_date), todo.priority]
}

with open("todo_data.json" ,'r') as r_file:
    r = json.load(r_file)


r.update(item)

with open("todo_data.json" ,'w') as file:
    json.dump(r, file)

