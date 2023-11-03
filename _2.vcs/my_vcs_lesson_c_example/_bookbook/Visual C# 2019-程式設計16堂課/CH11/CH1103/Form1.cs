using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics; //滙入監控程序

namespace CH1103
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //啟動瀏覽器，進入維基百科
        private void linkLb1_LinkClicked(object sender,
              LinkLabelLinkClickedEventArgs e)
        {
            linkLb1.LinkColor = Color.Pink;
            linkLb1.ActiveLinkColor = Color.Red;
            //被瀏覽過就改變顏色
            linkLb1.LinkVisited = true;
            linkLb1.VisitedLinkColor = Color.PowderBlue;
            //超連結部分永遠顯示底線
            linkLb1.LinkBehavior = LinkBehavior.AlwaysUnderline;
            Process.Start("https://zh.wikipedia.org/wiki/");
        }

        private void linkLb2_LinkClicked(object sender,
              LinkLabelLinkClickedEventArgs e)
        {
            //啟動小算盤應用程式
            Process.Start("calc.exe");
        }
    }
}
