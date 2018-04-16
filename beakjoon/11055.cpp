#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d", &input);
	input += 1;
	vector<int> v(input);
	for(int i = 1; i<input; i++)
		scanf("%d", &v[i]);

	vector<int> sum(input, 0);
	sum[1] = v[1];
	int max = sum[1];
	for(int i = 2; i < input; i++)
	{
		for(int j = 1; j < i; j++)
		{
			if(v[i] > v[j] && sum[i] < sum[j])
			{
				sum[i] = sum[j];
			}
			else if (v[i] == v[j])
			{
				sum[i] = sum[j] - v[i];
			}
		}
		sum[i] += v[i];
		if(sum[i] > max)
			max = sum[i];
	}
	printf("%d\n", max);
	return 0;
}