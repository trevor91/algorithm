#include <stdio.h>
#include <vector>
using namespace std;

int n,m,res=0;
void propagation(vector< vector<bool> > &visited, vector< vector<int> >& map, int y, int x)
{
    visited[y][x] = true;
    int move_y[] = {0,0,1,-1};
    int move_x[] = {1,-1,0,0};
    for(int z=0; z<4; z++)
    {
        int temp_y = y+move_y[z];
        int temp_x = x+move_x[z];
        if(temp_y<0 || temp_x <0 || temp_y >= n || temp_x >= m)
            continue;
        if(map[temp_y][temp_x] == 0 && visited[temp_y][temp_x] == false)
        {
            map[temp_y][temp_x] = 2;
            visited[temp_y][temp_x] = true;
            propagation(visited,map,temp_y,temp_x);
        }
    }
}

int find_zero(vector< vector<int> > map)
{
    vector< vector<bool> > visited(n, vector<bool>(m,false));
    int cnt_zero = 0;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(map[i][j] == 2 && visited[i][j] == false)
                propagation(visited,map,i,j);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(map[i][j] == 0)
                cnt_zero++;
    return cnt_zero;
}

int go(vector< vector<int> > &map, int wall, int y, int x)
{
    if(wall == 0)
    {
        int temp = find_zero(map);
        if(res < temp)
            res = temp;
        return 0;
    }
    
    for(int i=y; i<n; i++)
    {
        int j=0;
        if(i==y) j=x;
        for(; j<m; j++)
        {
            if(map[i][j] == 0)
            {
                map[i][j] = 1;
                go(map, wall-1, i,j);
                map[i][j] = 0;
            }
        }
    }
}

int main()
{
    scanf("%d %d", &n, &m);
    vector< vector<int> > map(n, vector<int>(m));
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &map[i][j]);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(map[i][j]==0)
                go(map, 3, i, j);
    printf("%d\n", res);
    return 0;
}