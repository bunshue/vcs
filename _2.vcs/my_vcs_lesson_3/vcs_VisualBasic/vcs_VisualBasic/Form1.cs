using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//for Interaction,          //參考/加入參考/.NET/Microsoft.VisualBasic

namespace vcs_VisualBasic
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //VisualBasic 使用範例

            string i;   //記錄使用者輸入的資料
            double num; //使用者輸入資料轉成double的值
            i = Microsoft.VisualBasic.Interaction.InputBox
                ("請輸入數值：", "求平方");
            num = Convert.ToDouble(i); //將使用者輸入的資料轉成double
            MessageBox.Show(i + "的平方等於" + (num * num).ToString() + "\n", "平方");

        }
    }
}

