# python3
x = 31
prime = 48112959837082048697

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def are_equal(string1, string2):
    return string1 == string2

def poly_hash(word):  
    hash = 0
    for c in word:
        hash = (hash * x + ord(c)) % prime # nice large prime number from https://primes.utm.edu/lists/small/small.html
    return hash

def rabin_karp(P, T):
    result = []
    pHash = poly_hash(P)
    for i in range(0, len(T) - len(P) + 1):
        tHash = poly_hash(T[i:i+len(P)])
        if pHash != tHash:
            continue
        if are_equal(T[i:i+len(P)], P):
            result.append(i)
    return result

def Rabin_Karp_Matcher(pattern, text, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    # print_occurrences(get_occurrences(*read_input()))
    print_occurrences(Rabin_Karp_Matcher(*read_input(), 906123948719713298744, 298417298472175097132))
    