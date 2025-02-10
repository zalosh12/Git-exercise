def build_full_bin_tree(depth, num):
    if depth == 0:
        return [num]
    left = build_full_bin_tree(depth - 1, num - ((2**depth)/2))
    right = build_full_bin_tree(depth - 1, num + ((2**depth)/2))
    return [num, left, right]

t = build_full_bin_tree(3,8)
print(t)


