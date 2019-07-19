using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SlideShowString
{
    public partial class Form_Help : Form
    {
        public Form_Help()
        {
            InitializeComponent();
            label1.Text += "";
            label1.Text += "使用說明\n\n";
            label1.Text += "(數字鍵)上下左右  移動位置\n";
            label1.Text += "+/-               放大縮小字型\n";
            label1.Text += "W/w               放大縮小螢幕寬占比\n";
            label1.Text += "H/h               放大縮小螢幕高占比\n";
            label1.Text += "F/S               增加減少播放速度\n";
            label1.Text += "PageUp/PageDown   上一首/下一首\n";
            label1.Text += "T/t               設定/取消最上層顯示\n";
            label1.Text += "L/C/R             靠左/置中/靠右\n";
            label1.Text += "F1                幫助畫面\n";
            label1.Text += "F10               設定畫面\n";



            label1.Text += "x                 離開\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
