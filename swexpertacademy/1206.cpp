#include <stdio.h>

int a[1000];
int max2(int a, int b)
{
	return a>b? a:b;
}
int max3(int a, int b, int c)
{
	int val;
	val = max2(a,b);
	return max2(val,c);
}
int max4(int a, int b, int c, int d)
{
	int val;
	val = max2(a,b);
	val = max2(val,c);
	return max2(val,d);
}
int calc(int building, int surround)
{
	return building > surround ? building - surround : 0;
}

int main()
{
	for(int testCase = 1; testCase < 11; testCase++)
	{
		int n;
	int rst = 0;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
		scanf("%d", &a[i]);

	for(int i=2; i<n-2; i++)
	{
		rst += calc(a[i], max4(a[i-2], a[i-1], a[i+1], a[i+2]));
	}
	if(n>4)
	{
		rst += calc(a[0], max2(a[1], a[2]));
		rst += calc(a[1], max3(a[0], a[2], a[3]));
		rst += calc(a[n-2], max3(a[n-1], a[n-3], a[n-4]));
		rst += calc(a[n-1], max2(a[n-2], a[n-3]));
	}
	else if(n==3)
	{
		int temp = max3(a[0], a[1], a[2]);
		if(max2(a[0], a[1]) == max2(a[1], a[2]))
			rst += temp - max2(a[0], a[2]);
		else if(max2(a[0], a[1]) == max2(a[0], a[2]))
			rst += temp - max2(a[1], a[2]);
		else if(max2(a[0], a[2]) == max2(a[1], a[2]))
			rst += temp - max2(a[0], a[1]);
	}
	else if(n==2)
		rst += a[0] > a[1] ? a[0]-a[1] : a[1]-a[0];
	else if(n==1)
		rst += a[0];
	else if(n==0)
		rst += 0;
	printf("#%d %d\n", testCase, rst);
	}
	return 0;
}