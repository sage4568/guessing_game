#include <iostream>
using namespace std;
int multiplication();
int multiplication(int x, int y)//function declaration
{
	return x*y;
}
int main(){
	int a=5, b=7, res;
	res=multiplication(a,b);//function calling
	cout<<"the product is: "<<res<<endl;
	return 0;
}
