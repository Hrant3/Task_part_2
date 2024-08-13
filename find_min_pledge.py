def find_min_pledge(pledge_list):
    # Step 1: Filter out non-positive numbers
    positive_pledges = set(x for x in pledge_list if x > 0)

    # Step 2: Find the smallest missing positive integer
    smallest_missing = 1
    while smallest_missing in positive_pledges:
        smallest_missing += 1

    return smallest_missing


#
#
# Test cases
assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1

print("All test cases passed!")