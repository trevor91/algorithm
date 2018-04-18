//https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE

#include <stdio.h>
#include <set>
using namespace std;

int arr[4][4];
int move_x[4] = {0,0,1,-1};
int move_y[4] = {1,-1,0,0};

int main()
{
	int testCnt;
	scanf("%d", &testCnt);
	for(int testCase = 1; testCase<=testCnt; testCase++)
	{
		set<int> memo[4][4][7];
		set<int> rst;/*set murge*/

		/*input*/
		for(int row = 0; row<4; row++)
		{
			for(int col = 0; col<4; col++)
			{
				scanf("%d", &arr[row][col]);
				memo[row][col][6].insert(arr[row][col]);
			}
		}

		
		/*dynamic*/
		for(int cnt=5; cnt>=0; cnt--)
		{
			for(int y=0; y<4; y++)
			{
				for(int x=0; x<4; x++)
				{
					/*adjacent list*/
					for(int i=0; i<4; i++)
					{
						/*check array area*/
						if(y+move_y[i] >= 0 && y+move_y[i] < 4 && x+move_x[i] >= 0 && x+move_x[i] < 4 )
						{
							set<int>& cur_set = memo[y+move_y[i]][x+move_x[i]][cnt+1];
							/*traveling set*/
							for(set<int>::iterator j = cur_set.begin(); j!=cur_set.end(); j++)
							{
								int val = *j;
								int insert_val = arr[y][x] + val * 10;
								memo[y][x][cnt].insert(insert_val);
								if(cnt == 0)
									rst.insert(insert_val);
							}
						}
					}
				}
			}
		}
		/*testCase i result is*/
		printf("#%d %d\n",testCase, rst.size());
	}
	return 0;
}