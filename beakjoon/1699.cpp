#include <stdio.h>
#include <string.h>
#include <math.h>

int min(int a, int b)
{
	return a>b? b:a;
}
int main()
{
	int n;
	scanf("%d", &n);
	int *memo = new int[n+1];
	memset(memo, -1, sizeof(int)*(n+1));
	
	memo[0] = 0;
	for(int i=1; i<=n; i++)
	{
		memo[i] = memo[i-1] + 1;
		for(int j=2; j<=sqrt(n); j++)
		{
			if(i-j*j < 0 || i-j*j>n)
				break;
			memo[i] = min(memo[i-j*j]+1, memo[i]);
		}
	}
	printf("%d\n", memo[n]);
	return 0;
}