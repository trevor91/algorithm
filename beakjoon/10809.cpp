#include <stdio.h>
#include <string.h>
int main()
{
	char in[101];
	int alpha[26];
	memset(alpha, -1, sizeof(alpha));
	int i=0;
	scanf("%s", in);
	while(in[i] != NULL)
	{
		if(alpha[in[i]-97] == -1)
			alpha[in[i]-97] = i;
		i++;
	}
	for(i=0; i<26; i++)
		printf("%d ", alpha[i]);
	return 0;
}