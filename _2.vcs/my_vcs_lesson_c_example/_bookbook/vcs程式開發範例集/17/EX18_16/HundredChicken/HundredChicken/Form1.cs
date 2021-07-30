using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace HundredChicken
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label4.Text = "公雞5元一隻，母雞3元一隻，小雞3" + "\r" + "只一元，用100元買100隻雞";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = 0, b = 0, c = 0, p = 0;//定義變數
            for (a = 1; a <= 19; a++)//公雞的百元中的搜尋
            {
                for (b = 1; b <= 33; b++)//母雞在百元中的搜尋
                {
                    c = 100 - a - b;//取得百中除了公雞和母雞後，小雞的總錢數
                    Math.DivRem(c, 3, out p);//計算小雞的個數
                    if (((5 * a + 3 * b + c / 3) == 100) && p == 0)//如果公雞、母雞和小雞的總錢數加起來為100
                    {
                        textBox1.Text = a.ToString();//顯示公雞的個數
                        textBox2.Text = b.ToString();//顯示母雞的個數
                        textBox3.Text = c.ToString();//顯示小雞的個數
                        return;
                    }
                }
            }
        }
    }
}
