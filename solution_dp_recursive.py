INF = 10**9

def prefix_sums(pages):
    pref = [0]*len(pages)
    for i in range(1, len(pages)):
        pref[i] = pref[i-1] + pages[i]  
    return pref

def f(i, j, pref):   
    if i == 0 and j == 0:    
        return 0
    if j == 0:           
        return INF
    best = INF    

    for k in range(j-1, i):                
        last = pref[i] - pref[k]            
        val = max(f(k, j-1, pref), last)   
        best = min(best, val)       
    return best

def main():
    C, B = map(int, input().split())
    pages = [0]
    for _ in range(C):
        pages.append(int(input()))
    pref = prefix_sums(pages)
    ans = f(C, B, pref)       
    print(ans)           

if __name__ == "__main__":
    main()