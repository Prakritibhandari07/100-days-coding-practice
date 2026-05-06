#include<iostream>
#include<cmath>
using namespace std;
void ddaoperation(int x0,int y0,int x1,int y1)
{
	int dx=x1-x0;
	int dy=y1-y0;
	int steps=abs(dx)>abs(dy)? abs(dx):abs(dy);
	float xincrement=dx/float(steps);
	float yincrement=dy/float(steps);
	float x=x0;
	float y=y0;
	cout<<"Points are:\n";
	for(int i=0;i<=steps;i++)
	{
		cout<<"("<<round(x)<<","<<round(y)<<")"<<"\n";
		x=x+xincrement;
		y=y+yincrement;
		
	}
}
int main()
{
	int x0,y0,x1,y1;
	cout<<"Enter the first coordinate:\n";
	cin>>x0>>y0;
	cout<<"Enter the second coordinate:\n";
	cin>>x1>>y1;
	ddaoperation(x0,y0,x1,y1);
	return 0;
}
