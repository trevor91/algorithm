#include <stdio.h>
#include <vector>
using namespace std;
int n,k;
int main()
{
	scanf("%d %d", &n, &k);
	vector<int> value(n+1);
	vector< vector<int> > memo(n+1, vector<int>(k+1));
	for(int i=1; i<=n; i++)
		scanf("%d",&value[i]);
	
	memo[0][0] = 1;
	for(int i=1; i<=n; i++)
	{
		for(int j=0; j<=k; j++)
		{
			memo[i][j] = memo[i-1][j];
			if(j-value[i] > -1)
				memo[i][j] += memo[i][j-value[i]];
		}
	}
	printf("%d\n", memo[n][k]);
	return 0;
}