using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_SlideShowString
{
    public partial class Form1 : Form
    {
        bool flag_release_mode = true;
        bool flag_pause = false;

        Graphics g;
        Font f;
        Bitmap bmp;

        int W = 0;      //final pictureBox1.Width for display
        int H = 0;      //final pictureBox1.Height for display
        int w = 0;      //final string width for display
        int h = 0;      //final string height for display

        int i = 0;

        //string filepath = "C:\\______test_vcs\\poetry.txt";
        //string filepath = "poetry_debug.txt";
        string filepath = "poetry.txt";

        List<String> all_strings = new List<String>();
        List<String> current_strings = new List<String>();  //new List<string>物件

        private const int SKY = 50;
        private const int EARTH = 30;
        private const int BORDER = 10;
        private const int D1 = 30;
        private const int D2 = 12;
        private const int D3 = 6;


        int strings_count = 0;
        int lyrics_count = 0;

        int lines_in_this_lyrics = 0;

        int show_lyrics_index = 0;

        string str_author = String.Empty;
        string str_title = String.Empty;
        string str_serial = String.Empty;
        string str_text = String.Empty;

        string string0 = String.Empty;

        int timer1_cnt = 0;
        int do_mouse_wheel_cnt = 0;
        int timer2_cnt = 0;
        int align_direction = 0;
        int play_sequence = 0;
        int default_font_size = 0;
        int user_font_size = 0;
        int slide_show_interval = 0;
        bool flag_top_most = false;
        int total_title_author_height = 0;
        int title_width = 0;
        int author_width = 0;
        int tmp_width = 0;
        int tmp_height = 0;

        Random r = new Random();

        public Form1()
        {
            InitializeComponent();
        }

        bool loadTextData()
        {
            bool flag_skip_comment = false;
            if (System.IO.File.Exists(filepath) == false)
            {
                richTextBox1.Text += "檔案 " + filepath + " 不存在，離開。\n";
                return false;
            }
            else
            {
                richTextBox1.Text += "檔案 " + filepath + " 存在, 開啟，並讀入文字資料\n";

                string line;
                StreamReader sr = new StreamReader(filepath, Encoding.Default);

                i = 0;
                lyrics_count = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine().Trim();            // 讀取文字到 line 變數
                    if (line.Length < 2)
                        continue;

                    if ((line[line.Length - 2] == '*') && (line[line.Length - 1] == '/'))
                    {
                        richTextBox1.Text += "got comment SP : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        flag_skip_comment = false;
                        continue;
                    }
                    else if (flag_skip_comment == true)
                    {
                        richTextBox1.Text += "got comment : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        continue;
                    }
                    else if ((line[0] == '/') && (line[1] == '*'))
                    {
                        flag_skip_comment = true;
                        richTextBox1.Text += "got comment ST : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        continue;
                    }
                    else if (line[0] == '@')
                    {
                        //richTextBox1.Text += "get author" + line + "\n";
                    }
                    else if (line[0] == '^')
                    {
                        align_direction = line[1];
                        //richTextBox1.Text += "value = " + align_direction.ToString() + "\n";
                        richTextBox1.Text += "設定對齊方向" + "\t";
                        if (align_direction == '0')
                            richTextBox1.Text += "靠右\n";
                        else if (align_direction == '1')
                            richTextBox1.Text += "靠右\n";
                        else
                            richTextBox1.Text += "正中\n";
                    }
                    else if (line[0] == '~')
                    {
                        play_sequence = line[1];
                        //richTextBox1.Text += "value = " + play_sequence.ToString() + "\n";
                        richTextBox1.Text += "設定播放順序" + "\t";
                        if (play_sequence == '0')
                            richTextBox1.Text += "依序\n";
                        else
                            richTextBox1.Text += "隨機\n";
                    }
                    else if (line[0] == '<')
                    {
                        if (line[1] == 'X')
                        {
                            default_font_size = 36;
                        }
                        else if (line[1] == 'L')
                        {
                            default_font_size = 24;
                        }
                        else if (line[1] == 'M')
                        {
                            default_font_size = 20;
                        }
                        else if (line[1] == 'S')
                        {
                            default_font_size = 16;
                        }
                        else if (line[1] == 'U')
                        {
                            default_font_size = -1;
                        }
                        richTextBox1.Text += "設定預設字型大小: " + default_font_size.ToString() + "\n";
                    }
                    else if (line[0] == '>')
                    {
                        user_font_size = int.Parse(line.Remove(0, 1));
                        richTextBox1.Text += "自訂字型大小: " + user_font_size.ToString() + "\n";
                    }
                    else if (line[0] == '{')
                    {
                        slide_show_interval = int.Parse(line.Remove(0, 1));
                        richTextBox1.Text += "播放速度: " + slide_show_interval.ToString() + " 秒\n";
                    }
                    else if (line[0] == '[')
                    {
                        if (line[1] == '0')
                        {
                            flag_top_most = false;
                            richTextBox1.Text += "設定非最上層顯示\n";
                        }
                        else if (line[1] == '1')
                        {
                            flag_top_most = true;
                            richTextBox1.Text += "設定最上層顯示\n";
                        }
                    }
                    else if (line[0] == '#')
                    {
                        //richTextBox1.Text += "get title" + line + "\n";
                    }
                    else if (line[0] == '$')
                    {
                        //richTextBox1.Text += "get serial" + line + "\n";
                        continue;
                    }
                    else if (line[0] == '%')
                    {
                        //comment
                        //richTextBox1.Text += "get comment" + line + "\n";
                        continue;
                    }
                    else if ((line[0] == '/')&&(line[1] == '/'))
                    {
                        //comment
                        //richTextBox1.Text += "get comment" + line + "\n";
                        continue;
                    }
                    else if (line[0] == '&')
                    {
                        //richTextBox1.Text += "get text start" + line + "\n";
                        //line = line.Remove(0, 1);
                        lyrics_count++;
                    }
                    //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";
                    all_strings.Add(line);
                }
                strings_count = all_strings.Count;
                sr.Close();

                richTextBox1.Text += "共有 " + lyrics_count.ToString() + " 首\n";
                richTextBox1.Text += "可用行數 " + strings_count.ToString() + "\n";

                //show_lyrics_index = 0;
                show_lyrics_index = get_next_show_lyrics_index(-1);

                if (default_font_size <= 0)
                {
                    if (user_font_size > 0)
                        default_font_size = user_font_size;
                    else
                        default_font_size = 16;
                }

                richTextBox1.Text += "設定字型大小: " + default_font_size.ToString() + "\n";

                return true;
            }
        }

        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (lyrics_count == 1)
            {
                richTextBox1.Text += "只有一首, 不動作\n";
                return;
            }

            if ((timer2_cnt - do_mouse_wheel_cnt) < 6)
            {
                //richTextBox1.Text += "太接近\n";
                return;
            }

            richTextBox1.Text += e.Delta.ToString() + " ";
            if (e.Delta < 0)
            {
                richTextBox1.Text += "下一首\n";
                slide_show_string();
                do_mouse_wheel_cnt = timer2_cnt;
            }
            else
            {
                richTextBox1.Text += "上一首\n";
                if (show_lyrics_index > 0)
                    show_lyrics_index--;
                else
                    show_lyrics_index = lyrics_count - 1;
                if (show_lyrics_index > 0)
                    show_lyrics_index--;
                else
                    show_lyrics_index = lyrics_count - 1;
                slide_show_string();
                do_mouse_wheel_cnt = timer2_cnt;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
            bool result;
            result = loadTextData();
            if (result == true)
            {
                slide_show_string();
                timer1.Enabled = true;
            }
            else
                timer1.Enabled = false;
        }

        int calculate_picturebox_parameters()
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            int screenHeight_max = screenHeight * 70 / 100;

            lines_in_this_lyrics = current_strings.Count;
            /*
            richTextBox1.Text += "current_strings 內容\tcount = " + current_strings.Count.ToString() + " (lines)\n";
            for (i = 0; i < current_strings.Count; i++)
            {
                richTextBox1.Text += current_strings[i] + "\n";
            }
            */

            w = 0;
            h = 0;

            for (i = 0; i < current_strings.Count; i++)
            {
                if(i == 1)
                    tmp_width = g.MeasureString(current_strings[i].Remove(0, 1), f).ToSize().Width;
                else
                    tmp_width = g.MeasureString(current_strings[i], f).ToSize().Width;
                //richTextBox1.Text += "i = " + i.ToString() + " tmp_width = " + tmp_width.ToString() + " " + current_strings[i] + "\n";
                tmp_height = g.MeasureString(current_strings[i], f).ToSize().Height;
                //richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
                //richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "\t";
                //richTextBox1.Text += "tmp_height = " + tmp_height.ToString() + "\n";
                //g.DrawRectangle(p, 150, 50, tmp_height - 1, tmp_width);

                if (w < tmp_width)
                    w = tmp_width;
                if (h < tmp_height)
                    h = tmp_height;
            }

            /*
            richTextBox1.Text += "w = " + w.ToString() + "\t";
            richTextBox1.Text += "h = " + h.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + " screenHeight_max = " + screenHeight_max.ToString() + "\n";
            */

            //especially calculate title + author

            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            int sky = SKY;
            int earth = EARTH;
            int d1 = D1;
            int d2 = D2;
            int d3 = D3;

            title_width = g.MeasureString(str_title, f).ToSize().Width;
            author_width = g.MeasureString(str_author, f).ToSize().Width;

            //total_title_author_height = sky + d1 + d2 + d3 + title_width + d1 + d2 + d3 + author_width + earth;
            total_title_author_height = sky + d1 + d2 + d3 + title_width + d2 + d3 + author_width + earth;

            //richTextBox1.Text += "total_title_author_height = " + total_title_author_height.ToString() + "\n";
            if (total_title_author_height > screenHeight_max)
            {
                richTextBox1.Text += "length too long, return fail........";
                return -1;
            }

            if (w < screenHeight_max)
            {
                //w -= 8;
                //richTextBox1.Text += "w = " + w.ToString() + "\n";
                return 0;
            }
            else
                return -1;

        }

        void slide_show_string()
        {
            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);

            int i;
            int flag_get_lyrics_index = 0;
            int flag_get_text_data = 0;

            int cnt = 0;

            /*
            richTextBox1.Text += "\n現在要播放 第 " + show_lyrics_index.ToString() + " 首" + "\n";
            richTextBox1.Text += "flag_get_lyrics_index = " + flag_get_lyrics_index.ToString() + "\n";
            richTextBox1.Text += "show_lyrics_index = " + show_lyrics_index.ToString() + "\n";
            richTextBox1.Text += "strings_count = " + strings_count.ToString() + "\n";

            //從頭播起 要更新 current_strings 資料
            richTextBox1.Text += "從頭播起 從大List裡找出第 " + show_lyrics_index.ToString() + "首的內容\n";
            */

            for (i = 0; i < strings_count; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + " first = " + strings[i][0] + "\n";
                if (all_strings[i][0] == '@')   //author
                {
                    if (flag_get_text_data == 1)
                    {
                        flag_get_text_data = 0;
                        break;
                    }
                    str_author = all_strings[i].Remove(0, 1);
                }
                else if (all_strings[i][0] == '#')  //title
                {
                    if (flag_get_text_data == 1)
                    {
                        flag_get_text_data = 0;
                        break;
                    }
                    str_title = all_strings[i].Remove(0, 1);
                }
                else if (all_strings[i][0] == '&')  //text
                {
                    //richTextBox1.Text += "got & now = " + all_strings[i] + " A = " + flag_get_lyrics_index.ToString() + " B = " + show_lyrics_index.ToString() + "\n";

                    if (flag_get_lyrics_index == show_lyrics_index)
                    {
                        //richTextBox1.Text += "let flag_get_text_data = 1\n";
                        flag_get_text_data = 1;
                        cnt = 0;
                        current_strings.Clear();
                        //richTextBox1.Text += "開始抓內容, now = " + all_strings[i] + "\n";
                    }
                    else
                    {
                        flag_get_lyrics_index++;

                        str_author = String.Empty;
                        str_title = String.Empty;
                        str_serial = String.Empty;
                        str_text = String.Empty;
                    }
                }

                if (flag_get_text_data == 1)
                {
                    cnt++;
                    //richTextBox1.Text += "get data cnt = " + cnt.ToString() + "\n";
                    lines_in_this_lyrics = cnt;
                    current_strings.Add(all_strings[i]);
                }
            }

            if ((str_author != String.Empty) && (str_title != String.Empty))
            {
                string0 = "【" + str_author + "‧" + str_title + "】";
            }
            else if ((str_author == String.Empty) && (str_title != String.Empty))
            {
                string0 = "【" + str_title + "】";
            }
            else if ((str_author != String.Empty) && (str_title == String.Empty))
            {
                string0 = "【" + str_author + "】";
            }
            else
            {
                string0 = "【        】";
            }
            current_strings.Insert(0, string0);

            richTextBox1.Text += "第 " + (show_lyrics_index + 1).ToString() + " 首, " + str_author + " " + str_title + ", 長度 " + lines_in_this_lyrics.ToString() + " 行\n";

            f = new Font("標楷體", default_font_size);

            bmp = new Bitmap(100, 100);     //initial W, H
            g = Graphics.FromImage(bmp);

            //更新全首的畫圖邊界
            int result = -1;
            while (result == -1)
            {
                result = calculate_picturebox_parameters();
                if (result == -1)
                {
                    float fontsize;
                    fontsize = f.Size;
                    if (fontsize > 2)
                        fontsize -= 1;
                    f = new Font("標楷體", fontsize);
                    richTextBox1.Text += "縮小字型為 " + fontsize.ToString() + "\n";
                }
            }

            int N = current_strings.Count;
            int p = 0;
            int sky = SKY;
            int earth = EARTH;
            int border = BORDER;

            W = h * N + p * (N * 2) + border * 2;
            H = w + sky + earth;

            pictureBox1.Width = W;
            pictureBox1.Height = H;

            /*
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";
            richTextBox1.Text += "p = " + p.ToString() + "\n";
            */

            if (H < total_title_author_height)
            {
                H = total_title_author_height;
                w = total_title_author_height - sky - earth;
            }

            bmp = new Bitmap(W, H);
            g = Graphics.FromImage(bmp);

            g.Clear(Color.SandyBrown);
            pictureBox1.Image = bmp;

            int x_st;
            int y_st;

            current_strings[1] = current_strings[1].Remove(0, 1); //remove '&'

            for (i = 0; i < current_strings.Count; i++)
            {
                x_st = p * (2 * (N - i) - 1) + h * (N - i - 1);
                y_st = sky;
                if (i != 0)
                {
                    g.DrawString(current_strings[i], f, new SolidBrush(Color.Black), border + x_st, y_st, drawFormat);
                    /*
                    int www = g.MeasureString(current_strings[i], f).ToSize().Width;
                    richTextBox1.Text += "www = " + www.ToString() + "  str = " + current_strings[i] + "\n";
                    g.DrawRectangle(new Pen(Color.Green, 1), border + x_st+1, y_st+1, h, www);
                    */

                }
                g.DrawRectangle(new Pen(Color.Red, 1), border + x_st, y_st, h, w);
            }
            x_st = 0;
            y_st = sky;

            g.DrawRectangle(new Pen(Color.Red, 5), border + x_st - 5, y_st - 5, h * N + p * (N * 2) + 10, w + 10);

            int d1 = D1;
            int d2 = D2;
            int d3 = D3;

            i = 0;
            x_st = p * (2 * (N - i) - 1) + h * (N - i - 1);
            y_st = sky;

            Point[] pts = new Point[5];
            pts[0].X = border + x_st;
            pts[0].Y = y_st + d1;
            pts[1].X = border + x_st + h;
            pts[1].Y = y_st + d1;
            pts[2].X = border + x_st + h;
            pts[2].Y = y_st + d1 + d2;
            pts[3].X = border + x_st + h / 2;
            pts[3].Y = y_st + d1 + d3;
            pts[4].X = border + x_st;
            pts[4].Y = y_st + d1 + d2;
            g.FillPolygon(new SolidBrush(Color.Red), pts);

            i = 0;
            x_st = p * (2 * (N - i) - 1) + h * (N - i - 1);
            y_st = sky + d1 + d2 + d3;
            g.DrawString(str_title, f, new SolidBrush(Color.Black), border + x_st, y_st, drawFormat);

            title_width = g.MeasureString(str_title, f).ToSize().Width;
            author_width = g.MeasureString(str_author, f).ToSize().Width;
            int y_st_title = 0;
            int dd = (w - d1 - d2 - d3 - title_width - d3 - d2 - author_width) / 2;

            y_st_title = sky + d1 + d2 + d3 + title_width + d3 + d2 + dd;

            g.DrawString(str_author, f, new SolidBrush(Color.Black), border + x_st, y_st_title, drawFormat);

            /*  debug
            int yy1;
            int yy2;
            yy1 = 0;
            yy2 = sky + d1 + d2 + d3 + title_width + d3 + d2;
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(border + x_st + 10 - 20, yy1, g.MeasureString(str_author, f).ToSize().Height - 20, yy2));

            yy1 = sky;
            yy2 = w;
            g.FillRectangle(new SolidBrush(Color.Yellow), new Rectangle(border + x_st + 10 - 50, yy1, g.MeasureString(str_author, f).ToSize().Height - 20, yy2));
            */

            y_st = sky + d1 + d2 + d3 + title_width + d3 + d2;

            pts[0].X = border + x_st;
            pts[0].Y = y_st;
            pts[1].X = border + x_st + h;
            pts[1].Y = y_st;
            pts[2].X = border + x_st + h;
            pts[2].Y = y_st - d2;
            pts[3].X = border + x_st + h / 2;
            pts[3].Y = y_st - d3;
            pts[4].X = border + x_st;
            pts[4].Y = y_st - d2; ;
            g.FillPolygon(new SolidBrush(Color.Red), pts);

            if (flag_release_mode == false)
            {
                string show_play_info = (show_lyrics_index + 1).ToString() + " / " + lyrics_count.ToString();
                tmp_width = g.MeasureString(show_play_info, new Font("標楷體", default_font_size * 2 / 3)).ToSize().Width;
                tmp_height = g.MeasureString(show_play_info, new Font("標楷體", default_font_size * 2 / 3)).ToSize().Height;
                g.DrawString(show_play_info, new Font("標楷體", default_font_size * 2 / 3), new SolidBrush(Color.Blue), new PointF((W - tmp_width) / 2, H - tmp_height));
            }

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            if (flag_release_mode == true)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                if (align_direction == '0')
                {   //靠右
                    this.Location = new System.Drawing.Point(screenWidth - W, (screenHeight - H) / 2);
                }
                else if (align_direction == '1')
                {   //靠左
                    this.Location = new System.Drawing.Point(0, (screenHeight - H) / 2);
                }
                else if (align_direction == '2')
                {   //正中
                    this.Location = new System.Drawing.Point((screenWidth - W) / 2, (screenHeight - H) / 2);
                }
                this.Size = new Size(W, H);
            }
            this.Text = str_title;

            show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);

            timer1_cnt = 0;

            if (flag_top_most == true)
                this.TopMost = true;
            else
                this.TopMost = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (lyrics_count == 1)
            {
                //richTextBox1.Text += "只有一首, 不動作\n";
                return;
            }

            if (slide_show_interval == 0)
            {
                //richTextBox1.Text += "停止自動播放\n";
                return;
            }

            timer1_cnt++;
            if (timer1_cnt > slide_show_interval)
            {
                timer1_cnt = 0;
                slide_show_string();
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            if (flag_pause == false)
            {
                g.FillRectangle(new SolidBrush(Color.SaddleBrown), new Rectangle(0, H - EARTH / 2, W, EARTH / 2));
                pictureBox1.Image = bmp;
                flag_pause = true;
                timer1.Enabled = false;
            }
            else
            {
                g.FillRectangle(new SolidBrush(Color.SandyBrown), new Rectangle(0, H - EARTH / 2, W, EARTH / 2));
                pictureBox1.Image = bmp;
                flag_pause = false;
                timer1.Enabled = true;
            }
        }

        //***********************
        private Point mouseOffset;//记录鼠标坐标
        private bool isMouseDown = false;//是否按下鼠标
        //***********************

        #region 移动无边框窗体
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            if (lyrics_count == 1)
            {
                richTextBox1.Text += "只有一首, 不動作\n";
                return;
            }
            slide_show_string();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 " + all_strings.Count.ToString() + " 個字串\n";


            for (int i = 0; i < all_strings.Count; i++)
            {
                richTextBox1.Text += all_strings[i] + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (lyrics_count == 1)
            {
                richTextBox1.Text += "只有一首, 不動作\n";
                return;
            }
            slide_show_string();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < current_strings.Count; i++)
            {
                richTextBox1.Text += current_strings[i] + "\n";
            }
        }

        int get_next_show_lyrics_index(int current_show_lyrics_index)
        {
            if (play_sequence == '0')
            {   //依序
                if (show_lyrics_index < (lyrics_count - 1))
                    show_lyrics_index++;
                else
                    show_lyrics_index = 0;
                if(current_show_lyrics_index == -1)
                    show_lyrics_index = 0;
                return show_lyrics_index;
            }
            else
            {   //隨機
                int next_show_lyrics_index = 0;
                if (lyrics_count == 1)
                    return 0;
                else
                {
                    do
                    {
                        next_show_lyrics_index = r.Next(lyrics_count);
                        //richTextBox1.Text += "get " + next_show_lyrics_index.ToString() + "\n";
                    } while (current_show_lyrics_index == next_show_lyrics_index);
                    return next_show_lyrics_index;
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "Opacity = " + this.Opacity.ToString() + "\n";
            /*
            string result2 = "";
            for (int i = 0; i < 30; i++)
            {
                result2 += r.Next(lyrics_count).ToString() + " ";
            }
            richTextBox1.Text += "取0~lyrics_count的亂數值：" + result2 + "\n";
            */

            int next;
            next = get_next_show_lyrics_index(show_lyrics_index);

            richTextBox1.Text += "current = " + show_lyrics_index.ToString() + " next = " + next.ToString() + "\n";

        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2_cnt++;
        }
    }
}
