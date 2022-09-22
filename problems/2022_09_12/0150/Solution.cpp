#include <fstream>
#include <iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (int i=0; i<tokens.size(); i++){
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/"){
                stk.push(stoi(tokens[i]));
            } 
            else {
                int num1 = stk.top();
                stk.pop();
                int num2 = stk.top();
                stk.pop();
                if(tokens[i]=="+"){
                    stk.push(num1 + num2);
                }
                else if(tokens[i]=="-"){
                    stk.push(num2 - num1);
                }
                else if(tokens[i]=="*"){
                    stk.push((long)num1 * (long)num2);
                }
                else if(tokens[i]=="/"){
                    stk.push(num2 / num1);
                }
            }
        }
        return stk.top();
    }
};