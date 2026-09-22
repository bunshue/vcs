using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                        //for FileAccess, File
using System.Diagnostics;               //for Process
using System.Runtime.InteropServices;   //for DllImport
using System.Globalization; //for CultureInfo

using MediaInfoNET;

/*
SendTo位置
Kilo
C:\Users\david\AppData\Roaming\Microsoft\Windows\SendTo
Sugar
C:\Users\070601\AppData\Roaming\Microsoft\Windows\SendTo
Tango
C:\Users\bunsh\AppData\Roaming\Microsoft\Windows\SendTo
*/

namespace vcs_SendTo_All
{
    public partial class Form1 : Form
    {
        int flag_operation_mode = MODE4;

        bool flag_debug_mode = true;  //debug模式

        private const int MODE0 = 0x00;   //顯示檔案名稱
        private const int MODE1 = 0x01;   //檢視檔案內容
        private const int MODE2 = 0x02;   //簡中轉正中
        private const int MODE3 = 0x03;   //計算檔案之MD5值
        private const int MODE4 = 0x04;   // reserved
        private const int MODE5 = 0x05;   //grep 多層
        private const int MODE6 = 0x06;   //轉出檔案目錄資料 目錄下檔名轉出純文字 右鍵匯出資料夾內的檔案資料

        string open_folder_directory = Application.StartupPath;

        ListView listView1 = new ListView();

        bool flag_show_big_files_only = false;  //false : 顯示所有檔案, true : 僅顯示大檔
        long file_size_limit = 0;   //檔案界限
        bool flag_show_file_path = true;  //false : 不顯示檔名, true : 顯示檔名
        int flag_search_mode = 0;  // 0 : 多層, 1 : 一層, 2 : 僅檔案

        Int64 total_size = 0;
        Int64 total_files = 0;

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        //------------------------------------------------------------  # 60個

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /* debug
            string sendto_folder = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            richTextBox1.Text += "[傳送到]資料夾位置:\n" + sendto_folder + "\n";
            richTextBox1.Text += "檔案總管 右鍵 傳送到 XXX, 可用XXX開啟檔案\n\n拉一個捷徑到\n%APPDATA%\\Microsoft\\Windows\\SendTo\n或\n" + sendto_folder;
            */

            show_item_location();

            //------------------------------------------------------------  # 60個

            if (flag_operation_mode == MODE0)
            {
                this.Text = "顯示檔案名稱";
            }
            else if (flag_operation_mode == MODE1)
            {
                this.Text = "檢視檔案內容";
                flag_show_file_path = Properties.Settings.Default.show_file_path;
            }
            else if (flag_operation_mode == MODE2)
            {
                this.Text = "簡中轉正中";
                // TBD
            }
            else if (flag_operation_mode == MODE3)
            {
                this.Text = "計算檔案之MD5值";
            }
            else if (flag_operation_mode == MODE4)
            {

            }
            else if (flag_operation_mode == MODE6)
            {
                //this.Text = "右鍵匯出資料夾內的檔案資料";
                flag_show_big_files_only = Properties.Settings.Default.show_big_files_only;
                if (flag_show_big_files_only == false)
                {
                    richTextBox1.Text += "顯示所有檔案\n";
                    this.Text = "轉出檔案目錄資料 目錄下檔名轉出純文字(全部)";
                }
                else
                {
                    richTextBox1.Text += "僅顯示大檔\n";
                    this.Text = "轉出檔案目錄資料 目錄下檔名轉出純文字(僅大檔)";
                }
                //檔案界限
                file_size_limit = Properties.Settings.Default.file_size_limit * 1024 * 1024;
                richTextBox1.Text += "檔案界限 : " + Properties.Settings.Default.file_size_limit.ToString() + " MB\n\n";
            }
            else
            {
                this.Text = "未定義";
            }

