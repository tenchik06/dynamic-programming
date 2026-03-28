INF = 10**9

def prefix_sums(pages):
    """Counts prefix sums"""
    pref = [0] * len(pages)         
    for i in range(1, len(pages)):
        pref[i] = pref[i-1] + pages[i]  
    return pref

def solve(C, B, pages):
    pref = prefix_sums(pages)  

    dp = [[-1]*(B+1) for _ in range(C+1)]
    cut = [[0]*(B+1) for _ in range(C+1)]     

    def f(i, j):
        if i == 0 and j == 0:   
            return 0
        if j == 0:      
            return INF

        if dp[i][j] != -1:  
            return dp[i][j]

        best = INF

        for k in range(j-1, i):       
            last = pref[i] - pref[k]     
            val = max(f(k, j-1), last)    

            if val < best:
                best = val
                cut[i][j] = k   

        dp[i][j] = best
        return best
    ans = f(C, B)   

    res = []
    i, j = C, B

    while j > 0:          
        k = cut[i][j]          
        res.append((k+1, i))
        i = k
        j -= 1

    res.reverse()      

    return ans, res

def main():
    C, B = map(int, input().split())
    pages = [0]
    for _ in range(C):
        pages.append(int(input()))
    ans, res = solve(C, B, pages)

    print(ans)         
    for l, r in res:
        print(l, r)

if __name__ == "__main__":
    main()