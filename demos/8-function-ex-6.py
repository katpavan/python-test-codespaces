def max(x, y):
    if x > y:
        return x
    else:
        return y

z = max(5,3) + 2

print(z)

# Traceback (most recent call last):
#   File "/workspaces/python-test-codespaces/function-ex-5.py", line 7, in <module>
#     z = max(5,3) + 2
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

