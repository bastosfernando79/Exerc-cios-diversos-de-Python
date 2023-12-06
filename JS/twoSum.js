function twoSum(nums, target) {
  let size = nums.length;
  let found = false;
  let x1 = 0;
  let x2 = 0;

  for (let i = 0; i < size; i++) {
    for (let j = i + 1; j < size; j++) {
      if (nums[i] + nums[j] === target) {
        x1 = i;
        x2 = j;
        found = true;
      }
      if (found === true) {
        break;
      }
    }
  }
  return [x1, x2];
}

let nums = [2, 7, 11, 15];
let target = 18;
let result = twoSum(nums, target);

console.log(result);
