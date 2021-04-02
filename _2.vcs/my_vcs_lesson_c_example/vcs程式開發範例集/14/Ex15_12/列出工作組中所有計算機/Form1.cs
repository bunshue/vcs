using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.DirectoryServices;
namespace 列出工作組中所有計算機
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent(); 
        }
        //
        private void Form1_Load(object sender, EventArgs e)
        {
           GroupInfo();
        }
        //
        private void GroupInfo()
        {
            
            DirectoryEntry MainGroup = new DirectoryEntry("WinNT:");
            foreach (DirectoryEntry domain in MainGroup.Children)
            {
                listBox1.Text = "";
                listBox1.Items.Add(domain.Name);
            }   
        }
        //
        private void ComputerInfo(string strname)
        {
            
            DirectoryEntry MainGroup = new DirectoryEntry("WinNT:");
            foreach (DirectoryEntry domain in MainGroup.Children)
            {
               
                if (domain.Name == strname)
                {
                    foreach (DirectoryEntry pc in domain.Children)
                    {
                        if (pc.Name != "Schema")//Schema是結束標記   
                            this.listBox2.Items.Add(pc.Name);
                    }
                }
            }
            MessageBox.Show("檢索完成");
        }
        //
        private void listBox1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("開始檢索請稍等。。。");
            listBox2.Items.Clear();
            ComputerInfo(this.listBox1.Text);
        }
        //
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }
    }
}