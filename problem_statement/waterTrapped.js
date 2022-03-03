// Water trap problem

let waterTrap = function (height){
    let trappedWater = 0, n = height.length;
    let l = 0, r = n-1; //for two pointer approach
    let leftMax = 0, rightMax =0; //for keeping the leftMax and rightMax height
    while(l<=r){ //min of both
        if(leftMax > rightMax){ //choose index as r
            trappedWater += Math.max(0, rightMax-height[r]);
            rightMax = Math.max(rightMax, height[r]); //adding the trapped water
            r--;
        } else{ //choose index as l
            trappedWater += Math.max(0, leftMax-height[l]);
            leftMax = Math.max(leftMax, height[l]); //adding the trapped water
            l++;
        }
    }
    return trappedWater; 
    // Alternative Approach:
    // let left = new Array(n), right = new Array(n);        
    // left[0] = height[0];
    // for(let i = 1; i < n; i++)
    //     left[i] = Math.max(left[i-1], height[i]);
    // right[n-1] = height[n-1];
    // for(let i = n-2; i>=0; i--)
    //     right[i]= Math.max(right[i+1], height[i]);

    // for(let i=0; i < n; i++)
        // trappedWater += (Math.min(left[i], right[i]) - height[i]);
}
console.log("Water trapped in [0,1,0,2,1,0,1,3,2,1,2,1]: ", waterTrap([0,1,0,2,1,0,1,3,2,1,2,1]));
console.log("Water trapped in [4,2,0,3,2,5]: ", waterTrap([4,2,0,3,2,5]));