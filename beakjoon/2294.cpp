#include <stdio.h>
#include <vector>
using namespace std;
#define INF 1000000000
int main()
{
	int n,k;
	scanf("%d %d", &n, &k);
	vector<int> value(n+1);
	vector<int> memo(k+1, INF);
	for(int i=1; i<=n; i++)
		scanf("%d", &value[i]);
	memo[0] = 1;
	for(int i=1; i<=n; i++)
		if(value[i] < k+1)
			memo[value[i]] = 1;
	for(int i=1; i<=n; i++)
		for(int j=0; j<=k; j++)
			if(j-value[i] > 0 && (memo[j] > memo[j-value[i]]+1))
				memo[j] = memo[j-value[i]]+1;
	if(memo[k] == INF)
		printf("%d\n", -1);
	else
		printf("%d\n", memo[k]);
	return 0;
}