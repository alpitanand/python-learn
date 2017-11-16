import shelve

books = shelve.open('books')
books['recipes'] = {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
                    'beans_on_toast': ['bread', 'bread'],
                    'scrambled_eggs': ['milk', 'egg', 'butter'],
                    'soup': ['tomato', 'water'],
                    'pasta': ['pasta', 'water', 'milk']}
books['maintenance'] = {'stuck': ['oil'],
                        'loose': ['gaffer tape']
                        }

print(books['recipes'])
books.close()


