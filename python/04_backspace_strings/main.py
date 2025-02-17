from typing import List


def transform(s: List[str]) -> List[str] :
    s_transformed = []
    for c in s:

        if c == "#":
            # remove a char
            if len(s_transformed) > 0 :
                s_transformed.pop()
        else:
            s_transformed.append(c)
    return s_transformed

def string_cmp_a( s1: List[str], s2: List[str] ) -> bool:

    # transform s1 and s2 into interpreted string
    s1_transformed = transform(s1)
    s2_transformed = transform(s2)


    # check the lengths, exit if different
    if len(s1_transformed) != len(s2_transformed):
        return False

    # check each character is the same
    for i in range(len(s1_transformed)):
        if s1_transformed[i] != s2_transformed[i]:
            return False

    return True
    
    # S: O(n1 + n2)  T: O(n1 + n2)
    
def resolve_hash(s: List[str], p: int) -> int:
    hash_counter = 0

    while p >= 0 :

        # we're pointing at a hash - add one to the counter (an dec)
        if s[p] == '#':
            hash_counter += 1

        # we're pointing at a char - take one from counter (and dec)
        elif hash_counter > 0:
            hash_counter -= 1

        # we're pointer at a char and no hashes left to resolv
        else:
            break

        p -= 1

    return p
            

def string_cmp_b( s1: List[str], s2: List[str] ) -> bool:

    p1 = len(s1) - 1
    p2 = len(s2) - 1

    
    while p1 >= 0 or p2 >= 0:
        
        p1 = resolve_hash(s1, p1)
        p2 = resolve_hash(s2, p2)

        print(f"p1 = {p1}, p2 = {p2}")

        if p1 < 0 and p2 < 0:
            # print("both strings matched")
            return True
        if p2 < 0 or p2 < 0:
            # print("one of the p's went out of bounds")
            return False

        if s1[p1] != s2[p2]:
            return False
        
        p1 -= 1
        p2 -= 1


    return True


def string_cmp( s1: List[str], s2: List[str]) -> bool:
    p1 = len(s1) - 1
    p2 = len(s2) - 1

    while p1 >= 0 or p2 >= 0:

        print(f"p1: {p1}, p2: {p2}")

        # resolve hashs
        if p1 >= 0 and s1[p1] == '#':
            backcount = 2
            while backcount > 0:
                p1 -= 1
                backcount -= 1

                if p1 >= 0 and s1[p1] == '#':
                    backcount += 2

        if p2 >= 0 and s2[p2] == '#':
            backcount = 2
            while backcount > 0 :
                p2 -= 1
                backcount -= 1

                if p2 >= 0 and s2[p2] == '#':
                    backcount +=2
        
        # both pointing at chars, compare
        if p1 >= 0 and p2 >= 0:
            if s1[p1] != s2[p2]:
                return False
            
            p1 -= 1
            p2 -= 1
        else:
            if p1 >= 0 or p2 >= 0:
                return False

    return True
 
#  from typing import List

def string_cmp_correct(s1: List[str], s2: List[str]) -> bool:
    p1 = len(s1) - 1
    p2 = len(s2) - 1

    while p1 >= 0 or p2 >= 0:
        # Resolve backspaces for s1
        if p1 >= 0 and s1[p1] == '#':
            backcount = 2
            while backcount > 0:
                p1 -= 1
                backcount -= 1
                if p1 >= 0 and s1[p1] == '#':
                    backcount += 2

        # Resolve backspaces for s2
        if p2 >= 0 and s2[p2] == '#':
            backcount = 2
            while backcount > 0:
                p2 -= 1
                backcount -= 1
                if p2 >= 0 and s2[p2] == '#':
                    backcount += 2

        # Compare characters
        if p1 >= 0 and p2 >= 0:
            if s1[p1] != s2[p2]:
                return False
            p1 -= 1
            p2 -= 1
        else:
            # If one pointer is valid and the other is not, strings are unequal
            if p1 >= 0 or p2 >= 0:
                return False

    return True


res = string_cmp("a", "")
assert res == False

res = string_cmp("a", "b")
assert res == False

res = string_cmp("abc", "abc")
assert res == True

res = string_cmp("ab#cd", "acd")
assert res == True

res = string_cmp("a##d", "d")
assert res == True

res = string_cmp("abc###", "")
assert res == True

res = string_cmp("abcd", "abc")
assert res == False

res = string_cmp("Abc", "abc")
assert res == False

print("all passed")