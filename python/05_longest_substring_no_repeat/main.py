# Given a string, find the length of the longest substring
# without repeating characters

# Questions:
# Do the characters need to be unique?  i.e. are we looking for contiguous repeats?
# Case sensitivity?  -> no, all lowercase

# Define solution here
# Attempt 1: Brute Force
def longest_substring_1(s: str) -> int:

    length = len(s)

    if length <= 1:
        return length

    longest = 0

    for start in range(0, (length - longest)):
        myset = set()

        for p in range(start, length):
            
            if s[p] in myset:
                # longest = max(longest, len(myset))
                break
            else:
                myset.add(s[p])
                longest = max(longest, len(myset))
    return longest

    # S =  O(N)
    # T =  O(N^2)


# Attempt 2: Optimising - use more space, do puzzle in 1 pass
def longest_substring_2(s: str) -> int:

    longest = 0

    hashmap = {}

    # init
    p1 = 0
    p2 = p1 + 1

    hashmap[s[p1]] = p1
    hashmap[s[p2]] = p2

    print(f"p1 = {p1}")
    print(f"p2 = {p2}")

    for p2 in range (p2, len(s)):

        print(f"hashmap = {hashmap}")
        if s[p2] in hashmap:

            cur_p1 = p1
            for p1 in range(cur_p1, hashmap[s[p2]]):
                hashmap.pop(s[p1])
            # adjust p1 & p2
            p1 = hashmap[s[p2]] + 1
            p2 = p1 + 1

            print(f"now hashmap = {hashmap}")

            # adjust hashmap
        else:
            hashmap[p2] = p2 


    # p1 = s[0]
    # # search for 1st character same, p2 is this -1 
    # # work out different between p1 and p2, this is now the longest (max(longest, difference))
    # # add each character as seen into our set
    # {a, b, c}
    # p1 = b, 


# Attempt 3: 
def longest_substring_3(s: str) -> int:
    # print(f"string = {s}")

    length = len(s)

    if length <= 1:
        return length

    hashmap = {}
    longest = 0
    p1 = 0

    for p2 in range( p1, length):

        # it's in the hashmap, slide p1 and remove anything with lesser indexes
        if s[p2] in hashmap:

            while p1 != p2:
                hashmap.pop(s[p1])
                p1 += 1
            hashmap[s[p1]] = p1
        
        #  not in hashmap, add it!
        else:
            hashmap[s[p2]] = p2
            longest = max(longest, len(hashmap))
        # print(f"hash = {hashmap}")
    return longest


# my version (it works!)
def longest_substring(s: str) -> int:

    length = len(s)

    if length <= 1:
        return length

    longest = 0
    p1 = 0
    hashmap = {}

    for p2 in range(p1, length):

        if s[p2] in hashmap:

            stop_at = hashmap[s[p2]] + 1

            while p1 != stop_at:
                hashmap.pop(s[p1])
                p1 += 1
            
            hashmap[s[p2]] = p2
            
        else:
            hashmap[s[p2]] = p2
            longest = max(longest, len(hashmap))
    
    return longest
    
    # S: O(N)
    # T: O(N)


# their solution (doens't use pop())
def longest_substring(s: str) -> int:

    if (len(s) <= 1):
        return len(s)

    hashmap = {}

    p1 = 0
    longest = 0

    for p2 in range(p1, len(s)):
        currentChar = s[p2]

        if currentChar in hashmap:
            prevSeenChar = hashmap[currentChar]

            if prevSeenChar  >= p1:
                p1 = prevSeenChar + 1

        hashmap[currentChar] = p2
        longest = max(longest, p2 - p1 + 1)
    
    return longest
    # S: O(N)
    # T: O(N)



# Put Test Cases Here
# "abcacbb" -> 3 or 6?  ("abc|bca|acb" or "abcacb")
res = longest_substring("abccabb")
assert(res == 3)

res = longest_substring("cccccc")
assert(res == 1)

res = longest_substring("")
assert(res == 0)

res = longest_substring("abcdba")
assert(res == 4)

res = longest_substring("a")
assert(res == 1)

res = longest_substring("aa")
assert(res == 1)

res = longest_substring("au")
assert(res == 2)

res = longest_substring("dvdf")
assert(res == 3)
print("All passed!")


