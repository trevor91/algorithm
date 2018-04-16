#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	input += 1;
	vector<int> v(input);
	for(int i = 1; i<input; i++)
		scanf("%d", &v[i]);

	vector<int> upCnt(input, 1);
	vector<int> downCnt(input, 1);
	for(int i = 2; i < input; i++)
	{
		for(int j = 1; j < i; j++)
		{
			if(v[j] < v[i] && upCnt[j] >= upCnt[i])
				upCnt[i] = upCnt[j] + 1;
			else if(v[j] == v[i] && upCnt[j] > upCnt[i])
				upCnt[i] = upCnt[j];
		}
	}

	for(int i = input-2; i > 0; i--)
	{
		for(int j = input-1; j > i; j--)
		{
			if(v[j] < v[i] && downCnt[j] >= downCnt[i])
				downCnt[i] = downCnt[j] + 1;
			else if(v[j] == v[i] && downCnt[j] > downCnt[i])
				downCnt[i] = downCnt[j];
		}
	}

	int rst = 0;
	for(int i = 1; i< input; i++)
	{
		if(rst < upCnt[i] + downCnt[i] -1)
			rst = upCnt[i] + downCnt[i] -1;
	}
	printf("%d\n", rst);
	return 0;
}