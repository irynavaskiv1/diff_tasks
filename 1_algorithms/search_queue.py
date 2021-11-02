from collections import deque


def person_is_seller(name):
    return name[0] == 'm'

graph = {}
graph["ira"] = ["1", "2", "3"]
graph["ania"] = ["4", "5"]
graph["myulia"] = ["mango"]


def search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.add(person)
    return False


search("myulia")
