#include <stdio.h>
using namespace std;

int main()
{
	int input;
	scanf("%d",&input);
	int sum = 0, max = -1001;
	int tmp;
	for(int i = 0; i<input; i++)
	{
		scanf("%d", &tmp);
		sum += tmp;
		if(tmp > sum)
			sum = tmp;
		if(sum > max)
			max = sum;
	}
	printf("%d\n", max);
	return 0;
}