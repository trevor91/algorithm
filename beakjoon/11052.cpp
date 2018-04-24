#include <stdio.h>
#include <string.h>
int main()
{
	int n;
	scanf("%d", &n);
	int *arr = new int[n+1];
	int *memo = new int[n+1];
	for(int i=1; i<=n; i++)
	{
		scanf("%d", &arr[i]);
		memo[i] = arr[i];
	}
	
	// memcpy(memo, arr, sizeof(arr) * n+1);
	
	for(int i=2; i<=n; i++)
	{
		for(int j=1; j<=(i/2); j++)
		{
			if(memo[i] < memo[j] + memo[i-j])
				memo[i] = memo[j] + memo[i-j];
		}
	}
	printf("%d\n", memo[n]);
	return 0;
}