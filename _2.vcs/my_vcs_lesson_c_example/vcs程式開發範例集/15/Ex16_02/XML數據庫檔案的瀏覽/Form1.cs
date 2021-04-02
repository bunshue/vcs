using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace XML數據庫檔案的瀏覽
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string strPath=null;//文件路徑
        private void button1_Click(object sender, EventArgs e)
        {
           
            openFileDialog1.Filter = "xml文件|*.xml";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                strPath = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (strPath != null)
            {
                DataSet ds = new DataSet();
                ds.ReadXmlSchema(strPath);
                ds.ReadXml(strPath);
                dataGridView1.DataSource = ds.Tables[0].DefaultView;
            }
            else
            {
                MessageBox.Show("請選擇XML文件");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}