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
        int flag_search_vcs_pattern = 0;

        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        string text_editor_path = String.Empty;
        string python_editor_path = String.Empty;
        string search_path = @"D:\_git\vcs\_2.vcs";
        string default_vcs_path = @"D:\_git\vcs\_2.vcs";
        string default_python_path = @"D:\_git\vcs\_4.python";

        private const int SEARCH_MODE_VCS = 0x00;	    //search vcs code, 搜尋vcs內的關鍵字
        private const int SEARCH_MODE_PYTHON = 0x01;	//search python code, 搜尋python內的關鍵字

        string result_str = string.Empty;

        int search_mode = SEARCH_MODE_VCS;

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

            tb_search.Size = new Size(160, 60);
            tb_search.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            bt_search_pattern_vcs.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_setup.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            lb_search_result1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 10);
            lb_search_result2.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 10 + 45);
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

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox2.Right + 10, richTextBox2.Bottom + 10);

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
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
                //bt_start_files_Click(sender, e); 播放
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
            FileInfo fi = new FileInfo(filename);

            //在這裡做處理檔案的事情
            get_fileinfo(fi);
        }

        private void bt_search_pattern_vcs_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_VCS);
            return;

            do_search_mode(SEARCH_MODE_PYTHON);
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

                path = default_vcs_path;
            }
            else if (mode == SEARCH_MODE_PYTHON)
            {
                search_mode = SEARCH_MODE_PYTHON;
                richTextBox1.Text += "python\t";
                result_str += "python\t";

                path = default_python_path;
            }
            else
            {
                //其他搜尋模式
            }
            richTextBox1.Text += tb_search.Text + "\n";
            result_str += tb_search.Text + "\n";

            Application.DoEvents();

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

        }

        private void bt_copy_rtb_data_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox2.Text + "\n");      //建議用此
            richTextBox2.Text += "已複製資料到系統剪貼簿\n";
        }

        //------------------------------------------------------------  # 60個

        //檢查空資料夾 ST

        //------------------------------------------------------------  # 60個

        private void tb_search_Click(object sender, EventArgs e)
        {
            tb_search.SelectAll();
        }

        //------------------------------------------------------------  # 60個

        private void bt_clear3_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void get_fileinfo(FileInfo fi)
        {
            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
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
        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
