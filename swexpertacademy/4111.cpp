//https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWJHjcFqdyoDFAUH&categoryId=AWJHjcFqdyoDFAUH&categoryType=CODE

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int testCnt;
	scanf("%d", &testCnt);
	for(int testCase = 1; testCase <= testCnt; testCase++)
	{
		int camera, device;
		scanf("%d %d", &camera, &device);
		vector<int> v(camera);
		int in;
		for(int i=0; i<camera; i++)
		{
			scanf("%d", &in);
			v[i] = in;
		}
		sort(v.begin(), v.end());
		for(int i=1; i<camera; i++)
			v[i-1] = v[i]-v[i-1];
		sort(v.begin(), v.end());
		int sum = 0;
		for(int i=0; i<camera-device; i++)
			sum += v[i];
		printf("#%d %d\n", testCase, sum);
	}
	return 0;
}