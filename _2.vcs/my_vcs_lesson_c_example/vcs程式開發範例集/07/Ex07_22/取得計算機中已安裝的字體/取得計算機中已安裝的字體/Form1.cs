using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Text;
namespace 取得計算機中已安裝的字體
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            InstalledFontCollection myFonts = new InstalledFontCollection();
            foreach (FontFamily family in myFonts.Families)
            {
                richTextBox1.AppendText(family.Name+"\n");
            }
        }
    }
}
