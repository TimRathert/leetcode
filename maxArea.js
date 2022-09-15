var maxArea = function(height) {
    max = 0;
    for (var i = 0; i < height.length; i++) {
        for (var j = 1; j < height.length-1; j++) {
            if (height[i] <= height[j]){
                if ((j-i)*height[i] > max){
                max = (j-i)*height[i]
                }
            }
        }
    }
    console.log(max)
};

maxArea[1,8,6,2,5,4,8,3,7]