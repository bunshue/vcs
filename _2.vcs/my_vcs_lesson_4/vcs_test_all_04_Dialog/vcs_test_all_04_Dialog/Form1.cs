using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileInfo

namespace vcs_test_all_04_Dialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int W = 170;
            int H = 320;

            x_st = 20;
            y_st = 20;
            dx = W + 20;
            dy = H + 20;

            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            groupBox0.Font = new Font("Arial", 11);
            groupBox1.Font = new Font("Arial", 11);
            groupBox2.Font = new Font("Arial", 11);
            groupBox3.Font = new Font("Arial", 11);
            groupBox4.Font = new Font("Arial", 11);
            groupBox5.Font = new Font("Arial", 11);                 

            richTextBox1.Size = new Size(400, 660);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 150 + 10;
            dy = 50 + 10;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button04.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button53.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button54.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            this.Size = new Size(1210, 740);
            this.Text = "vcs_test_all_04_Dialog";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button00_Click(object sender, EventArgs e)
        {
        }

        private void button01_Click(object sender, EventArgs e)
        {
        }

        private void button02_Click(object sender, EventArgs e)
        {
        }

        private void button03_Click(object sender, EventArgs e)
        {

        }

        private void button04_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                try
                {
                    richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
                }
                catch (System.IO.FileNotFoundException)
                {
                    MessageBox.Show("找不到檔案");
                }
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n";
                richTextBox1.Text += "已選取檔案: \n";
                foreach (string strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "\t" + strFilename + "\n";
                }
                richTextBox1.Text += "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

        }

        private void button13_Click(object sender, EventArgs e)
        {
            string open_filename = string.Empty;
            //開啟檔案對話方塊
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.Title = "開啟";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                open_filename = openFileDialog1.FileName;
                try
                {
                    richTextBox1.LoadFile(open_filename, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
                }
                catch (System.IO.FileNotFoundException)
                {
                    MessageBox.Show("找不到檔案");
                }
            }
            else
            {
                MessageBox.Show("Open File FAIL");
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        private void button50_Click(object sender, EventArgs e)
        {

        }

        private void button51_Click(object sender, EventArgs e)
        {

        }

        private void button52_Click(object sender, EventArgs e)
        {

        }

        private void button53_Click(object sender, EventArgs e)
        {

        }

        private void button54_Click(object sender, EventArgs e)
        {

        }
    }
}




/*

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "文字檔|*.*|C#文件|*.cs|所有檔|*.*";   //限定檔案格式
            openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }


另外

            OpenFileDialog P_OpenFileDialog = new OpenFileDialog();
            if (P_OpenFileDialog.ShowDialog() == DialogResult.OK)
            {
                filename = P_OpenFileDialog.FileName;
                FileStream fs = File.Open(filename, FileMode.Open);
                StreamReader sr = new StreamReader(fs);
                try
                {
                    // Read File text
                    for (int ii = 0; ii < 5; ii++)
                    {
                        context = sr.ReadLine();
                        richTextBox1.Text += "Line " + ii.ToString() + ", context : " + context + "\n";

                        string[] strArray = context.Split('\t');
                        for (int i = 0; i < strArray.Length; i++)
                        {
                            richTextBox1.Text += strArray[i] + "\n";
                        }
                    }

                    //this.Disp_Message("開啟檔案 : " + filename, 0);
                    //this.Disp_Message("讀取檔案成功 !!", 1);
                    MessageBox.Show("Open File : " + filename);
                    MessageBox.Show("Read File Successfully !!");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                    //this.Disp_Message("開啟檔案 : " + filename, 0);
                    //this.Disp_Message("讀取檔案失敗 !!", 2);
                    MessageBox.Show("Open File : " + filename);
                    MessageBox.Show("Read File Fail !!");
                }
                sr.Dispose();
                fs.Close();
            }


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



openFileDialog1.Filter = "點陣圖 (*.bmp)|*.bmp|JPEG (*.JPG)|*.JPG|" + "GIF(*.GIF)|*.GIF|All File (*.*)|*.*";

saveFileDialog1.Filter = "點陣圖 (*.bmp)|*.bmp|JPEG (*.JPG)|*.JPG|" + "GIF(*.GIF)| *. GIF|All File (*.*)|*.*";





richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



*/

