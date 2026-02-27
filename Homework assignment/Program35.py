def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        key = "".join(sorted(word))  # sort letters

        if key not in anagrams:
            anagrams[key] = []
        
        anagrams[key].append(word)

    return list(anagrams.values())


# Test Cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
