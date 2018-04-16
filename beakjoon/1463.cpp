#include <stdio.h>
#include <vector>
using namespace std;


int main()
{
	int in;
	scanf("%d", &in);
	vector<int> v(in+1,0);
	v[2] = 1;
	v[3] = 1;

	for(int i = 1 ; i < in ; i++)
	{
		if(v[i+1] == 0)
			v[i+1] = v[i] + 1;
		else
			if(v[i+1] > v[i] + 1)
				v[i+1] = v[i] + 1;
		if(in >= i*2)
		{
			if(v[i*2] == 0)
				v[i*2] = v[i] + 1;
			else
				if(v[i*2] > (v[i] + 1))
					v[i*2] = v[i] + 1;
		}
		if(in >= i*3)
		{
			if(v[i*3] == 0)
				v[i*3] = v[i] + 1;
			else
				if(v[i*3] > (v[i] + 1))
					v[i*3] = v[i] + 1;	
		}
	}

	printf("%d\n",v[in]);
	return 0;
}