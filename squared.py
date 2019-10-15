def squared(x, action="square"):
    if x == 0:
        return 0
    else:
        if action == "square":
            return x ** 2
        elif action == "cube":
            return x ** 3
