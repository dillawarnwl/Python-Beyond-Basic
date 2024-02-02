from functools import partial

even_or_odd = lambda n,den: "even" if n%den==0 else 'odd'
even_or_odd =partial(even_or_odd,den=2)
print(even_or_odd(4))


list_of_even = lambda num: [i for i in range(num) if i%2 == 0]
print(list_of_even(100))


def recursive(num):
    if num == 0:
        return
    print(num)
    recursive(num - 1)

recursive(4)
