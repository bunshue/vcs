using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D; //for SmoothingMode
using System.Runtime.InteropServices;   //for DllImport
using System.Text.RegularExpressions;
using System.Diagnostics;       //for Process

namespace vcs_MyPdfReader
{
    public partial class Form_List : Form
    {
        ListView listView1 = new ListView();
        RichTextBox richTextBox1 = new RichTextBox();

        string pdf_reader_filename = "vcs_MyPdfReader.txt";
        List<PdfFilenames> pdf_filename_data = new List<PdfFilenames>();

        string pdf_filename = string.Empty;
        string pdf_filename_short = string.Empty;
        string current_directory_pdf = Directory.GetCurrentDirectory();
        bool flag_already_use_webbrowser = false;

        int W = Screen.PrimaryScreen.WorkingArea.Width;
        int H = Screen.PrimaryScreen.WorkingArea.Height;

        int message_panel_width = 128;
        int message_panel_height = 0;

        int pdf_page = 1;
        int pdf_total_page = 0;

        public class PdfFilenames
        {
            public string filename;
            public int page;
            public PdfFilenames(string n, int p)
            {
                this.filename = n;
                this.page = p;
            }
        }

        void remove_item(List<PdfFilenames> tttt, string pattern)
        {
            int len = tttt.Count;
            int index = 0;
            for (index = 0; index < len; index++)
            {
                string name = tttt[index].filename;
                if (name == pattern)
                {
                    break;
                }
            }

            if (index < len)
                tttt.RemoveAt(index);
            //richTextBox1.Text += index.ToString() + "\n";
        }

        public Form_List()
        {
            InitializeComponent();
        }

        private void Form_List_Load(object sender, EventArgs e)
        {
            show_item_location();
            show_recent_pdf_files();
        }

        void show_item_location()
        {
            this.Size = new Size(1600, 800);
            this.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示

            listView1.Font = new Font("新細明體", 14F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(136)));
            listView1.Location = new Point(0, 0);
            listView1.Name = "listView1";
            listView1.Size = new Size(this.Size.Width - 100, 600 - 38);
            listView1.View = System.Windows.Forms.View.Details;
            listView1.KeyDown += new KeyEventHandler(listView1_KeyDown);
            listView1.MouseClick += new MouseEventHandler(listView1_MouseClick);
            listView1.MouseDoubleClick += new MouseEventHandler(listView1_MouseDoubleClick);

            listView1.GridLines = true;
            this.Controls.Add(listView1);

