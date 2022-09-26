var removeElement = function(nums, val) {
    let ogLength = nums.length;
    popper(nums, val);
    function popper(nums, val){
            if (nums.includes(val)) {nums.splice(nums.indexOf(val), 1)}
            if (nums.includes(val)) {popper(nums, val)}
        }
    let k = nums.length;
    
    function pusher(){
        if (nums.length !== ogLength) {nums.push(`_`)};
        if (nums.length !== ogLength) {pusher()}
    }
    
    console.log(nums, k)
};

removeElement([1,2,2,3,3,4],2)