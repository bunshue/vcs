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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            f1();
            f2(100);
            int A = f3(100);
            float B = f4(100, 2.5f);
            float C = f5(100);

            int X = 200, Y;
            Y = f6(ref X);  // 呼叫函數 f6，X 是實際參數
            label1.Text = "X = " + X.ToString() + ", Y = " + Y.ToString();
        }

        void f1()
        {
        }

        void f2(int k)
        {
        }

        int f3(int k)
        {
            int m = k + 5;
            return m;
        }

        float f4(int k, float j)
        {
            float m = k * j;
            return m;
        }

        public float f5(int k)
        {
            float m = k + 5;
            return m;
        }

        int f6(ref int k)
        {
            k = k * 10;
            int m = k + 5;
            return m;
        }

    }
}