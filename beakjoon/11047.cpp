#include <stdio.h>
#include <string.h>
int main()
{
	int n, k;
	scanf("%d %d", &n, &k);
	int coin_val[10];
	for(int i=0; i<n; i++)
		scanf("%d", &coin_val[i]);
	int cnt=0;
	while(k>0)
	{
		cnt += k / coin_val[--n];
		k %= coin_val[n];
	}
	printf("%d\n", cnt);
	return 0;
}