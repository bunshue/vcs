#include <stdio.h>
#include <unistd.h>	//for sleep
#include <pthread.h>
static void *SDL_input_event_loop (void *arg);

int main(int argc,char* argv[])
{
        printf("david: This is a c template.\n");

			pthread_t thread;
			pthread_create(&thread, NULL, SDL_input_event_loop, NULL);
			//pthread_detach (thread);

			pthread_join(thread, NULL); // 等待子執行緒執行完成
	
        return 0;
}

static void *SDL_input_event_loop (void *arg) {
	(void)arg;
	for (;;) {
		sleep(1);
		printf("s");
	}
	return 0;
}


