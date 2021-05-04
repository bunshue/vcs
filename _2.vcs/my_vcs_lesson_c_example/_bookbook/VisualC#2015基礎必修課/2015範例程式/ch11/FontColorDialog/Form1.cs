using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FontColorDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblMsg.Text = "神魔之塔";
            fontDialog1.ShowColor = true;    //顯示顏色設定清單
        }

        private void btnFont_Click(object sender, EventArgs e)
        {
            //檢查是否按<確定>鈕
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                //若按<確定>鈕，將字型設定顯示在lblMsg上面
                lblMsg.Font = fontDialog1.Font;
                lblMsg.ForeColor = fontDialog1.Color;   //將設定顏色當lblMsg的前景色
            }
        }

        private void btnBColor_Click(object sender, EventArgs e)
        {
            //檢查是否未按<取消>鈕
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                lblMsg.BackColor = colorDialog1.Color;    //將設定顏色當lblMsg的背景色
            }
        }
    }
}
