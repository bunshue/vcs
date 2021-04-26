using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_XML4
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_xml\person.xml";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟一XML文件檔並顯示在DataGridView上
            //使用DataSet讀XML文件

            DataSet ds = new DataSet();
            ds.ReadXmlSchema(filename);
            ds.ReadXml(filename);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}

