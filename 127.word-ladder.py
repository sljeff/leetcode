from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        word_map = self.make_word_map(wordList + [beginWord])

        LEN = {}
        SAVED = set()
        stack = deque([beginWord])
        while True:
            if not stack:
                break
            word = stack.popleft()
            if word in SAVED:
                continue
            SAVED.add(word)

            targets = word_map.get(word)
            if not targets:
                continue

            for target in targets:
                before_length = LEN.get(word, 0)
                length = before_length + 1
                exists_length = LEN.get(target)
                if exists_length:
                    length = min(exists_length, length)
                LEN[target] = length
                stack.append(target)

        return LEN[endWord] + 1 if LEN.get(endWord) else 0

    def make_word_map(self, words):
        word_map = {}
        for i in range(len(words)):
            word = words[i]
            for j in range(i + 1, len(words)):
                word2 = words[j]
                diff_count = 0
                for x in range(len(word)):
                    if word[x] == word2[x]:
                        continue
                    diff_count += 1
                    if diff_count > 1:
                        break
                if diff_count == 1:
                    word_map.setdefault(word, set()).add(word2)
                    word_map.setdefault(word2, set()).add(word)
        return word_map
