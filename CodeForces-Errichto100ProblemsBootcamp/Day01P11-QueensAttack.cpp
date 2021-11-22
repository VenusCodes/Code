#include <bits/stdc++.h>
using namespace std;

const int MAX = 1e5 +5;
bool row_taken[MAX], col_taken[MAX], diag_taken[MAX*2],diag2[MAX*2];

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int n,q;
	cin>>n>>q;
	for(int i = 0;i<q;++i){
		int r,c;
		cin>>r>>c;
		if(!row_taken[r] && !col_taken[c] && !diag_taken[c-r+n] && !diag2[c+r]) {
			cout<<"YES\n";
			row_taken[r] = true;
			col_taken[c] = true;
			diag2[c+r] = true;
			diag_taken[c-r+n] = true;
		}
		else{
			cout<<"NO\n";
		}
	}
}