            //設置欄名稱
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("頁數", 50, HorizontalAlignment.Center);
            listView1.Columns.Add("總頁數", 50, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Visible = true;

            richTextBox1.Text = "";
            richTextBox1.Name = "richTextBox1";
            richTextBox1.Location = new Point(0, this.listView1.Height + 130);
            richTextBox1.Size = new Size(this.Size.Width - 100, 200);
            richTextBox1.Dock = DockStyle.Bottom;
            this.Controls.Add(richTextBox1);

            int linewidth = 5;
            Bitmap bmp;
            Graphics g;
            Pen p = new Pen(Color.Red, linewidth);
            int x_st = 0;     //icon的 位置 X
            int y_st = 0;     //icon的 位置 Y
            int width = 50; //設定按鈕大小 W
            int height = 50; //設定按鈕大小 H
            int dx = width + 2;
            int dy = height + 2;

            Font f = new Font("Arial", 12);
            SolidBrush sb = new SolidBrush(Color.Red);

            Button bt_clear = new Button();  // 實例化按鈕
            bt_clear.Size = new Size(width, height);
            bt_clear.Text = "";
            bmp = new Bitmap(width, height);
            bt_clear.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("Clear", f, sb, new PointF(4, 15));
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear.Click += bt_clear_Click;     // 加入按鈕事件
            this.Controls.Add(bt_clear); // 將按鈕加入表單
            bt_clear.BringToFront();     //移到最上層

            f = new Font("Arial", 10);
            x_st = listView1.Width + 15;
            y_st = 10 + dy * 0;
            Button bt_recent0 = new Button();  // 實例化按鈕
            bt_recent0.Size = new Size(width, height);
            bt_recent0.Text = "";
            bmp = new Bitmap(width, height);
            bt_recent0.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("開啟\n檔案", f, sb, new PointF(8, 12));
            bt_recent0.Location = new Point(x_st, y_st);
            bt_recent0.Click += bt_recent0_Click;     // 加入按鈕事件
            this.Controls.Add(bt_recent0); // 將按鈕加入表單
            bt_recent0.BringToFront();     //移到最上層

            f = new Font("Arial", 9);
            x_st = listView1.Width + 15;
            y_st = 10 + dy * 1;
            Button bt_recent1 = new Button();  // 實例化按鈕
            bt_recent1.Size = new Size(width, height);
            bt_recent1.Text = "";
            bmp = new Bitmap(width, height);
            bt_recent1.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("  開啟\n資料夾", f, sb, new PointF(4, 12));
            bt_recent1.Location = new Point(x_st, y_st);
            bt_recent1.Click += bt_recent1_Click;     // 加入按鈕事件
            this.Controls.Add(bt_recent1); // 將按鈕加入表單
            bt_recent1.BringToFront();     //移到最上層

            f = new Font("Arial", 10);
            x_st = listView1.Width + 15;
            y_st = 10 + dy * 2;
            Button bt_recent2 = new Button();  // 實例化按鈕
            bt_recent2.Size = new Size(width, height);
            bt_recent2.Text = "";
            bmp = new Bitmap(width, height);
            bt_recent2.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("清除", f, sb, new PointF(8, 20));
            bt_recent2.Location = new Point(x_st, y_st);
            bt_recent2.Click += bt_recent2_Click;     // 加入按鈕事件
            this.Controls.Add(bt_recent2); // 將按鈕加入表單
            bt_recent2.BringToFront();     //移到最上層

            x_st = listView1.Width + 15;
            y_st = 10 + dy * 3;
            Button bt_recent3 = new Button();  // 實例化按鈕
            bt_recent3.Size = new Size(width, height);
            bt_recent3.Text = "";
            bmp = new Bitmap(width, height);
            bt_recent3.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("清除\n無效", f, sb, new PointF(8, 12));
            bt_recent3.Location = new Point(x_st, y_st);
            bt_recent3.Click += bt_recent3_Click;     // 加入按鈕事件
            this.Controls.Add(bt_recent3); // 將按鈕加入表單
            bt_recent3.BringToFront();     //移到最上層

            x_st = listView1.Width + 15;
            y_st = 10 + dy * 4;
            Button bt_recent4 = new Button();  // 實例化按鈕
            bt_recent4.Size = new Size(width, height);
            bt_recent4.Text = "";
            bmp = new Bitmap(width, height);
            bt_recent4.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("清除\n全部", f, sb, new PointF(8, 12));
            bt_recent4.Location = new Point(x_st, y_st);
            bt_recent4.Click += bt_recent4_Click;     // 加入按鈕事件
            this.Controls.Add(bt_recent4); // 將按鈕加入表單
            bt_recent4.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //[操作pdf文檔]之C#判斷pdf文檔的頁數：
        /// <summary>
        /// 擷取pdf文檔的頁數
        /// </summary>
        /// <param name="filePath"></param>
        /// <returns>-1表示檔案不存在</returns>
        public static int GetPDFofPageCount(string filePath)
        {
            int count = -1;//-1表示檔案不存在
            if (File.Exists(filePath))
            {
                using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read))
                {
                    StreamReader reader = new StreamReader(fs);
                    //從流的目前位置到末尾讀取流
                    string pdfText = reader.ReadToEnd();
                    //richTextBox1.Text += pdfText + "\n";
                    Regex rgx = new Regex(@"/Type\s*/Page[^s]");
                    MatchCollection matches = rgx.Matches(pdfText);
                    count = matches.Count;
                }
            }
            return count;
        }

