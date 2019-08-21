import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

"""if todos == response.json():
    print(True)
print(type(todos))
print(todos[:10])"""

users_completed_todos = {}

for todo in todos:
    if todo['completed']:
        try:
            users_completed_todos[todo['userId']] += 1
        except KeyError:
            users_completed_todos[todo['userId']] = 1

def determine_maximum_completed(users_completed_todos):
    for count in users_completed_todos.values():
        max_count = 0
        if count >= max_count:
            max_count = count
    return max_count

def create_top_users(users_completed_todos):
    top_users = []
    for userId, count in users_completed_todos.items():
        if count == determine_maximum_completed(users_completed_todos):
            top_users.append(userId)
    return top_users

top_users = create_top_users(users_completed_todos)
print(top_users)

def filter_top_users_completed_todos(top_users, todos):
    filtered_todos = []
    for todo in todos:
        if todo['userId'] in top_users and todo['completed']:
            filtered_todos.append(todo)
    print(filtered_todos)
    return filtered_todos

filtered_todos = filter_top_users_completed_todos(top_users, todos)

with open('filtered_data_file.json', mode='w') as data_file:
    json.dump(filtered_todos, data_file, indent=2)





