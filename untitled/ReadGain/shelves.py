import shelve

with shelve.open('Shelve') as fruit:
    fruit['orange'] = 'A sweet citrus fruit'
    fruit['apple'] = 'A red fruit'
    fruit['grapes'] = 'A fruit for fox'
    fruit['tomato'] = 'Not really a  fruit'
    fruit['car'] = 'Dude..!!!'
    fruit['ban'] = 'Come baby...!!!'
    fruit['prachee'] = 'My fav fruit'

    del fruit['ban']
    while True:
        shelf_key = input("Enter a fruit:\n")
        if shelf_key == 'quit':
            break
        # elif shelf_key not in fruit.keys():
        #     print("Enter valid key")
        else:
            des = fruit.get(shelf_key, "We don't have such fruit "+shelf_key)
            print(des)
    ordered_keys = list(fruit.keys())
    ordered_keys.sort()
    for keys in ordered_keys:
        print(keys)
    for f in fruit.items():
        print(f)


