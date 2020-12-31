using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_CSV3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtFile.Text = Path.GetFullPath(
                Path.Combine(Application.StartupPath, "..\\..")) +
                "\\Data.csv";
            txtFile.Select(0, 0);
        }

        // Read the CSV file.
        // Assumes each line has the same number of fields
        // and no line is blank.
        private void btnGo_Click(object sender, EventArgs e)
        {
            // Get the data.
            string[,] values = LoadCsv(txtFile.Text);
            int num_rows = values.GetUpperBound(0) + 1;
            int num_cols = values.GetUpperBound(1) + 1;

            // Display the data to show we have it.

            // Make column headers.
            // For this example, we assume the first row
            // contains the column names.
            dgvValues.Columns.Clear();
            for (int c = 0; c < num_cols; c++)
                dgvValues.Columns.Add(values[0, c], values[0, c]);

            // Add the data.
            for (int r = 1; r < num_rows; r++)
            {
                dgvValues.Rows.Add();
                for (int c = 0; c < num_cols; c++)
                {
                    dgvValues.Rows[r - 1].Cells[c].Value = values[r, c];
                }
            }

            //// Make the columns autosize.
            //foreach (DataGridViewColumn col in dgvValues.Columns)
            //    col.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;
        }

        // Load a CSV file into an array of rows and columns.
        // Assume there may be blank lines but every line has
        // the same number of fields.
        private string[,] LoadCsv(string filename)
        {
            // Get the file's text.
            string whole_file = File.ReadAllText(filename);

            // Split into lines.
            whole_file = whole_file.Replace('\n', '\r');
            string[] lines = whole_file.Split(new char[] { '\r' },
                StringSplitOptions.RemoveEmptyEntries);

            // See how many rows and columns there are.
            int num_rows = lines.Length;
            int num_cols = lines[0].Split(',').Length;

            // Allocate the data array.
            string[,] values = new string[num_rows, num_cols];

            // Load the array.
            for (int r = 0; r < num_rows; r++)
            {
                string[] line_r = lines[r].Split(',');
                for (int c = 0; c < num_cols; c++)
                {
                    values[r, c] = line_r[c];
                }
            }

            // Return the values.
            return values;
        }
    }
}
    