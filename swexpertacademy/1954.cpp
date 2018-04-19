//https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE

#include <stdio.h>

int main()
{
	int testCnt;
	scanf("%d", &testCnt);
	for(int testCase = 1; testCase<=testCnt; testCase++)
	{
		int n;
		scanf("%d", &n);
		int size = n;
		printf("#%d\n", testCase);

		/*array setting*/
		int **arr = new int*[size];
		for(int i=0; i<size; i++)
			arr[i] = new int[size];

		/*input value*/
		int row=0, col=-1;
		int plus = 1;
		int value = 1;
		for(int i=n; i>0; i--)
		{
			for(int i=0; i<n; i++)
			{
				col = col+plus;
				arr[row][col] = value;
				value++;
			}
			n--;
			for(int i=0; i<n; i++)
			{
				row  = row+plus;
				arr[row][col] = value;
				value++;
			}
			plus *= -1;
		}

		/*print*/
		for(int i=0; i<size; i++)
		{
			for(int j=0; j<size; j++)
				printf("%d ", arr[i][j]);
			printf("\n");
		}

		/*delete array*/
		for(int i=0; i<size; i++)
			delete arr[i];
		delete arr;
	}
	return 0;
}