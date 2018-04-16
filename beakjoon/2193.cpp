/*
d[1] = 	1
d[2] = 	10
d[3] = 	101, 			100
d[4] = 	1010, 			1001, 	1000
d[5] = 	10101, 10100,	10010,	10001,10000
-> 마지막수가 0이면 0,1 이 오고,,, 1이면 0만.
*/

#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);

	vector< vector<long long> > v;
	v.resize(input+1, vector<long long>(2,0));

	v[1][0] = 0;
	v[1][1] = 1;
	for(int i = 2;i<input+1;i++) // #row
	{
		v[i][1] += v[i-1][0];
		v[i][0] += v[i-1][0];
		v[i][0] += v[i-1][1];
	}

	printf("%lld\n", v[input][0]+v[input][1]);
	return 0;
}