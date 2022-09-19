stage = int(input())
matrix = [[0] * stage for i in range(stage)]
x, y, stepy, stepx, i = 0, 0, 0, 1, 1
while i < len(matrix[0]) ** 2:
    for j in range(len(matrix[0]) - stage, abs(x + (stage * stepx)), stepx):
        matrix[y][j] = i
        x = j
        i += 1
    stepx -= stepy
    stepy += stepx
    stepx = stepy - stepx
    stage -= 1
    for j in range(len(matrix[0]) - stage, abs(y + (stage * stepy)), stepy):
        matrix[j][x] = i
        y = j
        i += 1
    stepx -= stepy
    stepy += stepx
    stepx = stepy - stepx
    stepx *= -1
    stepy *= -1
print(matrix)