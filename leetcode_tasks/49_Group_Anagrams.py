def groupAnagrams(strs: list[str]) -> list[list[str]]:
    annograms = {}
    
    for word in strs:
        all_symb_words = [0 for _ in range(26)]
        
        for symb in word:
            all_symb_words[ord(symb) - ord('a')] += 1
            
        word_hash = tuple(all_symb_words)
        
        if word_hash in annograms:
            annograms[word_hash].append(word)
        else:
            annograms[word_hash] = [word]
    
    return list(annograms.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    strs2 = [""]
    print(groupAnagrams(strs2))
    strs3 = ["a"]
    print(groupAnagrams(strs3))
