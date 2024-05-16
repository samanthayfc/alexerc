my_dict = {foo: 1, bar: 2, baz: 3, qux: 4}
my_dict = {k: v for k, v in my_dict.items() if k != foo}
print(my_dict) # {bar: 2, baz: 3, qux: 4}
