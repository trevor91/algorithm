#include <stdio.h>
int num[20000001];
int main()
{
	int n;
	scanf("%d",&n);
	int temp;
	for(int i=0; i<n; i++)
	{
		scanf("%d", &temp);
		num[temp+10000000]++;	
	}
	scanf("%d", &n);
	for(int i=0; i<n; i++)
	{
		scanf("%d", &temp);
		printf("%d ", num[temp+10000000]);
	}
	return 0;
}