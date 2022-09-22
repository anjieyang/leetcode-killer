#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
    int left=0;
    int right=numbers.size()-1;
    while(left < right){
        int sum = numbers[left] + numbers[right];
        if(sum < target){
            left++;
        } 
        else if(sum > target){
            right--;
        } 
        else {
            return vector<int>(left+1, right+1);
        }
    }
    return vector<int>(-1, -1);
    }
};