#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int n,s,m;
	scanf("%d %d %d", &n,&s,&m);
	vector<int> v(n+1);
	for(int i=1; i<=n; i++)
		scanf("%d", &v[i]);
	vector< vector<bool> > memo(n+1,vector<bool>(1001,false));
	memo[0][s] = true;
	int max = s;
	for(int song_num=1; song_num <= n; song_num++)
	{
		for (int volum=0; volum <= m; volum++)
		{
			if(memo[song_num-1][volum] == true)
			{
				if(volum-v[song_num] > -1)
					memo[song_num][volum-v[song_num]] = true;
				if(volum+v[song_num] <= m)
					memo[song_num][volum+v[song_num]] = true;
			}
		}
	}
	int rst = -1;
	for(int i=m; i>-1; i--)
	{
		if(memo[n][i] == true)
		{
			rst = i;
			break;
		}
	}
	printf("%d\n",rst);
	return 0;
}