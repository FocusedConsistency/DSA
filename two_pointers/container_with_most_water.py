def max_area(heights: List[int]):
    left = 0
    right = len(heights) - 1
    area_max = 0

    while left < right:
        # Calculating current area and storing it if it's larger than previous max
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        area_max = max(area_max, area)

        # Move the shorter pointer towards the other
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return area_max
