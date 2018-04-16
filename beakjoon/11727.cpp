#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	vector<int> v1(input+1,0);
	vector<int> v2(input+1,0);
	/*
	v1[i] = v1[i-1] + v1[i-2]
	v2[i] = (v1[i-2] + v2[i-2] * 2 + v2[i-1])
	*/

	//set v1
	v1[1] = 1;
	v1[2] = 2;
	for(int i = 3;i <input+1;i++)
		v1[i] = (v1[i-1]+v1[i-2]) % 10007;

	//set v2
	v2[1] = 0;
	v2[2] = 1;
	for(int i = 3; i<input+1; i++)
		v2[i] = (v1[i-2] + v2[i-2] * 2 + v2[i-1]) % 10007;

	printf("%d\n",(v1[input]+v2[input])%10007);
}