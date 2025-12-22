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

/*
DrawListBox使用方法
方案總管/加入/現有項目, 選DrawListBox.cs, 會自動帶入DrawListBox.Designer.cs
改namespace
工具箱會出現 DrawListBox
使用方法如同ListBox, 就是多了顏色, 把GradualC改為true
*/

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
                drawListBox2.Items.Add("ListBox用多顏色背景表示\t\t" + i.ToString());
            }
        }
    }
}

