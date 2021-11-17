using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridView7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the DataTable object.
            DataTable dt = new DataTable("People");

            // Add columns to the DataTable.
            dt.Columns.Add("First Name",    System.Type.GetType("System.String"));
            dt.Columns.Add("Last Name",     System.Type.GetType("System.String"));
            dt.Columns.Add("Occupation",    System.Type.GetType("System.String"));
            dt.Columns.Add("Salary",        System.Type.GetType("System.Int32"));

            // Make all columns required.
            for (int i = 0; i < dt.Columns.Count; i++)
            {
                dt.Columns[i].AllowDBNull = false;
            }

            // Make the First Name/Last Name combination require uniqueness.
            DataColumn[] unique_cols = 
            {
                dt.Columns["First Name"],
                dt.Columns["Last Name"]
            };
            dt.Constraints.Add(new UniqueConstraint(unique_cols));

            // Add items to the table.
            dt.Rows.Add(new object[] {"Rod", "Stephens", "Nerd", 10000});
            dt.Rows.Add(new object[] {"Sergio", "Aragones", "Cartoonist", 20000});
            dt.Rows.Add(new object[] {"Eoin", "Colfer", "Author", 30000});
            dt.Rows.Add(new object[] {"Terry", "Pratchett", "Author", 40000});

            // Make the DataGridView use the DataTable as its data source.
            dataGridView1.DataSource = dt;
        }

        // An error in the data occurred.
        private void dataGridView1_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            // Don't throw an exception when we're done.
            e.ThrowException = false;

            // Display an error message.
            richTextBox1.Text += "輸入資料錯誤, 欄位 : " + dataGridView1.Columns[e.ColumnIndex].HeaderText + "\t原因 : " + e.Exception.Message + "\n";

            // If this is true, then the user is trapped in this cell.
            e.Cancel = false;
        }
    }
}
