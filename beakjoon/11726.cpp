#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);

	vector<int> v(input+1, 0);
	v[1] = 1;
	v[2] = 2;

	for(int i = 3 ; i < input+1 ; i++)
		v[i] = (v[i-1] + v[i-2]) % 10007;
	printf("%d\n",v[input]);
	return 0;
}