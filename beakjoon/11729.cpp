#include <stdio.h>
void go(int n, int start, int end)
{
	if(n==0) return;
	go(n-1, start, 6-start-end);
	printf("%d %d\n", start, end);
	go(n-1, 6-start-end, end);
}
int main()
{
	int n;
	scanf("%d", &n);
	int rst = 2;
	for(int i=1; i<n; i++)
		rst *= 2;
	printf("%d\n", rst-1);
	go(n,1,3);
	return 0;
}