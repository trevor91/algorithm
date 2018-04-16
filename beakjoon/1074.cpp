#include <stdio.h>
int cnt = 0;
bool finish = false;
int n,r,c;
void go(int n, int start_r, int start_c)
{
	if(finish) return;
	if(start_r > r || start_r+n < r || start_c > c || start_c+n < c)
	{
		cnt += n*n;
		return;
	}
	if(start_r==r && start_c==c)
	{
		finish = true;
		return;
	}
	if(n==1) {cnt++;return;}
	int h=n/2;
	go(h, start_r, start_c);
	go(h, start_r, start_c+h);
	go(h, start_r+h, start_c);
	go(h, start_r+h, start_c+h);
}

int main()
{
	scanf("%d %d %d", &n, &r, &c);
	int a = 2;
	for(int i=1; i<n; i++)
		a *= 2;
	go(a,0,0);
	printf("%d\n", cnt);
	return 0;
}