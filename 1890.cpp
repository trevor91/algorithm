#include <stdio.h>
using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	char v[100][100];
	unsigned long long memo[100][100];

	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			scanf("%d",&v[i][j]);

	memo[0][0] = 1;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			int jump = v[i][j];
			if(jump==0)
				continue;
			if(jump+i < n)
				memo[jump+i][j] += memo[i][j];
			if(jump+j < n)
				memo[i][j+jump] += memo[i][j];
		}
	}
	printf("%lld\n", memo[n-1][n-1]);
	return 0;
}