            int len = System.Environment.GetCommandLineArgs().Length;
            int i;
            //richTextBox1.Text += "參數長度\t" + len.ToString() + "\t分別是:\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "第 " + i.ToString() + " 項\t" + System.Environment.GetCommandLineArgs()[i] + "\n";
            }

            List<String> filenames = new List<String>();

            for (i = 1; i < len; i++)
            {
                filenames.Add(System.Environment.GetCommandLineArgs()[i]);
            }

            filenames.Sort();  // 排序

            total_size = 0;
            total_files = 0;

            for (i = 0; i < (len - 1); i++)
            {
                string filename = filenames[i];

                if (flag_operation_mode == MODE0)
                {
                    richTextBox1.Text += filename + "\t";

                    if (System.IO.File.Exists(filename) == true)
                    {
                        FileInfo fi;

                        try
                        {   //可能會產生錯誤的程式區段
                            fi = new FileInfo(filename);
                            richTextBox1.Text += "檔案, 大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                        }
                        catch (Exception ex)
                        {   //定義產生錯誤時的例外處理程式碼
                            richTextBox1.Text += "錯誤訊息1 : " + ex.Message + "\n";
                            return;
                        }
                        finally
                        {
                            //一定會被執行的程式區段
                        }
                    }
                    else if (Directory.Exists(filename) == true)
                    {
                        richTextBox1.Text += "資料夾\n";
                    }
                    else
                    {
                        richTextBox1.Text += "XXXXXXXXXXXX\n";
                    }
                }
                else if (flag_operation_mode == MODE1)
                {
                    //必須是檔案 若是資料夾 要跳過
                    if (System.IO.File.Exists(filename) == false)            //確認檔案是否存在
                    {
                        richTextBox1.Text += "非檔案 : " + filename + "\n";
                    }
                    else
                    {
                        //檢視檔案內容
                        print_file_content(filename);
                    }
                }
                else if (flag_operation_mode == MODE2)
                {
                    //簡中轉正中
                    //TBD
                    //convert_sc_to_tc(filename);
                }
                else if (flag_operation_mode == MODE6)
                {
                    //轉出檔案目錄資料 目錄下檔名轉出純文字 全部

                    //TBD
                }
            }

            if (flag_operation_mode == MODE6)
            {
            }

            if (flag_debug_mode == true)
            {
                //TBD
            }
        }

        void show_item_location()
        {
            richTextBox1.Dock = DockStyle.Fill;
            bt_copy.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0);
            bt_save.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0);
            bt_open_folder.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0 + bt_refresh.Size.Height);
            bt_refresh.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0 + bt_refresh.Size.Height * 2);
            bt_clear.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0 + bt_setup.Size.Height);
            bt_setup.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0 + bt_setup.Size.Height * 2);

            bt_open_folder.BackgroundImage = vcs_SendTo_All.Properties.Resources.folder_open;
            bt_refresh.BackgroundImage = vcs_SendTo_All.Properties.Resources.refresh;

            this.Size = new Size(660, 600);
            this.Text = "vcs_SendTo_All";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void bt_copy_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        void print_file_content(string filename)
        {
            if (flag_show_file_path == true)
            {
                richTextBox1.Text += "\n#檔案 : " + filename + "\n\n";
            }

            /*
            //二進位檔轉成文字檔
            byte[] data;
            long len;
            int i;

            //全部binary讀取
            data = System.IO.File.ReadAllBytes(filename);
            len = data.Length;

            //richTextBox1.Text += "檔案名稱 : " + filename + "\n";
            //richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";
            //print_data(data, len);

            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            return;
            */

            //純文字
            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = System.IO.File.ReadAllLines(filename, Encoding.GetEncoding("utf-8"));   //指名編碼格式

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";
            richTextBox1.Text += "print(\"------------------------------------------------------------\")  # 60個\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_save_Click(object sender, EventArgs e)
        {
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            //設定頁
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_refresh_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 refresh\n";
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            Process.Start(open_folder_directory);
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
