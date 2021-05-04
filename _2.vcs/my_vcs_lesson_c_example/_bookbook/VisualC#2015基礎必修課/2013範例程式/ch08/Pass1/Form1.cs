using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pass1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //以傳值方式呼叫PassValue方法
        private void PassValue(int x, int y)
        {
            label1.Text += "2.方法中:變數計算前: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
            x += 3; //虛引數x加3
            y += 2; //虛引數y加2
            label1.Text += "3.方法中:變數計算後: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int a = 10, b = 15;
            label1.Text = "1.主程式:呼叫方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
            PassValue(a, b);
            label1.Text += "4.主程式:呼叫方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
        }
    }
}
