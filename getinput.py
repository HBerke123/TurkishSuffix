def ginput():
    try:
        return int(input())
    except ValueError:
        return None