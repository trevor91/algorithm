#include <stdio.h>

int score[1001][1001];
int arr[1001][1001];
int n,m;

int max(int a, int b)
{
	if(a>b)
		return a;
	return b;
}
int main()
{
	scanf("%d %d", &n,&m);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%d",&arr[i][j]);
	score[1][1] = arr[1][1];

	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=m;j++)
		{
			if(i+1<=n)
				score[i+1][j] = max(score[i+1][j], score[i][j]+arr[i+1][j]);
			if(j+1<=m)
				score[i][j+1] = max(score[i][j+1], score[i][j]+arr[i][j+1]);
		}
	}
	printf("%d\n",score[n][m]);
	return 0;
}