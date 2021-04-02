using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;//需引用命名空間Using System.Diagnostics

namespace AddHyperLink
{
    public partial class AddHyperLink : Form
    {
        public AddHyperLink()
        {
            InitializeComponent();
        }

        private void richTextBox1_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            this.Text = e.LinkText;//設置與窗體關聯的文本
            Process.Start("iexplore", e.LinkText);// 在IE瀏覽器中瀏覽單擊的超鏈接
        }

        private void AddHyperLink_Load(object sender, EventArgs e)
        {

        }
    }
}
