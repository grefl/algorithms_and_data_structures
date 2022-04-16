


function two_sum(nums, target) {
  const map = {}
  
  for (let i = 0; i < nums.length; i +=1) {
      const num = nums[i];
      const diff = target - num;
      console.log(diff, num)
      console.log(map)
      if (map[diff] !== undefined) return [map[diff], i];
      else map[num] = i;
  }
  console.log(map)
  return [-1, -1] 
}

console.log(two_sum([2,7,11,15], 9))
