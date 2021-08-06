using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//ListBox用多顏色背景表示
//自建ListBox
//加入/現有項目 選取DrawListBox.cs

namespace vcs_ListBox8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int i;

            for (i = 0; i < 20; i++)
            {
                drawListBox1.Items.Add("ListBox用多顏色背景表示\t\t" + i.ToString());
            }



        }
    }
}
