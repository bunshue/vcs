using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridView5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Load_DataGridView_Data();
        }

        void Load_DataGridView_Data()
        {
            // Make the DataTable object.
            DataTable dt = new DataTable("People");

            // Add columns to the DataTable.
            dt.Columns.Add("First Name", System.Type.GetType("System.String"));
            dt.Columns.Add("Last Name", System.Type.GetType("System.String"));
            dt.Columns.Add("Occupation", System.Type.GetType("System.String"));
            dt.Columns.Add("Salary", System.Type.GetType("System.Int32"));

            // Make all columns required.
            for (int i = 0; i < dt.Columns.Count; i++)
            {
                dt.Columns[i].AllowDBNull = false;
            }

            // Make First Name + Last Name require uniqueness.
            DataColumn[] unique_cols = 
            {
                dt.Columns["First Name"],
                dt.Columns["Last Name"]
            };
            dt.Constraints.Add(new UniqueConstraint(unique_cols));

            // Add items to the table.
            dt.Rows.Add(new object[] { "Rod", "Stephens", "Nerd", 10000 });
            dt.Rows.Add(new object[] { "Sergio", "Aragones", "Cartoonist", 20000 });
            dt.Rows.Add(new object[] { "Eoin", "Colfer", "Author", 30000 });
            dt.Rows.Add(new object[] { "Terry", "Pratchett", "Author", 40000 });

            // Make the DataGridView use the DataTable as its data source.
            dataGridView1.DataSource = dt;
        }
    }
}
