//https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIseXoKEUcDFAWN&categoryId=AWIseXoKEUcDFAWN&categoryType=CODE

#include <stdio.h>
#include <algorithm>
int main()
{
	int testCnt;
	scanf("%d", &testCnt);
	for(int testCase=1; testCase<=testCnt; testCase++)
	{
		int n;
		scanf("%d", &n);
		int *arr = new int[n];
		int sum = 0;
		for(int i=0; i<n; i++)
		{
			scanf("%d", &arr[i]);
			sum += arr[i];
		}

		/*sort*/
		std::sort(arr, arr+n);
		for(int i=n-3; i>=0; i=i-3)
			sum -= arr[i];
		printf("#%d %d\n", testCase, sum);
	}
	return 0;
}