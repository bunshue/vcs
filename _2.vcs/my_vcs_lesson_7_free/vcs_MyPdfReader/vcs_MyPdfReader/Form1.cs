using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;   //for ArrayList
using System.Drawing.Drawing2D; //for SmoothingMode
using System.Runtime.InteropServices;   //for DllImport
using System.Text.RegularExpressions;

namespace vcs_MyPdfReader
{
    public partial class Form1 : Form
    {
        private const int PDF_ZOOM_FACTOR = 130;

        ArrayList pdf_filename_ArrayListData = new ArrayList();

        string pdf_filename = string.Empty;
        string pdf_filename_short = string.Empty;
        string current_directory_pdf = Directory.GetCurrentDirectory();
        bool flag_already_use_webbrowser = false;

        int W = Screen.PrimaryScreen.WorkingArea.Width;
        int H = Screen.PrimaryScreen.WorkingArea.Height;

        int message_panel_width = 128;
        int message_panel_height = 0;

        int pdf_page = 0;
        int pdf_total_page = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        WebBrowser webBrowser1;
        TextBox tb_pdf_page = new TextBox();
        Label lb_pdf_total_page = new Label();
        RichTextBox richTextBox1 = new RichTextBox();
        Panel panel1 = new Panel();

        Timer timer_display = new Timer();

        //在控件上加ToolTip
        ToolTip tooltip = new ToolTip();


        private string form_list_data;
        public string SetupForm1Data
        {
            set
            {
                form_list_data = value;
            }
        }

        public void setForm1Value()
        {
            //this.richTextBox1.Text += "父得到信息 : " + form_list_data + "\n";
        }

        Form_List form_list = new Form_List();     //實體化Form_List視窗物件

        public Form1()
        {
            InitializeComponent();
        }

        void Init_Controls()
        {
            this.panel1.BackColor = Color.Pink;
            this.panel1.Location = new System.Drawing.Point(W - message_panel_width, 0);
            this.panel1.Size = new System.Drawing.Size(message_panel_width, message_panel_height);
            this.Controls.Add(this.panel1);

            this.richTextBox1.Location = new System.Drawing.Point(0, message_panel_height / 2);
            this.richTextBox1.Size = new System.Drawing.Size(message_panel_width, message_panel_height / 2);
            this.panel1.Controls.Add(this.richTextBox1);

            timer_display.Interval = 100;
            timer_display.Tick += new EventHandler(timer_display_Tick);

            this.panel1.Visible = true;
            this.webBrowser1 = new WebBrowser();
            this.webBrowser1.Location = new System.Drawing.Point(0, 0);
            //this.webBrowser1.Name = "webBrowser1";
            this.webBrowser1.Size = new System.Drawing.Size(W - message_panel_width, H - 50);
            //this.webBrowser1.TabIndex = 2;
            //this.webBrowser1.Visible = false;   //fail
            this.Controls.Add(this.webBrowser1);

            int w = 50;
            int h = 120;
            tb_pdf_page.Width = w;
            tb_pdf_page.Height = h / 2;
            tb_pdf_page.Font = new Font("Arial", 18);
            tb_pdf_page.Text = "5";
            //this.tb_file_l.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
            tb_pdf_page.KeyPress += new System.Windows.Forms.KeyPressEventHandler(tb_pdf_page_KeyPress);
            tb_pdf_page.TextAlign = HorizontalAlignment.Center;
            tb_pdf_page.Location = new Point(15, this.panel1.Height / 2 - tb_pdf_page.Height);
            this.panel1.Controls.Add(tb_pdf_page);    // 將控件加入表單
            tb_pdf_page.BringToFront();

            lb_pdf_total_page.Text = "";
            lb_pdf_total_page.Font = new Font("標楷體", 20);
            lb_pdf_total_page.ForeColor = Color.Black;
            lb_pdf_total_page.Location = new Point(15 + 50, this.panel1.Height / 2 - tb_pdf_page.Height + 3);
            lb_pdf_total_page.AutoSize = true;
            this.panel1.Controls.Add(lb_pdf_total_page);    // 將控件加入表單
        }

        void show_item_location()
        {
            //使用ToolTip
            tooltip.ForeColor = Color.Blue;	//ForeColor:取得或設定工具提示的前景色彩
            tooltip.BackColor = Color.LightGray;	//BackColor:取得或設定工具提示的背景色彩.
            tooltip.AutoPopDelay = 5000;	//AutoPopDelay:當指標靜止於控制項上時,ToolTip 保持可見的時間 (以毫秒為單位).預設值為 5000.

            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;

            this.ClientSize = new Size(W, H);
            this.Location = new Point(0, 0);

            lb_main_mesg1.Location = new System.Drawing.Point(500, 10);

            if (flag_already_use_webbrowser == false)
            {
                bt_control_setup();
                flag_already_use_webbrowser = true;
            }

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            //this.ShowInTaskbar = false;
            this.KeyPreview = true;
            //this.TopMost = true;

            lb_main_mesg1.Text = "";
            lb_main_mesg1.BringToFront();
            this.Text = "Pdf Reader";
        }

