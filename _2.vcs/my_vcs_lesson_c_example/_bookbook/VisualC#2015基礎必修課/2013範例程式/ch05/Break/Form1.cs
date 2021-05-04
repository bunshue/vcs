using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Break
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int num = 49;
            int x = 2;  //x從2開始
            string msg = num.ToString() + "是質數";//預設num為質數
            while (x < num) //當x<num時就執行迴圈
            {
                if (num % x == 0)   //若num除以x的餘數為0(就是整除)
                {
                    msg = num.ToString() + "不是質數";//num不是質數
                    break;  //用break敘述跳離迴圈
                }
                else   //其餘即不能整除
                    x++;    //x+1
            }
            MessageBox.Show(msg);   //顯示msg字串
            Application.Exit();
        }
    }
}
