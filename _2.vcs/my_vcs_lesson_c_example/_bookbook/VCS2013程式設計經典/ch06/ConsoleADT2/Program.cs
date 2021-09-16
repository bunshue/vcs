using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleADT2
{
    class Program
    {
        struct Student
        {
            public int No;
            public string Name;
            public int Score;
        };
        // 初值置入結構陣列
        // 1001,"Paul",85,90,66
        // 1002,"Jack",80,80,77
        // 1003,"Mary",75,70,80
        // 1004,"Jane",90,85,99
        // 1005,"Nacy",70,80,60
        // 結構陣列如何在宣告建立結構陣列時,同時設定初值
        static void Main(string[] args)
        {
           int i, j ;
	       Student temp;
           
           // Student[] bcc = new Student[5];
           // bcc[0].No = 1001; bcc[0].Name = "Paul"; bcc[0].Score = 85;
           // bcc[1].No = 1002; bcc[1].Name = "Jack"; bcc[1].Score = 80;
           // bcc[2].No = 1003; bcc[2].Name = "Mary"; bcc[2].Score = 70;
           // bcc[3].No = 1004; bcc[3].Name = "Jane"; bcc[3].Score = 90;
           // bcc[4].No = 1005; bcc[4].Name = "Nacy"; bcc[4].Score = 75;

           Student[] bcc = new Student[] {
               new Student(){No=1001,Name="Paul", Score=85},
               new Student(){No=1002,Name="Jack", Score=80},
               new Student(){No=1003,Name="Mary", Score=70},
               new Student(){No=1004,Name="Jane", Score=90},
               new Student(){No=1005,Name="Nacy", Score=75}
           };
           
           for (i = 0; i < bcc.Length; i++)
           {
                for (j = i + 1; j < bcc.Length; j++)
                {
                    if (bcc[j].Score > bcc[i].Score)
                    {
                        temp = bcc[i];
                        bcc[i] = bcc[j];
                        bcc[j] = temp;
                    }
                }
           }
           Console.WriteLine("  座號   姓名   計概");
           Console.WriteLine(" ====== ====== ====== ");
           for (i = 0; i < bcc.Length; i++)
           {
                Console.WriteLine("  {0}   {1}    {2}", bcc[i].No , bcc[i].Name, bcc[i].Score);
           }
           Console.Read();
         
       }
    }
}
