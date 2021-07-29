using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;

namespace LookupNear
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static int[] a = new int[21] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };//定義數組
        public string LOCATE(int[] XX, int N, int X)//N數值的個數，M尋找的數值
        {
            int tem_n;//定義變數
            int jl, ju, jm;
            jl = 0;
            ju = N + 1;
        //利用二分尋找法進行查詢
        rebound://goto語句
            if (ju - jl > 1)//如果沒有搜尋完
            {
                jm = (ju + jl) / 2;//取得中間的位置
                if (XX[N] > XX[1] == X > XX[jm])//利用二分尋找進行判斷
                    jl = jm;
                else
                    ju = jm;
                goto rebound;
            }
            tem_n = jl;//取得近似值的位置
            if (X - XX[tem_n] > (XX[tem_n + 1] - N))//判斷左右那個更接近
                tem_n = jl + 1;
            return "a[" + tem_n.ToString() + "]:" + XX[tem_n].ToString();//傳回近似值
        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            string str1 = "";
            int n1 = 20;
            for (int i = 0; i <= n1; i++)
            {
                a[i] = i * 2 + i - 2;
                str1 = str1 + a[i].ToString() + ",";
            }
            listBox1.Items.Add("一維數組 a :");
            listBox1.Items.Add(str1.Trim());
        }



        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("尋找的近似值為：");
            listBox1.Items.Add(LOCATE(a, 20, Convert.ToInt32(textBox1.Text)));
        }
    }
}

