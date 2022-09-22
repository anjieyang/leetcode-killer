#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <vector>
using namespace std;

struct TrieNode {
	bool flag;
	vector<TrieNode*> children;
	TrieNode() :flag(false), children(26, nullptr) {}
};

class WordDictionary {
private:
	TrieNode* root;

	void deleteNodes(TrieNode* root) {
		for (int i = 0; i < 26; ++i) {
			if (root->children[i]) {
				deleteNodes(root->children[i]);
			}
		}
		delete root;
	}

	void dfs(TrieNode* root, const string& word, int index, bool& result) {
		if (index == word.size()) {
			if (root->flag) {
				result = true;
			}
			return;
		}
		if (word[index] != '.') {
			if (!root->children[word[index] - 'a']) {
				return;
			}
			dfs(root->children[word[index] - 'a'], word, index + 1, result);
		}
		else {
			for (int i = 0; i < 26; ++i) {
				if (root->children[i]) {
					dfs(root->children[i], word, index + 1, result);
				}
			}
		}
	}
public:
	WordDictionary() :root(new TrieNode) {}

	~WordDictionary() { deleteNodes(root); }

	void addWord(string word) {
		TrieNode* current = root;
		for (int i = 0; i < word.size(); ++i) {
			if (!current->children[word[i] - 'a']) {
				current->children[word[i] - 'a'] = new TrieNode;
			}
			current = current->children[word[i] - 'a'];
		}
		current->flag = true;
	}

	bool search(string word) {
		bool result = false;
		dfs(root, word, 0, result);
		return result;
	}
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */