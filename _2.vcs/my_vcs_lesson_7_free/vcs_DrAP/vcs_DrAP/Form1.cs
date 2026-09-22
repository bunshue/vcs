using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileInfo DirectoryInfo
using System.Diagnostics;   //for Process
using System.Globalization; //for CultureInfo

using MediaInfoNET;

namespace vcs_DrAP
{
    public partial class Form1 : Form
    {
        private const int FUNCTION_NONE = 0x00;                     //無
        private const int FUNCTION_SEARCH_ALL_FILES = 0x01;         //轉出
        private const int FUNCTION_SEARCH_ONE_LAYER_FILES = 0x02;   //轉出一層
        private const int FUNCTION_FIND_SAME_FILES = 0x03;          //找同檔
        private const int FUNCTION_FIND_SAME_FILES2 = 0x04;         //找可能相同檔案
        private const int FUNCTION_SEARCH_TEXT = 0x08;  //搜尋關鍵字, vcs, python, ...
        private const int FUNCTION_TEST = 0xFF;         //測試

        /*
        private const int FILETYPE_VIDEO = 0x00;        //影片
        private const int FILETYPE_AUDIO = 0x01;        //音樂
        private const int FILETYPE_ALL = 0x02;          //全部
        private const int FILETYPE_OTHERS = 0xFF;       //其他
        */

        int flag_function = FUNCTION_NONE;

        string path = String.Empty;
        Int64 total_size = 0;
        Int64 total_files = 0;
        Int64 folder_files = 0;
        int flag_search_vcs_pattern = 0;

        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        string text_editor_path = String.Empty;
        string python_editor_path = String.Empty;
        string winmerge_path = String.Empty;
        string search_path = @"D:\_git\vcs\_2.vcs";
        string default_vcs_path = @"D:\_git\vcs\_2.vcs";
        string default_python_path = @"D:\_git\vcs\_4.python";

        private const int SEARCH_MODE_VCS = 0x00;	    //search vcs code, 搜尋vcs內的關鍵字
        private const int SEARCH_MODE_PYTHON = 0x01;	//search python code, 搜尋python內的關鍵字

        string result_str = string.Empty;

        int search_mode = SEARCH_MODE_VCS;
        bool flag_show_30_message = false;

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

        public class MyFileInfo
        {
            public string filename;
            public string filepath;
            public string fileextension;
            public long filesize;
            public DateTime filecreationtime;

            public int video_width;
            public int video_height;
            public int video_fps;
            public string video_duration;

            public MyFileInfo(string n, string p, string e, long s, DateTime c)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;
            }

            public MyFileInfo(string n, string p, string e, long s, DateTime c, int w, int h, int f, string d)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;

                this.video_width = w;
                this.video_height = h;
                this.video_fps = f;
                this.video_duration = d;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            update_default_setting();

            this.listView1.GridLines = true;
        }

        void show_item_location()
        {
            int x_st = 10;
            int y_st = 10;
            int w = 50;
            int h = 50;
            int dx = w + 5;
            int dy = h + 5;

            bt_start_files.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            bt_delete_file.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            cb_option1.Location = new Point(x_st + dx * 4, y_st + dy * 0);  // 滿30結束
            tb_search.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            bt_search_pattern_vcs.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_open_with_vcs.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            bt_open_dir2.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            bt_compare.Location = new Point(x_st + dx * 9, y_st + dy * 0);
            bt_replace.Location = new Point(x_st + dx * 9, y_st + dy * 1);

            groupbox_python.Size = new Size(112, 106);
            groupbox_python.Location = new Point(x_st + dx * 11, y_st + dy * 0);
            groupbox_result.Size = new Size(110, 106);
            groupbox_result.Location = new Point(x_st + dx * 11 + 120, y_st + dy * 0);
            bt_setup.Location = new Point(x_st + dx * 11 + 120 + 120, y_st + dy * 1);
            lb_search_result1.Location = new Point(10, 25);
            lb_search_result2.Location = new Point(10, 60);
            lb_search_result1.Text = "";
            lb_search_result2.Text = "";

            listView1.Size = new Size(1490, 490);
            listView1.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_clear3.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear3.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear3.Size.Height);

            richTextBox1.Size = new Size(930, 360);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_clear1.Width, richTextBox1.Location.Y);

            richTextBox2.Size = new Size(556, 360);
            richTextBox2.Location = new Point(x_st + dx * 17, y_st + dy * 11);

            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - bt_clear2.Width, richTextBox2.Location.Y);
            bt_copy_rtb_data.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - bt_clear2.Width, richTextBox2.Location.Y + bt_clear2.Height);

            x_st = 10;
            y_st = 15;
            dx = 100;
            dy = 22;
            bt_search_pattern_python.Size = new Size(45, 45);
            bt_search_pattern_python.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_edit_python_files.Size = new Size(45, 45);
            bt_edit_python_files.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 2);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox2.Right + 10, richTextBox2.Bottom + 10);

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);

            bt_minimize_setup();
            bt_exit_setup();
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Save();
        }

        //------------------------------------------------------------  # 60個

        void show_file_info3()
        {
            richTextBox1.Text += "show_file_info3 ST 搜尋檔案內容\n";

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("檔名3", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (fileinfos.Count == 0)
            {
                result_str += "找不到資料c\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                result_str += "找到 " + fileinfos.Count.ToString() + " 筆資料c\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = fileinfos[i].filepath;
                i1.SubItems.Add(sub_i1a);

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1b);
                sub_i1a.ForeColor = Color.Blue;
                sub_i1b.ForeColor = Color.Blue;

                sub_i1a.Font = new Font("Times New Roman", 10, FontStyle.Bold);
                sub_i1b.Font = new Font("Times New Roman", 10, FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        //------------------------------------------------------------  # 60個

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

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;
            /*
            int selNdx;
            string fullname;

            selNdx = listView1.SelectedIndices[0];

            result_str += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            result_str += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            result_str += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            result_str += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            */

            int selNdx;
            string fullname;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            result_str += "count = " + selectCount.ToString() + "\t";
            result_str += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";

            if (flag_function == FUNCTION_SEARCH_TEXT)
            {
                //搜尋字串模式
                result_str += "aaaa b1你選擇了檔名1:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
                result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
            }
            else
            {
                //轉出模式
                //result_str += "b你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                //result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
            }

            if (flag_search_vcs_pattern == 0)
            {
                FileInfo fi = new FileInfo(fullname);

                //result_str += "fullname = " + fullname + ",  ext = " + fi.Extension + "\n";

                if (fi.Extension == ".txt")
                {
                    //Process.Start(text_editor_path, fullname);
                }
                else
                {
                    result_str += "video_player_path = " + video_player_path + "\n";
                    result_str += "fullname = " + fullname + "\n";

                    if (video_player_path == String.Empty)
                    {
                        //Process.Start(fullname); //使用預設程式開啟
                    }
                    else
                    {
                        //Process.Start(video_player_path, fullname);    //指名播放程式開啟
                    }
                }
            }
            else
            {
                //Process.Start(text_editor_path, fullname);
            }
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx;
            string fullname;
            int selectCount = listView1.SelectedIndices.Count;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //result_str += "count = " + selectCount.ToString() + "\t";
            //result_str += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            //result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";

            if (flag_function == FUNCTION_SEARCH_TEXT)
            {
                //搜尋字串模式
                result_str += "aaaa b2你選擇了檔名2:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
                result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
            }
            else
            {
                //轉出模式
                //result_str += "b你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                //result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
            }

            if (flag_search_vcs_pattern == 0)
            {
                FileInfo fi = new FileInfo(fullname);

                //result_str += "fullname = " + fullname + ",  ext = " + fi.Extension + "\n";

                if (fi.Extension == ".txt")
                {
                    if (System.IO.File.Exists(text_editor_path) == true)
                    {
                        Process.Start(text_editor_path, fullname);
                    }
                }
                else if (fi.Extension == ".py")
                {
                    if (System.IO.File.Exists(python_editor_path) == true)
                    {
                        Process.Start(python_editor_path, fullname);
                    }
                }
                else
                {
                    result_str += "video_player_path = " + video_player_path + "\n";
                    result_str += "fullname = " + fullname + "\n";

                    if (video_player_path == String.Empty)
                    {
                        Process.Start(fullname); //使用預設程式開啟
                    }
                    else
                    {
                        if (System.IO.File.Exists(video_player_path) == true)
                        {
                            Process.Start(video_player_path, fullname);    //指名播放程式開啟
                        }
                    }
                }
            }
            else
            {
                //result_str += "text_editor_path = " + text_editor_path + "\t" + "fullname = " + fullname + "\n";
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, fullname);
                }
                else
                {
                    result_str += "開啟程式不存在\n";
                }
            }
        }

        private void bt_start_files_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;
            /*
            result_str += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < selectCount; i++)
            {
                result_str += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            result_str += "開啟\n";
            */

            int selNdx;
            string all_filename = string.Empty;

            if (selectCount <= 0)  //總共選擇的個數
            {
                result_str += "無檔案\n";
                return;
            }

            //result_str += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < selectCount; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //result_str += listView1.Items[selNdx].Text + "\n";

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
            }

            //指定應用程式路徑
            string target = String.Empty;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二

            if (flag_search_vcs_pattern == 0)
            {
                target = video_player_path;
            }
            else
            {
                target = text_editor_path;
            }

            if (flag_search_vcs_pattern == 0)
            {
                ProcessStartInfo pInfo = new ProcessStartInfo(target);
                pInfo.Arguments = all_filename;

                /*
                // debug mesg
                result_str += "target : " + target + "\n";
                result_str += "all_filename : " + all_filename + "\n";
                */

                if (video_player_path == String.Empty)
                {
                    all_filename = all_filename.Trim().Replace("\"", "");
                    Process.Start(all_filename); //使用預設程式開啟, 無法一次播放多個檔案
                }
                else
                {
                    Process.Start(video_player_path, all_filename);    //指名播放程式開啟
                }

                /*
                using (Process process = new Process())
                {
                    process.StartInfo = pInfo;
                    process.Start();
                }
                */
            }
            else
            {
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, all_filename);
                }
            }
        }

        private void bt_edit_python_files_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;
            /*
            result_str += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < selectCount; i++)
            {
                result_str += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            result_str += "開啟\n";
            */

            int selNdx;
            string all_filename = string.Empty;

            if (selectCount <= 0)  //總共選擇的個數
            {
                result_str += "無檔案\n";
                return;
            }

            //result_str += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < selectCount; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //result_str += listView1.Items[selNdx].Text + "\n";

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
            }

            result_str += "all_filename : " + all_filename + "\n";

            string prog = @"C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\idlelib\idle.pyw";

            if (python_editor_path == string.Empty)
            {
                python_editor_path = prog;
            }

            Process.Start(python_editor_path, all_filename);

            return;

            //指定應用程式路徑
            string target = String.Empty;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二

            if (flag_search_vcs_pattern == 0)
            {
                target = video_player_path;
            }
            else
            {
                target = text_editor_path;
            }

            if (flag_search_vcs_pattern == 0)
            {
                if (video_player_path == String.Empty)
                {
                    all_filename = all_filename.Trim().Replace("\"", "");
                    Process.Start(all_filename); //使用預設程式開啟, 無法一次播放多個檔案
                }
                else
                {
                    Process.Start(video_player_path, all_filename);    //指名播放程式開啟
                }
            }
            else
            {
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, all_filename);
                }
            }
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;

            //result_str += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.A)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    //result_str += "Ctrl + A\n";
                    //result_str += "共有項目" + listView1.Items.Count.ToString() + " 個\n";

                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //result_str += listView1.Items[i] + "\n";
                        listView1.Items[i].Selected = true;
                    }
                }
            }

            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 bt_start_files_Click
                bt_start_files_Click(sender, e);
            }

            if (e.KeyCode == Keys.F2)
            {
                result_str += "你按了F2\n";

                if (selectCount <= 0)  //總共選擇的個數
                    return;

                int selNdx = listView1.SelectedIndices[0];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += "count = " + selectCount.ToString() + "\t";
                result_str += "你選擇了" + listView1.Items[selNdx].Text + "\t內容為：\n";

                //ListViewItem t = listView1.Items[selNdx]; //相同寫法
                //richTextBox1.Text += t.Text + "\t" + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                result_str += listView1.Items[selNdx].Text + "\t" + listView1.Items[selNdx].SubItems[1].Text + "\t" + listView1.Items[selNdx].SubItems[2].Text + "\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //C# 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }

            /*
            //C# 限制textbox只能輸入數字
            if(e.KeyChar.CompareTo('0')<0 || e.KeyChar.CompareTo('9')>0) //比較輸入值的範圍是否超出數字
                e.Handled = true;// Handled 為是否鎖住輸入
            */
        }

        //------------------------------------------------------------  # 60個

        private void bt_delete_file_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;

            result_str += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";

            for (int i = 0; i < selectCount; i++)
            {
                result_str += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }

            result_str += "刪除\n";

            for (int i = selectCount - 1; i >= 0; i--)
            {
                result_str += "刪除檔案: " + listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";

                richTextBox1.Text += "目前不支援直接刪除檔案\n";
                /*  直接刪除檔案
                File.SetAttributes(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text, FileAttributes.Normal);
                File.Delete(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text);
                */
                listView1.SelectedItems[i].Remove();
            }
        }

        //------------------------------------------------------------  # 60個

        private void ProcessDirectoryS(string foldername)
        {
            //搜尋子目錄內的所有檔案   一層
            //使用 Directory.GetDirectories() 和 Directory.GetFiles()

            // 找資料夾, 一層
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            Array.Sort(dirs);  // 排序
            foreach (string dir in dirs)
            {
                // 資料夾
                ProcessDirectoryS(dir);
            }

            // 找檔案, 一層
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            Array.Sort(filenames);  // 排序
            foreach (string filename in filenames)
            {
                // 檔案
                ProcessFileS(filename);
            }
        }

        //------------------------------------------------------------  # 60個

        private void ProcessFileS(string filename)
        {
            if (cb_option1.Checked == true)
            {
                if (fileinfos.Count >= 30)
                {
                    if (flag_show_30_message == false)
                    {
                        flag_show_30_message = true;
                        richTextBox1.Text += "滿30結束\n";
                    }
                    return;
                }
            }

            FileInfo fi = new FileInfo(filename);

            //在這裡做處理檔案的事情
            get_fileinfo(fi, 1);

            //------------------------------------------------------------  # 60個

            if (cb_option1.Checked == true)
            {
                if (fileinfos.Count >= 30)
                {
                    if (flag_show_30_message == false)
                    {
                        flag_show_30_message = true;
                        richTextBox1.Text += "滿30結束\n";
                    }
                    return;
                }
            }
        }

        private void bt_search_pattern_vcs_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_VCS);
            return;
        }

        private void tb_search_KeyPress(object sender, KeyPressEventArgs e)
        {
            //改用KeyDown
            /*
            if (e.KeyChar == (Char)13)      //Enter
            {
                bt_search_pattern_vcs_Click(sender, e);
            }
            */
        }

        private void richTextBox2_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox2.SelectionStart = richTextBox2.TextLength;
            richTextBox2.ScrollToCaret();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox1.SelectionStart = richTextBox1.TextLength;
            richTextBox1.ScrollToCaret();
        }

        private void tb_search_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 bt_search_pattern_vcs_Click
                bt_search_pattern_vcs_Click(sender, e);
            }
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void ProcessFile2(string filename)
        {
            FileInfo fi = new FileInfo(filename);

            //在這裡做處理檔案的事情
            get_fileinfo(fi, 2);
        }

        private void bt_search_pattern_python_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_PYTHON);
            return;
        }

        //------------------------------------------------------------  # 60個

        void do_search_mode(int mode)
        {
            //開始計時
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            result_str = "";

            string path = string.Empty;
            richTextBox1.Clear();
            richTextBox2.Clear();
            listView1.Clear();
            flag_function = FUNCTION_SEARCH_TEXT;
            Application.DoEvents();

            richTextBox1.Text += "搜尋開始\t";
            result_str += "搜尋開始\t";
            lb_search_result1.Text = "";

            if (mode == SEARCH_MODE_VCS)
            {
                search_mode = SEARCH_MODE_VCS;
                richTextBox1.Text += "vcs\t";
                result_str += "vcs\t";

                bt_search_pattern_vcs.BackgroundImage = null;
                bt_search_pattern_vcs.BackColor = Color.Red;
                path = default_vcs_path;
            }
            else if (mode == SEARCH_MODE_PYTHON)
            {
                search_mode = SEARCH_MODE_PYTHON;
                richTextBox1.Text += "python\t";
                result_str += "python\t";

                bt_search_pattern_python.BackgroundImage = null;
                bt_search_pattern_python.BackColor = Color.Red;
                path = default_python_path;
            }
            else
            {
                //其他搜尋模式
            }
            richTextBox1.Text += tb_search.Text + "\n";
            result_str += tb_search.Text + "\n";

            bt_start_files.BackgroundImage = vcs_DrAP.Properties.Resources.ultraedit;
            Application.DoEvents();

            flag_show_30_message = false;

            if (tb_search.Text == "")
            {
                result_str += "未輸入搜尋內容\n";

                stopwatch.Stop();
                result_str += "停止計時\t";
                result_str += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
                lb_search_result2.Text = ((float)stopwatch.ElapsedMilliseconds / 1000).ToString("F2") + " 秒";
                richTextBox2.Text += result_str;
                return;
            }

            fileinfos.Clear();

            if (path == String.Empty)
                path = search_path;

            richTextBox1.Text += "搜尋資料夾: " + path + "\n\n";

            if (Directory.Exists(path) == true)
            {
                // path 是個 資料夾
                ProcessDirectoryS(path);
            }

            show_file_info3();

            flag_search_vcs_pattern = 1;
            if (mode == SEARCH_MODE_VCS)
            {
                bt_search_pattern_vcs.BackColor = SystemColors.ControlLight;
                bt_search_pattern_vcs.BackgroundImage = vcs_DrAP.Properties.Resources.vcs;
            }
            else if (mode == SEARCH_MODE_PYTHON)
            {
                bt_search_pattern_python.BackColor = SystemColors.ControlLight;
                bt_search_pattern_python.BackgroundImage = vcs_DrAP.Properties.Resources.python;
            }
            else
            {
                bt_search_pattern_vcs.BackColor = SystemColors.ControlLight;
                bt_search_pattern_vcs.BackgroundImage = vcs_DrAP.Properties.Resources.vcs;
            }
            stopwatch.Stop();
            result_str += "停止計時\t";
            result_str += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            lb_search_result2.Text = ((float)stopwatch.ElapsedMilliseconds / 1000).ToString("F2") + " 秒";
            richTextBox2.Text += result_str;
            return;
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗

            update_default_setting();
        }

        void update_default_setting()
        {
            video_player_path = Properties.Settings.Default.video_player_path;
            audio_player_path = Properties.Settings.Default.audio_player_path;
            picture_viewer_path = Properties.Settings.Default.picture_viewer_path;
            text_editor_path = Properties.Settings.Default.text_editor_path;
            python_editor_path = Properties.Settings.Default.python_editor_path;
            winmerge_path = Properties.Settings.Default.winmerge_path;

            if (System.IO.File.Exists(Properties.Settings.Default.video_player_path) == false)
            {
                result_str += "播放影片程式不存在 : " + Properties.Settings.Default.video_player_path + "\n使用Windows預設播放影片程式\n";
                video_player_path = String.Empty;
            }

            if (System.IO.File.Exists(Properties.Settings.Default.audio_player_path) == false)
            {
                result_str += "播放音樂程式不存在 : " + Properties.Settings.Default.audio_player_path + "\n使用Windows預設播放音樂程式\n";
                audio_player_path = String.Empty;
            }

            if (System.IO.File.Exists(Properties.Settings.Default.picture_viewer_path) == false)
            {
                result_str += "播放圖片程式不存在 : " + Properties.Settings.Default.picture_viewer_path + "\n使用Windows預設播放圖片程式\n";
                picture_viewer_path = String.Empty;
            }

            if (System.IO.File.Exists(Properties.Settings.Default.text_editor_path) == false)
            {
                result_str += "文字編輯程式不存在 : " + Properties.Settings.Default.text_editor_path + "\n使用Windows預設文字編輯程式\n";
                text_editor_path = String.Empty;
            }

            if (System.IO.File.Exists(Properties.Settings.Default.python_editor_path) == false)
            {
                result_str += "python編輯程式不存在 : " + Properties.Settings.Default.python_editor_path + "\n使用Windows預設文字編輯程式\n";
                python_editor_path = String.Empty;
            }

            if (System.IO.File.Exists(Properties.Settings.Default.winmerge_path) == false)
            {
                result_str += "winmerge程式不存在 : " + Properties.Settings.Default.winmerge_path + "\n使用Windows預設文字編輯程式\n";
                winmerge_path = String.Empty;
            }
        }

        private void bt_copy_rtb_data_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox2.Text + "\n");      //建議用此
            richTextBox2.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_compare_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;

            if (selectCount != 2)
            {
                richTextBox1.Text += "必須要選取2個檔案才能比較\n";
                return;
            }

            result_str += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < selectCount; i++)
            {
                result_str += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }

            int selNdx;
            string all_filename = string.Empty;

            //result_str += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < selectCount; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //result_str += listView1.Items[selNdx].Text + "\n";

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
            }

            result_str += "all_filename : " + all_filename + "\n";

            string prog = @"C:/Program Files (x86)/WinMerge/WinMergeU.exe";

            if (winmerge_path == string.Empty)
            {
                winmerge_path = prog;
            }

            Process.Start(winmerge_path, all_filename);
            return;
        }

        //------------------------------------------------------------  # 60個

        //檢查空資料夾 ST

        private void bt_replace_Click(object sender, EventArgs e)
        {
            Form_Replace frm = new Form_Replace();    //實體化 Form_Replace 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        //------------------------------------------------------------  # 60個

        private void tb_search_Click(object sender, EventArgs e)
        {
            tb_search.SelectAll();
        }

        //------------------------------------------------------------  # 60個

        private void bt_open_dir2_Click(object sender, EventArgs e)
        {
            int cnt = listView1.SelectedItems.Count;
            if (cnt > 0)
            {
                int selNdx = listView1.SelectedIndices[0];

                result_str += "aaaa b3你選擇了檔名3:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";

                string foldername = listView1.Items[selNdx].SubItems[1].Text;
                result_str += "資料夾:\t" + foldername + "\n";

                string fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                result_str += "全檔名:\t" + fullname + "\n";

                /*
                //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
                string file = @"C:\Windows\explorer.exe";
                string argument = @"/select, " + foldername;
                Process.Start(file, argument);
                */
                Process.Start(foldername);
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_open_with_vcs_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用vcs開啟\n";

            result_str = "";

            int cnt = listView1.SelectedItems.Count;
            if (cnt > 0)
            {
                int selNdx = listView1.SelectedIndices[0];

                result_str += "aaaa b3你選擇了檔名3:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";

                string foldername = listView1.Items[selNdx].SubItems[1].Text;
                result_str += "資料夾:\t" + foldername + "\n";

                string fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                result_str += "全檔名:\t" + fullname + "\n";

                richTextBox1.Text += result_str + "\n";

                //撈出資料夾內特定類型的檔案
                string searchDirectory = foldername;
                string searchPattern = "*.csproj";

                richTextBox1.Text += "撈出資料夾內特定類型的檔案\t單層\tPattern : " + searchPattern + "\n";

                List<string> filenames = new List<string>();
                string[] pattern_array = searchPattern.Split(';');

                // Search.
                System.IO.SearchOption search_option = System.IO.SearchOption.TopDirectoryOnly;
                foreach (string pattern in pattern_array)
                {
                    foreach (string filename in Directory.GetFiles(searchDirectory, pattern, search_option))
                    {
                        if (!filenames.Contains(filename))
                        {
                            filenames.Add(filename);
                        }
                    }
                }

                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "找到 : " + filename + "\n";
                    Process.Start(filename);
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_clear3_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void get_fileinfo(FileInfo fi, int type)
        {
            if (type == 1)
            {
                //result_str += fi.Name + "\t" + fi.Length.ToString() + "\n";
                bool res;
                string pattern = string.Empty;// = "Form1.cs";

                if (search_mode == SEARCH_MODE_VCS)
                    pattern = ".cs";
                else if (search_mode == SEARCH_MODE_PYTHON)
                    pattern = "py";
                else
                    pattern = ".cs";

                res = fi.FullName.ToLower().Replace(" ", "").EndsWith(pattern.ToLower());

                if (res == false)   //vcs加搜尋txt檔案
                {
                    if (search_mode == SEARCH_MODE_VCS) //vcs 加搜尋 .txt
                    {
                        res = fi.FullName.ToLower().Replace(" ", "").Contains("____txt");
                    }
                }

                if (res == true)
                {
                    //result_str += "aaaa : " + fi.FullName + "\n";

                    if (search_mode == SEARCH_MODE_VCS) //有一些vcs檔案 要跳開 (先改成小寫名)
                    {
                        if (fi.FullName.ToLower().Replace(" ", "").Contains("program.cs"))
                        {
                            res = false;
                            return;
                        }
                        /*
                        else if (fi.FullName.ToLower().Replace(" ", "").Contains("assemblyinfo.cs"))
                        {
                            res = false;
                            return;
                        }
                        */
                        else if (fi.FullName.ToLower().Replace(" ", "").Contains("csproj"))
                        {
                            res = false;
                            return;
                        }
                        /*
                        else if (fi.FullName.ToLower().Replace(" ", "").Contains("designer"))
                        {
                            res = false;
                            return;
                        }
                        */
                    }

                    //result_str += fi.FullName + "\n";
                    StreamReader sr = new StreamReader(fi.FullName, Encoding.UTF8);

                    int flag_pattern_match = 0;
                    int i = 0;
                    String line;

                    //寫法一
                    while (!sr.EndOfStream)
                    {               // 每次讀取一行，直到檔尾
                        i++;
                        line = sr.ReadLine();            // 讀取文字到 line 變數
                        res = line.ToLower().Replace(" ", "").Contains(tb_search.Text.ToLower().Replace(" ", ""));
                        if (res == true)
                        {
                            //result_str += "第" + i.ToString() + "行： " + line + "\n";
                            result_str += line + "\n";
                            flag_pattern_match = 1;
                        }
                    }
                    if (flag_pattern_match == 1)
                    {
                        result_str += "上面搜尋到的資料在檔案\t" + fi.FullName + "\n\n";
                        fileinfos.Add(new MyFileInfo(fi.Name, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
                    }
                    sr.Close();
                }
                else
                {
                    return;
                }
            }
            else if (type == 2)
            {
                total_size += fi.Length;
                total_files++;
                folder_files++;

                //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
                //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
            }
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

/*
richTextBox1.Text += "\n類型:\t\t檔案資料夾\n";
richTextBox1.Text += "位置:\t\t" + Directory.GetParent(foldername) + "\n";
richTextBox1.Text += "大小:\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "(" + total_size.ToString() + "位元組)\n";
richTextBox1.Text += "包含:\t\t" + total_files.ToString() + "個檔案，" + (total_folders - 1).ToString() + "個資料夾\n";
DirectoryInfo di = new DirectoryInfo(foldername);
richTextBox1.Text += "建立日期:\t" + di.CreationTime.ToString() + "\n\n";


        Int64 folder_size = 0;

            richTextBox1.Text += "資料夾 : " + foldername + " ";
            richTextBox1.Text += "子目錄數 : " + dirs.Length.ToString() + "\t";
            richTextBox1.Text += "檔案數 : " + folder_files.ToString() + "\t";
            richTextBox1.Text += "檔案大小總計 : " + folder_size.ToString() + "\n";
min_size_mb = 10;  // 最小值 10 MB
            if (dirs.Length == 0)
            {
                richTextBox1.Text += "資料夾 : " + foldername + " 是最底層的資料夾\n";
                if (folder_size < min_size_mb * 1024 * 1024)
                {
                    DirectoryInfo di = new DirectoryInfo(foldername);
                    //richTextBox1.Text += "建立日期:\t" + di.CreationTime.ToString() + "\n\n";
                    folderinfos.Add(new MyFolderInfo(foldername, foldername, folder_size, di.CreationTime));
                }
            }

//------------------------------------------------------------  # 60個

        public class MyFolderInfo
        {
            public string foldername;
            public string folderpath;
            public long foldersize;
            public DateTime foldercreationtime;
            public MyFolderInfo(string n, string p, long s, DateTime c)
            {
                this.foldername = n;
                this.folderpath = p;
                this.foldersize = s;
                this.foldercreationtime = c;
            }
        }

        List<MyFolderInfo> folderinfos = new List<MyFolderInfo>();
//folderinfos.Add(new MyFolderInfo(foldername, foldername, folder_size, di.CreationTime));

//------------------------------------------------------------  # 60個

            FileInfo fi = new FileInfo(path);
            fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

                result_str += "a你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;

                //result_str += "a你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                //result_str += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;

//------------------------------------------------------------  # 60個
         void show_file_info6()
        {
            richTextBox1.Text += "show_file_info6 ST 找小資料夾\n";

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("最底層資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 250, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 250, HorizontalAlignment.Left);
            listView1.Visible = true;

            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號       先不排序
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            for (int i = 0; i < folderinfos.Count; i++)
            {
                //richTextBox1.Text += "name : " + folderinfos[i].foldername + " path : " + folderinfos[i].folderpath + " size : " + folderinfos[i].filesize.ToString() + "\n";

                ListViewItem i1 = new ListViewItem(folderinfos[i].foldername);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(folderinfos[i].foldersize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = Color.Blue;
                sub_i1a.Font = new Font("Times New Roman", 10, FontStyle.Bold);

                sub_i1b.Text = folderinfos[i].foldercreationtime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

//------------------------------------------------------------  # 60個

                selNdx = listView1.SelectedIndices[0];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //result_str += "count = " + selectCount.ToString() + "\t";
                result_str += "你選擇了資料夾:\t" + listView1.Items[selNdx].Text + "\n";

                fullname = listView1.Items[selNdx].Text;

                richTextBox1.Text += "開啟路徑: " + fullname + "\n";

                // old
                //開啟檔案總管
                if (Directory.GetParent(fullname) == null)
                    Process.Start(fullname);             //若是根目錄 不要擷取其父目錄的路徑
                else
                    Process.Start(Directory.GetParent(fullname).ToString()); //GetParent 擷取其父目錄的路徑

                //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
                string file = @"C:\Windows\explorer.exe";
                string argument = @"/select, " + fullname;
                Process.Start(file, argument);

//------------------------------------------------------------  # 60個

//richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                FileInfo fi = new FileInfo(filename);
                fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
//fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length));
//------------------------------------------------------------  # 60個

        void show_file_info1()  //轉出一層
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
                listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

                result_str += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";
                lb_search_result1.Text = fileinfos.Count.ToString();

            for (int i = 0; i < fileinfos.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                ListViewItem i1;

                ListViewItem.ListViewSubItem sub_i1s = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                string item = string.Empty;
                string items = string.Empty;
                string itema = string.Empty;
                string itemb = string.Empty;
                string itemc = string.Empty;

                richTextBox1.Text += "aaaa1\n";

                    richTextBox1.Text += "aaaa2\n";
                    //debug mesg
                    //result_str += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    result_str += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                    //result_str += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = Color.Blue;
                    sub_i1b.ForeColor = Color.Blue;

                    sub_i1a.Font = new Font("Times New Roman", 10, FontStyle.Bold);
                    sub_i1b.Font = new Font("Times New Roman", 10, FontStyle.Bold);

-----
                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    result_str += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = Color.Blue;
                    sub_i1b.ForeColor = Color.Blue;

                    sub_i1a.Font = new Font("Times New Roman", 10, FontStyle.Bold);
                    sub_i1b.Font = new Font("Times New Roman", 10, FontStyle.Bold);
                }

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }

            richTextBox1.Text += result_str + "\n";
        }

//------------------------------------------------------------  # 60個

            //播放 listview 多選的檔案
int selectCount = listView1.SelectedIndices.Count;
            int selNdx;
            string all_filename = string.Empty;
            string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
            if (selectCount <= 0)  //總共選擇的個數
                return;

            int SelectedItemsCount = listView1.SelectedItems.Count;
            //richTextBox1.Text += "總共選了 : " + SelectedItemsCount.ToString() + " 個檔案，分別是 : \n";
            for (int i = 0; i < SelectedItemsCount; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
            }

//------------------------------------------------------------  # 60個

        List<String> old_search_path = new List<String>();

            // 可用foreach 取出List 裡的值
            //result_str += "\n可用foreach 取出List 裡的值\n";
            this.listBox1.Items.Clear();
            foreach (string sss in old_search_path)
            {
                richTextBox1.Text += "add " + sss + "\n";
                this.listBox1.Items.Add(sss);
            }

            //預設搜尋路徑
            string PATH = Properties.Settings.Default.search_path;
            //result_str += "PATH = " + PATH + "\n";

            string[] path = PATH.Split(';');

            foreach (string p in path)
            {
                if (p.Length > 0)
                {
                    //check existency
                    if (Directory.Exists(p) == true)
                    {
                        // path 是個 資料夾
                        //result_str += "len = " + p.Length.ToString() + "\t" + p + "\n";
                        result_str += "加入路徑 : " + p + "\n";
                        old_search_path.Add(p);       //目前只能 儲存/加入 一個路徑
                    }
                    else
                    {
                        result_str += "搜尋預設路徑不存在 : " + p + "\tskip\n";
                    }
                }
            }

//------------------------------------------------------------  # 60個

//search_path = @"D:\vcs\astro\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";
//this.listBox1.Items.Add(search_path);

            //儲存搜尋路徑
            string save_path = string.Empty;
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                save_path += listBox1.Items[i];
                if (i < (listBox1.Items.Count - 1))
                    save_path += ";";
            }
            Properties.Settings.Default.search_path = save_path;

//------------------------------------------------------------  # 60個

        void save_log_to_local_drive()
        {
            string filename = string.Empty;

            //磁碟資訊
            string hddname = string.Empty;

            result_str += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                path = listBox1.Items[i].ToString();

                //找資料夾所在的硬碟的標籤

                //richTextBox1.Text += "\n資料夾路徑" + path + "\n";

                if (System.IO.File.Exists(path) == true)
                {
                    // path 是個 檔案
                    richTextBox1.Text += "是個檔案\n";
                }
                else if (Directory.Exists(path) == true)
                {
                    // path 是個 資料夾
                    DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                    richTextBox1.Text += "Name : " + d.Name + "\n";
                    richTextBox1.Text += "FullName : " + d.FullName + "\n";
                    richTextBox1.Text += "Parent : " + d.Parent + "\n";
                    richTextBox1.Text += "Root : " + d.Root + "\n";

                    DriveInfo drive = new DriveInfo(d.Root.ToString());

                    if (drive.IsReady == true)
                    {
                        hddname = drive.VolumeLabel;
                    }
                    else
                    {
                        richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
                        hddname = "NotReady";
                    }
                }
                else
                {
                    richTextBox1.Text += "非合法路徑或檔案f\n";
                }
            }
            filename = "AP." + hddname + DateTime.Now.ToString(".yyyy.MMdd.HHmm") + ".txt";
            //不儲存磁碟資訊
            //filename = "AP." + DateTime.Now.ToString("yyyy.MMdd.HHmm") + ".txt";

            //建立一個檔案
            //StreamWriter sw = System.IO.File.CreateText(filename);
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("UTF-8"));   //指名編碼格式
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

*/

