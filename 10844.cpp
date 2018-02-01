#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d", &input);
	vector< vector<long long> > v;
	v.resize(input+1, vector<long long>(10,1));
	v[1][0] = 0;
	for(int i = 2 ; i < input+1 ; i++) // i: 자릿수
	{
		for(int j = 0 ; j < 10 ; j++) // j: 마지막 수
		{
			v[i][j] = 0;
			if(j != 0) //[i-1]0~8 -> [i]1~9 
				v[i][j] += v[i-1][j-1];
			if(j != 9) //[i-1]1~9 -> [i]0~8
				v[i][j] += v[i-1][j+1];
			// printf("%d\t",v[i][j]);
			v[i][j] %= 1000000000;
		}
		// printf("\n");
	}

	long long rst = 0;
	for(int i = 0 ; i < 10 ; i++)
		rst += v[input][i];
	rst %= 1000000000;
	printf("%d\n", rst);
	return 0;
}