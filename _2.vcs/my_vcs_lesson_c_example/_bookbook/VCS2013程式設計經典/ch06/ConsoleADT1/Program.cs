using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleADT1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] stu_No = new int[]{1001,1002,1003,1004,1005};
            string[] stu_Name = new string[]{"Lida","Jack","Mary","Nacy","Jane"};
            int[] stu_Chin = new int[]{85,80,75,90,60};
            int[] stu_Eng = new int[]{90,80,70,60,88};
            int[] stu_Math = new int[]{66,77,88,99,60};

            int i, j, tmp;
            string s;

            for (i = 0; i < stu_No.Length; i++)
            {
                for (j = i + 1; j < stu_No.Length; j++)
                {
                    if (stu_Chin[j] < stu_Chin[i])
                    {
                        tmp = stu_No[i];
                        stu_No[i] = stu_No[j];
                        stu_No[j] = tmp;

                        s = stu_Name[i];
                        stu_Name[i] = stu_Name[j];
                        stu_Name[j] = s;

                        tmp = stu_Chin[i];
                        stu_Chin[i] = stu_Chin[j];
                        stu_Chin[j] = tmp;

                        tmp = stu_Eng[i];
                        stu_Eng[i] = stu_Eng[j];
                        stu_Eng[j] = tmp;

                        tmp = stu_Math[i];
                        stu_Math[i] = stu_Math[j];
                        stu_Math[j] = tmp;
                    }
                }
            }
            Console.WriteLine("  座號   姓名   國文  英文  數學");
            Console.WriteLine(" ====== ====== ====== ===== ===== ");
            for (i = 0; i < stu_No.Length; i++)
            {
                Console.WriteLine(" {0},  {1},   {2},    {3},   {4}", stu_No[i], stu_Name[i], stu_Chin[i], stu_Eng[i], stu_Math[i]);
            }
            Console.Read();
        }
    }
}
