using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Function : Form
    {
        public Function()
        {
            InitializeComponent();
        }

        bool isPass(int s)
        {
            if (s >= 60) return true;
            else return false;
        }

        char ScoreToGrade(int s)
        {
            if (s >= 90) return 'A';
            else if (s >= 80) return 'B';
            else if (s >= 70) return 'C';
            else if (s >= 60) return 'D';
            else return 'E';
        }

        string scoreProcessing(int s)
        {
            string res = "";

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            return res;
        }

        int sumArray(int[] a)
        {
            int sum = 0;

            for (int i = 0; i < a.Length; i++)
                sum += a[i];

            return sum;
        }

        void MaxMinArray(int[] a, out int max, out int min)
        {
            max = a[0];
            min = a[0];

            for (int i = 1; i < a.Length; i++)
            {
                if (a[i] > max) max = a[i];
                if (a[i] < min) min = a[i];
            }
        }

        int add(int a, int b) { return a + b; }
        double add(double a, double b) { return a + b; }

        int add(int[] a)
        {
            int sum = 0;

            for (int i = 0; i < a.Length; i++)
                sum += a[i];

            return sum;
        }
        
        double add(double[] a)
        {
            double sum = 0.0;

            for (int i = 0; i < a.Length; i++)
                sum += a[i];

            return sum;
        }
       
        void func0()
        {
            /*-------------------------------
             *  計算五個成績是否及格與等級  *
             *-----------------------------*/

            string res = "";

            // txtNum1.Text
            int s = Convert.ToInt32(txtNum1.Text);

            if (s >= 60) res += s + ":及格, ";
            else res += s + ":不及格, ";

            if (s >= 90) res += "等級為A\r\n";
            else if (s >= 80) res += "等級為B\r\n";
            else if (s >= 70) res += "等級為C\r\n";
            else if (s >= 60) res += "等級為D\r\n";
            else res += "等級為E\r\n";

            // txtNum2.Text
            s = Convert.ToInt32(txtNum2.Text);

            if (s >= 60) res += s + ":及格, ";
            else res += s + ":不及格, ";

            if (s >= 90) res += "等級為A\r\n";
            else if (s >= 80) res += "等級為B\r\n";
            else if (s >= 70) res += "等級為C\r\n";
            else if (s >= 60) res += "等級為D\r\n";
            else res += "等級為E\r\n";

            // txtNum3.Text
            s = Convert.ToInt32(txtNum3.Text);

            if (s >= 60) res += s + ":及格, ";
            else res += s + ":不及格, ";

            if (s >= 90) res += "等級為A\r\n";
            else if (s >= 80) res += "等級為B\r\n";
            else if (s >= 70) res += "等級為C\r\n";
            else if (s >= 60) res += "等級為D\r\n";
            else res += "等級為E\r\n";

            // txtNum4.Text
            s = Convert.ToInt32(txtNum4.Text);

            if (s >= 60) res += s + ":及格, ";
            else res += s + ":不及格, ";

            if (s >= 90) res += "等級為A\r\n";
            else if (s >= 80) res += "等級為B\r\n";
            else if (s >= 70) res += "等級為C\r\n";
            else if (s >= 60) res += "等級為D\r\n";
            else res += "等級為E\r\n";

            // txtNum5.Text
            s = Convert.ToInt32(txtNum5.Text);

            if (s >= 60) res += s + ":及格, ";
            else res += s + ":不及格, ";

            if (s >= 90) res += "等級為A\r\n";
            else if (s >= 80) res += "等級為B\r\n";
            else if (s >= 70) res += "等級為C\r\n";
            else if (s >= 60) res += "等級為D\r\n";
            else res += "等級為E\r\n";

            txtOutput.Text = res;
        }

        void func1()
        {
            /*-----------------------
             *     使用函數呼叫1    *
             *---------------------*/

            string res = "";

            // txtNum1.Text
            int s = Convert.ToInt32(txtNum1.Text);

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            // txtNum2.Text
            s = Convert.ToInt32(txtNum2.Text);

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            // txtNum3.Text
            s = Convert.ToInt32(txtNum3.Text);

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            // txtNum4.Text
            s = Convert.ToInt32(txtNum4.Text);

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            // txtNum5.Text
            s = Convert.ToInt32(txtNum5.Text);

            if (isPass(s)) res += s + ":及格, ";
            else res += s + ":不及格, ";

            res += "等級為" + ScoreToGrade(s) + "\r\n";

            txtOutput.Text = res; 
        }

        void func2()
        {
            /*-----------------------
             *     使用函數呼叫2     *
             *---------------------*/

            string res = "";

            // txtNum1.Text
            int s = Convert.ToInt32(txtNum1.Text);

            res += scoreProcessing(s);
                      
            // txtNum2.Text
            s = Convert.ToInt32(txtNum2.Text);

            res += scoreProcessing(s);

            // txtNum3.Text
            s = Convert.ToInt32(txtNum3.Text);

            res += scoreProcessing(s);

            // txtNum4.Text
            s = Convert.ToInt32(txtNum4.Text);

            res += scoreProcessing(s);

            // txtNum5.Text
            s = Convert.ToInt32(txtNum5.Text);

            res += scoreProcessing(s);

            txtOutput.Text = res;
        }

        void func3()
        {
            /*------------------------
            *      使用陣列改寫      *
            *-----------------------*/

            int[] s = new int[5];

            s[0] = Convert.ToInt32(txtNum1.Text);
            s[1] = Convert.ToInt32(txtNum2.Text);
            s[2] = Convert.ToInt32(txtNum3.Text);
            s[3] = Convert.ToInt32(txtNum4.Text);
            s[4] = Convert.ToInt32(txtNum5.Text);

            string res = "";

            for (int i = 0; i < 5; i++)
            {
                /*
                if (isPass(s[i])) res += s[i] + ":及格, ";
                else res += s[i] + ":不及格, ";

                res += "等級為" + ScoreToGrade(s[i]) + "\r\n";*/

                res += scoreProcessing(s[i]);
            }

            txtOutput.Text = res;
        }

        void func4()
        {
           /*------------------------------------
           *      統計幾人及格, 各等級幾人      *
           *-----------------------------------*/

            int[] s = new int[5];

            s[0] = Convert.ToInt32(txtNum1.Text);
            s[1] = Convert.ToInt32(txtNum2.Text);
            s[2] = Convert.ToInt32(txtNum3.Text);
            s[3] = Convert.ToInt32(txtNum4.Text);
            s[4] = Convert.ToInt32(txtNum5.Text);

            int pass = 0, A = 0, B = 0, C = 0, D = 0, E = 0;
            int sum = 0;

            for (int i = 0; i < 5; i++)
            {
                if (isPass(s[i])) pass++;

                switch ( ScoreToGrade(s[i]) ) {
                    case 'A': A++; break;
                    case 'B': B++; break;
                    case 'C': C++; break;
                    case 'D': D++; break;
                    case 'E': E++; break;
                }

                sum += s[i];
            }

            string res = "及格: " + pass + "人\r\n";
            res += "等級A: " + A + "人\r\n";
            res += "等級B: " + B + "人\r\n";
            res += "等級C: " + C + "人\r\n";
            res += "等級D: " + D + "人\r\n";
            res += "等級E: " + E + "人\r\n";
            res += "平均 = " + (sum / 5.0);

            txtOutput.Text = res;
        }

        void func5()
        {
            /*------------------------------------------------
            *      統計幾人及格, 各等級幾人: 以陣列儲存      *
            *-----------------------------------------------*/

            int[] s = new int[5];

            s[0] = Convert.ToInt32(txtNum1.Text);
            s[1] = Convert.ToInt32(txtNum2.Text);
            s[2] = Convert.ToInt32(txtNum3.Text);
            s[3] = Convert.ToInt32(txtNum4.Text);
            s[4] = Convert.ToInt32(txtNum5.Text);

            int pass = 0;
            int[] ctr = { 0, 0, 0, 0, 0 };
            int sum = 0;

            for (int i = 0; i < 5; i++)
            {
                if (isPass(s[i])) pass++;

                ctr[ScoreToGrade(s[i]) - 'A']++;

                sum += s[i];
            }

            string res = "及格: " + pass + "人\r\n";

            for (int i = 0; i < 5; i++)
            {
                res += "等級" + (char)('A' + i) + ": " + ctr[i] + "人\r\n";
            }

            res += "平均 = " + (sum / 5.0);

            txtOutput.Text = res;
        }

        
        void passArray()
        {
            int[] s = new int[5];

            s[0] = Convert.ToInt32(txtNum1.Text);
            s[1] = Convert.ToInt32(txtNum2.Text);
            s[2] = Convert.ToInt32(txtNum3.Text);
            s[3] = Convert.ToInt32(txtNum4.Text);
            s[4] = Convert.ToInt32(txtNum5.Text);

            int sum = sumArray(s);

            string res = "和 = " + sum + "\r\n";
            res += "平均 = " + (sum / 5.0) + "\r\n";
            
            int max, min;

            MaxMinArray(s, out max, out min);
            res += "最高分 = " + max + "\r\n";
            res += "最低分 = " + min + "\r\n";
         
            txtOutput.Text = res;
        }

        void method_overloading()
        {
            string res = "";

            res += "add(5, 10) = " + add(5, 10) + "\r\n";
            res += "add(5.2, 10.3) = " + add(5.2, 10.3) + "\r\n";
            res += "add(5, 10.3) = " + add(5, 10.3) + "\r\n";

            //res += add(5, "10") + "\r\n"; // error

            int[] intArray = { 1, 2, 3, 4, 5 };
            int sum = add(intArray);  //OK
            res += sum.ToString();

            double[] dArray = { 10.1, 20.2, 30.3, 40.4, 50.5 };
            double dSum = add(dArray);
            res += "\r\n" + dSum.ToString();

            txtOutput.Text = res;
        }

        private void btnCompute_Click(object sender, EventArgs e)
        {
            /*-------------------------------
             *  計算五個成績是否及格與等級  *
             *-----------------------------*/
            //func0();
            
            /*-----------------------
             *     使用函數呼叫1    *
             *---------------------*/
            //func1();

            /*-----------------------
             *     使用函數呼叫2    *
             *---------------------*/
            //func2();

            /*------------------------
            *      使用陣列改寫      *
            *-----------------------*/
            //func3();
            
            /*------------------------------------
            *      統計幾人及格, 各等級幾人      *
            *-----------------------------------*/
            //func4();
           
            /*------------------------------------------------
            *      統計幾人及格, 各等級幾人: 以陣列儲存      *
            *-----------------------------------------------*/
            //func5();

            /*------------------------------------------------
            *      pass array into function: 傳遞陣列        *
            *-----------------------------------------------*/
            // passArray();

            /*------------------------------*/
            /*      method overloading      */
            /*------------------------------*/
            method_overloading();  

        }
    }
}
