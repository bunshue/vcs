using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace MatrixAdd
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, j;
            int [,] A = new int [3,3] {{1,3,5},{7,9,11},{13,15,17}};//二維陣列的宣告 
            int [,] B = new int[3, 3] { { 9, 8, 7 }, { 6, 5, 4 }, { 3, 2, 1 } };//二維陣列的宣告
            int [,] C = new int[3, 3] { { 0, 0, 0}, { 0, 0, 0 }, { 0, 0, 0 } } ;
            for(i=0;i<3;i++)
	            for(j=0;j<3;j++)
	                C[i,j]=A[i,j]+B[i,j];// 矩陣C=矩陣A+矩陣B 
	
            WriteLine("矩陣A內容"); 
            for(i=0;i<3;i++)
	        {
		        for(j=0;j<3;j++)
                    Write("{0} \t", A[i, j]);
                WriteLine();
            }
            WriteLine("矩陣B內容");
            for (i = 0; i < 3; i++)
            {
                for (j = 0; j < 3; j++)
                    Write("{0} \t", B[i, j]);
                WriteLine();

            }
            WriteLine("[矩陣A和矩陣B相加的結果]"); //印出A+B的內容
            for (i = 0; i < 3; i++)
            {
                for (j = 0; j < 3; j++)
                    Write("{0} \t", C[i, j]);
                WriteLine();
            }
            Read();
        }
    }
}
