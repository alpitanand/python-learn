import shelve

# blt = ['Lettuce', 'Tomato', 'Orange', 'Grapes', 'Mango']
# beans_on_toast = ['Beans', 'Bread']
# scrambled_eggs = ['Bread', 'Butter']
# soup = ['tin of soup']
# pasta = ['pasta', 'pasta soup']
# paneer = ['Çurd', 'Cheese']

# after adding to dataBase you can easily comment out all the adding and looping coz its been already added to database.

with shelve.open("Recipe", writeback=True) as recipe:
    # recipe['blt'] = blt
    # recipe['beans_on_toast'] = beans_on_toast
    # recipe['scrambled_eggs'] = scrambled_eggs
    # recipe['soup'] = soup
    # recipe['pasta'] = pasta
    # recipe['paneer'] = paneer
    # recipe["blt"].append("Alpit")
    # temp_list = recipe['blt']
    # temp_list.append("Alpit")
    # recipe['blt'] = temp_list
    # for stake in temp_list:
    #     print(stake)
    recipe['soup'].append('croutons')
    for rec in recipe:
        print("{} {}".format(rec, recipe[rec]))
