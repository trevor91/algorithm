//https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&&&&&&

#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int rst[] = {0,0,0,0,0,0};
bool visited[] = {0,0,0,0,0,0};
void go(int arr[], int start_index, int size, int cnt)
{
	int idx = size-start_index-1;
	int max = arr[idx];

	/*trick?*/
	if(idx == 0)
	{
		for(int i=size-1; i>0; i--)
		{
			if(arr[i] == arr[i-1])
				break;
			if(i==1)
			{
				//cnt odd, even check
				if(cnt % 2)
				{
					int temp = arr[0];
					arr[0] = arr[1];
					arr[1] = temp;
				}
			}
		}
		copy(arr, arr+size, rst);
		return;
	}

	/*Change chance is done*/
	if(cnt == 0)
	{
		// visited check
		int left = 0;
		for(int j = 0; j<size; j++)
		{
			if(visited[j])
				left=j;
			else
				break;
		}
		if(left > 0)
			sort(arr, arr+left+1);

		/*if (rst < arr) -> rst = arr*/
		for(int i=size-1; i>=0; i--)
		{
			if(rst[i] == arr[i])
				continue;
			else if(rst[i] < arr[i])
				copy(arr, arr+size, rst);
			break;
		}
		return;
	}

	/*Find MAX in arr*/
	for(int i=idx-1; i>=0; i--)
	{
		if(arr[i] >= max)
		{
			max = arr[i];
			idx = i;
		}
	}

	/*First number == MAX*/
	if(idx == (size-start_index-1) && start_index < size)
		go(arr, start_index+1, size, cnt);
	
	/*First number != MAX : swap*/
	else
	{
		int temp = arr[idx];
		arr[idx] = arr[size-start_index-1];
		arr[size-start_index-1] = temp;
		visited[idx] = 1;
		visited[size-start_index-1] = 1;
		go(arr, start_index+1, size, cnt-1);
	}
}

int main()
{
	int testCnt;
	scanf("%d", &testCnt);
	for(int testCase = 1; testCase <= testCnt; testCase++)
	{
		int card, change;
		int cards[6];
		scanf("%d %d\n", &card, &change);
		int n=0; // 카드 갯수 1~6
		for(double i=5.0; i>=0; i--)
		{
			int val = card / (int)pow(10.0, i);
			if(val)
			{
				cards[int(i)] = val;
				if(n==0 && i!=0.) n = (int)i+1;
				card %= (int)pow(10.0, i);
			}
			else if(i==0.)
			{
				if(n==0)
					n = 1;
				cards[0] = 0;
			}
		}
		copy(cards, cards+n, rst);

		go(cards, 0, n, change);

		/*Result printing*/
		printf("#%d ",testCase);
		for(int i=n-1; i>=0; i--)
		{
			printf("%d",rst[i]);
			rst[i] = 0;
			visited[i] = 0;
		}
		printf("\n");
	}
	return 0;
}