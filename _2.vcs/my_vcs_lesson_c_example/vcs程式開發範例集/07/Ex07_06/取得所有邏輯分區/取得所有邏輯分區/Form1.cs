using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 取得所有邏輯分區
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public void listFolders(ComboBox tscb)//取得本地磁盤目錄
        {
            string[] logicdrives = System.IO.Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                tscb.Items.Add(logicdrives[i]);
                tscb.SelectedIndex = 0;
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            listFolders(comboBox1);
        }
    }
}
