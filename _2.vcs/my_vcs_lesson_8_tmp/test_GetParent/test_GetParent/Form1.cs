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
using System.Diagnostics;
using System.Runtime.InteropServices;


namespace test_GetParent
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class Account
        {
            public int ID { get; set; }
            public double Balance { get; set; }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            GetLogicalDrives();


        }


        // Print out all logical drives on the system.
        void GetLogicalDrives()
        {
            try
            {
                string[] drives = System.IO.Directory.GetLogicalDrives();

                foreach (string str in drives)
                {
                    System.Console.WriteLine(str);
                    richTextBox1.Text += "drive : " + str + "\n";
                }
            }
            catch (System.IO.IOException)
            {
                System.Console.WriteLine("An I/O error occurs.");
            }
            catch (System.Security.SecurityException)
            {
                System.Console.WriteLine("The caller does not have the " +
                    "required permission.");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_case1\pic1.jpg";
            FileStream fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            Byte[] image = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(image, 0, filelength); //按位元組流讀取
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();

            //pictureBox1.Image = (Image)image;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //程式所在位置
            string appPath = Application.ExecutablePath;
            richTextBox1.Text += "程式所在位置" + appPath + "\n";


            System.Net.IPHostEntry IPHost = System.Net.Dns.GetHostEntry(Environment.MachineName);
            if (IPHost.AddressList.Length > 0)
            {
                richTextBox1.Text += "電腦本機IP " + IPHost.AddressList[0].ToString() + "\n";
                //MessageBox.Show(IPHost.AddressList[0].ToString(), "電腦本機IP");
            }

            //搜尋指定字串的位置
            //使用System.Text.RegularExpressions來搜尋指定字串
            //準備要搜尋的來源字串
            string strTxt = "彩袖殷勤捧玉鍾，當筵拚卻醉顏紅。舞低楊柳樓心月，歌盡桃花扇底風。從別後，憶相逢，幾回魂夢與君同。今宵賸把銀釭照，猶恐相逢是夢中。";
            //指定字串
            string strKey = "，";
            System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(strTxt, strKey);
            foreach (System.Text.RegularExpressions.Match m in matches)
            {
                richTextBox1.Text += "找到在 " + m.Index.ToString() + "\n";

            }








        }

        private void button4_Click(object sender, EventArgs e)
        {
            for (int i = 1; i <= 10; i++)
            {
                this.Controls["label" + i.ToString()].Text = "這是label" + i.ToString();

            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合手機號碼格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[0-9]{4}-[0-9]{6}$");
            if (rex.IsMatch(txtInput.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }


        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用正則表達式判斷字串是否符合身分證格式。
            System.Text.RegularExpressions.Regex rex = new System.Text.RegularExpressions.Regex("^[A-Z]{1}[0-9]{9}$");
            if (rex.IsMatch(txtInput.Text))
            {
                MessageBox.Show("符合");
            }
            else
            {
                MessageBox.Show("不符合");
            }

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //列出所有已安裝字型
            foreach (FontFamily oneFontFamily in FontFamily.Families)
            {
                listBox1.Items.Add(oneFontFamily.Name);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            System.Globalization.CultureInfo cuinfo = new System.Globalization.CultureInfo("zh-TW");
            cuinfo.DateTimeFormat.Calendar = cuinfo.OptionalCalendars[2];
            //richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd", cuinfo) + "\n";
            MessageBox.Show(DateTime.Now.ToString("yyyy/MM/dd", cuinfo));

        }

        private void button9_Click(object sender, EventArgs e)
        {
            String strOrg = "ABCDE";
            // Encoding.GetBytes方法，將 String 轉為 Byte 序列
            byte[] stringConvByte = Encoding.Default.GetBytes(strOrg);
            // Encoding.GetString方法，將 Byte 序列 轉為 String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);

            int i;
            richTextBox1.Text += "len of strOrg = " + strOrg.Length.ToString() + "\n";
            for (i = 0; i < strOrg.Length; i++)
            {
                richTextBox1.Text += "value is " + strOrg[i] + "\n";
                richTextBox1.Text += "value is " + strOrg[i].ToString() + "\n";
                //richTextBox1.Text += "value is\n";

            }
            richTextBox1.Text += "len of stringConvByte = " + stringConvByte.Length.ToString() + "\n";
            for (i = 0; i < stringConvByte.Length; i++)
            {
                richTextBox1.Text += "value is " + stringConvByte[i].ToString("X2") + "\n";
                //richTextBox1.Text += "value is\n";

            }
            richTextBox1.Text += "len of byteConvStrig = " + byteConvStrig.Length.ToString() + "\n";


        }




        private void button10_Click(object sender, EventArgs e)
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

            // Display the list in an Excel spreadsheet.
            DisplayInExcel(bankAccounts);

        }




        static void DisplayInExcel(IEnumerable<Account> accounts)
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

            // Establish column headings in cells A1 and B1.
            workSheet.Cells[1, "A"] = "ID Number";
            workSheet.Cells[1, "B"] = "Current Balance";

            var row = 1;
            foreach (var acct in accounts)
            {
                row++;
                workSheet.Cells[row, "A"] = acct.ID;
                workSheet.Cells[row, "B"] = acct.Balance;
            }

            workSheet.Columns[1].AutoFit();
            workSheet.Columns[2].AutoFit();

            // Call to AutoFormat in Visual C#. This statement replaces the 
            // two calls to AutoFit.
            workSheet.Range["A1", "B3"].AutoFormat(
                Excel.XlRangeAutoFormat.xlRangeAutoFormatClassic2);

            // Put the spreadsheet contents on the clipboard. The Copy method has one
            // optional parameter for specifying a destination. Because no argument  
            // is sent, the destination is the Clipboard.
            workSheet.Range["A1:B3"].Copy();


            String filename = Application.StartupPath + "\\csv_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xlsx";
            workSheet.SaveAs(filename);

        }
    }
}
