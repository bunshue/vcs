#include <stdio.h>
struct super_operations {
  int   a;  
  int   b;
  void  (*read_inode) (int);
};//super_operations�O�@�ӧt��function pointer��sturcture�A
  //�ӳo��function�ݶǶi�@�Ӿ�Ƥ޼ơC
  //�o��pointer�W��read_inode�A�ݭn���V���̭n�A�]�w�C

void func_A(int a){
  printf("�ϥ�func_A��ơA�L�X %d by func_A\n", a);
}

void func_B(int a){
  printf("�ϥ�func_B��ơA�L�X %d by func_B\n", a);
}

int main()
{
  super_operations AA;	//��super_operations�w�q�@���ܼ�AA
  AA.a    = 123;		//�]�w�ܼ�AA��a�Pb���ȡC
  AA.b    = 231;

  AA.read_inode = func_A;	//�]�wfunction pointer�u�Vfunc_A
  AA.read_inode(123);		//��123�޶i��read_inode�ҫ��V����ơA�Yfunc_A

  printf("\n");

  AA.read_inode = func_B;	//�]�wfunction pointer�u�Vfunc_B
  AA.read_inode(123);		//��123�޶i��read_inode�ҫ��V����ơA�Yfunc_B

  return 0;
}



