#include <stdio.h>
#include <string.h>

int main()
{
	char in[101];
	scanf("%s", in);
	int l=0, r=strlen(in)-1;
	bool rst=true;
	while(r>=l)
	{
		if(in[l++] == in[r--])
			continue;
		else
		{
			rst = false;
			break;
		}
	}
	printf(rst? "true\n" : "false\n");
	return 0;
}