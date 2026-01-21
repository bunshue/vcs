using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileInfo
using System.Drawing.Text;  //for InstalledFontCollection, PrivateFontCollection

namespace vcs_test_all_04_Dialog
{
    public partial class Form1 : Form
    {
        FontFamily old_font_name;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            old_font_name = label1.Font.FontFamily;

            label1.Text = "春雁	王恭\n春风一夜到衡阳，楚水燕山万里长。\n莫道春来便归去，江南虽好是他乡。";
            //label1.Text = "唐 王昌齡 出塞\n秦時明月漢時關\n萬里長征人未還\n但使龍城飛將在\n不教胡馬度陰山。";
            label2.Text = "瀏覽資料夾內的字型檔";

            //顯示目前字型種類
            richTextBox1.Text += "fontname = " + label1.Font.Name + "\n";
            tb_font_size.Text = label1.Font.Size.ToString();

            //設定前景色, 使用自定義色彩
            // Use dark custom colors for the foreground dialog.
            int[] fg_colors = {
                0x808080, 0xFF0000, 0xFF8000, 0xFFFF00, 0x00FF00,
                0x00FFFF, 0x0000FF, 0xFF00FF, 0x000000, 0xC00000,
                0x804000, 0xC0C000, 0x008000, 0x00C0C0, 0x0000C0,
                0x800080 };
            colorDialog_forecolor.CustomColors = fg_colors;
            // Make the background dialog open with the custom colors displayed.
            colorDialog_forecolor.FullOpen = false;

            //設定背景色, 使用自定義色彩
            // Use light custom colors for the background dialog.
            int[] bg_colors = {
                0xFFFFFF, 0xFFC0C0, 0xFFE0C0, 0xFFFFC0, 0xC0FFC0,
                0xC0FFFF, 0xC0C0FF, 0xFFC0FF, 0xE0E0E0, 0xFF8080,
                0xFFC080, 0xFFFF80, 0x80FF80, 0x80FFFF, 0x8080FF,
                0xFF80FF
            };
            colorDialog_backcolor.CustomColors = bg_colors;
            // Make the background dialog open with the custom colors displayed.
            colorDialog_backcolor.FullOpen = true;
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

