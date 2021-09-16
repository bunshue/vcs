using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormFirst
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // === 表單載入時執行
        private void Form1_Load_1(object sender, EventArgs e)
        {
            label1.Text = "表單載入時...";
            label1.Font = new Font("標楷體", 14, FontStyle.Underline);
            this.BackColor = Color.Red; //this為目前表單，背景色設為紅色
        }

        // === 按一下表單時執行
        private void Form1_Click(object sender, EventArgs e)
        {
            label1.Text = "按一下表單...";
            this.BackColor = Color.Yellow; // 表單背景色彩為黃色 
        }
        // === 按兩下表單時執行
        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            label1.Text = "按兩下表單...";
            this.BackColor = Color.Aqua;   // 表單背景色彩為淺藍色
        }        
    }
}
