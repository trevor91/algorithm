#include <stdio.h>

int n=0;
int cnt[] = {0,0,0}; //-1,0,1 count
int v[2190][2190];
void check(int start_row, int end_row, int start_col, int end_col)
{
	for(int i=start_row;i<end_row;i++)
	{
		for(int j=start_col;j<end_col;j++)
		{
			if(v[i][j] != v[start_row][start_col])
			{
				int gap = (end_row - start_row)/3;
				check(start_row, start_row+gap, start_col, start_col+gap);
				check(start_row, start_row+gap, start_col+gap, start_col+gap*2);
				check(start_row, start_row+gap, start_col+gap*2, start_col+gap*3);

				check(start_row+gap, start_row+gap*2, start_col, start_col+gap);
				check(start_row+gap, start_row+gap*2, start_col+gap, start_col+gap*2);
				check(start_row+gap, start_row+gap*2, start_col+gap*2, start_col+gap*3);

				check(start_row+gap*2, start_row+gap*3, start_col, start_col+gap);
				check(start_row+gap*2, start_row+gap*3, start_col+gap, start_col+gap*2);
				check(start_row+gap*2, start_row+gap*3, start_col+gap*2, start_col+gap*3);
				return;
			}
		}
	}
	cnt[v[start_row][start_col]+1]++;
}

int main()
{
	scanf("%d",&n); 
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			scanf("%d",&v[i][j]);
	check(0,n,0,n);
	printf("%d\n%d\n%d\n",cnt[0],cnt[1],cnt[2]);
	return 0;
}