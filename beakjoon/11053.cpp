/*
10	20	10	30	20	50
입력받았을때 
d[i]는 i번째를 마지막 수로 갖는 수열의 길이.

10	20	10	30	20	50
d[1] = 1
d[2] = 2 // d[1]의 값보다 2번째 값이 더 크니. +1
d[3] = 1 // d[1~2]중에서 가장 큰 d[2]의 값보다 3번째 값이 작으니.
그 다음번 큰값인 d[1]과 비교. -> 3번째 값이 그 다음 비교값보다 크거나 같으니 그 다음하고 비교비교... 
d[4] = 3 // d[1~3]중에서 가장 큰 d[2]의 값보다 4번째 값이 크니. +1
d[5] = 2 // d[1~4]중에서 가장 큰 d[4]의 값보다 5번째 값이 작으니.
d[6] = 4
*/
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	if(input==1)
	{
		printf("%d\n",1);
		return 0;
	}
	input += 1;
	vector<int> v(input);
	for(int i = 1; i<input; i++)
		scanf("%d", &v[i]);

	vector<int> cnt(input, 1);
	int max = 0;
	for(int i = 2; i < input; i++)
	{
		for(int j = 1; j < i; j++)
		{
			if(v[j] < v[i] && cnt[j] >= cnt[i])
			{
				cnt[i] = cnt[j] + 1;
			}
			else if(v[j] == v[i] && cnt[j] >= cnt[i])
			{
				cnt[i] = cnt[j];
			}
		}
		if(cnt[i] > max)
			max = cnt[i];
	}
	printf("%d\n", max);
	return 0;
}