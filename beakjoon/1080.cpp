#include <stdio.h>
int a[50][50];
int b[50][50];

void reverse(int x, int y)
{
	a[x][y] = a[x][y] ? 0 : 1;
}
int main()
{
	int n,m;
	scanf("%d %d", &n, &m);
	int rst = 0;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			scanf("%1d",&a[i][j]);

	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			scanf("%1d",&b[i][j]);
	for(int i=0;i<n-2;i++)
	{
		for(int j=0;j<m-2;j++)
		{
			if(a[i][j] != b[i][j])
			{
				rst++;
				for(int x=i; x<i+3; x++)
				{
					for(int y=j; y<j+3; y++)
					{
						reverse(x,y);
					}
				}
			}
		}
	}	
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(a[i][j] != b[i][j])
				rst = -1;
	printf("%d\n", rst);
	return 0;
}