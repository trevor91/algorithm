#include <stdio.h>
#include <vector>
using namespace std;

int testCase;
int size;

int main()
{
	scanf("%d", &testCase);
	for(int i=0; i<testCase ; i++)
	{
		scanf("%d", &size);
		vector<int> v(size);
		for(int j=0; j<size; j++)
		{
			int temp;
			scanf("%d", &temp);
			v.push_back(temp);
		}
		while(1)
		{
			if(v.size()==1)
			{
				printf("%d\n", v[0]);
				break;
			}
			int sum=0;
			int idx=1;
			for(int j=idx; j<size; j++)
			{
				if(sum < v[i] + v[i-1])
				{
					sum = v[i] + v[i-1];
					idx = i;
				}
			}
			v[idx-1] = sum;
			v.erase(v.begin() + idx);
		}

	}
	return 0;
}