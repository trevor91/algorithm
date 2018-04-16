#include <stdio.h>
#include <iostream>
using namespace std;
int n,m;
int arr[2001];
bool memo[2001][2001];

int main()
{
	scanf("%d", &n);
	for(int i=1; i<=n; i++)
		scanf("%d", &arr[i]);

	memo[1][1] = 1;
	for(int i=2; i<=n; i++)
	{
		memo[i][i] = 1;
		if(arr[i-1] == arr[i])
			memo[i-1][i] = 1;
	}
	for(int i=3; i<=n; i++)
		for(int j=1; j<=n-i+1; j++)
			if((arr[j]==arr[j+i-1]) && memo[j+1][j+i-2])
				memo[j][j+i-1] = 1;

	scanf("%d", &m);
	int s,e;
	for(int i=0; i<m; i++)
	{
		scanf("%d %d", &s, &e);
		printf("%d\n", memo[s][e]);
	}
}