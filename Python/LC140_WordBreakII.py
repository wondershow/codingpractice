class Solution:
    """
        DP using memo
        O(n^2) time if not considering string contatnation, it could be o(2^n)
        
        consider the case 'aaaaa' where the word_dict is [a,aa,aaa,aaaa,aaaaa]
        
        so the result is a,aa,aaa (adding commas inbetween every neighboring a-a, so it is 2^n in the worst case. 
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(string, word_dict, memo):
            if string in memo:
                return memo[string]
            res = []
            if string in word_dict:
                res.append(string)
            
            for i in range(1, len(string)):
                if string[i:] in word_dict:
                    left = helper(string[:i], word_dict, memo)
                    for item in left:
                        new_item = item + " " + string[i:]
                        res.append(new_item)
            memo[string] = res
            return res
        memo = {}
        helper(s, set(wordDict), memo)
        return memo[s]
