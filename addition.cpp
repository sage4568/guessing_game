#include <iostream>
using namespace std;
int addition();
int addition(int x, int y)//function declaration
{
	return x+y;
}
int main(){
	int a=5, b=7, res;
	res=addition(a,b);//function calling
	cout<<"the sum is: "<<res<<endl;
	return 0;
}
