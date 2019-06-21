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
        bool flag_release_mode = false;
        //bool flag_need_author = true;
        //bool flag_need_title = true;

        Bitmap bmp;
        //bool flag_pause = false;
        //int cnt = 0;
        //int total = 100;
        int W;
        int H;
        int i = 0;

        //string filepath = "C:\\______test_vcs\\poetry.txt";
        string filepath = "poetry.txt";

        List<String> all_strings = new List<String>();
        List<String> current_strings = new List<String>();  //new List<string>物件

        int strings_count = 0;
        int lyrics_count = 0;

        int lines_in_this_lyrics = 0;

        int show_lyrics_index = 0;
        int flag_playing = 0;
        int flag_playing_step = 0;

        string str_author = String.Empty;
        string str_title = String.Empty;
        string str_serial = String.Empty;
        string str_text = String.Empty;

        string string0 = String.Empty;

        Graphics g;
        SolidBrush sb;
        Font f;
        int show_head_size = 0;
        int show_waist_size = 0;
        int show_max_width_size = 0;
        int show_max_height_size = 0;


        public Form1()
        {
            InitializeComponent();
            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bmp);
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 24);
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
                show_lyrics_index = 0;
                return true;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.Text += "目前解析度  " + screenWidth.ToString() + " X " + screenHeight.ToString() + "\n";

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);

            if (flag_release_mode == true)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new System.Drawing.Point(screenWidth - pictureBox1.Width, 200);
                this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
            }

            bool result;
            result = loadTextData();
            if (result == true)
                timer1_Tick(sender, e);
            else
                timer1.Enabled = false;
        }

        int calculate_picturebox_parameters()
        {

            lines_in_this_lyrics = current_strings.Count;
            richTextBox1.Text += "current_strings 內容\tcount = " + current_strings.Count.ToString() + " (lines)\n";
            for (i = 0; i < current_strings.Count; i++)
            {
                richTextBox1.Text += current_strings[i] + "\n";
            }

            Size sss;
            show_head_size = 0;
            show_waist_size = 0;
            show_max_width_size = 0;
            show_max_height_size = 0;

            for (i = 0; i < current_strings.Count; i++)
            {
                sss = g.MeasureString(current_strings[i], f).ToSize();
                richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
                richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
                richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
                //g.DrawRectangle(p, 150, 50, sss.Height - 1, sss.Width);

                if (show_max_width_size < sss.Width)
                    show_max_width_size = sss.Width;
                if (show_max_height_size < sss.Height)
                    show_max_height_size = sss.Height;
            }

            if (show_max_width_size < pictureBox1.Height)
                show_head_size = (pictureBox1.Height - show_max_width_size) / 2;
            else
                show_head_size = 0;

            if (show_max_height_size * 3 < pictureBox1.Width)
                show_waist_size = (pictureBox1.Width - show_max_height_size * 3) / 4;
            else
                show_waist_size = 0;

            richTextBox1.Text += "show_head_size = " + show_head_size.ToString() + "\t";
            richTextBox1.Text += "show_waist_size = " + show_waist_size.ToString() + "\n";
            richTextBox1.Text += "show_max_width_size = " + show_max_width_size.ToString() + "\t";
            richTextBox1.Text += "show_max_height_size = " + show_max_height_size.ToString() + "\n";

            richTextBox1.Text += "show_max_width_size = " + show_max_width_size.ToString() + " 90% W = " + (pictureBox1.Height * 90 / 100).ToString() + "\n";

            if (show_max_width_size < (pictureBox1.Height * 90 / 100))
                return 0;
            else
                return -1;

        }

        void slide_show_string()
        {
            //  畫背景色
            W = pictureBox1.Width;
            H = pictureBox1.Height;
            int xx;
            int yy;
            for (yy = 0; yy < H; yy++)
            {
                for (xx = 0; xx < W; xx++)
                {
                    bmp.SetPixel(xx, yy, Color.FromArgb(30, 0x11, 0x33, 0x55));
                }
            }

            int i;

            int flag_get_lyrics_index = 0;
            int flag_get_text_data = 0;

            int cnt = 0;

            String show_string0 = String.Empty;
            String show_string1 = String.Empty;
            String show_string2 = String.Empty;


            string show_play_info = (show_lyrics_index + 1).ToString() + " / " + lyrics_count.ToString();
            g.DrawString(show_play_info, new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(40, pictureBox1.Height - 25));

            richTextBox1.Text += "現在要播放 第 " + show_lyrics_index.ToString() + " 首" + "\t";
            if (flag_playing == 0)
            {
                //richTextBox1.Text += "flag_get_lyrics_index = " + flag_get_lyrics_index.ToString() + "\n";
                //richTextBox1.Text += "show_lyrics_index = " + show_lyrics_index.ToString() + "\n";
                //richTextBox1.Text += "strings_count = " + strings_count.ToString() + "\n";

                //從頭播起 要更新 current_strings 資料
                richTextBox1.Text += "從頭播起 從大List裡找出第 " + show_lyrics_index.ToString() + "首的內容\n";
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
                        richTextBox1.Text += "got & now = " + all_strings[i] + " A = " + flag_get_lyrics_index.ToString() + " B = " + show_lyrics_index.ToString() + "\n";

                        if (flag_get_lyrics_index == show_lyrics_index)
                        {
                            richTextBox1.Text += "let flag_get_text_data = 1\n";
                            flag_get_text_data = 1;
                            cnt = 0;
                            current_strings.Clear();
                            richTextBox1.Text += "開始抓內容, now = " + all_strings[i] + "\n";
                        }
                        else
                        {
                            flag_get_lyrics_index++;

                            str_author = String.Empty;
                            str_title = String.Empty;
                            str_serial = String.Empty;
                            str_text = String.Empty;

                            show_string0 = String.Empty;
                            show_string1 = String.Empty;
                            show_string2 = String.Empty;
                        }
                    }

                    if (flag_get_text_data == 1)
                    {
                        cnt++;
                        richTextBox1.Text += "get data cnt = " + cnt.ToString() + "\n";
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

                richTextBox1.Text += "第 " + show_lyrics_index.ToString() + " 首, 長度 " + lines_in_this_lyrics.ToString() + " 行\n";
                richTextBox1.Text += "第 " + show_lyrics_index.ToString() + " 首, author : " + str_author + " , title : " + str_title + "\n";

                show_string0 = current_strings[0];
                show_string1 = current_strings[1].Remove(0, 1); //remove '&'
                if(lines_in_this_lyrics > 1)
                    show_string2 = current_strings[2];

                if (lines_in_this_lyrics > 2)
                    flag_playing = 1;
                else
                {
                    flag_playing = 0;
                    flag_playing_step = 0;
                    show_lyrics_index++;
                }

                f = new Font("標楷體", 24);
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

            }
            else
            {
                richTextBox1.Text += "接著播\n";
                //接著之前的資料
                flag_playing_step++;
                if(flag_playing_step == 1)
                {
                    if(lines_in_this_lyrics > 3)
                        show_string0 = current_strings[3];
                    if(lines_in_this_lyrics > 4)
                        show_string1 = current_strings[4];
                    if (lines_in_this_lyrics > 5)
                        show_string2 = current_strings[5];
                }
                else if(flag_playing_step == 2)
                {
                    if(lines_in_this_lyrics > 6)
                        show_string0 = current_strings[6];
                    if(lines_in_this_lyrics > 7)
                        show_string1 = current_strings[7];
                    if (lines_in_this_lyrics > 8)
                        show_string2 = current_strings[8];
                }
                else if(flag_playing_step == 3)
                {
                    if(lines_in_this_lyrics > 9)
                        show_string0 = current_strings[9];
                    if(lines_in_this_lyrics > 10)
                        show_string1 = current_strings[10];
                    if(lines_in_this_lyrics > 11)
                        show_string2 = current_strings[11];
                }

                if (lines_in_this_lyrics <= (flag_playing_step * 3 + 2))
                {
                    flag_playing = 0;
                    show_lyrics_index++;
                    flag_playing_step = 0;
                    //if (show_lyrics_index > lyrics_count)
                        //richTextBox1.Text += "顯示完畢\n";
                    if (show_lyrics_index >= lyrics_count)
                    {
                        show_lyrics_index = 0;
                    }
                }
            }


            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            //richTextBox1.Text += "pictureBox W = " + pictureBox1.Width.ToString() + "\t";
            //richTextBox1.Text += "H = " + pictureBox1.Height.ToString() + "\n";

            Pen p;
            p = new Pen(Color.Red, 3);

            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            /*
            g.DrawRectangle(p, pictureBox1.Width * 5 / 100, pictureBox1.Height * 5 / 100, pictureBox1.Width * 90 / 100 - 1, pictureBox1.Height * 90 / 100 - 1);
            g.DrawRectangle(p, pictureBox1.Width * 10 / 100, pictureBox1.Height * 10 / 100, pictureBox1.Width * 80 / 100 - 1, pictureBox1.Height * 80 / 100 - 1);
            g.DrawRectangle(p, pictureBox1.Width * 20 / 100, pictureBox1.Height * 20 / 100, pictureBox1.Width * 60 / 100 - 1, pictureBox1.Height * 60 / 100 - 1);
            g.DrawRectangle(p, pictureBox1.Width * 30 / 100, pictureBox1.Height * 30 / 100, pictureBox1.Width * 40 / 100 - 1, pictureBox1.Height * 40 / 100 - 1);
            g.DrawRectangle(p, pictureBox1.Width * 40 / 100, pictureBox1.Height * 40 / 100, pictureBox1.Width * 20 / 100 - 1, pictureBox1.Height * 20 / 100 - 1);
            */

            g.DrawString(show_string0, f, new SolidBrush(Color.Black), 0 + show_waist_size * 3 + show_max_height_size * 2, show_head_size, drawFormat);
            g.DrawString(show_string1, f, new SolidBrush(Color.Black), 0 + show_waist_size * 2 + show_max_height_size, show_head_size, drawFormat);
            g.DrawString(show_string2, f, new SolidBrush(Color.Black), 0 + show_waist_size, show_head_size, drawFormat);

            pictureBox1.Image = bmp;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            slide_show_string();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            timer1_Tick(sender, e);

            /*
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
            //Application.Exit();
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
            timer1_Tick(sender, e);
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
    }
}
