#include <iostream>
using namespace std;

int main(){
	int i = 4;
	int *p = &i;
	*p = 1;
	cout << *p << " " << i << endl;
}
