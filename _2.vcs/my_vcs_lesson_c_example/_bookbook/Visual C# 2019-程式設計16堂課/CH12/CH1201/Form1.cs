using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1201
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void 新增NToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //建立子表單
            MDISon oneChild = new MDISon();
            //將目前的表單指定為oneChild的MDI父表單
            oneChild.MdiParent = this;
            oneChild.Size = new Size(50, 100);
            //記錄子表單的數量
            int count = this.MdiChildren.Length;
            //設定子表單的標題
            oneChild.Text = $"我是子表單-{count.ToString()}";
            oneChild.Show();   //顯示MDI子表單
        }
    }
}