        private void bt_recent0_Click(object sender, EventArgs e)
        {
            open_listview_pdf_file();
        }

        private void bt_recent1_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 0)
            {
                richTextBox1.Text += "未選取檔案\n";
                return;
            }

            int selNdx;
            string foldername = string.Empty;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目

            /*
            richTextBox1.Text += "1你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
            richTextBox1.Text += "2你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox1.Text += "3你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox1.Text += "4你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            richTextBox1.Text += "5你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[4].Text + "\n";
            */

            foldername = listView1.Items[selNdx].SubItems[4].Text;
            richTextBox1.Text += "資料夾:\t" + foldername + "\n";

            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾 : " + foldername + ", 不存在\n";
            }
            else
            {
                //開啟檔案總管
                Process.Start(foldername);
            }
        }

        private void bt_recent2_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 0)
            {
                richTextBox1.Text += "未選取檔案\n";
                return;
            }

            int len = listView1.SelectedItems.Count;
            richTextBox1.Text += "你選擇了 " + len.ToString() + " 個檔案, 依序是 :\n";

            int i;
            for (i = 0; i < len; i++)
            {
                int selNdx;
                string full_filename = string.Empty;

                //listView1.SelectedItems[i].Remove();    //刪除之 但有問題

                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目

                /*
                richTextBox1.Text += "1你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
                richTextBox1.Text += "2你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
                richTextBox1.Text += "3你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                richTextBox1.Text += "4你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                richTextBox1.Text += "5你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[4].Text + "\n";
                */

                full_filename = listView1.Items[selNdx].SubItems[4].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                richTextBox1.Text += full_filename + "\n";

                if (File.Exists(full_filename) == false)   //確認檔案是否存在
                {
                    richTextBox1.Text += "檔案 : " + full_filename + ", 不存在\n";
                }
                else
                {
                    richTextBox1.Text += "檔案 : " + full_filename + ", 存在\n";
                    richTextBox1.Text += "刪除之\n";


                    remove_item(pdf_filename_data, full_filename);

                    //richTextBox1.Text += "顯示結果\n";
                    //show_pdf_filename_data();

                }
            }
        }

        private void bt_recent3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 bt_recent3 清除無效\n";
        }

        private void bt_recent4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 bt_recent4 清除全部\n";

            pdf_filename_data = new List<PdfFilenames>();

            show_recent_pdf_files();

            listView1.Clear();

            //存檔 移除檔案紀錄
            if (File.Exists(pdf_reader_filename) == true)
            {
                File.Delete(pdf_reader_filename);
            }
        }

        void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox1.Text += "KeyDown ";
        }

        void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "MouseClick ";
        }

        void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            open_listview_pdf_file();
        }

        void open_listview_pdf_file()
        {
            if (listView1.SelectedItems.Count == 0)
            {
                richTextBox1.Text += "未選取檔案\n";
                return;
            }

            int selNdx;
            string full_filename = string.Empty;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目

            /*
            richTextBox1.Text += "1你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
            richTextBox1.Text += "2你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox1.Text += "3你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox1.Text += "4你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            richTextBox1.Text += "5你選擇了檔名 :\t" + listView1.Items[selNdx].SubItems[4].Text + "\n";
            */

            full_filename = listView1.Items[selNdx].SubItems[4].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
            richTextBox1.Text += full_filename + "\n";

            if (File.Exists(full_filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案 : " + full_filename + ", 不存在\n";
            }
            else
            {
                Form1 f1 = (Form1)this.Owner;
                f1.SetupForm1Data = full_filename;
                f1.setForm1Value();
                this.DialogResult = DialogResult.Ignore;
            }
        }

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

        void show_pdf_filename_data()
        {
            richTextBox1.Text += "顯示pdf_filename_data資料\n";
            int len = pdf_filename_data.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 個項目\n";

            int i = 0;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + " : " + pdf_filename_data[i].filename + "\t" + pdf_filename_data[i].page.ToString() + "\n";
            }
        }

        void show_recent_pdf_files()
        {
            //從檔案讀出資料
            int i = 0;
            if (File.Exists(pdf_reader_filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "記錄檔不存在\n";
            }
            else
            {
                richTextBox1.Text += "讀取檔案\n";

                pdf_filename_data = new List<PdfFilenames>();

                using (TextReader reader = new StreamReader(pdf_reader_filename, Encoding.Default))
                {
                    i = 0;
                    string line;
                    line = reader.ReadLine();
                    while (line != null)
                    {
                        i++;
                        richTextBox1.Text += "i = " + i.ToString() + "\t" + line + "\n";

                        string[] strArray = line.Split(',');

                        string name = strArray[0];
                        int page = int.Parse(strArray[1]);

                        pdf_filename_data.Add(new PdfFilenames(name, page));

                        line = reader.ReadLine();
                    }
                }
            }

            int len = pdf_filename_data.Count;
            if (len == 0)
            {
                richTextBox1.Text += "無資料\n";
            }
            else
            {
                richTextBox1.Text += "找到 " + len.ToString() + " 筆資料a\n";
            }
            pdf_filename_data.Reverse();

            listView1.Clear();

            //設置欄名稱
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("頁數", 80, HorizontalAlignment.Center);
            listView1.Columns.Add("總頁數", 80, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);

            richTextBox1.Text += "共有 " + len.ToString() + " 個項目\n";

            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += pdf_filename_data[i].filename + "\n";

                string filename = pdf_filename_data[i].filename;
                int page = pdf_filename_data[i].page;
                richTextBox1.Text += filename + "\n";
                try
                {
                    AddItemsToListView(filename, page);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息e04 : " + ex.Message + "\n";
                }
            }
        }

        void AddItemsToListView(string filename, int page)
        {
            string short_filename = "";
            string long_foldername = "";
            string file_size = "";
            string file_last_write_time = "";

            FileInfo fi = new FileInfo(filename);
            short_filename = fi.Name;

            if (File.Exists(filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案 : " + filename + ", 不存在\n";
            }
            else
            {
                richTextBox1.Text += "名稱 : " + fi.Name + "\n";
                richTextBox1.Text += "大小 : " + fi.Length + "\n";
                richTextBox1.Text += "資料夾 : " + fi.Directory + "\n";
                richTextBox1.Text += "修改日期 : " + fi.LastWriteTime + "\n";

                long_foldername = fi.Directory.ToString();
                file_size = ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length));
                file_last_write_time = "";
            }

            ListViewItem i1 = new ListViewItem(short_filename);

            i1.UseItemStyleForSubItems = false;

            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();
            ListViewItem.ListViewSubItem sub_i1d = new ListViewItem.ListViewSubItem();

            int total_page = GetPDFofPageCount(filename);
            sub_i1a.Text = page.ToString();
            i1.SubItems.Add(sub_i1a);
            sub_i1b.Text = total_page.ToString();
            i1.SubItems.Add(sub_i1b);
            sub_i1c.Text = file_size;
            i1.SubItems.Add(sub_i1c);
            sub_i1d.Text = long_foldername;
            i1.SubItems.Add(sub_i1d);

            sub_i1a.ForeColor = Color.Blue;
            sub_i1b.ForeColor = Color.Blue;
            sub_i1c.ForeColor = Color.Blue;
            sub_i1d.ForeColor = Color.Blue;
            sub_i1a.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1b.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1c.Font = new Font("Times New Roman", 12, FontStyle.Bold);
            sub_i1d.Font = new Font("Times New Roman", 12, FontStyle.Bold);

            listView1.Items.Add(i1);
            //設置ListView最後一行可見
            //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
        }
    }
}
