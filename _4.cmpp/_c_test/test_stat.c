#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

int main(int argc,char* argv[])
{
        int i;
	struct stat buf;
	//if(stat("zzz.txt", &buf) == -1)
	if(stat(".mkshrc", &buf) == -1)
	{
		perror("fail to stat\n");
		exit(1);
	}
        printf("stat ok\n");

	printf("file_size = %d\n", buf.st_size);
	printf("st_size = %d bytes\n", buf.st_size);
	printf("st_blksize = %d\n", buf.st_blksize);
	printf("st_blocks = %d\n", buf.st_blocks);
	printf("st_atime = %d\n", buf.st_atime);
	printf("st_mtime = %d\n", buf.st_mtime);
	printf("st_ctime = %d\n", buf.st_ctime);
	printf("st_dev = %d\n", buf.st_dev);
	printf("st_ino = %d\n", buf.st_ino);
	printf("st_mode = 0x%x = %d\n", buf.st_mode, buf.st_mode);
	printf("st_nlink = %d\n", buf.st_nlink);
	printf("st_uid = %d\n", buf.st_uid);
	printf("st_gid = %d\n", buf.st_gid);
	printf("st_nlink = %d\n", buf.st_nlink);
	printf("st_rdev = %d\n", buf.st_rdev);

	printf("File type:                ");

	switch (buf.st_mode & S_IFMT) {
		case S_IFBLK:  printf("block device\n");            break;
		case S_IFCHR:  printf("character device\n");        break;
		case S_IFDIR:  printf("directory\n");               break;
		case S_IFIFO:  printf("FIFO/pipe\n");               break;
		case S_IFLNK:  printf("symlink\n");                 break;
		case S_IFREG:  printf("regular file\n");            break;
		case S_IFSOCK: printf("socket\n");                  break;
		default:       printf("unknown?\n");                break;
	}

	printf("I-node number:            %ld\n", (long) buf.st_ino);

	printf("Mode:                     %lo (octal)\n", (unsigned long) buf.st_mode);
	printf("Link count:               %ld\n", (long) buf.st_nlink);
	printf("Ownership:                UID=%ld   GID=%ld\n", (long) buf.st_uid, (long) buf.st_gid);
	printf("Preferred I/O block size: %ld bytes\n", (long) buf.st_blksize);
	printf("File size:                %lld bytes\n", (long long) buf.st_size);
	printf("Blocks allocated:         %lld\n", (long long) buf.st_blocks);
	printf("Last status change:       %s", ctime(&buf.st_ctime));
	printf("Last file access:         %s", ctime(&buf.st_atime));
	printf("Last file modification:   %s", ctime(&buf.st_mtime));


        return 0;
}

