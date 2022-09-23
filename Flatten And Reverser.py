values = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
result = []

def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            result.append(i)

flatten(values)
print(result)
