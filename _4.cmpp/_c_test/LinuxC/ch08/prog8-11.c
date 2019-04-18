 #include <stdio.h>
 main()
 {
    int strlen1(const char*);
    char s[]="Hello";
    int a;
    
    a=strlen1(s);
    printf("%d\n",a);
 }

 int strlen1(char *s)
 {
    char *p;
    p=s;
    while(*p!='\0')
        p++;
    return(p-s);
 }
