class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0

        q, visited = [beginWord], {beginWord}
        ans = 1

        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word==endWord: return ans

                for j in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        charList = list(word)
                        charList[j] = c
                        newWord = ''.join(charList)
                        if newWord in wordSet and newWord not in visited:
                            q.append(newWord)
                            visited.add(newWord)
            ans+=1
        return 0

'''
Time Complexity :- BigO(M^2 * N), where M is size of dequeued word & N is size of our word list

Space Complexity :- BigO(M * N) where M is no. of character that we had in our string & N is the size of our wordList.
'''

