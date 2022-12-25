def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(size[0])
        height.append(size[1])

    width.sort(reverse=True)
    height.sort(reverse=True)

    print(width, height)
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))