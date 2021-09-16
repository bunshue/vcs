using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_4_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 讀入coffeeData.xml的XML文件結構
            DataSet dataSet = new DataSet();
            dataSet.InferXmlSchema(
                @"c:\coffeeData.xml", 
                new string[] { "urn:schemas-microsoft-com:officedata" });

            // 加入記錄
            DataRow newRow;

            newRow = dataSet.Tables["Products"].NewRow();
            newRow["ProductID"] = "A001";
            newRow["ReorderLevel"] = 10;
            newRow["Discontinued"] = 0;
            dataSet.Tables["Products"].Rows.Add(newRow);

            newRow = dataSet.Tables["Products"].NewRow();
            newRow["ProductID"] = "A002";
            newRow["ReorderLevel"] = 20;
            newRow["Discontinued"] = 0;
            dataSet.Tables["Products"].Rows.Add(newRow);

            newRow = dataSet.Tables["Products"].NewRow();
            newRow["ProductID"] = "A003";
            newRow["ReorderLevel"] = 30;
            newRow["Discontinued"] = 1;
            dataSet.Tables["Products"].Rows.Add(newRow);

            dataSet.Tables["Products"].AcceptChanges();
            dataGridView1.DataSource = dataSet.Tables["Products"];
        }
    }
}
