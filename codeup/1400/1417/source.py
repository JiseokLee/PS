heights = list(map(int, input().split()))
heights.sort(reverse=True)

print(heights[2])
