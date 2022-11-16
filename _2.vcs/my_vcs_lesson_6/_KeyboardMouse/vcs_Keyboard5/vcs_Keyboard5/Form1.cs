using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//複合控制項(Composite Control)

//專案 / 右鍵 / 加入 / 使用者控制項(U)  將 UserControl1.cs 改成 keyboard1.cs


namespace vcs_Keyboard5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "螢幕鍵盤, 使用 Label";
            label2.Text = "螢幕鍵盤, 使用 Button";
            int x_st = 20;
            int y_st = 20;
            int dy = 300;
            label1.Location = new Point(x_st, y_st + dy * 0);
            keyboard11.Location = new Point(x_st, y_st + dy * 0 + 30);

            label2.Location = new Point(x_st, y_st + dy * 1);
            keyboard21.Location = new Point(x_st, y_st + dy * 1 + 30);


        }
    }
}
