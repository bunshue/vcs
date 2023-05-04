using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream

namespace vcs_SaveFileDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //saveFileDialog1
            saveFileDialog1.Title = "測試把資料寫進檔案";
            //saveFileDialog1.ShowHelp = true;
            saveFileDialog1.FileName = "";
            saveFileDialog1.Filter = "文字檔|*.*|C#文件|*.cs|所有檔|*.*";   //限定檔案格式
            //saveFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;

            //saveFileDialog1.InitialDirectory = "c:\\";
            //saveFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            saveFileDialog1.InitialDirectory = @"C:\______test_files1\";
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.FileName = "test_write_a_file.txt";
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + saveFileDialog1.FileName + "\n";
                //richTextBox1.Text += "length : " + saveFileDialog1.FileName.Length.ToString() + "\n";

                //StreamReader sr = new StreamReader(saveFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                FileStream filestream = File.Open(saveFileDialog1.FileName, FileMode.Create);
                StreamWriter str_writer = new StreamWriter(filestream);

                str_writer.WriteLine(richTextBox1.Text);
                // Dispose StreamWriter
                str_writer.Dispose();
                // Close FileStream
                filestream.Close();

                richTextBox1.Text += "儲存資料完畢111，檔案：" + saveFileDialog1.FileName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //儲存檔案對話方塊
            string save_filename;
            //開啟檔案對話方塊
            saveFileDialog1.DefaultExt = "*.txt";
            saveFileDialog1.Filter = "文字檔(*.txt)|*.txt | Word檔(*.doc)|*.doc | Excel檔(*.xls)|*.xls | 所有檔案(*.*)|*.*";   //要在對話方塊中顯示的檔篩選器
            //saveFileDialog1.Filter = "JPeg Image|*.jpg|Bitmap Image|*.bmp|Gif Image|*.gif";
            saveFileDialog1.FilterIndex = 1;                  //預設上述種類的第幾項，由1開始。
            saveFileDialog1.RestoreDirectory = true;          //控制對話方塊在關閉之前是否恢復目前的目錄
            saveFileDialog1.Title = "另存為";                 //將顯示在對話方塊標題列中的字元
            saveFileDialog1.FileName = "file_to_save.txt";    //預設儲存的檔名
            saveFileDialog1.InitialDirectory = "c:\\______test_files1";  //預設儲存的路徑
            //saveFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                save_filename = saveFileDialog1.FileName;

                //法一
                //richTextBox1.SaveFile(save_filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔

                //法二
                //StreamWriter sw = new StreamWriter(file);                                 //覆蓋舊檔
                StreamWriter sw = new StreamWriter(save_filename, true);                    //附加在檔案後面
                //StreamWriter sw = new StreamWriter(save_filename, true, Encoding.UTF8);   //設定編碼方式
                sw.Write(richTextBox1.Text);
                sw.Close();
            }
            else
            {
                MessageBox.Show("Save File FAIL");
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            SaveFileDialog sFd = new SaveFileDialog();
            sFd.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            sFd.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";     //限定檔案格式
            sFd.Title = "限定選擇純文字檔，從目前目錄開始尋找檔案";
            sFd.FileName = "SaveDataToFile.txt";     //預設檔名
            sFd.ShowDialog();
            if (sFd.FileName != "")
            {
                //MessageBox.Show("OPEN FILE OK");
                using (StreamWriter sw = File.CreateText(sFd.FileName))
                {
                    // Print Header
                    string header = "";
                    header = "AAA";
                    header += "BBB";
                    header += "CCC";
                    header += "DDD";
                    header += "EEE";
                    sw.WriteLine(header);
                    sw.Close();
                    MessageBox.Show("Save file OK, 檔名：" + sFd.FileName);
                }
            }
            else
                MessageBox.Show("OPEN FILE FAIL");


        }
    }
}