        void bt_control_setup()
        {
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

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(width, height);
            bt_exit.Text = "";
            bmp = new Bitmap(width, height);
            bt_exit.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, linewidth + 1, linewidth + 1, width - 1 - (linewidth + 1) * 2, height - 1 - (linewidth + 1) * 2);
            g.DrawLine(p, 0, 0, width - 1, height - 1);
            g.DrawLine(p, width - 1, 0, 0, height - 1);
            bt_exit.Location = new Point(this.panel1.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(width, height);
            bt_minimize.Text = "";
            bmp = new Bitmap(width, height);
            bt_minimize.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, linewidth + 1, linewidth + 1, width - 1 - (linewidth + 1) * 2, height - 1 - (linewidth + 1) * 2);
            g.DrawLine(p, width / 4, height / 2 - 1, width * 3 / 4, height / 2 - 1);
            bt_minimize.Location = new Point(this.panel1.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層

            Font f = new Font("Arial", 12);
            SolidBrush sb = new SolidBrush(Color.Red);

            x_st = 75 + dx * 0;
            y_st = 60 + dy * 0;
            Button bt_open_pdf = new Button();  // 實例化按鈕
            bt_open_pdf.Size = new Size(width, height);
            bt_open_pdf.Text = "";
            bt_open_pdf.BackgroundImage = Properties.Resources.open_folder;
            bt_open_pdf.BackgroundImageLayout = ImageLayout.Zoom;
            bt_open_pdf.Location = new Point(x_st, y_st);
            bt_open_pdf.Click += bt_open_pdf_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_open_pdf); // 將按鈕加入表單
            bt_open_pdf.BringToFront();     //移到最上層

            x_st = 75 + dx * 0;
            y_st = 60 + dy * 1;
            Button bt_open_recent_pdf = new Button();  // 實例化按鈕
            bt_open_recent_pdf.Size = new Size(width, height);
            bt_open_recent_pdf.Text = "";
            bmp = new Bitmap(width, height);
            bt_open_recent_pdf.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("最近", f, sb, new PointF(4, 15));
            bt_open_recent_pdf.Location = new Point(x_st, y_st);
            bt_open_recent_pdf.Click += bt_open_recent_pdf_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_open_recent_pdf); // 將按鈕加入表單
            bt_open_recent_pdf.BringToFront();     //移到最上層

