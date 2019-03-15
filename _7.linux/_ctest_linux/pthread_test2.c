#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

// 子執行緒函數
void* child(void* data) {
  char *str = (char*) data; // 取得輸入資料
  for(int i = 0;i < 10;++i) {
    printf("%s %d\n", str, i); // 每秒輸出文字
    sleep(1);
  }
  pthread_exit(NULL); // 離開子執行緒
}

// 主程式
int main() {
  pthread_t t; // 宣告 pthread 變數
  pthread_create(&t, NULL, child, "one child thread"); // 建立子執行緒

  // 主執行緒工作
  for(int i = 0;i < 3;++i) {
    printf("Master %d\n", i); // 每秒輸出文字
    sleep(1);
  }

	printf("main thread ends, wait others to finish\n");

  pthread_join(t, NULL); // 等待子執行緒執行完成
	printf("every thread ends, .... finish\n");
  return 0;
}






