def robot_in_a_grid(start, end, grid):
    # if starting location is blocked - no path possible
    if grid[start[0]][start[1]] == 'x':
        return None

    # find path and store parents in parent dict()
    # will return True if path is found, otherwise returns None
    parent = dict()
    if helper(start, end, grid, parent):
        return generate_path(start, end, parent)

    # no path has been found
    return None


def helper(curr, end, grid, parent):
    if curr == end:
        return True

    # move right - boundary check and position check
    if curr[1] + 1 < len(grid) and grid[curr[0]][curr[1] + 1] != 'x':
        next_location = (curr[0], curr[1] + 1)
        parent[next_location] = curr
        if helper(next_location, end, grid, parent):
            return True

    # move down - boundary check and position check
    if curr[0] + 1 < len(grid) and grid[curr[0] + 1][curr[1]] != 'x':
        next_location = (curr[0] + 1, curr[1])
        parent[next_location] = curr
        if helper(next_location, end, grid, parent):
            return True

    # if backtracking - delete current location from parent dictionary
    if curr in parent:
        del parent[curr]


def generate_path(start, end, parent):
    path = list()
    curr = end
    while curr != start:
        path.insert(0, curr)
        curr = parent[curr]

    path.insert(0, start)
    return path


g = [[0, 'x', 0, 0],
     [0, 0, 0, 0],
     [0, 'x', 0, 'x'],
     [0, 'x', 0, 0]]
c = (0, 0)
d = (3, 3)
print(robot_in_a_grid(c, d, g))