            x_st = 75 + dx * 0;
            y_st = 60 + dy * 2;
            Button bt_test = new Button();  // 實例化按鈕
            bt_test.Size = new Size(width, height);
            bt_test.Text = "";
            bmp = new Bitmap(width, height);
            bt_test.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawString("測試", f, sb, new PointF(4, 15));
            bt_test.Location = new Point(x_st, y_st);
            bt_test.Click += bt_test_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_test); // 將按鈕加入表單
            bt_test.BringToFront();     //移到最上層

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
            this.panel1.Controls.Add(bt_clear); // 將按鈕加入表單
            bt_clear.BringToFront();     //移到最上層

            //使用ToolTip
            tooltip.SetToolTip(bt_exit, "關閉");
            tooltip.SetToolTip(bt_minimize, "最小化");
            tooltip.SetToolTip(bt_open_pdf, "開啟pdf檔案");
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            do_close();
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_open_pdf_Click(object sender, EventArgs e)
        {
            show_main_message1("開啟pdf", S_OK, 30);
            do_open_pdf();
        }

        private void bt_open_recent_pdf_Click(object sender, EventArgs e)
        {
            show_main_message1("開啟最近pdf", S_OK, 30);

            form_list.Owner = this;
            //form_list.StartPosition = FormStartPosition.CenterScreen;    //設定視窗居中顯示
            DialogResult result = form_list.ShowDialog();

            if (result == DialogResult.Ignore)
            {
                show_main_message1(form_list_data, S_OK, 100);
                //richTextBox1.Text += "你選擇了 " + form_list_data + "\n";

                string full_filename = form_list_data;

                if (File.Exists(full_filename) == false)   //確認檔案是否存在
                {
                    richTextBox1.Text += "檔案 : " + full_filename + ", 不存在\n";
                    show_main_message1("未選取檔案", S_OK, 30);
                    pdf_filename = "";
                    current_directory_pdf = Directory.GetCurrentDirectory();
                }
                else
                {
                    show_item_location();
                    pdf_filename = full_filename;
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory_pdf = Path.GetDirectoryName(pdf_filename);
                    webBrowser1.Navigate(pdf_filename);
                    pdf_total_page = GetPDFofPageCount(pdf_filename);
                    richTextBox1.Text += "檔案 : " + pdf_filename + "\n";
                    richTextBox1.Text += "頁數 : " + pdf_total_page.ToString() + "\n";
                    show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
                    pdf_page = 0;
                    tb_pdf_page.Text = pdf_page.ToString();
                    lb_pdf_total_page.Text = pdf_total_page.ToString();

                    //檢查ArrayList
                    update_pdf_filename_ArrayListData(pdf_filename);

                    richTextBox1.Text += "加入一筆資料至ArrayList\n";
                    pdf_filename_ArrayListData.Insert(0, pdf_filename); //插入一個元素
                    richTextBox1.Text += "目前ArrayList內共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";

                    //this.Focus();
                    this.KeyPreview = true;
                }
            }
        }

        private void bt_test_Click(object sender, EventArgs e)
        {
            show_main_message1("測試", S_OK, 30);

            /*
            richTextBox1.Text += "C#擷取pdf文檔的頁數\n";

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";

            int pages = GetPDFofPageCount(filename);
            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "頁數 : " + pages.ToString() + "\n";
            */

            show_pdf_filename_ArrayListData();

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

        private void tb_pdf_page_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                this.richTextBox1.Focus();
                e.Handled = true;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            message_panel_height = H - 50;

            Init_Controls();

            if (Environment.GetCommandLineArgs().Length == 2)
            {
                string filename = Environment.GetCommandLineArgs()[1];

                var GetExtension = Path.GetExtension(filename);

                if (GetExtension.ToLower() == ".pdf")
                {
                    if (File.Exists(filename) == true)
                    {
                        pdf_filename = filename;
                        pdf_filename_short = Path.GetFileName(pdf_filename);
                        current_directory_pdf = Path.GetDirectoryName(pdf_filename);
                        webBrowser1.Navigate(pdf_filename);
                        pdf_total_page = GetPDFofPageCount(pdf_filename);
                        richTextBox1.Text += "檔案 : " + pdf_filename + "\n";
                        richTextBox1.Text += "頁數 : " + pdf_total_page.ToString() + "\n";
                        pdf_page = 0;
                        tb_pdf_page.Text = pdf_page.ToString();
                        lb_pdf_total_page.Text = pdf_total_page.ToString();
                    }
                }
            }

            int i = 0;
            foreach (string arg in Environment.GetCommandLineArgs())
            {
                //lb_main_mesg1.Text += "第 " + i.ToString() + " 項 : " + arg + "\n";
                i++;
            }

            /*
            richTextBox1.Text += "取得預設資料 :\n";
            richTextBox1.Text += "filename : \t" + Properties.Settings.Default.filename + "\n";
            richTextBox1.Text += "position : \t" + Properties.Settings.Default.position.ToString() + "\n";
            */


            //取得系統參數資料
            richTextBox1.Text += "讀出系統變數至ArrayList\n";
            ArrayList tmp_array_list = Properties.Settings.Default.pdf_filenames;
            if (tmp_array_list == null)
            {
                pdf_filename_ArrayListData = new ArrayList();
            }
            else
            {
                pdf_filename_ArrayListData = tmp_array_list;
            }

            pdf_filename = Properties.Settings.Default.pdf_filename;
            pdf_page = Properties.Settings.Default.pdf_page;

            if (pdf_page == -1)
            {
                pdf_page = 0;
            }
            tb_pdf_page.Text = pdf_page.ToString();

            if (File.Exists(pdf_filename) == true)
            {
                pdf_filename_short = Path.GetFileName(pdf_filename);
                current_directory_pdf = Path.GetDirectoryName(pdf_filename);

                //預設
                //webBrowser1.Navigate(pdf_filename);

                //指名頁數
                if (pdf_page > 0)
                {
                    webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + pdf_page.ToString());
                }
                else
                {
                    webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0");
                }
                pdf_total_page = GetPDFofPageCount(pdf_filename);
                richTextBox1.Text += "檔案 : " + pdf_filename + "\n";
                richTextBox1.Text += "頁數 : " + pdf_total_page.ToString() + "\n";
                tb_pdf_page.Text = pdf_page.ToString();
                lb_pdf_total_page.Text = pdf_total_page.ToString();
                show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
            }
            show_item_location();
            this.webBrowser1.Focus();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.T)
            {
                show_main_message1("Test 1", S_OK, 30);
            }
            else if (e.KeyData == Keys.T)
            {
                show_main_message1("Test 2", S_OK, 30);
            }
            else if (e.KeyData == Keys.PageUp)
            {
            }
            else if (e.KeyData == Keys.PageDown)
            {
            }
            else if ((e.KeyData == Keys.Escape) || (e.KeyData == Keys.X))
            {
                do_close();
            }
            else if (e.KeyData == Keys.Back)
            {
            }
            else if (e.KeyData == Keys.H)
            {
            }
            else if (e.KeyData == Keys.I)
            {
            }
            else if (e.KeyData == Keys.O)
            {
            }
            else if (e.KeyData == Keys.M)
            {
            }
            else if (e.KeyData == Keys.P)
            {
                do_open_pdf();
            }
            else if ((e.KeyData == Keys.D0) || (e.KeyData == Keys.NumPad0))
            {
            }
            else if (e.KeyCode == Keys.Up)
            {
            }
            else if (e.KeyCode == Keys.Down)
            {
            }
            else if (e.KeyCode == Keys.Left)
            {
            }
            else if (e.KeyCode == Keys.Right)
            {
            }
            else if ((e.KeyData == Keys.Space) || (e.KeyData == Keys.Enter))
            {
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            do_close();
        }

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
        }

        void do_open_pdf()	//開啟pdf檔案
        {
            show_main_message1("開啟pdf檔案", S_OK, 30);
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "開啟pdf檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.pdf";
            openFileDialog1.Filter = "pdf檔(*.pdf)|*.pdf";
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            //openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
            openFileDialog1.InitialDirectory = current_directory_pdf;
            //openFileDialog1.InitialDirectory = @"D:\______C_data1\_______doc\doc1";
            openFileDialog1.Multiselect = false;    //單選

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                /*
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                */

                show_item_location();
                pdf_filename = openFileDialog1.FileName;
                pdf_filename_short = Path.GetFileName(pdf_filename);
                current_directory_pdf = Path.GetDirectoryName(pdf_filename);
                webBrowser1.Navigate(pdf_filename);
                pdf_total_page = GetPDFofPageCount(pdf_filename);
                richTextBox1.Text += "檔案 : " + pdf_filename + "\n";
                richTextBox1.Text += "頁數 : " + pdf_total_page.ToString() + "\n";
                show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
                pdf_page = 0;
                tb_pdf_page.Text = pdf_page.ToString();
                lb_pdf_total_page.Text = pdf_total_page.ToString();

                //檢查ArrayList
                update_pdf_filename_ArrayListData(pdf_filename);

                richTextBox1.Text += "加入一筆資料至ArrayList\n";
                pdf_filename_ArrayListData.Insert(0, pdf_filename); //插入一個元素
                richTextBox1.Text += "目前ArrayList內共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";
            }
            else
            {
                show_main_message1("未選取檔案", S_OK, 30);
                pdf_filename = "";
                current_directory_pdf = Directory.GetCurrentDirectory();
            }
            //this.Focus();
            this.KeyPreview = true;
        }

        void do_close()	//關閉程式
        {
            bool conversionSuccessful = int.TryParse(tb_pdf_page.Text, out pdf_page);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到int數字： " + pdf_page + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
            }

            Properties.Settings.Default.pdf_filename = pdf_filename;
            Properties.Settings.Default.pdf_page = pdf_page;

            //richTextBox1.Text += "將ArrayList寫入系統變數\n";
            Properties.Settings.Default.pdf_filenames = pdf_filename_ArrayListData;

            Properties.Settings.Default.Save();

            Application.Exit();
        }

        void show_pdf_filename_ArrayListData()
        {
            richTextBox1.Text += "顯示ArrayList資料\n";
            richTextBox1.Text += "共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";

            int i = 0;
            /*
            for (i = 0; i < pdf_filename_ArrayListData.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + pdf_filename_ArrayListData[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in pdf_filename_ArrayListData)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        void update_pdf_filename_ArrayListData(string new_data)
        {
            bool flag_file_exists = false;
            foreach (string str_name in pdf_filename_ArrayListData)
            {
                if (new_data == str_name)
                {
                    flag_file_exists = true;
                }
            }

            if (flag_file_exists == true)
            {
                richTextBox1.Text += "找到一樣的項目\n";
                richTextBox1.Text += "將此項目刪除\n";

                pdf_filename_ArrayListData.Remove(new_data);

                //pdf_filename_ArrayListData.Insert(0, new_data); //插入一個元素
            }
        }
    }
}
