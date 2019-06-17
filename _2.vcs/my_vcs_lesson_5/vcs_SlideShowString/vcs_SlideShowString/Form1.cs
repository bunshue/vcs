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
        bool flag_debug_mode = true;
        //bool flag_need_author = true;
        //bool flag_need_title = true;

        Bitmap bmp;
        //bool flag_pause = false;
        //int cnt = 0;
        //int total = 100;
        int W;
        int H;
        int i = 0;

        string filepath = "C:\\______test_vcs\\poetry.txt";

        List<String> strings = new List<String>();
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
        string string1 = String.Empty;
        string string2 = String.Empty;
        string string3 = String.Empty;
        string string4 = String.Empty;
        string string5 = String.Empty;
        string string6 = String.Empty;
        string string7 = String.Empty;
        string string8 = String.Empty;
        string string9 = String.Empty;
        string string10 = String.Empty;
        string string11 = String.Empty;

        Graphics g;
        SolidBrush sb;
        Font f;

        public Form1()
        {
            InitializeComponent();
            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bmp);
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 24);
        }

        void loadTextData()
        {
            if (System.IO.File.Exists(filepath) == false)
            {
                richTextBox1.Text += "檔案 " + filepath + " 不存在，離開。\n";
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
                    strings.Add(line);
                }
                strings_count = strings.Count;
                sr.Close();
            }

            richTextBox1.Text += "共有 " + lyrics_count.ToString() + " 首\n";
            richTextBox1.Text += "可用行數 " + strings_count.ToString() + "\n";
            show_lyrics_index = 0;
            return;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lyrics_index.Text = "";

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.Text += "目前解析度  " + screenWidth.ToString() + " X " + screenHeight.ToString() + "\n";

            /*
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;

            if (flag_debug_mode == false)
            {
                this.Location = new System.Drawing.Point(screenWidth - 250, 200);
            }
            */


            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);

            if (flag_debug_mode == false)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new System.Drawing.Point(screenWidth - 250, 200);
                this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
            }

            loadTextData();

            timer1_Tick(sender, e);
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
            int head;
            int waist;
            int max_width = 0;
            int max_height = 0;

            int flag_get_lyrics_index = 0;
            int flag_get_text_data = 0;

            int cnt = 0;

            String show_string0 = String.Empty;
            String show_string1 = String.Empty;
            String show_string2 = String.Empty;


            lyrics_index.Text = (show_lyrics_index + 1).ToString() + " / " + lyrics_count.ToString();

            if (flag_playing == 0)
            {
                //richTextBox1.Text += "flag_get_lyrics_index = " + flag_get_lyrics_index.ToString() + "\n";
                //richTextBox1.Text += "show_lyrics_index = " + show_lyrics_index.ToString() + "\n";
                //richTextBox1.Text += "strings_count = " + strings_count.ToString() + "\n";


                //從頭播起
                for (i = 0; i < strings_count; i++)
                {
                    //richTextBox1.Text += "i = " + i.ToString() + " first = " + strings[i][0] + "\n";
                    if (strings[i][0] == '@')   //author
                    {
                        if (flag_get_text_data == 1)
                        {
                            flag_get_text_data = 0;
                            break;
                        }
                        str_author = strings[i].Remove(0, 1);
                    }
                    else if (strings[i][0] == '#')  //title
                    {
                        if (flag_get_text_data == 1)
                        {
                            flag_get_text_data = 0;
                            break;
                        }
                        str_title = strings[i].Remove(0, 1);
                    }
                    else if (strings[i][0] == '&')  //text
                    {
                        if (flag_get_lyrics_index == show_lyrics_index)
                        {
                            richTextBox1.Text += "let flag_get_text_data = 1\n";
                            flag_get_text_data = 1;
                            cnt = 0;
                            string1 = String.Empty;
                            string2 = String.Empty;
                            string3 = String.Empty;
                            string4 = String.Empty;
                            string5 = String.Empty;
                            string6 = String.Empty;
                            string7 = String.Empty;
                            string8 = String.Empty;
                            string9 = String.Empty;
                            string10 = String.Empty;
                            string11 = String.Empty;
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
                        if (cnt == 1)
                        {
                            string1 = strings[i].Remove(0, 1);
                        }
                        else if (cnt == 2)
                            string2 = strings[i];
                        else if (cnt == 3)
                            string3 = strings[i];
                        else if (cnt == 4)
                            string4 = strings[i];
                        else if (cnt == 5)
                            string5 = strings[i];
                        else if (cnt == 6)
                            string6 = strings[i];
                        else if (cnt == 7)
                            string7 = strings[i];
                        else if (cnt == 8)
                            string8 = strings[i];
                        else if (cnt == 9)
                            string9 = strings[i];
                        else if (cnt == 10)
                            string10 = strings[i];
                        else if (cnt == 11)
                            string11 = strings[i];
                        lines_in_this_lyrics = cnt;
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

                richTextBox1.Text += "第 " + show_lyrics_index.ToString() + " 首, 長度 " + lines_in_this_lyrics.ToString() + " 行\n";
                richTextBox1.Text += "第 " + show_lyrics_index.ToString() + " 首, author : " + str_author + " , title : " + str_title + "\n";

                show_string0 = string0;
                show_string1 = string1;
                show_string2 = string2;

                if (lines_in_this_lyrics > 2)
                    flag_playing = 1;
                else
                {
                    flag_playing = 0;
                    flag_playing_step = 0;
                    show_lyrics_index++;
                }
            }
            else
            {
                //接著之前的資料
                flag_playing_step++;
                if(flag_playing_step == 1)
                {
                    if(lines_in_this_lyrics >= 3)
                        show_string0 = string3;
                    if(lines_in_this_lyrics >= 4)
                        show_string1 = string4;
                    if(lines_in_this_lyrics >= 5)
                        show_string2 = string5;
                }
                else if(flag_playing_step == 2)
                {
                    if(lines_in_this_lyrics >= 6)
                        show_string0 = string6;
                    if(lines_in_this_lyrics >= 7)
                        show_string1 = string7;
                    if(lines_in_this_lyrics >= 8)
                        show_string2 = string8;
                }
                else if(flag_playing_step == 3)
                {
                    if(lines_in_this_lyrics >= 9)
                        show_string0 = string9;
                    if(lines_in_this_lyrics >= 10)
                        show_string1 = string10;
                    if(lines_in_this_lyrics >= 11)
                        show_string2 = string11;
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


            richTextBox1.Text += "pictureBox W = " + pictureBox1.Width.ToString() + "\t";
            richTextBox1.Text += "H = " + pictureBox1.Height.ToString() + "\n";

            Pen p;
            p = new Pen(Color.Red, 3);

            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height);

            Size sss;

            sss = g.MeasureString(show_string0, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 150, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            sss = g.MeasureString(show_string1, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 100, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            sss = g.MeasureString(show_string2, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 50, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            richTextBox1.Text += "max_width = " + max_width.ToString() + "\t";
            richTextBox1.Text += "max_height = " + max_height.ToString() + "\n";

            if (max_width < pictureBox1.Height)
                head = (pictureBox1.Height - max_width) / 2;
            else
                head = 0;

            if (max_height * 3 < pictureBox1.Width)
                waist = (pictureBox1.Width - max_height * 3) / 4;
            else
                waist = 0;

            richTextBox1.Text += "head = " + head.ToString() + "\t";
            richTextBox1.Text += "waist = " + waist.ToString() + "\n";

            g.DrawString(show_string0, f, new SolidBrush(Color.Black), 0 + waist * 3 + max_height * 2, head, drawFormat);
            g.DrawString(show_string1, f, new SolidBrush(Color.Black), 0 + waist * 2 + max_height, head, drawFormat);
            g.DrawString(show_string2, f, new SolidBrush(Color.Black), 0 + waist, head, drawFormat);


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
            richTextBox1.Text += "共有 " + strings.Count.ToString() + " 個字串\n";


            for (int i = 0; i < strings.Count; i++)
            {
                richTextBox1.Text += strings[i] + "\n";
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
    }
}
