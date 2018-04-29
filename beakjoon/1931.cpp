/*
3
7 7
7 8
8 8
*/

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const pair<int,int> &v1, const pair<int,int> &v2)
{
	if(v1.second == v2.second)
		return v1.first < v2.first;
	return v1.second < v2.second;
}

int main()
{
	int n;
	scanf("%d", &n);
	vector< pair<int, int> > v(n);
	for(int i=0; i<n; i++)
		scanf("%d %d", &v[i].first, &v[i].second);
	sort(v.begin(), v.end(), cmp);
	unsigned int start_define = 0;
	unsigned int end_min = -1;
	int rst = 0;

	for(int i=0; i<n; i++)
	{
		if(v[i].first >= start_define)
		{
			if(v[i].second < end_min)
			{
				end_min = v[i].second;
				rst++;
				start_define = end_min;
				end_min = -1;
			}
		}
	}
	printf("%d\n",rst);
	return 0;
}