using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EventTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //表單載入時會執行Form1_Load事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "Load"; //設標題文字為"Load"字串
            this.Width = 500; this.Height = 300;   //設表單寬度為500
            this.BackColor = Color.Yellow;      //設表單背景色為黃色
        }
        //表單啟動時會執行Form1_Activated事件處理函式
        private void Form1_Activated(object sender, EventArgs e)
        {
            this.Text += ",Act";    //標題文字增加",Act"字串
        }
        //表單重繪時會執行Form1_Paint事件處理函式
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            this.Text += ",Paint";  //標題文字增加",Paint"字串
        }
        //在表單上按一下會執行Form1_Click事件處理函式
        private void Form1_Click(object sender, EventArgs e)
        {
            this.Text += ",Click";  //標題文字增加",Click"字串
            this.Width += 10;     //表單寬度加10
        }
        //在表單上快按兩下時會執行Form1_DoubleClick事件處理函式
        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            this.Text += ",Dclick";  //標題文字增加",Dclick"字串
        }
    }
}
