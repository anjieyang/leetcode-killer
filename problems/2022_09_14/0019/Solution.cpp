#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <vector>
using namespace std;

//Definition for singly-linked list.
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = new ListNode(0, head);
        int length = 0;
        while (head!=NULL) {
            ++length;
            head = head->next;
        }

        ListNode* current = temp;
        for (int i = 1; i < length - n + 1; ++i) {
            current = current->next;
        }
        current->next = current->next->next;
        delete temp;
        return temp->next;
    }
};