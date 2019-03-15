#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

// 計數器
int counter = 0;

// 子執行緒函數
void* child()
{
	for(int i = 0;i < 3;++i)
	{
		int tmp = counter;
		sleep(1); // 故意讓它延遲一下
		counter = tmp + 1;
		printf("Counter = %d\n", counter);
	}
	pthread_exit(NULL);
}

// 主程式
int main()
{
	pthread_t t1, t2;
	pthread_create(&t1, NULL, child, NULL);
	pthread_create(&t2, NULL, child, NULL);
	pthread_join(t1, NULL);
	pthread_join(t2, NULL);
	return 0;
}





