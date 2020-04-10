using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Excel = Microsoft.Office.Interop.Excel;

/*
參考/加入參考/COM/Microsoft Excel 12.0 Object Library

加入必要的 using 指示詞
using Excel = Microsoft.Office.Interop.Excel;
*/


namespace vcs_ReadWrite_EXCEL4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        class AnimalData
        {
            public string Name_C { get; set; }
            public string Name_E { get; set; }
            public string Name_N { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public DateTime Birthday { get; set; }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //二維陣列
            AnimalData[] AnimalDataArray = new AnimalData[]{
            new AnimalData { Name_C = "鼠", Name_E = "mouse", Name_N = "Mickey", Age= 20 , Weight = 5, Birthday = DateTime.Parse("1928/11/18") },
            new AnimalData { Name_C = "牛", Name_E = "bull", Name_N = "Benny", Age= 30 , Weight = 82, Birthday = DateTime.Parse("2000/8/14") },
            new AnimalData { Name_C = "虎", Name_E = "tiger", Name_N = "Eric", Age= 15 , Weight = 55, Birthday = DateTime.Parse("1993/12/13") },
            new AnimalData { Name_C = "兔", Name_E = "rabbit", Name_N = "Cony", Age= 22 , Weight = 12, Birthday = DateTime.Parse("2013/4/17") }
            };

            Excel.Application xlsApp = new Excel.Application();
            Excel.Workbook xlsWookBook;
            Excel.Worksheet xlsWookSheet;
            object misValue = System.Reflection.Missing.Value;
            xlsWookBook = xlsApp.Workbooks.Add(misValue);
            xlsWookSheet = (Excel.Worksheet)xlsWookBook.Worksheets.get_Item(1);
            xlsApp.Visible = true;

            richTextBox1.Text += "data:\n";

            richTextBox1.Text += "len = " + AnimalDataArray.Length.ToString() + "\n";

            int i;
            int j;
            for (i = 0; i < AnimalDataArray.Length; i++)
            {
                richTextBox1.Text += AnimalDataArray[i].Name_C + "\t" + AnimalDataArray[i].Name_E + "\t" + AnimalDataArray[i].Name_N + "\t"
                    + AnimalDataArray[i].Age.ToString() + "\t" + AnimalDataArray[i].Weight.ToString() + "\t" + AnimalDataArray[i].Birthday + "\n";

                j = 0; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Name_C;
                j = 1; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Name_E;
                j = 2; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Name_N;
                j = 3; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Age;
                j = 4; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Weight;
                j = 5; xlsWookSheet.Cells[i + 1, j + 1] = AnimalDataArray[i].Birthday;
            }

            /*
            for (int i = 0; i <= dgv.Rows.Count - 1; i++)
            {
                for (int j = 0; j < dgv.Columns.Count; j++)
                {
                    DataGridViewCell dgvCell = dgv[j, i];
                    richTextBox1.Text += dgvCell.Value + "\t";
                    xlsWookSheet.Cells[i + 1, j + 1] = dgvCell.Value;
                }
                richTextBox1.Text += "\n";
            }
            */

            String filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";

            xlsWookBook.SaveAs(filename, Excel.XlFileFormat.xlWorkbookNormal, misValue, misValue, misValue, misValue, Excel.XlSaveAsAccessMode.xlExclusive, misValue, misValue, misValue, misValue, misValue);
            xlsWookBook.Close(true, misValue, misValue);
            xlsApp.Quit();
            xlsWookSheet = null;
            xlsWookBook = null;
            xlsApp = null;


            richTextBox1.Text += "存檔檔名: " + filename + "\n";




        }
    }
}
