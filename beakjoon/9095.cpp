#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int inputCnt;
	scanf("%d",&inputCnt);

	vector<int> v(11,0);
	v[1] = 1;
	v[2] = 2;
	v[3] = 4;
	for(int i =4; i<11; i++)
		v[i] = v[i-1] + v[i-2] + v[i-3];
	for(int i = 0; i < inputCnt; i++)
	{
		int temp;
		scanf("%d",&temp);
		printf("%d\n", v[temp]);
	}
	return 0;
}