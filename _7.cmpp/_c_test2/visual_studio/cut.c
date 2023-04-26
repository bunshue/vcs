#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define M2F2_SECTOR_SIZE	2324
int main()
{
	typedef struct 
    {
    	unsigned char header[12];
    	unsigned char sync[4];
    	unsigned char subheader[8];
    	unsigned char data[M2F2_SECTOR_SIZE];	//data should be sent to demux
     	unsigned char spare[4];
    } vcdsector_t;
    	
    
    vcdsector_t vcd_sector;
    
    int 		fd;
    int 		offset = 0;
    int status;
    int i;
	char* 		file = "/home/david/avseq01.dat";
	char		file2[1024];
	char* data;
	FILE*		fp;
	static int  sector_count = 0;
    	sector_count=0;
    do {
    	fd = open(file, O_RDONLY);
    	assert(fd);
    	//offset = sector_count * 2352 + 44;
    	offset = sector_count * 2352;
    	assert(lseek(fd, offset, SEEK_SET) != -1);	//return 0 if successful 
    	printf("read ST : sector count = %4d\n", sector_count);
    	status=read(fd, &vcd_sector, sizeof(vcdsector_t));
    	printf("read SP : sector count = %4d w/ status=%d\n", sector_count,status);
	sprintf(file2,"%d",sector_count);
	fp=fopen(file2,"wb");
	//fwrite(vcd_sector,2352,1,fp);
	data=(char*)&vcd_sector;
	for(i=0;i<2352;i++)
	{
		//printf("%d",data[i]);
		fputc(data[i],fp);
	}
	printf("\n");
	



	fclose(fp);
	
	printf("---------------------------------------------------------\n");
	if (status == 0)
		perror("error code:");
	close(fd);

	if(sector_count==300)
		return 0;
	
    	sector_count+=1;
    	
	} while (1);
	return 0;
}


