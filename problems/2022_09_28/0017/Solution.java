class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        
        if (digits.length() == 0) {
            return res;
        }
        
        Map<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        
        String temp = "";
        int index = 0;
        
        backtrack(index, temp, digits, res, map);
        return res;
    }
    
    private static void backtrack(int i, String temp, String digits, List<String> res, Map<Character, String> map) {
        if (i == digits.length()) {
            res.add(temp);
            return;
        }
        
        char digit = digits.charAt(i);
        String str = map.get(digit);
        
        for (int j = 0; j < str.length(); ++j) {
            char c = str.charAt(j);
            temp += c;
            backtrack(i + 1, temp, digits, res, map);
            temp = temp.substring(0, temp.length() - 1);
        }
    }
}