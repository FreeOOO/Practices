#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main(){
	int value,sum = 0;
	while(cin >> value){
		sum += value;
	}
	cout << sum << endl;
}
