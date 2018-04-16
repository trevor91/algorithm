#include <stdio.h>
#include <string.h>
int main()
{
	int n, k;
	scanf("%d %d",&n,&k);
	int *value = new int[n+1];
	int *memo = new int[k+1];
	for(int i=1; i<=n; i++)
		scanf("%d", &value[i]);
	memset(memo,0,sizeof(int)*(k+1));
	memo[0] = 1;
	for(int i=1; i<=n; i++)
	{
		for(int j=0; j<=k; j++)
		{
			if(j-value[i] > -1)
				memo[j] += memo[j-value[i]];
		}
	}
	printf("%d\n", memo[k]);
	return 0;
}