#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>	//for sleep
#include <sys/time.h>	//for timezone

#define MST (-7)
#define UTC (0)
#define CCT (+8)

void cur_time(void);

char *myasctime(const struct tm *timeptr);

int main(int argc,char* argv[])
{
	printf("---test 1---------------------------------------------------------------\n");
	struct tm t;

	t.tm_sec    = 10;
	t.tm_min    = 10;
	t.tm_hour   = 6;
	t.tm_mday   = 25;
	t.tm_mon    = 2;
	t.tm_year   = 89;
	t.tm_wday   = 6;

	puts(asctime(&t));

	printf("\n\n%s\n\n", asctime(&t));

	asctime(&t);
	puts(asctime(&t));
	printf("\n\n%s\n\n", asctime(&t));

	myasctime(&t);
	puts(myasctime(&t));
	printf("\n\n%s\n\n", myasctime(&t));


	time_t curtime;

	time(&curtime);

	printf("Current time\n%s\n", ctime(&curtime));

	time_t rawtime;
	struct tm * timeinfo;
	struct tm * tt;

	time (&rawtime);
	timeinfo = localtime (&rawtime);
	printf ("Current local time and date: %s\n", asctime(timeinfo));

	tt = localtime(&rawtime);

	printf("tm_year  :   %d\n", tt->tm_year + 1900);
	printf("tm_mon   :   %d\n", tt->tm_mon + 1);
	printf("tm_mday  :   %d\n", tt->tm_mday);
	printf("tm_hour  :   %d\n", tt->tm_hour);
	printf("tm_min   :   %d\n", tt->tm_min);
	printf("tm_sec   :   %d\n", tt->tm_sec);
	printf("tm_yday  :   %d\n", tt->tm_yday);
	printf("tm_wday  :   %d\n", tt->tm_wday);
	printf("tm_isdst :   %d\n", tt->tm_isdst);

	

	time_t start_t, end_t;
	double diff_t;

	printf("Starting of the program...\n");
	time(&start_t);

	printf("Sleeping for 2 seconds...\n");
	sleep(2);

	time(&end_t);
	diff_t = difftime(end_t, start_t);

	printf("Execution time = %f  OK\n", diff_t);


	printf("---test 2---------------------------------------------------------------\n");
	clock_t start_t2, end_t2, total_t;
	int i;
	
	start_t2 = clock();
	printf("Starting of the program, start_t2 = %ld\n", start_t2);
	
	printf("Going to scan a big loop, start_t2 = %ld\n", start_t2);
	for(i=0; i< 10000000; i++)
	{
	}
	end_t2 = clock();
	printf("End of the big loop, end_t2 = %ld\n", end_t2);
	
	total_t = (double)(end_t2 - start_t2) / CLOCKS_PER_SEC;
	printf("Total time taken by CPU: %ld\n", total_t  );
	printf("Exiting of the program...\n");
	



	printf("---test 3---------------------------------------------------------------\n");

	
	long fiveseconds = CLOCKS_PER_SEC * 2;

	printf("CLOCKS_PER_SEC = %d\n", CLOCKS_PER_SEC);

	printf("sleep 2 sec ST...\n");
	while (clock() < fiveseconds) {
	}
	printf("sleep 2 sec SP...\n");


	printf("---test 4, gettimeofday---------------------------------------------------------------\n");

        struct  timeval    tv;
        struct  timezone   tz;
        gettimeofday(&tv,&tz);
  
        printf("tv_sec:%ld\n",tv.tv_sec);
        printf("tv_usec:%ld\n",tv.tv_usec);
        printf("tz_minuteswest:%d\n",tz.tz_minuteswest);
        printf("tz_dsttime:%d\n",tz.tz_dsttime);


	printf("---test 5---------------------------------------------------------------\n");

	time_t rawtime2;
	struct tm * ptm;

	time ( &rawtime2 );

	ptm = gmtime ( &rawtime2 );

	puts ("Current time around the World:");
	printf ("Phoenix, AZ (U.S.) :  %2d:%02d\n", (ptm->tm_hour+MST)%24, ptm->tm_min);
	printf ("Reykjavik (Iceland) : %2d:%02d\n", (ptm->tm_hour+UTC)%24, ptm->tm_min);
	printf ("Beijing (China) :     %2d:%02d\n", (ptm->tm_hour+CCT)%24, ptm->tm_min);


	cur_time();




	printf("---test 6, mktime---------------------------------------------------------------\n");

	struct tm time_str;
	char daybuf[20];

	time_str.tm_year = 2018 - 1900;
	time_str.tm_mon = 9 - 1;
	time_str.tm_mday = 27;
	time_str.tm_hour = 11;
	time_str.tm_min = 59;
	time_str.tm_sec = 16;
	time_str.tm_isdst = -1;
	if (mktime(&time_str) == -1)
		(void)puts("-unknown-");
	else {
		(void)strftime(daybuf, sizeof(daybuf), "%A", &time_str);
		(void)puts(daybuf);
		printf("dd = %d\n", time_str.tm_yday);
	}



	printf("---test 7, strftime---------------------------------------------------------------\n");

	time_t t1 = time(NULL);
	struct tm *nPtr = localtime(&t1);
	char now[30];
	char now2[130];

	//strftime() transform tm to specified string

	strftime(now, 30, "%m/%d/%Y %a", nPtr);
	printf("%s\n", now);
	strftime(now, 30, "%H:%M:%S", nPtr);
	printf("%s\n", now);

	strftime(now2, 130, "%a %A %b %B %c %d %H %I %j %m %M %P %S %U %w %W %x %X %y %Y %Z", nPtr); 
	printf("%s\n", now2);

	strftime(now, 30, "%a", nPtr);printf("%%a\t%s\n", now);
	strftime(now, 30, "%A", nPtr);printf("%%A\t%s\n", now);
	strftime(now, 30, "%b", nPtr);printf("%%b\t%s\n", now);
	strftime(now, 30, "%B", nPtr);printf("%%B\t%s\n", now);
	strftime(now, 30, "%c", nPtr);printf("%%c\t%s\n", now);
	strftime(now, 30, "%d", nPtr);printf("%%d\t%s\n", now);

	strftime(now, 30, "%H", nPtr);printf("%%H\t%s\n", now);
	strftime(now, 30, "%I", nPtr);printf("%%I\t%s\n", now);
	strftime(now, 30, "%j", nPtr);printf("%%j\t%s\n", now);
	strftime(now, 30, "%m", nPtr);printf("%%m\t%s\n", now);
	strftime(now, 30, "%M", nPtr);printf("%%M\t%s\n", now);
	strftime(now, 30, "%P", nPtr);printf("%%P\t%s\n", now);

	strftime(now, 30, "%S", nPtr);printf("%%S\t%s\n", now);
	strftime(now, 30, "%U", nPtr);printf("%%U\t%s\n", now);
	strftime(now, 30, "%w", nPtr);printf("%%w\t%s\n", now);
	strftime(now, 30, "%W", nPtr);printf("%%W\t%s\n", now);
	strftime(now, 30, "%x", nPtr);printf("%%x\t%s\n", now);
	strftime(now, 30, "%X", nPtr);printf("%%X\t%s\n", now);

	strftime(now, 30, "%y", nPtr);printf("%%y\t%s\n", now);
	strftime(now, 30, "%Y", nPtr);printf("%%Y\t%s\n", now);
	strftime(now, 30, "%Z", nPtr);printf("%%Z\t%s\n", now);


	printf("---test 8---------------------------------------------------------------\n");
     
	time_t t3 = time(NULL);
	printf("自 1970 年 1 月 1 日後經過了 %ld 秒....\n", t3);
	char *now3 = ctime(&t3);
	printf(now3);

	time_t t4 = time(NULL);
	struct tm *nPtr3 = localtime(&t4);

	char *now4 = asctime(nPtr3);

	printf(now4);

	printf("---test 9---------------------------------------------------------------\n");

	time_t t2 = time(NULL);
	struct tm *nPtr2 = localtime(&t2);
	int year = nPtr2->tm_year + 1900;
	int month = nPtr2->tm_mon + 1;
	int mday = nPtr2->tm_mday;
	int wday = nPtr2->tm_wday;

	printf("今天是 %u 年 %u 月 %u 號星期 %u\n", year, month, mday, wday);	

	printf("---test 10---------------------------------------------------------------\n");

	printf("---test 11---------------------------------------------------------------\n");
	printf("---test 12---------------------------------------------------------------\n");
	printf("---test 13---------------------------------------------------------------\n");
	printf("---test 14---------------------------------------------------------------\n");

        return 0;
}




char *myasctime(const struct tm *timeptr)
{
    static char wday_name[7][3] = {
        "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"
    };
    static char mon_name[12][3] = {
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    };
    static char result[26];


    sprintf(result, "%.3s %.3s%3d %.2d:%.2d:%.2d %d\n",
        wday_name[timeptr->tm_wday],
        mon_name[timeptr->tm_mon],
        timeptr->tm_mday, timeptr->tm_hour,
        timeptr->tm_min, timeptr->tm_sec,
        1900 + timeptr->tm_year);
    return result;
}


void cur_time(void){
    char *wday[]={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
    time_t timep;
    struct tm *p;
    time(&timep);
    p=gmtime(&timep); /* get current time */
    printf("%d/%02d/%02d ",(1900+p->tm_year),(1+p->tm_mon),p->tm_mday);
    printf("%s %02d:%02d:%02d\n",wday[p->tm_wday],(p->tm_hour+8),p->tm_min,p->tm_sec);
}



