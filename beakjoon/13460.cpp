#include <stdio.h>
#include <queue>
using namespace std;
#define R 0
#define L 1
#define U 2
#define D 3

bool visited[10][10][10][10][4] = {false,};
struct data{
	char red_y;
	char red_x;
	char blue_y;
	char blue_x;
	char cnt;
	int direction;
};
data move(char board[][10], data args)
{
	int move_x=0;
	int move_y=0;
	if(args.direction==R) {move_x = 1;}
	else if(args.direction==L) {move_x = -1;}
	else if(args.direction==U) {move_y = 1;}
	else if(args.direction==D) {move_y = -1;}
	bool move_red = true;
	bool move_blue = true;
	while(move_red || move_blue)
	{
		if(move_red)
		{
			move_red = false;
			if(!(args.red_y==0 && args.red_x==0))
			{
				switch(board[args.red_y + move_y][args.red_x + move_x])
				{
					case '.':
						if((args.red_y+move_y == args.blue_y) && (args.red_x+move_x == args.blue_x))
						{
							if(board[args.blue_y + move_y][args.blue_x + move_x]=='.')
							{
								args.red_y += move_y;
								args.red_x += move_x;
								args.blue_y += move_y;
								args.blue_x += move_x;
								move_red = true;
								move_blue = true;
							}
						}
						else
						{
							args.red_y += move_y;
							args.red_x += move_x;
							move_red = true;
						}
						break;
					case 'O':
						args.red_y = 0;
						args.red_x = 0;
				}
			}
		}
		if(move_blue)
		{
			move_blue = false;
			switch(board[args.blue_y + move_y][args.blue_x + move_x])
			{
				case '.':
					if((args.blue_y+move_y == args.red_y) && (args.blue_x+move_x == args.red_x))
					{
						if(board[args.red_y + move_y][args.red_x + move_x]=='.')
						{
							args.red_y += move_y;
							args.red_x += move_x;
							args.blue_y += move_y;
							args.blue_x += move_x;
							move_blue = true;
							move_red=true;
						}
					}
					else
					{
						args.blue_y += move_y;
						args.blue_x += move_x;
						move_blue = true;
					}
					break;
				case 'O':
					args.blue_y = 0;
					args.blue_x = 0;
					return args;
			}
		}
	}
	return args;
}

void q_push(queue<data>& q, data temp, char dir)
{
	temp.direction = dir;
	temp.cnt++;
	if(!visited[temp.red_y][temp.red_x][temp.blue_y][temp.blue_x][dir])
	{
		q.push(temp);
		visited[temp.red_y][temp.red_x][temp.blue_y][temp.blue_x][dir]=true;
	}
}
int main()
{
	int n,m, temp; //temp input '\n'
	scanf("%d %d %d", &n, &m, &temp);
	char board[10][10] = {0,};
	char red_x, red_y, blue_x, blue_y;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			scanf("%c", &board[i][j]);
			if(board[i][j] == 'B')
			{
				blue_y = i;
				blue_x = j;
				board[i][j] = '.';
			}
			else if(board[i][j] == 'R')
			{
				red_y = i;
				red_x = j;
				board[i][j] = '.';
			}
		}
		scanf("%d", &temp); //input '\n'
	}

	queue<data> q;
	for(int i=0; i<4; i++)
	{
		q.push(data{red_y,red_x,blue_y,blue_x, 1, i});
		visited[red_y][red_x][blue_y][blue_x][i] = true;
	}

	while(!q.empty())
	{
		data temp = q.front();
		q.pop();
		if(temp.cnt > 10) break;
		temp = move(board, temp);
		visited[temp.red_y][temp.red_x][temp.blue_y][temp.blue_x][temp.direction] = true;
		if(temp.blue_x==0 && temp.blue_y==0) continue;
		if(temp.red_x==0 && temp.red_y==0)
		{
			printf("%d\n", temp.cnt);
			return 0;
		}
		for(int i=0; i<4; i++) q_push(q,temp,i);
	}
	printf("-1\n");
	return 0;
}