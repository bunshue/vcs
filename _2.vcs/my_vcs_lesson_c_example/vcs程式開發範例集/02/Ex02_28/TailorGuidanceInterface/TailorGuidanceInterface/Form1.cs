using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TailorGuidanceInterface
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
       
        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            try
            {
                if (treeView1.SelectedNode.Text == "公司信息")
                {
                    Form2 frm = new Form2();
                
                    frm.Show();
                }
            }
            catch (Exception ee)
            { MessageBox.Show(ee.Message); }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {   
            this.toolStripStatusLabel4.Text = "             系统时间：" + DateTime.Now.ToLongTimeString();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
         
        }


    }
}