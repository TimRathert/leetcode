// accepted a month ago. going to try again from scratch and see what I can do
var searchInsert = function(nums, target) {
    if (nums.includes(target)){
      return nums.indexOf(target)}
    else {
      if (nums[nums.length-1] > target){
        for (let i = 0; i<nums.length; i++){
            if (nums[i] > target){return i}
        }
      }
      else {return nums.length}  
    }        
};

// second attemt. Much more lean!
var searchInsert = function(nums, target) {
	for (let i = 0; i<nums.length; i++){
    if(nums[i]===target || nums[i]>target){return i}
    if(i === nums.length-1){return i+1}
  }    
};
