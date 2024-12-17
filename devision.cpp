#include <iostream>
using namespace std;
double devision();
double devision(double x, double y)//function declaration
{
	return x/y;
}
int main(){
	int a=5, b=7;
	double res;
	res=devision(a,b);//function calling
	cout<<"the division is: "<<res<<endl;
	return 0;
}
