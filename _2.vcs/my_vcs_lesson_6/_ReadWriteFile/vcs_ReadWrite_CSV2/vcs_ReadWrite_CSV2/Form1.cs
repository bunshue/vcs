using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Excel = Microsoft.Office.Interop.Excel;

// Data from https://covidtracking.com/api

namespace vcs_ReadWrite_CSV2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        object[,] csv_data;

        private int colDate = 1;
        private int colState = 2;
        private int colPositive = 3;
        private int colNegative = 4;
        private int colPending = 5;
        private int colHospitalizedNow = 6;
        private int colHospitalizedTotal = 7;
        private int colIcuNow = 8;
        private int colIcuTotal = 9;
        private int colVentNow = 10;
        private int colVentTotal = 11;
        private int colRecovered = 12;
        private int colDeaths = 17;
        private int colPositiveIncrease = 25;
        private int colHospitalizedIncrease = 24;
        private int colDeathsIncrease = 23;

        private void FindColumns(object[,] fields)
        {
            colDate = FindColumn(fields, "date");
            colState = FindColumn(fields, "state");
            colPositive = FindColumn(fields, "positive");
            colNegative = FindColumn(fields, "negative");
            colPending = FindColumn(fields, "pending");
            colHospitalizedNow = FindColumn(fields, "hospitalizedCurrently");
            colHospitalizedTotal = FindColumn(fields, "hospitalizedCumulative");
            colIcuNow = FindColumn(fields, "inIcuCurrently");
            colIcuTotal = FindColumn(fields, "inIcuCumulative");
            colVentNow = FindColumn(fields, "onVentilatorCurrently");
            colVentTotal = FindColumn(fields, "onVentilatorCumulative");
            colRecovered = FindColumn(fields, "recovered");
            colDeaths = FindColumn(fields, "death");
            colPositiveIncrease = FindColumn(fields, "positiveIncrease");
            colHospitalizedIncrease = FindColumn(fields, "hospitalizedIncrease");
            colDeathsIncrease = FindColumn(fields, "deathIncrease");
        }

        // See which column contains the indicated column header.
        private int FindColumn(object[,] fields, string header)
        {
            for (int i = fields.GetLowerBound(1); i <= fields.GetUpperBound(1); i++)
            {
                if (fields[1, i].ToString().ToLower() == header.ToLower())
                    return i;
            }
            throw new Exception("Cannot find column " + header);
        }

        private object[,] LoadData(string filename)
        {
            // Read the file.
            object[,] fields = LoadCsv(filename);
            return fields;
        }

        // Return a value from the CSV file.
        private int ParseValue(object value)
        {
            if (value == null) return 0;
 
            int result;
            if (int.TryParse(value.ToString(), out result))
                return result;
            return 0;
        }

        // Load a CSV file into a 1-based array.
        private object[,] LoadCsv(string filename)
        {
            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            //excel_app.Visible = true;

            // Open the workbook read-only.
            //filename = Application.StartupPath + "\\" + filename;
            Excel.Workbook workbook = excel_app.Workbooks.Open(
                filename,
                Type.Missing, true, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Get the used range.
            Excel.Range used_range = sheet.UsedRange;
    
            // Get the sheet's values.
            object[,] values = (object[,])used_range.Value2;

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            return values;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_csv\vcs_ReadWrite_CSV_state_data.csv";

            //filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_csv\vcs_ReadWrite_CSV_���Z��.csv";

            richTextBox1.Text += "filename = " + filename + "\n";

            csv_data = LoadData(filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ShowData(csv_data);
        }

        void ShowData(object[,] fields)
        {
            if (fields == null)
            {
                richTextBox1.Text += "�L���\n";
                return;
            }
            else
                richTextBox1.Text += "���OK\n";

            int i;
            int j;
            int column_st = fields.GetLowerBound(1);
            int column_sp = fields.GetUpperBound(1);
            int num_column = column_sp - column_st + 1;
            int num_row = fields.GetUpperBound(0);

            richTextBox1.Text += "�@�� " + num_column.ToString() + " ��(column)���\n";
            richTextBox1.Text += "�@�� " + num_row.ToString() + " �C(row)���\n";

            for (i = fields.GetLowerBound(1); i <= fields.GetUpperBound(1); i++)
            {
                richTextBox1.Text += "�Ĥ@�C �� " + i.ToString() + " �� : " + fields[1, i].ToString() + "\n";
            }

            if (num_row > 10)
                num_row = 10;
            for (i = 1; i <= num_row; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (j = column_st; j <= column_sp; j++)
                {
                    if (fields[i, j] == null)
                        richTextBox1.Text += "N.A.";
                    else
                        richTextBox1.Text += fields[i, j].ToString();
                    if (j < column_sp)
                        richTextBox1.Text += "\t";
                }
                richTextBox1.Text += "\n";
            }
            //FindColumns(fields);



        }
    }
}
