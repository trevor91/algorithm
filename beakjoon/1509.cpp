#include <stdio.h>
#include <string.h>
using namespace std;

char in[2501];
bool check[2500][2500];
int memo[2500];

int main()
{
	scanf("%s", &in);
	int length = strlen(in);
	for(int i=0; i<length; i++)
		check[i][i]=1;
	for(int i=1; i<length; i++)
		if(in[i-1] == in[i])
			check[i-1][i] = 1;
	for(int i=3; i<=length; i++)
		for(int j=0; j<=length-i; j++)
			if(in[j]==in[j+i-1] && check[j+1][j+i-2])
				check[j][j+i-1]=1;

	for(int i=0; i<length; i++)
	{
		memo[i] = 2500;
		for(int j=i; j>=0; j--)
		{
			if(check[j][i]==1)
			{
				if(memo[i]>memo[j-1]+1)
					memo[i]=memo[j-1]+1;
			}
		}
	}
	printf("%d\n", memo[length-1]);
}