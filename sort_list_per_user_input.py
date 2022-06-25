numrat = []
while True:
    numri = input("Enter a number, press quit to stop: ")
    if numri == "quit":
        break
    else:
        numrat.append(int(numri))
action = input('''
    "Press asc to sort in ascending order, 
    Press desc to sort in descending order,
    or None to print numbers unsorted.
    ''')
if action.lower() not in ("asc", "desc", 'none'):
    print("You are only allowed to insert \"no\",\"asc\",\"desc")
    print(input('''
    "Press asc to sort the list in ascending order, 
    Press desc to sort it in descending order,
    or None to print numbers unsorted.
    '''))


def sorting(numrat, action):
    if action.lower() == "asc":
        numrat.sort()
        print(numrat)
    elif action.lower() == "desc":
        numrat.sort(reverse=True)
        print(numrat)
    else:
        print(numrat)
sorting(numrat, action)
