#include <stdio.h>
#include <vector>
#include <list>
using namespace std;

struct c
{
    int y;
    int x;
};
int main()
{
    int n,k;
    scanf("%d", &n);
    scanf("%d", &k);
    vector< vector<int> > mat(n, vector<int>(n,0));
    for(int i=0; i<k; i++)
    {
        int x,y;
        scanf("%d %d", &y, &x);
        mat[y-1][x-1] = 1; //apple
    }
    int l;
    scanf("%d", &l);

    list<c> bem_position;
    bem_position.push_front(c{0,0});
    mat[0][0] = -1; //bem

    int move_y=0, move_x=1; //go to the right
    int len=1;
    int sec=1;

    for(int i=0; i<l+1; i++)
    {
        int x; char d;
        scanf("%d %c", &x, &d);
        int turn = x-sec+1;
        if(turn<1) turn=1234567;

        for(int j=0; j<turn; j++)
        {
            /*next position*/
            int next_y = bem_position.front().y + move_y;
            int next_x = bem_position.front().x + move_x;
            /*check the range*/
            if(next_y < 0 || next_x < 0 || next_y >= n || next_x >= n ||
                        mat[next_y][next_x] == -1) //crash my body
            {
                printf("%d\n", sec);
                return 0;
            }
            /*apple*/
            if(mat[next_y][next_x] == 1)
            {
                bem_position.push_front(c{next_y,next_x});
                mat[next_y][next_x] = -1;
            }
            /*road*/
            else if(mat[next_y][next_x]== 0 )
            {                
                mat[bem_position.back().y][bem_position.back().x] = 0;
                bem_position.push_front(c{next_y,next_x});
                bem_position.pop_back();
                mat[next_y][next_x] = -1;
            }
            sec++;
        }
        if(d == 'D')
        {
            if(move_x!=0) {move_y=move_x; move_x=0;}
            else if(move_y!=0) {move_x=-move_y; move_y=0;}
        }
        else if(d == 'L')
        {
            if(move_x!=0) {move_y=-move_x; move_x=0;}
            else if(move_y!=0) {move_x=move_y; move_y=0;}
        }
    }
    printf("%d\n",sec);
    return 0;
}
