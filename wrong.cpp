#pragma GCC optimize("O3,unroll-loops")
#include<bits/stdc++.h>
using namespace std;

#define int long long
#define no  cout << "No" << endl;
#define yes cout << "Yes" << endl;
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) ((a)*(b)/gcd(a, b))
#define lp(a,n)  for(int i =a; i< n; i++)
#define print(x) for(auto i: x) { cout << i << " "; }; cout << "\n";

#define MOD 1000000007;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> a(n), b(m);

    lp(0, n){
        cin >> a[i];
    }
    lp(0, m){
        cin >> b[i];
    }

    // can have two values a[i] and b[0] - a[i] ;
    // must always be a[i-1] <= a[i]

    a[0] = min(a[0], b[0] - a[0]);

    lp(1, n){
        int first = a[i];
        int second = b[0] - a[i];

        if(a[i-1] <= first){
            if(a[i-1] <= second){
                a[i] = min(first, second);
            }
        }else if(a[i-1] <= second){
            a[i] = second;
        }else{
            no;
            return;
        }
    }

    yes;
}

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int x = 1;
    cin >> x;
    while(x--){
        solve();
    }
}