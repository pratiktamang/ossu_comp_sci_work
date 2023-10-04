
# Test cases
# twoSum([2,7,11,15],9)  # [0,1]
# twoSum([3,2,4],6)      # [1,2]
# twoSum([3,3],6)        # [0,1]

# Soluton 1
  # Time complexity: O(N^2);
  # Space Complexity: O(1);

def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        print([i,j])
        return [i,j]

# Soluton 2 - Optimized
  # Time complexity: O(N);
  # Space Complexity: O(N); 

def twoSum(nums, target):
  numToIndex = {}
  for i in range(len(nums)):
    if target - nums[i] in numToIndex:
      return [numToIndex[target - nums[i]], i]
    numToIndex[nums[i]] = i
  return []

"""
Consider
  a+b = target => (6 + 3 = 9)
then,
  target - a = b => (9 - 6 = 3)
  target - b = a => (9 - 3 = 6)

Let's break down the code:

The function initializes an empty dictionary numToIndex which will be used to store each number in
nums as a key and its index as the value.

We then loop through each number in the nums list using a for loop.

For each number nums[i], we check if the difference between the target and nums[i] (i.e., target - nums[i])
exists as a key in our dictionary numToIndex.

If it does, it means we have found two numbers in the list that add up to the target: the current number nums[i]
and the number whose index is stored in the dictionary for the key target - nums[i].

We then return the indices of these two numbers as a list.

If the difference does not exist in the dictionary, we store the current number nums[i] and its
index i in the dictionary.

If we finish looping through all the numbers in the list without finding two numbers that add up
to the target, we return an empty list.

The explanation at the bottom helps understand the logic:

Consider two numbers a and b such that a + b = target. For example, if target = 9, a = 6, and b = 3.

When we are at a (which is 6), we check if target - a (which is 9 - 6 = 3) exists in our dictionary.
If it does, it means the number b (3) was encountered earlier in the list and its index is stored in the dictionary.
Therefore, we can immediately return the indices of a and b.

Similarly, when we are at b (which is 3), we check if target - b (which is 9 - 3 = 6) exists in our dictionary.
If it does, it means the number a (6) was encountered earlier in the list and its index is stored in the dictionary.

This approach makes the function efficient because it only needs a single pass through the nums list to find the
solution, if it exists.
"""