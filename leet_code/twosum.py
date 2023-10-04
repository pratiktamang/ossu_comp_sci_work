
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

# Consider a+b = target(6 + 3 = 9)

# then,
# target - a = b(9 - 6 = 3)
# target - b = a(9 - 3 = 6)