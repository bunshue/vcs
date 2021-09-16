using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;

namespace ReadXml
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DataSet ds = new DataSet();	//建立ds屬於DataSet物件
            ds.ReadXml("person.xml");		//讀入person.xml文件檔
            //在dataGridView1控制項上顯示person.xml文件檔的所有資料
            dataGridView1.DataSource = ds.Tables["學生"];
        }
    }
}
