#include <stdio.h>
struct super_operations {
  int   a;  
  int   b;
  void  (*read_inode) (int);
};//super_operations琌Τfunction pointersturcture
  //τ硂function惠肚秈俱计ま计
  //硂pointerread_inode璶柑璶砞﹚

void func_A(int a){
  printf("ㄏノfunc_Aㄧ计 %d by func_A\n", a);
}

void func_B(int a){
  printf("ㄏノfunc_Bㄧ计 %d by func_B\n", a);
}

int main()
{
  super_operations AA;	//ノsuper_operations﹚竡跑计AA
  AA.a    = 123;		//砞﹚跑计AAずa籔b
  AA.b    = 231;

  AA.read_inode = func_A;	//砞﹚function pointerfunc_A
  AA.read_inode(123);		//р123ま秈倒read_inode┮ㄧ计func_A

  printf("\n");

  AA.read_inode = func_B;	//砞﹚function pointerfunc_B
  AA.read_inode(123);		//р123ま秈倒read_inode┮ㄧ计func_B

  return 0;
}



