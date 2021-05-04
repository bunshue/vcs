using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Rnd2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int[] num = new int[5]; //紀錄5個整數亂數
            Random rnd = new Random();//建立rnd亂數物件
            label1.Text = "";//清空label1
            for (int i = 0; i <= 4; i++)
            {
                int r = rnd.Next(49) + 1; //產生1~49亂數
                bool same = false;  //檢查亂數是否重複，預設為不重複
                foreach (int n in num)//逐一檢查num陣列元素
                    if (r == n) { same = true; break; }//若相同就設same=true並離開迴圈
                if (same == false)//若same=false
                    num[i] = r; //將亂數存入陣列中
                else
                    i--;//i減1重新產生亂數
            }
            for (int i = 0; i <= 4; i++)    //逐一顯示亂數
            {
                label1.Text += "第" + (i + 1).ToString() + "個亂數: "
                  + num[i].ToString() + "\n";
            }
        }
    }
}
