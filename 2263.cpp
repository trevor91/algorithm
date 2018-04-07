#include <stdio.h>
int in[100001];
int post[100001];

void go(int start, int end)
{
	if(start > end) return;
	int root = post[end];
	printf("%d ", root);
	int i;
	for(i=start; i<end; i++)
		if(in[i] == root)
		{
			for(int j=end; j>i; j--)
				post[j] = post[j-1];
			break;
		}
	go(start, i-1);
	go(i+1, end);
}
int main()
{
	int n;
	scanf("%d", &n);
	for(int i=1; i<=n; i++)
		scanf("%d", &in[i]);
	for(int i=1; i<=n; i++)
		scanf("%d", &post[i]);
	go(1, n);
	return 0;
}