#include <stdio.h>
#include <vector>
using namespace std;

struct matrix
{
	int r;
	int c;
};
int main()
{
	int n;
	scanf("%d", &n);
	vector<matrix> mat(n+1);
	vector< vector<int> > memo(n+1, vector<int>(n+1));
	for(int i=1; i<=n; i++)
		scanf("%d %d", &mat[i].r, &mat[i].c);
	for(int i=2; i<=n; i++)
		memo[i-1][i] = mat[i-1].r * mat[i-1].c * mat[i].c;
	for(int gap=2; gap<n; gap++)
	{
		for(int position=1+gap; position <= n; position++)
		{
			int temp = mat[position-gap].r * mat[position-gap].c * mat[position].c;
			temp += memo[position-gap+1][position];
			memo[position-gap][position] = temp;
			for(int in=1; in<gap; in++)
			{
				temp = mat[position-gap].r * mat[position-gap+in].c * mat[position].c;
				temp += memo[position-gap][position-gap+in];
				temp += memo[position-gap+in+1][position];
				if(memo[position-gap][position] >  temp)
					memo[position-gap][position] =  temp;
			}
		}
	}
	printf("%d\n", memo[1][n]);
	return 0;
}