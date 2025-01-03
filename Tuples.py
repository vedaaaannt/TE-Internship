Fruits=("Orange", "Apple", "Watermelon", "Guava")           # Initializing 1st Tuple
Cars=("Ferrari","BMW","Porsche","Toyota","BMW")             # Initializing 2nd Tuple

print(Fruits)
print(Cars)

print(Cars[:3])                                             # Slicing Function

print(Cars+Fruits)                                          # Concatenation Function

print(Fruits*2)                                             # Iteration Function

print(Fruits.index("Apple"))                                # .index() Function

print(Cars.count("BMW"))                                    # .count() Function

print(len(Cars))                                            # len() Function

print(max(Cars))                                            # max() Function

for i in Fruits:
    print(i)