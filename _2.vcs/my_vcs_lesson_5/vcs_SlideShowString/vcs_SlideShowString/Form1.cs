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
        //bool flag_pause = false;

        Graphics g;
        Font f;
        Bitmap bmp;

        int W;      //final pictureBox1.Width for display
        int H;      //final pictureBox1.Height for display
        int i = 0;

        //string filepath = "C:\\______test_vcs\\poetry.txt";
        string filepath = "poetry.txt";
        //string filepath = "poetry_debug.txt";

        List<String> all_strings = new List<String>();
        List<String> current_strings = new List<String>();  //new List<string>物件

        int strings_count = 0;
        int lyrics_count = 0;

        int lines_in_this_lyrics = 0;

        int show_lyrics_index = 0;

        string str_author = String.Empty;
        string str_title = String.Empty;
        string str_serial = String.Empty;
        string str_text = String.Empty;

        string string0 = String.Empty;

        Size sss;
        int show_head_size = 0;
        int show_max_width_size = 0;
        int show_max_height_size = 0;
        int timer1_cnt = 0;
        int do_mouse_wheel_cnt = 0;
        int timer2_cnt = 0;
        int align_direction = 0;
        int play_sequence = 0;
        int default_font_size = 0;
        int user_font_size = 0;
        int slide_show_interval = 0;

        Random r = new Random();

        public Form1()
        {
            InitializeComponent();
        }

        bool loadTextData()
        {
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
                    if (line.Length <= 0)
                        continue;
                    if (line[0] == '@')
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
                        else
                            richTextBox1.Text += "靠左\n";
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
                        if (line[1] == 'L')
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

            show_head_size = 0;
            show_max_width_size = 0;
            show_max_height_size = 0;

            for (i = 0; i < current_strings.Count; i++)
            {
                sss = g.MeasureString(current_strings[i], f).ToSize();
                //richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
                //richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
                //richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
                //g.DrawRectangle(p, 150, 50, sss.Height - 1, sss.Width);

                if (show_max_width_size < sss.Width)
                    show_max_width_size = sss.Width;
                if (show_max_height_size < sss.Height)
                    show_max_height_size = sss.Height;
            }

            if (show_max_width_size < screenHeight_max)
                show_head_size = (screenHeight_max - show_max_width_size) / 2;
            else
                show_head_size = 0;

            /*
            richTextBox1.Text += "show_head_size = " + show_head_size.ToString() + "\t";
            richTextBox1.Text += "show_max_width_size = " + show_max_width_size.ToString() + "\t";
            richTextBox1.Text += "show_max_height_size = " + show_max_height_size.ToString() + "\n";
            richTextBox1.Text += "show_max_width_size = " + show_max_width_size.ToString() + " screenHeight_max = " + screenHeight_max.ToString() + "\n";
            */

            if (show_max_width_size < screenHeight_max)
                return 0;
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

            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bmp);

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
            int sky = 50;
            int earth = 30;
            int border = 10;

            pictureBox1.Width = show_max_height_size * N + p * (N * 2) + border * 2;
            pictureBox1.Height = show_max_width_size + sky + earth;

            W = pictureBox1.Width;
            H = pictureBox1.Height;

            /*
            richTextBox1.Text += "W = " + pictureBox1.Width.ToString() + ", H = " + pictureBox1.Height.ToString() + "\n";
            richTextBox1.Text += "w = " + show_max_width_size.ToString() + ", h = " + show_max_height_size.ToString() + "\n";
            richTextBox1.Text += "p = " + p.ToString() + "\n";
            */

            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bmp);

            g.Clear(Color.SandyBrown);
            pictureBox1.Image = bmp;

            int x_st;
            int y_st;

            current_strings[1] = current_strings[1].Remove(0, 1); //remove '&'

            for (i = 0; i < current_strings.Count; i++)
            {
                x_st = p * (2 * (N - i) - 1) + show_max_height_size * (N - i - 1);
                y_st = sky;
                if (i != 0)
                    g.DrawString(current_strings[i], f, new SolidBrush(Color.Black), border + x_st, y_st, drawFormat);
                g.DrawRectangle(new Pen(Color.Red, 1), border + x_st, y_st, show_max_height_size, show_max_width_size);
            }
            x_st = 0;
            y_st = sky;

            g.DrawRectangle(new Pen(Color.Red, 5), border + x_st - 5, y_st - 5, show_max_height_size * N + p * (N * 2) + 10, show_max_width_size + 10);

            int down1 = 50;
            int down2 = 12;
            int down3 = 6;

            i = 0;
            x_st = p * (2 * (N - i) - 1) + show_max_height_size * (N - i - 1);
            y_st = sky;

            Point[] pts = new Point[5];
            pts[0].X = border + x_st;
            pts[0].Y = y_st + down1;
            pts[1].X = border + x_st + show_max_height_size;
            pts[1].Y = y_st + down1;
            pts[2].X = border + x_st + show_max_height_size;
            pts[2].Y = y_st + down1 + down2;
            pts[3].X = border + x_st + show_max_height_size / 2;
            pts[3].Y = y_st + down1 + down3;
            pts[4].X = border + x_st;
            pts[4].Y = y_st + down1 + down2;
            g.FillPolygon(new SolidBrush(Color.Red), pts);

            i = 0;
            x_st = p * (2 * (N - i) - 1) + show_max_height_size * (N - i - 1);
            y_st = sky + down1 + down2 + down3;
            g.DrawString(str_title, f, new SolidBrush(Color.Black), border + x_st, y_st, drawFormat);

            sss = g.MeasureString(str_title, f).ToSize();

            g.DrawString(str_author, f, new SolidBrush(Color.Black), border + x_st, y_st + sss.Width + down1 + down2 + down3, drawFormat);


            y_st = sky + down1 + down2 + down3 + sss.Width + down3 + down2;

            pts[0].X = border + x_st;
            pts[0].Y = y_st;
            pts[1].X = border + x_st + show_max_height_size;
            pts[1].Y = y_st;
            pts[2].X = border + x_st + show_max_height_size;
            pts[2].Y = y_st - down2;
            pts[3].X = border + x_st + show_max_height_size / 2;
            pts[3].Y = y_st - down3;
            pts[4].X = border + x_st;
            pts[4].Y = y_st - down2; ;
            g.FillPolygon(new SolidBrush(Color.Red), pts);

            if (flag_release_mode == false)
            {
                string show_play_info = (show_lyrics_index + 1).ToString() + " / " + lyrics_count.ToString();
                sss = g.MeasureString(show_play_info, new Font("標楷體", default_font_size * 2 / 3)).ToSize();
                g.DrawString(show_play_info, new Font("標楷體", default_font_size * 2 / 3), new SolidBrush(Color.Blue), new PointF((W - sss.Width) / 2, H - sss.Height + 1));
            }

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            if (flag_release_mode == true)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                if (align_direction == '0')
                {   //靠右
                    this.Location = new System.Drawing.Point(screenWidth - pictureBox1.Width, (screenHeight - pictureBox1.Height) / 2);
                }
                else
                {   //靠左
                    this.Location = new System.Drawing.Point(0, (screenHeight - pictureBox1.Height) / 2);
                }
                this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
            }

            show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);

            timer1_cnt = 0;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (lyrics_count == 1)
            {
                //richTextBox1.Text += "只有一首, 不動作\n";
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
            /*  不是很好用
            if (flag_pause == false)
            {
                flag_pause = true;
                timer1.Enabled = false;
            }
            else
            {
                flag_pause = false;
                timer1.Enabled = true;
            }
            */
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
