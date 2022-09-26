//first pass - accepted 5%, 20%
var search = function(nums, target) {
	for (let i = 0; i<nums.length; i++){
    if (nums[i] === target){return i}
  }
  return -1
};

//second pass - accepted 23%, 78%
var search = function(nums, target) {
	return (nums.indexOf(target))
};
