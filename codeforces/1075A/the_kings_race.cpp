#include <bits/stdc++.h>

using namespace std;

int main(void) {
	long long n;
	cin >> n;
	
	long long int x, y;
	cin >> x >> y;
	
	long long black = max(n-x, n-y);
	long long white = max(x-1, y-1);
	
	if(white == 0) {
		cout << "White";
	}
	else if(black == 0) {
		cout << "Black";
	}
	else if(white <= black) {
		cout << "White";
	}
	else {
		cout << "Black";
	}
	
	return 0;
}
