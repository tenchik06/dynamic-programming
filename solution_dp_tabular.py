def solve(C, B, pages):
    pref = [0]*(C+1)        
    for i in range(1, C+1):
        pref[i] = pref[i-1] + pages[i]

    INF = 10**9

    dp = [[INF]*(B+1) for _ in range(C+1)]    
    cut = [[0]*(B+1) for _ in range(C+1)]    

    dp[0][0] = 0

    for i in range(1, C+1):                 
        for j in range(1, min(i, B)+1):   
            for k in range(j-1, i):         
                last = pref[i] - pref[k]          
                val = max(dp[k][j-1], last)      

                if val < dp[i][j]:            
                    dp[i][j] = val
                    cut[i][j] = k             

    ans = dp[C][B]

    res = []
    i = C
    j = B

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