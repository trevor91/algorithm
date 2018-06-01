#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	int* a = new int[n];
	for(int i=0; i<n; i++) scanf("%d",&a[i]);
	int b,c;
	scanf("%d %d", &b, &c);

	long long cnt=0;
	for(int i=0; i<n; i++)
	{
		a[i] -= b;
		cnt++;
		cnt += a[i] / c;
		if(a[i] % c > 0)
			cnt++;
	}
	printf("%lld\n", cnt);
	return 0;
}