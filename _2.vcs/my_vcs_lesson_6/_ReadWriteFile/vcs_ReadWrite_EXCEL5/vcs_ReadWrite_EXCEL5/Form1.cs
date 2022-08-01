using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using Excel = Microsoft.Office.Interop.Excel;
//using System.Diagnostics;
//using System.Runtime.InteropServices;

/*
加入必要的 using 指示詞
using Excel = Microsoft.Office.Interop.Excel;

順序
1. 加入以上using
2. 參考/加入參考/COM/Microsoft Office 12.0 Object Library
                     Microsoft Excel 12.0 Object Library


參考/加入參考/COM/Microsoft Excel 12.0 Object Library (用此即可)
*/

namespace vcs_ReadWrite_EXCEL5
{
    public partial class Form1 : Form
    {
        public class Account
        {
            public int ID { get; set; }
            public double Balance { get; set; }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //System.Diagnostics.Debug.WriteLine("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

            // Create a list of accounts.
            var bankAccounts = new List<Account> 
            {
                new Account { 
                              ID = 345678,
                              Balance = 541.27
                            },
                new Account {
                              ID = 1230221,
                              Balance = -127.44
                            }
            };

            // Display the list in an Excel spreadsheet.    電子表格程序
            DisplayInExcel(bankAccounts);



        }

        void DisplayInExcel(IEnumerable<Account> accounts)
        {
            var excelApp = new Excel.Application();
            // Make the object visible.
            excelApp.Visible = true;

            // Create a new, empty workbook and add it to the collection returned 
            // by property Workbooks. The new workbook becomes the active workbook.
            // Add has an optional parameter for specifying a praticular template. 
            // Because no argument is sent in this example, Add creates a new workbook. 
            excelApp.Workbooks.Add();

            // This example uses a single workSheet. 
            Excel._Worksheet workSheet = excelApp.ActiveSheet;

            // Earlier versions of C# require explicit casting.
            //Excel._Worksheet workSheet = (Excel.Worksheet)excelApp.ActiveSheet;

            //設定標題
            // Establish column headings in cells A1 and B1.
            workSheet.Cells[1, "A"] = "ID Number";
            workSheet.Cells[1, "B"] = "Current Balance";

            //加入資料
            var row = 1;
            foreach (var acct in accounts)
            {
                row++;
                workSheet.Cells[row, "A"] = acct.ID;
                workSheet.Cells[row, "B"] = acct.Balance;
            }

            //在 DisplayInExcel 結尾加入下列程式碼，以調整資料行寬度以容納內容。
            workSheet.Columns[1].AutoFit();
            workSheet.Columns[2].AutoFit();

            //加入表格的其他格式
            // Call to AutoFormat in Visual C#. This statement replaces the 
            // two calls to AutoFit.
            // Call to AutoFormat in Visual C# 2010.
            workSheet.Range["A1", "B3"].AutoFormat(Excel.XlRangeAutoFormat.xlRangeAutoFormatClassic2);

            //Copy 方法會將工作表加入剪貼簿
            // Put the spreadsheet contents on the clipboard. The Copy method has one
            // optional parameter for specifying a destination. Because no argument  
            // is sent, the destination is the Clipboard.
            workSheet.Range["A1:B3"].Copy();

            string filename = Application.StartupPath + "\\excel_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xlsx";
            workSheet.SaveAs(filename);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }



    }
}
