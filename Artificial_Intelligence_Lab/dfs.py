def dfs(maze, start, end):
    stack = [(start, [start])]  # store (position, path_to_here)
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        # If we reached the end, return the path
        if (x, y) == end:
            return path

        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy

            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                stack.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # No path found


# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = dfs(maze, start, end)
print("Path:", path)
