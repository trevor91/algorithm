#include <stdio.h>
#include <string.h>

int main()
{
	int n;
	scanf("%d", &n);
	int **memo = new int*[n+1];
	for(int i=0; i<=n; i++)
	{
		memo[i] = new int[10];
		memset(memo[i],0,sizeof(int)*10);
	}
	memo[0][0] = 1;
	for(int i=1; i<=n; i++)
	{
		for(int j=0; j<=9; j++)
		{
			if(memo[i-1][j])
			{
				for(int k=j; k<=9; k++)
				{
					memo[i][k] += memo[i-1][j];
					memo[i][k] %= 10007;
				}	
			}
		}
	}
	int sum=0;
	for(int i=0; i<=9; i++)
	{
		sum += memo[n][i];
		sum %= 10007;
	}
	printf("%d\n",sum);
	return 0;
}