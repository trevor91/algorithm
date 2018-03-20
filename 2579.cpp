#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	input += 1;
	vector<int> v(input,0);
	for(int i = 1; i < input; i++)
		scanf("%d",&v[i]);
	if(input < 4)
	{
		int sum=0;
		for(int i=1;i<input;i++)
			sum += v[i];
		printf("%d\n",sum);
	}
	else
	{
		vector< vector<int> > d(input,vector<int>(2));
		d[1][0] = v[1];
		d[1][1] = v[1];
		d[2][0] = v[2];
		d[2][1] = v[1]+v[2];
		for(int i = 3 ; i < input; i++)
		{
			d[i][1] = d[i-1][0] + v[i];
			if(d[i-2][0] > d[i-2][1])
				d[i][0] = d[i-2][0] + v[i];
			else
				d[i][0] = d[i-2][1] + v[i];
		}
		if(d[input-1][0] > d[input-1][1])
			printf("%d\n",d[input-1][0]);
		else
			printf("%d\n",d[input-1][1]);
	}
	return 0;
}