class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const prefix = [1];
        const suffix = [1];
        const res = [];

        for (let i = 0; i < nums.length - 1; ++i) {
            prefix.push(prefix[i] * nums[i]);
        }

        for (let i = nums.length - 1; i > 0; --i) {
            suffix.unshift(suffix[0] * nums[i]);
        }

        for (let i = 0; i < nums.length; ++i) {
            res.push(prefix[i] * suffix[i]);
        }

        return res;
    }
}
