#include<bits/stdc++.h>
using namespace std ;
int MOD = 1e4 ;
int n, x, fact ;

int dp[100][100000] ;
int solve(int in, int k) {
    int ans = 0 ;
    if (in == 0) {
        return fact ;
    }
    int& curr = dp[in][k] ;
    if (curr != -1) return curr ;
    for(int i=k+2; i<=x; ++i) {
        ans = (ans + solve(in-1, i)) % MOD ;
    }
    return curr = ans ;
}
int main() {
    cin >> n >> x ;
    memset(dp, -1, sizeof(dp)) ;
    fact = 1 ;
    for (int i=1; i<=n; ++i) {
        fact *= i ;
    }
    int ans = 0 ;
    for (int i=1; i<=x; ++i) {
        ans = (ans + solve(n-1, i)) % MOD ;
    }
    cout << ans << "\n" ;
    return 0 ;
}