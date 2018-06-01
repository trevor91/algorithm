#include <stdio.h>
#define RIGHT	0
#define LEFT	1
#define UP		2
#define DOWN	3
#define MAX		20
int n;
int arr[MAX][MAX]={0,};
int max=0;

void prt(int mat[MAX][MAX])
{
	for(int i=0; i<n;i++)
	{
		for(int j=0; j<n; j++)
			printf("%d", mat[i][j]);
		printf("\n");
	}
	printf("----------\n");
}

void setMax(int mat[MAX][MAX])
{
	for(int y=0; y<n; y++)
		for(int x=0; x<n; x++)
			if(max < mat[y][x])
				max = mat[y][x];
}

bool rangeCheck(int a, int b)
{
	return (a>=0 && b>=0 && a<n && b<n)? true:false;
}

int move_x=0, move_y=0, y=0, x=0, increase_y=1, increase_x=1;
void valSetting(int dir)
{
	move_x=0, move_y=0, y=0, x=0, increase_y=1, increase_x=1;
	if(dir==RIGHT)		{move_x=-1; x=n-1; increase_x=-1;}
	else if(dir==LEFT)	{move_x=1;}
	else if(dir==UP)	{move_y=1;}
	else if(dir==DOWN)	{move_y=-1; y=n-1; increase_y=-1;}
}
void go(int arr[MAX][MAX], int cnt, int dir)
{
	int mat[MAX][MAX];
	for(int y=0; y<n; y++)
		for(int x=0; x<n; x++)
			mat[y][x] = arr[y][x];
	if(cnt == 0) {setMax(mat);return;}
	valSetting(dir);

	//calculation
	for(; (y<n && y>=0); y+=increase_y)
	{
		for(; (x<n && x>=0); x+=increase_x)
		{
			if(mat[y][x]!=0)
			{
				int temp_y = y+move_y;
				int temp_x = x+move_x;
				while(rangeCheck(temp_y,temp_x))
				{
					if(mat[temp_y][temp_x]==mat[y][x])
					{
						mat[y][x] += mat[y][x];
						mat[temp_y][temp_x] = 0;
						break;
					}
					else if(mat[temp_y][temp_x]==0)
					{
						temp_y+=move_y; temp_x+=move_x;
					}
					else
					{
						break;
					}
				}
			}
		}
		if(dir==RIGHT) x = n-1;
		else if(dir==LEFT || dir==UP|| dir==DOWN) x = 0;
	}

	//push
	valSetting(dir);
	move_y *= -1;
	move_x *= -1;

	for(; (y<n && y>=0); y+=increase_y)
	{
		for(; (x<n && x>=0); x+=increase_x)
		{
			if(mat[y][x] != 0)
			{
				int temp_y = y+move_y;
				int temp_x = x+move_x;
				bool ismove=false;
				while(rangeCheck(temp_y,temp_x))
				{
					if(mat[temp_y][temp_x]==0)
					{
						temp_y+=move_y; temp_x+=move_x;
						ismove=true;
					}
					else
						break;
				}
				temp_y-=move_y; temp_x-=move_x;
				if(ismove)
				{
					mat[temp_y][temp_x] = mat[y][x];
					mat[y][x] = 0;
				}
			}
		}
		if(dir==RIGHT) x = n-1;
		else if(dir==LEFT || dir==UP || dir==DOWN) x = 0;
	}
	// printf("cnt: %d dir:%d\n", cnt, dir);
	// prt(mat);

	bool isChange = false;
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(arr[i][j] != mat[i][j])
				{isChange = true;break;}

	for(int i=0; i<4; i++)
	{
		if(dir==i && !isChange)
			continue;
		go(mat,cnt-1,i);
	}
}

int main()
{
	scanf("%d", &n);
	for(int i=0; i<n;i++)
		for(int j=0; j<n; j++)
			scanf("%d", &arr[i][j]);

	for(int i=0; i<4; i++)
		go(arr, 5, i);
	printf("%d\n",max);
	return 0;
}