            label1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Size = new Size(400, 320);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_open_folder.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 105);
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
            bt_plus.BackgroundImage = Properties.Resources.plus;
            bt_plus.BackgroundImageLayout = ImageLayout.Zoom;
            bt_minus.BackgroundImage = Properties.Resources.minus;
            bt_minus.BackgroundImageLayout = ImageLayout.Zoom;
            label2.Location = new Point(x_st + dx * 3 + 60, y_st + dy * 1 - 80);
            comboBox1.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 40);

            bt_plus.Location = new Point(x_st + dx * 5 + 150, y_st + dy * 0);
            bt_minus.Location = new Point(x_st + dx * 5 + 150, y_st + dy * 0 + 60);
            tb_font_size.Location = new Point(x_st + dx * 5 + 150, y_st + dy * 0 + 120);

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
            //選取資料夾
            folderBrowserDialog1.SelectedPath = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
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
            saveFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\";
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

        private void button21_Click(object sender, EventArgs e)
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
            saveFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設儲存的路徑
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

        private void button22_Click(object sender, EventArgs e)
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
            {
                MessageBox.Show("OPEN FILE FAIL");
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {
            //色彩對話方塊 選擇背景色
            colorDialog1.Color = richTextBox1.BackColor;    //顏色對話框的預設顏色
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.BackColor = colorDialog1.Color;
                button30.BackColor = colorDialog1.Color;
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //設定部分背景顏色
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            colorDialog1.AnyColor = true;      			//顯示基本顏色集中可用的所有顏色
            colorDialog1.FullOpen = true;      //創建自定義顏色的控件在對話框打開時是可見的
            colorDialog1.SolidColorOnly = false;			//不限制只選擇純色
            if (colorDialog1.ShowDialog() == DialogResult.OK)   //彈出對話框
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //設定前景色/背景色

            //設定前景色, 使用自定義色彩
            colorDialog_forecolor.Color = this.ForeColor;

            if (colorDialog_forecolor.ShowDialog() == DialogResult.OK)
            {
                this.ForeColor = colorDialog_forecolor.Color;
            }

            //設定背景色, 使用自定義色彩
            colorDialog_backcolor.Color = this.BackColor;

            if (colorDialog_backcolor.ShowDialog() == DialogResult.OK)
            {
                this.BackColor = colorDialog_backcolor.Color;
                button32.BackColor = colorDialog_backcolor.Color;
            }
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
            //設定字型
            fontDialog1.AllowVerticalFonts = true;//指示對話框既顯示垂直字體又顯示水平字體
            fontDialog1.FixedPitchOnly = true; 			//只允許選擇固定間距字體
            fontDialog1.ShowApply = true;      		//包含應用按鈕
            fontDialog1.ShowEffects = true;    //允許指定刪除線、下畫線和文本顏色選項的控件
            fontDialog1.ShowColor = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = label1.Font;           //字型對話框的預設字型
            fontDialog1.Color = label1.ForeColor;     //字型對話框的預設顏色

            if (fontDialog1.ShowDialog() == DialogResult.OK)    //開啟字型對話方塊
            {
                label1.Font = fontDialog1.Font;       //以在字型對話方塊內所指定的字型來指定給label1
                label1.ForeColor = fontDialog1.Color; //以在字型對話方塊內所指定的顏色來指定給label1
                richTextBox1.Font = fontDialog1.Font;       //以在字型對話方塊內所指定的字型來指定給richTextBox1
                richTextBox1.ForeColor = fontDialog1.Color; //以在字型對話方塊內所指定的顏色來指定給richTextBox1
            }
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //設定部分字型顏色
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;
            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.SelectionFont = fontDialog1.Font;
                richTextBox1.SelectionColor = fontDialog1.Color;
                //richTextBox1.SelectionBackColor
            }
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
            //設定印表機
            printDialog1.AllowCurrentPage = true;       //顯示當前頁
            printDialog1.AllowPrintToFile = true;       //允許選擇打印到文件
            printDialog1.AllowSelection = true;         //啟用“選擇”單選按鈕
            printDialog1.AllowSomePages = true;         //啟用“頁”單選按鈕
            //printDialog1.Document = printDocument1;   //指定設置的PrintDocument對象
            //printDialog1.PrinterSettings = printDocument1.PrinterSettings;    //打印頁的默認設置
            printDialog1.PrintToFile = false;           //不選擇“打印到文件”
            printDialog1.ShowHelp = true;               //顯示“幫助”按鈕
            printDialog1.ShowNetwork = true;            //可以選擇網絡打印機
            if (printDialog1.ShowDialog() == DialogResult.OK)
            {
                //printDocument1.Print();    //打印
            }
            else
            {
            }
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

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();

            folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            //folderBrowserDialog1.SelectedPath = @"D:\_git\整理字型";
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                /*
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";
                */
                comboBox1.Items.Clear();

                //string foldername = folderBrowserDialog1.SelectedPath;
                string foldername = @"D:\_git\vcs\_1.data\______test_files1\_font";

                richTextBox1.Text += "撈出資料夾 " + foldername + " 內所有圖片檔案合併\n";

                // Get the picture files in the source directory.
                List<string> files = new List<string>();
                foreach (string filename in Directory.GetFiles(foldername))
                {
                    int pos = filename.LastIndexOf('.');
                    string extension = filename.Substring(pos).ToLower();
                    if ((extension == ".ttf") || (extension == ".ttc") || (extension == ".otf"))
                    {
                        files.Add(filename);
                        comboBox1.Items.Add(filename);
                    }
                }

                int num_images = files.Count;
                if (num_images == 0)
                {
                    richTextBox1.Text += "無字型檔\n";
                    return;
                }

                for (int i = 0; i < num_images; i++)
                {
                    richTextBox1.Text += "第 " + (i + 1).ToString() + " 個檔案\t" + files[i] + "\n";
                }
                comboBox1.SelectedIndex = 0;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "你選擇了 : " + comboBox1.SelectedItem.ToString() + "\n";
            string font_filename = comboBox1.SelectedItem.ToString();

            apply_selected_font(font_filename);
        }

        void apply_selected_font(string font_filename)
        {
            //指明使用特定字型檔

            //讀取字體文件
            PrivateFontCollection pfc = new PrivateFontCollection();
            pfc.AddFontFile(font_filename);

            //實例化字體
            Font f = new Font(pfc.Families[0], label1.Font.Size);

            //設置字體
            label1.Font = f;
            old_font_name = pfc.Families[0];
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            float old_font_size = label1.Font.Size;
            old_font_size += 4;

            //實例化字體
            Font f = new Font(old_font_name, old_font_size);

            //設置字體
            label1.Font = f;
            tb_font_size.Text = label1.Font.Size.ToString();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            float old_font_size = label1.Font.Size;
            old_font_size -= 4;
            if (old_font_size < 10)
                old_font_size = 10;

            //實例化字體
            Font f = new Font(old_font_name, old_font_size);

            //設置字體
            label1.Font = f;
            tb_font_size.Text = label1.Font.Size.ToString();
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

