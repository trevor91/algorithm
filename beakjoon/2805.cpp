#include<stdio.h>
int arr[1000000];
int n, m, max = 0;

long long cut(int height)
{
	long long sum = 0;
	for(int i=0; i<n; i++)
		if(arr[i]>height)
			sum += arr[i] - height;
	return sum;
}

void go(long long start, long long end)
{
	long long mid = (start+end)/2;
	long long sum = cut(mid);
	if(end-start < 2)
	{
		if(cut(end) >= m)
			printf("%d\n",end);
		else
			printf("%d\n",start);
		return;
	}
	if(sum < m)
		go(start, mid);
	else if(sum >= m)
	{
		if(m > cut(mid+1))
		{
			printf("%d\n", mid);
			return;
		}
		go(mid+1, end);
	}
}

int main()
{
	scanf("%d %d", &n,&m);
	for(int i = 0; i<n; i++)
	{
		scanf("%d",&arr[i]);
		if(arr[i] > max)
			max = arr[i];
	}
	go(0, max);
	return 0;
}