#include <stdio.h>
#include <string.h>
int n;
int *b;
int reverse(int arg)
{
	return arg ? 0 : 1;
}
int go(int arr[])
{
	int rst = 0;
	for(int i=1; i<n; i++)
	{
		if(arr[i-1] != b[i-1])
		{
			rst++;
			for(int j=i-1; j<i+2; j++)
				if(j<n)
					arr[j] = reverse(arr[j]);
		}
	}
	return rst;
}
bool isSame(int arr[])
{
	bool ret = true;
	for(int i=0; i<n; i++)
	{
		if(arr[i]!=b[i])
		{
			ret = false;
			break;
		}
	}
	return ret;
}
int main()
{
	scanf("%d", &n);
	int *a = new int[n];
	b = new int[n];
	for(int i=0; i<n; i++)
		scanf("%1d", &a[i]);
	int *a2 = new int[n];
	memcpy(a2, a, sizeof(int) * n);
	for(int i=0; i<n; i++)
		scanf("%1d", &b[i]);
	int rst = go(a);
	rst = isSame(a) ? rst : -1;

	a2[0] = reverse(a2[0]);
	a2[1] = reverse(a2[1]);
	int rst2 = go(a2);
	rst2 = isSame(a2) ? rst2+1 : -1;

	if(rst == -1 || rst2 == -1)
		rst = rst>rst2 ? rst : rst2;
	if(rst && rst2)
		rst = rst < rst2 ? rst2 : rst;
	printf("%d\n", rst);
	return 0;
}