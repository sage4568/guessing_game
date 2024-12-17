#include <iostream>
using namespace std;
int subtraction();
int subtraction(int x, int y)//function declaration
{
	return x-y;
}
int main(){
	int a=5, b=7, res;
	res=subtraction(a,b);//function calling
	cout<<"the diff is: "<<res<<endl;
	return 0;
}
