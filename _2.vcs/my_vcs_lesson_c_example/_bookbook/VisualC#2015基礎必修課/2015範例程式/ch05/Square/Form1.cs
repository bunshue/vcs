using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Square
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DialogResult dr;    //宣告DialogResult型別變數dr
            string i;   //記錄使用者輸入的資料
            double num; //使用者輸入資料轉成double的值
            do    //do...while迴圈
            {
                i = Microsoft.VisualBasic.Interaction.InputBox
                    ("請輸入數值：", "求平方");
                num = Convert.ToDouble(i); //將使用者輸入的資料轉成double
                dr = MessageBox.Show(i + "的平方等於" + (num * num).ToString() +
                    "\n是否繼續？", "平方", MessageBoxButtons.YesNo);
            } while (dr == DialogResult.Yes);  //若傳回值為Yes就繼續迴圈
            Application.Exit(); //結束程式
        }
    }
}
