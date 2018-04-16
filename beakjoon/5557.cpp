#include <stdio.h>
#include <vector>
using namespace std;
#define MIN 0
#define MAX 20

int main()
{
	int n;
	scanf("%d", &n);
	vector<int> v(n+1);
	for(int i=1; i<=n; i++)
		scanf("%d",&v[i]);

	vector< vector<long long> > memo(n+1,vector<long long>(MAX+1));
	memo[1][v[1]] = 1;
	for(int i=2; i<n; i++)
	{
		for(int j=0; j<=MAX; j++)
		{
			if(memo[i-1][j] > 0)
			{
				if(j - v[i] >= MIN)
					memo[i][j - v[i]] += memo[i-1][j];
				if(j + v[i] <= MAX)
					memo[i][j + v[i]] += memo[i-1][j];
			}
		}
	}
	printf("%lld\n", memo[n-1][v[n]]);
	return 0;
}