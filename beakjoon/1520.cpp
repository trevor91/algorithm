#include <stdio.h>
#include <string.h>

int map[501][501];
int visited[501][501];
int m,n;
int increament[2][4] = {{0,0,1,-1},{1,-1,0,0}};

bool checkPosition(int y, int x)
{
	return (y > m || x > n || y < 1 || x < 1) ? false : true;
}

int go(int y, int x)
{
	if(y==m && x==n)
		return 1;
	int& ret = visited[y][x];
	if(ret != -1) return ret;
	ret = 0;
	for(int i=0; i<4; i++)
		if(checkPosition(y+increament[0][i], x+increament[1][i]))
			if(map[y][x] > map[y+increament[0][i]][x+increament[1][i]])
				ret += go(y+increament[0][i], x+increament[1][i]);
	return ret;
}

int main()
{
	scanf("%d %d", &m, &n);
	for(int i=1; i<=m; i++)
		for(int j=1; j<=n; j++)
			scanf("%d", &map[i][j]);
	memset(visited, -1, sizeof(visited));
	printf("%d\n", go(1,1));
	return 0;
}