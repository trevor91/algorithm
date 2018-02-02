#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	input += 1;
	vector<int> v(input);
	for(int i = 1; i < input; i++)
		scanf("%d",&v[i]);

	vector<int> cnt(input,1);
	int rst = 1;
	for(int i = 2; i < input; i++)
	{
		for(int j = 1; j < i; j++)
		{
			if(v[i] < v[j] && cnt[i] <= cnt[j])
			{
				cnt[i] = cnt[j] + 1;
			}
			else if ( v[i] == v[j] && cnt[i] < cnt[j])
			{
				cnt[i] = cnt[j];
			}
		}
		if(rst < cnt[i])
			rst = cnt[i];
	}
	printf("%d\n",rst);
	return 0;

}