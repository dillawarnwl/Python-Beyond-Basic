# lambda function syntax
# func_name = lambda varialbe: expression
greet = lambda name:print("Assalam-o-Alaikum! " + name)
greet("Ali")
# or
greet = (lambda name: print(f"Assalam-o-Alaikum! {name}"))("Ali")
print(greet)

# lambda function with conditions syntax
# func_name = lambda varialbe: "statement" if condition else "statement"
even_or_odd = lambda num: f"{num} is even." if num%2==0 else f"{num} is odd."
print(even_or_odd(3))

# lambda function with loops syntax
# func_name = lambda varialbe: [iterater for iterater in iterable condition]
even_or_odd = lambda nums: [num for num in range(nums) if num%2==0]
print(even_or_odd(50))