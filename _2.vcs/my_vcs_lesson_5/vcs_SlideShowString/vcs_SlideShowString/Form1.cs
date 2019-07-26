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

        bool flag_debug_message = true;    //print some message, font size, timer cnt, index.....

        string filepath_setup = "poetry.ini";
        string filepath_poetry = "poetry.txt";
        //string filepath_poetry = "poetry_debug.txt";

        Graphics g;
        Font f;
        Bitmap bmp;
        int W = 0;      //final pictureBox1.Width for display
        int H = 0;      //final pictureBox1.Height for display
        int w = 0;      //final string width for display
        int h = 0;      //final string height for display
        int i = 0;

        List<String> all_strings = new List<String>();
        List<String> current_strings = new List<String>();  //new List<string>物件

        private const int SKY = 50;
        private const int EARTH = 30;
        private const int BORDER = 10;
        private const int D1 = 30;
        private const int D2 = 12;
        private const int D3 = 6;
        private const int PLAYMODE_SEQUENCE = 0;
        private const int PLAYMODE_RANDOM = 1;
        private const int MOVE_STEP = 50;

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
        string font_type = String.Empty;
        int font_size_default = 0;
        int font_size_user = 0;
        float font_size_current;
        float font_size_current_max;
        int display_width = 0;      //percentage
        int display_height = 0;     //percentage
        int slide_show_interval = 0;
        bool flag_top_most = false;
        bool flag_pause = false;
        int setda = 0;  //setda = sky + earth + T + A + d1 + d2 + d3 + d2 + d3 = H - dd * 2
        int title_width = 0;    //T
        int author_width = 0;   //A
        int tmp_width = 0;
        int tmp_height = 0;
        int flag_down_up_cnt = 0;
        int flag_right_left_cnt = 0;
        int[] random_play_sequence = new int[1024];
        int random_play_sequence_index = 0;
        int move_step = MOVE_STEP;
        
        public Form1()
        {
            InitializeComponent();
        }

        bool loadTextSetup()
        {
            bool flag_skip_comment = false;
            if (System.IO.File.Exists(filepath_setup) == false)
            {
                richTextBox1.Text += "setup檔案 " + filepath_setup + " 不存在，製作一個。";

                StreamWriter sw = File.CreateText(filepath_setup);      //StreamWriter，使用 UTF-8 編碼方式寫入指定檔案。

                string content = "";
                content += "^0\n";
                content += "//設定對齊方向0:靠右，1:靠左，2:正中\n";
                content += "\n";
                content += "~1\n";
                content += "//設定順序0:依序，1:隨機\n";
                content += "\n";
                content += "<M\n";
                content += "//設定字型大小X:超大(36)，L:大(24)，M:中(20)，S:小(16)，U:自訂\n";
                content += "\n";
                content += ">18\n";
                content += "//自訂字型大小\n";
                content += "\n";
                content += "?細明體\n";
                content += "?微軟正黑體\n";
                content += "?標楷體\n";
                content += "//設定顯示字型\n";
                content += "\n";
                content += "{10\n";
                content += "//播放速度:秒，寫0為停止自動播放\n";
                content += "\n";
                content += "[1\n";
                content += "//最上層顯示0:否，1:是\n";
                content += "\n";
                content += "width:15\n";
                content += "\n";
                content += "height:75\n";
                content += "\n";

                sw.WriteLine(content);
                sw.Close();

                richTextBox1.Text += "setup檔案 " + filepath_setup + " 製作完成並載入\n";
                loadTextSetup();
                return true;
            }
            else
            {
                richTextBox1.Text += "setup檔案 " + filepath_setup + " 存在, 開啟，並讀入文字資料\n";

                string line;
                //StreamReader sr = new StreamReader(filepath_setup, Encoding.Default);
                StreamReader sr = new StreamReader(filepath_setup, Encoding.UTF8);

                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine().Trim();            // 讀取文字到 line 變數
                    if (line.Length < 2)
                        continue;

                    if ((line[line.Length - 2] == '*') && (line[line.Length - 1] == '/'))
                    {
                        //richTextBox1.Text += "got comment SP : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        flag_skip_comment = false;
                        continue;
                    }
                    else if (flag_skip_comment == true)
                    {
                        //richTextBox1.Text += "got comment : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        continue;
                    }
                    else if ((line[0] == '/') && (line[1] == '*'))
                    {
                        flag_skip_comment = true;
                        //richTextBox1.Text += "got comment ST : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
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
                        {
                            play_sequence = PLAYMODE_SEQUENCE;
                            richTextBox1.Text += "依序\n";
                        }
                        else if (play_sequence == '1')
                        {
                            play_sequence = PLAYMODE_RANDOM;
                            richTextBox1.Text += "隨機\n";
                        }
                        else
                        {
                            play_sequence = PLAYMODE_SEQUENCE;
                            richTextBox1.Text += "依序\n";
                        }
                    }
                    else if (line[0] == '<')
                    {
                        if (line[1] == 'X')
                        {
                            font_size_default = 36;
                        }
                        else if (line[1] == 'L')
                        {
                            font_size_default = 24;
                        }
                        else if (line[1] == 'M')
                        {
                            font_size_default = 20;
                        }
                        else if (line[1] == 'S')
                        {
                            font_size_default = 16;
                        }
                        else if (line[1] == 'U')
                        {
                            font_size_default = -1;
                        }
                        richTextBox1.Text += "設定預設字型大小: " + font_size_default.ToString() + "\n";
                    }
                    else if (line[0] == '>')
                    {
                        font_size_user = int.Parse(line.Remove(0, 1));
                        richTextBox1.Text += "自訂字型大小: " + font_size_user.ToString() + "\n";
                    }
                    else if (line[0] == '?')
                    {
                        font_type = line.Remove(0, 1);
                        richTextBox1.Text += "字型: " + font_type + "\n";
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
                    else if ((line[0] == '/') && (line[1] == '/'))
                    {
                        //comment
                        //richTextBox1.Text += "get comment" + line + "\n";
                        continue;
                    }
                    else if (line[0] == '&')
                    {
                        //richTextBox1.Text += "get text start" + line + "\n";
                        //line = line.Remove(0, 1);
                        //lyrics_count++;
                    }
                    else if (line.StartsWith("width"))
                    {
                        display_width = int.Parse(line.Remove(0, 6));
                        richTextBox1.Text += "display width = " + display_width.ToString() + " %\n";
                    }
                    else if (line.StartsWith("height"))
                    {
                        display_height = int.Parse(line.Remove(0, 7));
                        richTextBox1.Text += "display height = " + display_height.ToString() + " %\n";
                    }


                    //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";
                    //all_strings.Add(line);
                }
                //strings_count = all_strings.Count;
                sr.Close();

                //richTextBox1.Text += "共有 " + lyrics_count.ToString() + " 首\n";
                //richTextBox1.Text += "可用行數 " + strings_count.ToString() + "\n";

                if (font_size_default <= 0)
                {
                    if (font_size_user > 0)
                        font_size_default = font_size_user;
                    else
                        font_size_default = 16;
                }

                richTextBox1.Text += "設定字型大小: " + font_size_default.ToString() + "\n";


                if (font_type == string.Empty)
                {
                    font_type = "標楷體";
                }
                richTextBox1.Text += "設定字型: " + font_type + "\n";

                if ((display_width < 5) || (display_width > 100))
                {
                    display_width = 15;
                }
                if ((display_height < 5) || (display_height > 100))
                {
                    display_height = 70;
                }
                richTextBox1.Text += "顯示百分比: W = " + display_width.ToString() + " %, H = " + display_height.ToString() + " %\n";


                return true;
            }

        }

        bool loadTextData()
        {
            bool flag_skip_comment = false;
            if (System.IO.File.Exists(filepath_poetry) == false)
            {
                richTextBox1.Text += "poetry檔案 " + filepath_poetry + " 不存在，離開。\n";
                return false;
            }
            else
            {
                richTextBox1.Text += "poetry檔案 " + filepath_poetry + " 存在, 開啟，並讀入文字資料\n";

                string line;
                StreamReader sr = new StreamReader(filepath_poetry, Encoding.Default);

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
                        //richTextBox1.Text += "got comment SP : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        flag_skip_comment = false;
                        continue;
                    }
                    else if (flag_skip_comment == true)
                    {
                        //richTextBox1.Text += "got comment : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
                        continue;
                    }
                    else if ((line[0] == '/') && (line[1] == '*'))
                    {
                        flag_skip_comment = true;
                        //richTextBox1.Text += "got comment ST : " + line + "\t len = " + line.Length.ToString() + "\tskip\n";
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
                        {
                            play_sequence = PLAYMODE_SEQUENCE;
                            richTextBox1.Text += "依序\n";
                        }
                        else if (play_sequence == '1')
                        {
                            play_sequence = PLAYMODE_RANDOM;
                            richTextBox1.Text += "隨機\n";
                        }
                        else
                        {
                            play_sequence = PLAYMODE_SEQUENCE;
                            richTextBox1.Text += "依序\n";
                        }
                    }
                    else if (line[0] == '<')
                    {
                        if (line[1] == 'X')
                        {
                            font_size_default = 36;
                        }
                        else if (line[1] == 'L')
                        {
                            font_size_default = 24;
                        }
                        else if (line[1] == 'M')
                        {
                            font_size_default = 20;
                        }
                        else if (line[1] == 'S')
                        {
                            font_size_default = 16;
                        }
                        else if (line[1] == 'U')
                        {
                            font_size_default = -1;
                        }
                        richTextBox1.Text += "設定預設字型大小: " + font_size_default.ToString() + "\n";
                    }
                    else if (line[0] == '>')
                    {
                        font_size_user = int.Parse(line.Remove(0, 1));
                        richTextBox1.Text += "自訂字型大小: " + font_size_user.ToString() + "\n";
                    }
                    else if (line[0] == '?')
                    {
                        font_type = line.Remove(0, 1);
                        richTextBox1.Text += "字型: " + font_type + "\n";
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
                    else if (line.StartsWith("width"))
                    {
                        display_width = int.Parse(line.Remove(0, 6));
                        richTextBox1.Text += "display width = " + display_width.ToString() + " %\n";
                    }
                    else if (line.StartsWith("height"))
                    {
                        display_height = int.Parse(line.Remove(0, 7));
                        richTextBox1.Text += "display height = " + display_height.ToString() + " %\n";
                    }


                    //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";
                    all_strings.Add(line);
                }
                strings_count = all_strings.Count;
                sr.Close();

                richTextBox1.Text += "共有 " + lyrics_count.ToString() + " 首\n";
                richTextBox1.Text += "可用行數 " + strings_count.ToString() + "\n";


                /*
                if (font_size_default <= 0)
                {
                    if (font_size_user > 0)
                        font_size_default = font_size_user;
                    else
                        font_size_default = 16;
                }

                richTextBox1.Text += "設定字型大小: " + font_size_default.ToString() + "\n";


                if (font_type == string.Empty)
                {
                    font_type = "標楷體";
                }
                richTextBox1.Text += "設定字型: " + font_type + "\n";

                if ((display_width < 5) || (display_width > 100))
                {
                    display_width = 15;
                }
                if ((display_height < 5) || (display_height > 100))
                {
                    display_height = 70;
                }
                richTextBox1.Text += "顯示百分比: W = " + display_width.ToString() + " %, H = " + display_height.ToString() + " %\n";
                */

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
                show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);
                slide_show_string();
                do_mouse_wheel_cnt = timer2_cnt;
            }
            else
            {
                if (lyrics_count == 1)
                {
                    richTextBox1.Text += "只有一首, 不動作\n";
                    return;
                }

                richTextBox1.Text += "上一首\n";
                show_lyrics_index = get_prev_show_lyrics_index(show_lyrics_index);
                slide_show_string();
                do_mouse_wheel_cnt = timer2_cnt;

                flag_pause = true;
                timer1.Enabled = false;
                this.TopMost = false;
            }
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)
            {
                if (flag_pause == false)
                {
                    flag_pause = true;
                    timer1.Enabled = false;
                    this.TopMost = false;
                }
                else
                {
                    flag_pause = false;
                    timer1.Enabled = true;
                    timer1_cnt = 0;
                    if (flag_top_most == true)
                    {
                        this.TopMost = true;
                        g.DrawLine(new Pen(Brushes.SaddleBrown, 3), 0, H - 2, W - 1, H - 2);
                    }
                    else
                    {
                        this.TopMost = false;
                        g.DrawLine(new Pen(Brushes.SandyBrown, 3), 0, H - 2, W - 1, H - 2);
                    }
                }
                draw_pause_border();
                pictureBox1.Focus();
            }
            else if (e.KeyCode == Keys.PageDown)
            {
                richTextBox1.Text += "下一首\n";
                if (lyrics_count == 1)
                {
                    richTextBox1.Text += "只有一首, 不動作\n";
                    return;
                }
                show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);
                flag_pause = false;
                slide_show_string();
                timer1.Enabled = true;
                timer1_cnt = 0;
                if (flag_top_most == true)
                    this.TopMost = true;
                else
                    this.TopMost = false;
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                if (lyrics_count == 1)
                {
                    richTextBox1.Text += "只有一首, 不動作\n";
                    return;
                }

                richTextBox1.Text += "上一首\n";
                show_lyrics_index = get_prev_show_lyrics_index(show_lyrics_index);
                slide_show_string();
                timer2_cnt = 0;
                do_mouse_wheel_cnt = timer2_cnt;

                flag_pause = true;
                timer1.Enabled = false;
                this.TopMost = false;
            }
            else if (e.KeyCode == Keys.Up)
            {
                richTextBox1.Text += "Up\n";
            }
            else if (e.KeyCode == Keys.Down)
            {
                richTextBox1.Text += "Down\n";
            }
            else if (e.KeyCode == Keys.NumPad8)
            {
                richTextBox1.Text += "Up\n";
                flag_down_up_cnt--;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad9)
            {
                richTextBox1.Text += "Up\n";
                flag_down_up_cnt--;
                richTextBox1.Text += "Right\n";
                flag_right_left_cnt++;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad6)
            {
                richTextBox1.Text += "Right\n";
                flag_right_left_cnt++;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad3)
            {
                richTextBox1.Text += "Right\n";
                flag_right_left_cnt++;
                richTextBox1.Text += "Down\n";
                flag_down_up_cnt++;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad2)
            {
                richTextBox1.Text += "Down\n";
                flag_down_up_cnt++;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad1)
            {
                richTextBox1.Text += "Down\n";
                flag_down_up_cnt++;
                richTextBox1.Text += "Left\n";
                flag_right_left_cnt--;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad4)
            {
                richTextBox1.Text += "Left\n";
                flag_right_left_cnt--;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad7)
            {
                richTextBox1.Text += "Left\n";
                flag_right_left_cnt--;
                richTextBox1.Text += "Up\n";
                flag_down_up_cnt--;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.NumPad5)
            {
                richTextBox1.Text += "Restore position\n";
                flag_right_left_cnt = 0;
                flag_down_up_cnt = 0;
                slide_show_string();
            }
            else if (e.KeyCode == Keys.Home)
            {
                richTextBox1.Text += "Home\n";
                if (lyrics_count == 1)
                {
                    richTextBox1.Text += "只有一首, 不動作\n";
                    return;
                }
                show_lyrics_index = 0;
                flag_pause = false;
                slide_show_string();
                timer1.Enabled = true;
                timer1_cnt = 0;
            }
            else if (e.KeyCode == Keys.End)
            {
                richTextBox1.Text += "End\n";
                if (lyrics_count == 1)
                {
                    richTextBox1.Text += "只有一首, 不動作\n";
                    return;
                }
                show_lyrics_index = lyrics_count - 1;
                flag_pause = false;
                slide_show_string();
                timer1.Enabled = true;
                timer1_cnt = 0;
            }
            else if (e.KeyCode == Keys.Add)
            {
                font_size_default = (int)font_size_current;
                if (font_size_default < 40)
                {
                    font_size_default += 2;
                    richTextBox1.Text += "Add, font size = " + font_size_default.ToString() + "\n";
                    slide_show_string();
                }
            }
            else if (e.KeyCode == Keys.Subtract)
            {
                font_size_default = (int)font_size_current;
                if (font_size_default > 10)
                {
                    font_size_default -= 2;
                    richTextBox1.Text += "Subtract, font size = " + font_size_default.ToString() + "\n";
                    slide_show_string();
                }
            }
            else if ((e.KeyCode == Keys.X) || (e.KeyCode == Keys.Escape))
            {
                Application.Exit();
            }
            else if (e.KeyCode == Keys.F1)
            {
                richTextBox1.Text += "F1 : Help\n";
                this.TopMost = false;
                Form_Help help = new Form_Help();   //實體化Form_Help視窗物件
                help.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                help.ShowDialog();                  //顯示Form_Help視窗
            }
            else if (e.KeyCode == Keys.F10)
            {
                richTextBox1.Text += "F10 : Setup\n";
                this.TopMost = false;
                Form_Setup setup = new Form_Setup();   //實體化Form_Setup視窗物件
                setup.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                setup.ShowDialog();                  //顯示Form_Setup視窗
            }
            else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
            {
                if (e.KeyCode == Keys.W)
                {
                    if (display_width < 100)
                    {
                        display_width++;
                    }
                    richTextBox1.Text += "display width = " + display_width.ToString() + " %\n";
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.H)
                {
                    if (display_height < 100)
                    {
                        display_height++;
                    }
                    richTextBox1.Text += "display height = " + display_height.ToString() + " %\n";
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.T)
                {
                    flag_top_most = true;
                    richTextBox1.Text += "設定最上層顯示\n";
                }
                else if (e.KeyCode == Keys.R)
                {
                    richTextBox1.Text += "靠右\n";
                    align_direction = '0';
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.L)
                {
                    richTextBox1.Text += "靠左\n";
                    align_direction = '1';
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.C)
                {
                    richTextBox1.Text += "正中\n";
                    align_direction = '2';
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.F)
                {
                    if (slide_show_interval > 1)
                        slide_show_interval--;
                    richTextBox1.Text += "加速, " + slide_show_interval.ToString() + " 秒\n";
                }
                else if (e.KeyCode == Keys.S)
                {
                    slide_show_interval++;
                    richTextBox1.Text += "減速, " + slide_show_interval.ToString() + " 秒\n";
                }
                else if (e.KeyCode == Keys.Oemtilde)    //~
                {
                    if (play_sequence == PLAYMODE_SEQUENCE)
                    {   //依序 -> 隨機 從頭
                        richTextBox1.Text += "依序 -> 隨機 從頭\n";
                        play_sequence = PLAYMODE_RANDOM;
                        show_lyrics_index = random_play_sequence[0];
                    }
                    else if (play_sequence == PLAYMODE_RANDOM)
                    {   //隨機 -> 依序 從頭
                        richTextBox1.Text += "隨機 -> 依序 從頭\n";
                        play_sequence = PLAYMODE_SEQUENCE;
                        show_lyrics_index = 0;
                    }
                    else
                    {   //依序 從頭
                        richTextBox1.Text += "-> 依序 從頭\n";
                        play_sequence = PLAYMODE_SEQUENCE;
                        show_lyrics_index = 0;
                    }
                    slide_show_string();
                }
                else if (e.KeyCode == Keys.N)
                {
                    richTextBox1.Text += "念經模式, 字很大 佔很多 放中間\n";
                    display_width = 90;
                    display_height = 88;
                    font_size_default = 50;

                    align_direction = '2';  //正中

                    slide_show_string();
                }
            }
            else if (e.KeyCode == Keys.W)
            {
                if (display_width > 5)
                {
                    display_width--;
                }
                richTextBox1.Text += "display width = " + display_width.ToString() + " %\n";
                slide_show_string();
            }
            else if (e.KeyCode == Keys.H)
            {
                if (display_height > 5)
                {
                    display_height--;
                }
                richTextBox1.Text += "display height = " + display_height.ToString() + " %\n";
                slide_show_string();
            }
            else if (e.KeyCode == Keys.T)
            {
                flag_top_most = false;
                richTextBox1.Text += "設定非最上層顯示\n";
            }
            else if (e.KeyCode == Keys.F)
            {
                if (slide_show_interval > 1)
                    slide_show_interval--;
                richTextBox1.Text += "加速, " + slide_show_interval.ToString() + " 秒\n";
            }
            else if (e.KeyCode == Keys.S)
            {
                slide_show_interval++;
                richTextBox1.Text += "減速, " + slide_show_interval.ToString() + " 秒\n";
            }
            else if (e.KeyCode == Keys.D)
            {
                if (flag_debug_message == true)
                {
                    flag_debug_message = false;
                }
                else
                {
                    flag_debug_message = true;
                }
                slide_show_string();
            }
            else
            {
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";
            }
        } 

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件

            bool result;

            result = loadTextSetup();

            if (result == false)
                return;

            result = loadTextData();

            if (result == false)
                return;

            Random r = new Random();
            int tmp;

            for (i = 0; i < lyrics_count; i++)
            {
                random_play_sequence[i] = i;
            }

            /*
            richTextBox1.Text += "原陣列 : ";
            for (i = 0; i < lyrics_count; i++)
            {
                richTextBox1.Text += random_play_sequence[i].ToString() + " ";

            }
            richTextBox1.Text += "\n";
            */

            for (i = lyrics_count - 1; i > 0; i--)
            {
                int n = r.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = random_play_sequence[i];
                random_play_sequence[i] = random_play_sequence[n];
                random_play_sequence[n] = tmp;
            }

            //debug, 改成原數字反相
            for (i = 0; i < lyrics_count; i++)
            {
                //random_play_sequence[i] = lyrics_count - i - 1;
            }

            richTextBox1.Text += "不重覆亂數：";
            for (i = 0; i < lyrics_count; i++)
            {
                richTextBox1.Text += random_play_sequence[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //show_lyrics_index = 0;
            //show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);

            if (play_sequence == PLAYMODE_SEQUENCE)
            {   //依序
                show_lyrics_index = 0;
            }
            else if (play_sequence == PLAYMODE_RANDOM)
            {   //隨機
                show_lyrics_index = random_play_sequence[0];
            }
            else
                show_lyrics_index = 0;

            if (result == true)
            {
                slide_show_string();
                timer1.Enabled = true;
            }
            else
                timer1.Enabled = false;

            if (flag_release_mode == true)
            {
                richTextBox1.Visible = false;
                button1.Visible = false;
                button2.Visible = false;
                button3.Visible = false;
                button4.Visible = false;
                button5.Visible = false;
                button6.Visible = false;
                button7.Visible = false;
                button8.Visible = false;
            }
            else
            {
                richTextBox1.Visible = true;
                button1.Visible = true;
                button2.Visible = true;
                button3.Visible = true;
                button4.Visible = true;
                button5.Visible = true;
                button6.Visible = true;
                button7.Visible = true;
                button8.Visible = true;
            }
        }

        int calculate_picturebox_parameters()
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            int screenHeight_max = screenHeight * display_height / 100;
            int screenWidth_max = screenWidth * display_width / 100;

            //richTextBox1.Text += "SW X SH = " + screenWidth_max.ToString() + " X " + screenHeight_max.ToString() + "\n";

            lines_in_this_lyrics = current_strings.Count;

            /*
            richTextBox1.Text += "\ncurrent_strings 內容\tcount = " + current_strings.Count.ToString() + " (lines)\n";
            for (i = 0; i < current_strings.Count; i++)
            {
                richTextBox1.Text += current_strings[i] + "\n";
            }
            */

            int longest_length = 0;
            int longest_index = 0;
            int len = 0;
            for (i = 1; i < current_strings.Count; i++)
            {
                if (i == 1)
                {
                    //richTextBox1.Text += "第 " + i.ToString() + " 行 內容 " + current_strings[i] + " len = " + (current_strings[i].Length - 1).ToString() + "\n";
                    len = current_strings[i].Length - 1;

                }
                else
                {
                    //richTextBox1.Text += "第 " + i.ToString() + " 行 內容 " + current_strings[i] + " len = " + current_strings[i].Length.ToString() + "\n";
                    len = current_strings[i].Length;
                }
                if (longest_length < len)
                {
                    longest_length = len;
                    longest_index = i;
                }
            }
            richTextBox1.Text += "最長行 第 " + longest_index.ToString() + " 行 長度 " + longest_length.ToString() + "\n";

            w = 0;
            h = 0;

            if (longest_index == 1)
                w = g.MeasureString(current_strings[longest_index].Remove(0, 1), f).ToSize().Width;
            else
                w = g.MeasureString(current_strings[longest_index], f).ToSize().Width;

            h = g.MeasureString(current_strings[longest_index], f).ToSize().Height;


            /*
            for (i = 0; i < current_strings.Count; i++)
            {
                if (i == 1)
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
            */

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

            setda = sky + d1 + d2 + d3 + title_width + d2 + d3 + author_width + earth;      //H - dd * 2
            //richTextBox1.Text += "setda = " + setda.ToString() + "\n";


            int N = current_strings.Count;
            int p = 0;
            int border = BORDER;

            int tmp_W = h * N + p * (N * 2) + border * 2;

            richTextBox1.Text += "字型 " + f.Size.ToString() + "\t總寬度 = " + tmp_W.ToString() + "\t標題行長度 = " + setda.ToString() + "\t內文最長長度 = " + w.ToString() + "\t單行寬度 = " + h.ToString() + "\n";

            //richTextBox1.Text += "tmp_W = " + tmp_W.ToString() + "\n";

            if (tmp_W > screenWidth_max)
            {
                richTextBox1.Text += "總寬度太寬\n";
                return -1;
            }

            if (setda > screenHeight_max)
            {
                richTextBox1.Text += "標題行太長\n";
                return -1;
            }

            if (w > screenHeight_max)
            {
                richTextBox1.Text += "內文太長\n";
				return -1;
            }

            //richTextBox1.Text += "OK\n";
            return 0;
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

            //richTextBox1.Clear();
            richTextBox1.Text += "\n\n第 " + (show_lyrics_index + 1).ToString() + " 首, " + str_author + " " + str_title + ", 長度 " + lines_in_this_lyrics.ToString() + " 行\n";

            f = new Font(font_type, font_size_default);

            bmp = new Bitmap(100, 100);     //initial W, H
            g = Graphics.FromImage(bmp);

            richTextBox1.Text += "開始字型為 " + font_size_default.ToString() + "\n";

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            int screenHeight_max = screenHeight * display_height / 100;
            int screenWidth_max = screenWidth * display_width / 100;

            richTextBox1.Text += "最大邊界 SW X SH = " + screenWidth_max.ToString() + " X " + screenHeight_max.ToString() + "\n";

            //更新全首的畫圖邊界
            int result = -1;
            while (result == -1)
            {
                result = calculate_picturebox_parameters();
                if (result == -1)
                {
                    float fontsize;
                    fontsize = f.Size;
                    if (fontsize > 5)
                        fontsize -= 1;      //這個地方要考慮 若是字串超長 永遠無法滿足 該要如何處理例外
                    f = new Font(font_type, fontsize);
                    richTextBox1.Text += "縮小字型為 " + fontsize.ToString() + "\n";
                }
            }
            font_size_current = f.Size;

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

            if (H < setda)
            {
                H = setda;
                w = setda - sky - earth;
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

            draw_pause_border();

            if ((flag_debug_message == true) || (flag_release_mode == false))
            {
                string str;

                //顯示目前字型大小
                int fs;

                if (lines_in_this_lyrics <= 3)
                    fs = SKY / 4;
                else
                    fs = SKY / 3;

                str = font_size_current.ToString() + "/" + font_size_default.ToString() + "/" + display_width.ToString() + "/" + display_height.ToString();
                g.DrawString(str, new Font(font_type, fs), new SolidBrush(Color.Blue), new PointF(3, 13));

                //顯示曲目
                if (lines_in_this_lyrics <= 3)
                    fs = EARTH * 2 / 5;
                else
                    fs = EARTH * 2 / 5;

                str = (show_lyrics_index + 1).ToString() + "/" + lyrics_count.ToString();
                tmp_width = g.MeasureString(str, new Font(font_type, fs)).ToSize().Width;
                tmp_height = g.MeasureString(str, new Font(font_type, fs)).ToSize().Height;
                g.DrawString(str, new Font(font_type, fs), new SolidBrush(Color.Blue), new PointF((W - tmp_width) * 2 / 3, H - tmp_height - 3));
            }

            if (flag_release_mode == true)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                if (align_direction == '0')
                {   //靠右置中
                    x_st = screenWidth - W + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                else if (align_direction == '1')
                {   //靠左置中
                    x_st = 0 + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                else if (align_direction == '2')
                {   //正中置中
                    x_st = (screenWidth - W) / 2 + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                if (x_st < 0)
                    x_st = 0;
                if (y_st < 0)
                    y_st = 0;
                if ((x_st + W) > screenWidth)
                    x_st = screenWidth - W;
                if ((y_st + H) > screenHeight)
                    y_st = screenHeight - H;
                this.Location = new System.Drawing.Point(x_st, y_st);

                this.Size = new Size(W, H);
            }
            else
            {
                //pictureBox1.Location = new System.Drawing.Point(0 + flag_right_left_cnt * move_step, (this.Size.Height - H) / 2 + flag_down_up_cnt * move_step);
                pictureBox1.Location = new System.Drawing.Point(0 + flag_right_left_cnt * move_step, 0 + flag_down_up_cnt * move_step);
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new System.Drawing.Point(0, 0);
                richTextBox1.Text += "目前W = " + W.ToString() + " H = " + H.ToString() + "\n";

                richTextBox1.Size = new System.Drawing.Size(W * 3, H);
                richTextBox1.Location = new Point(W * 1 + 120, 0);

                button1.Location = new Point(W * 1 + 10, 10);
                button2.Location = new Point(W * 1 + 10, 50);
                button3.Location = new Point(W * 1 + 10, 90);
                button4.Location = new Point(W * 1 + 10, 130);
                button5.Location = new Point(W * 1 + 10, 170);
                button6.Location = new Point(W * 1 + 10, 210);
                button7.Location = new Point(W * 1 + 10, 250);
                button8.Location = new Point(W * 1 + 10, 290);

                this.Size = new Size(W * 4 + 120, H);
            }
            this.Text = str_title;

            timer1_cnt = 0;

            if (flag_top_most == true)
            {
                this.TopMost = true;
                g.DrawLine(new Pen(Brushes.SaddleBrown, 3), 0, H - 2, W - 1, H - 2);
            }
            else
            {
                this.TopMost = false;
                g.DrawLine(new Pen(Brushes.SandyBrown, 3), 0, H - 2, W - 1, H - 2);
            }
        }


        void reload_slide_show_string()
        {
            g.Clear(Color.Red);
            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);

            int i;

            /*
            richTextBox1.Text += "\n現在要播放 第 " + show_lyrics_index.ToString() + " 首" + "\n";
            richTextBox1.Text += "flag_get_lyrics_index = " + flag_get_lyrics_index.ToString() + "\n";
            richTextBox1.Text += "show_lyrics_index = " + show_lyrics_index.ToString() + "\n";
            richTextBox1.Text += "strings_count = " + strings_count.ToString() + "\n";

            //從頭播起 要更新 current_strings 資料
            richTextBox1.Text += "從頭播起 從大List裡找出第 " + show_lyrics_index.ToString() + "首的內容\n";
            */


            f = new Font(font_type, font_size_default);

            bmp = new Bitmap(100, 100);     //initial W, H
            g = Graphics.FromImage(bmp);

            richTextBox1.Text += "開始字型為 " + font_size_default.ToString() + "\n";

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            int screenHeight_max = screenHeight * display_height / 100;
            int screenWidth_max = screenWidth * display_width / 100;

            richTextBox1.Text += "最大邊界 SW X SH = " + screenWidth_max.ToString() + " X " + screenHeight_max.ToString() + "\n";

            font_size_current = f.Size;

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

            if (H < setda)
            {
                H = setda;
                w = setda - sky - earth;
            }

            bmp = new Bitmap(W, H);
            g = Graphics.FromImage(bmp);

            g.Clear(Color.SandyBrown);
            pictureBox1.Image = bmp;

            int x_st;
            int y_st;

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

            draw_pause_border();

            if ((flag_debug_message == true) || (flag_release_mode == false))
            {
                string str;

                //顯示目前字型大小
                int fs;

                if (lines_in_this_lyrics <= 3)
                    fs = SKY / 4;
                else
                    fs = SKY / 3;

                str = font_size_current.ToString() + "/" + font_size_default.ToString() + "/" + display_width.ToString() + "/" + display_height.ToString();
                g.DrawString(str, new Font(font_type, fs), new SolidBrush(Color.Blue), new PointF(3, 13));

                //顯示曲目
                if (lines_in_this_lyrics <= 3)
                    fs = EARTH * 2 / 5;
                else
                    fs = EARTH * 2 / 5;

                str = (show_lyrics_index + 1).ToString() + "/" + lyrics_count.ToString();
                tmp_width = g.MeasureString(str, new Font(font_type, fs)).ToSize().Width;
                tmp_height = g.MeasureString(str, new Font(font_type, fs)).ToSize().Height;
                g.DrawString(str, new Font(font_type, fs), new SolidBrush(Color.Blue), new PointF((W - tmp_width) * 2 / 3, H - tmp_height - 3));
            }

            if (flag_release_mode == true)
            {
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                if (align_direction == '0')
                {   //靠右置中
                    x_st = screenWidth - W + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                else if (align_direction == '1')
                {   //靠左置中
                    x_st = 0 + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                else if (align_direction == '2')
                {   //正中置中
                    x_st = (screenWidth - W) / 2 + flag_right_left_cnt * move_step;
                    y_st = (screenHeight - H) / 2 + flag_down_up_cnt * move_step;
                }
                if (x_st < 0)
                    x_st = 0;
                if (y_st < 0)
                    y_st = 0;
                if ((x_st + W) > screenWidth)
                    x_st = screenWidth - W;
                if ((y_st + H) > screenHeight)
                    y_st = screenHeight - H;
                this.Location = new System.Drawing.Point(x_st, y_st);

                this.Size = new Size(W, H);
            }
            else
            {
                pictureBox1.Location = new System.Drawing.Point(0 + flag_right_left_cnt * move_step, (this.Size.Height - H) / 2 + flag_down_up_cnt * move_step);
                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new System.Drawing.Point(0, 0);
            }
            this.Text = str_title;

            timer1_cnt = 0;

            if (flag_top_most == true)
            {
                this.TopMost = true;
                g.DrawLine(new Pen(Brushes.SaddleBrown, 3), 0, H - 2, W - 1, H - 2);
            }
            else
            {
                this.TopMost = false;
                g.DrawLine(new Pen(Brushes.SandyBrown, 3), 0, H - 2, W - 1, H - 2);
            }
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

            //richTextBox1.Text += "T";
            timer1_cnt++;

            if (timer1_cnt > slide_show_interval)
            {
                timer1_cnt = 0;
                show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);
                slide_show_string();
            }
            else
            {
                if ((flag_debug_message == true) || (flag_release_mode == false))  //顯示要換首的剩餘時間
                {
                    int fs = EARTH * 2 / 5;
                    string str = (slide_show_interval - timer1_cnt).ToString() + "/" + slide_show_interval.ToString();

                    tmp_width = g.MeasureString(str, new Font(font_type, fs)).ToSize().Width;
                    tmp_height = g.MeasureString(str, new Font(font_type, fs)).ToSize().Height;
                    g.FillRectangle(new SolidBrush(Color.SandyBrown), new Rectangle(3, H - tmp_height - 3, tmp_width, tmp_height));
                    g.DrawString(str, new Font(font_type, fs), new SolidBrush(Color.Blue), 3, H - tmp_height - 3);
                }
                pictureBox1.Image = bmp;
            }
        }

        bool flag_show_pause_border = false;

        void draw_pause_border()
        {
            if (flag_pause == true)
            {
                richTextBox1.Text += "畫邊框\n";
                g.FillRectangle(new SolidBrush(Color.SaddleBrown), new Rectangle(0, H - EARTH / 2, W, EARTH / 2));
                g.FillRectangle(new SolidBrush(Color.SaddleBrown), new Rectangle(0, 0, W, EARTH / 2));
                g.DrawRectangle(new Pen(Color.SaddleBrown, 2), 1, 1, W - 2, H - 2);
                flag_show_pause_border = true;
            }
            else if ((flag_pause == false) && (flag_show_pause_border == true))
            {
                richTextBox1.Text += "取消邊框\n";
                g.FillRectangle(new SolidBrush(Color.SandyBrown), new Rectangle(0, H - EARTH / 2, W, EARTH / 2));
                g.FillRectangle(new SolidBrush(Color.SandyBrown), new Rectangle(0, 0, W, EARTH / 2));
                g.DrawRectangle(new Pen(Color.SandyBrown, 2), 1, 1, W - 2, H - 2);
                flag_show_pause_border = false;
            }
            else
            {
                richTextBox1.Text += "不動作\n";
            }
            pictureBox1.Image = bmp;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
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
            /*
            if (lyrics_count == 1)
            {
                richTextBox1.Text += "只有一首, 不動作\n";
                return;
            }
            show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);
            slide_show_string();
            */

            /*  old pause method
            if (flag_pause == false)
            {
                flag_pause = true;
                timer1.Enabled = false;
                this.TopMost = false;
            }
            else
            {
                flag_pause = false;
                timer1.Enabled = true;
                timer1_cnt = 0;
                if (flag_top_most == true)
                {
                    this.TopMost = true;
                    g.DrawLine(new Pen(Brushes.SaddleBrown, 3), 0, H - 2, W - 1, H - 2);
                }
                else
                {
                    this.TopMost = false;
                    g.DrawLine(new Pen(Brushes.SandyBrown, 3), 0, H - 2, W - 1, H - 2);
                }
            }
            draw_pause_border();
            pictureBox1.Focus();
            */

            /*
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            int screenHeight_max = screenHeight * display_height / 100;
            int screenWidth_max = screenWidth * display_width / 100;

            richTextBox1.Text += "最大邊界 SW X SH = " + screenWidth_max.ToString() + " X " + screenHeight_max.ToString() + "\n";
            richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";
            richTextBox1.Text += "X = " + MousePosition.X.ToString() + " Y = " + MousePosition.Y.ToString() + "\n";
            richTextBox1.Text += "px = " + (pictureBox1.Location.X).ToString() + " py = " + (pictureBox1.Location.Y).ToString() + "\n";
            */

            //取得滑鼠在pictureBox1內的座標
            //int px = MousePosition.X - pictureBox1.Location.X;
            //int py = MousePosition.Y - pictureBox1.Location.Y;

            int px = MousePosition.X - pictureBox1.Location.X - this.Location.X;
            int py = MousePosition.Y - pictureBox1.Location.Y - this.Location.Y;
            /*
            richTextBox1.Text += "MousePosition.X = " + MousePosition.X.ToString() + " MousePosition.Y = " + MousePosition.Y.ToString() + "\n";
            richTextBox1.Text += "this.Location.X = " + this.Location.X.ToString() + " this.Location.Y = " + this.Location.Y.ToString() + "\n";
            richTextBox1.Text += "pictureBox1.Location.X = " + pictureBox1.Location.X.ToString() + " pictureBox1.Location.Y = " + pictureBox1.Location.Y.ToString() + "\n";
            richTextBox1.Text += "px = " + px.ToString() + " py = " + py.ToString() + "\n";

            if (px < (W / 3))
                richTextBox1.Text += "左\n";
            else if (px > (W * 2 / 3))
                richTextBox1.Text += "右\n";
            else
                richTextBox1.Text += "中\n";
            */
            if ((px > (W - BORDER - h)) && (px < W - BORDER) && (py > SKY) && (py < (SKY + D1)))
            {
                //g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(100, 100, 100, 100));
                int x_st = W - BORDER - h + pictureBox1.Location.X + this.Location.X;
                int y_st = SKY + pictureBox1.Location.Y + this.Location.X;
                //int ww = h;
                //int hh = D1;
                richTextBox1.Text += "PAUSE\n";
                //richTextBox1.Text += "x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + "\n";
                //richTextBox1.Text += "ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";
                //g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, ww, hh));

                if (flag_pause == false)
                {
                    flag_pause = true;
                    timer1.Enabled = false;
                    this.TopMost = false;
                }
                else
                {
                    flag_pause = false;
                    timer1.Enabled = true;
                    timer1_cnt = 0;
                    if (flag_top_most == true)
                    {
                        this.TopMost = true;
                        g.DrawLine(new Pen(Brushes.SaddleBrown, 3), 0, H - 2, W - 1, H - 2);
                    }
                    else
                    {
                        this.TopMost = false;
                        g.DrawLine(new Pen(Brushes.SandyBrown, 3), 0, H - 2, W - 1, H - 2);
                    }
                }
                draw_pause_border();
                pictureBox1.Focus();
            }
       
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
            show_lyrics_index = get_next_show_lyrics_index(show_lyrics_index);
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

        /*
        int get_next_show_lyrics_index(int current_show_lyrics_index)
        {
            if (lyrics_count == 1)
                return 0;

            if (play_sequence == PLAYMODE_SEQUENCE)
            {   //依序
                if (show_lyrics_index < (lyrics_count - 1))
                    show_lyrics_index++;
                else
                    show_lyrics_index = 0;
                if (current_show_lyrics_index == -1)
                    show_lyrics_index = 0;
                return show_lyrics_index;
            }
            else if (play_sequence == PLAYMODE_RANDOM)
            {   //隨機
                int next_show_lyrics_index = 0;

                if (random_play_sequence_index < (lyrics_count - 1))
                    random_play_sequence_index++;
                else
                    random_play_sequence_index = 0;

                next_show_lyrics_index = random_play_sequence[random_play_sequence_index];

                return next_show_lyrics_index;
            }
            else
                return 0;
        }
        */

        int get_next_show_lyrics_index(int current_show_lyrics_index)
        {
            if (lyrics_count == 1)
                return 0;

            font_size_current_max = 0;

            int next_show_lyrics_index = 0;

            if (play_sequence == PLAYMODE_SEQUENCE)
            {   //依序
                if (current_show_lyrics_index < (lyrics_count - 1))
                    current_show_lyrics_index++;
                else
                    current_show_lyrics_index = 0;
                next_show_lyrics_index = current_show_lyrics_index;
            }
            else if (play_sequence == PLAYMODE_RANDOM)
            {   //隨機
                if (random_play_sequence_index < (lyrics_count - 1))
                    random_play_sequence_index++;
                else
                    random_play_sequence_index = 0;
                next_show_lyrics_index = random_play_sequence[random_play_sequence_index];
            }
            else
                return 0;
            return next_show_lyrics_index;
        }

        int get_prev_show_lyrics_index(int current_show_lyrics_index)
        {
            if (lyrics_count == 1)
                return 0;

            font_size_current_max = 0;

            int prev_show_lyrics_index = 0;

            if (play_sequence == PLAYMODE_SEQUENCE)
            {   //依序
                if (current_show_lyrics_index > 0)
                    current_show_lyrics_index--;
                else
                    current_show_lyrics_index = lyrics_count - 1;
                prev_show_lyrics_index = current_show_lyrics_index;
            }
            else if (play_sequence == PLAYMODE_RANDOM)
            {   //隨機
                if (random_play_sequence_index > 0)
                    random_play_sequence_index--;
                else
                    random_play_sequence_index = lyrics_count - 1;
                prev_show_lyrics_index = random_play_sequence[random_play_sequence_index];
            }
            else
                return 0;
            return prev_show_lyrics_index;
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

            /*
            int next;
            next = get_next_show_lyrics_index(show_lyrics_index);

            richTextBox1.Text += "current = " + show_lyrics_index.ToString() + " next = " + next.ToString() + "\n";
            */

            richTextBox1.Text += "Reload\n";

            richTextBox1.Text += "\n\n第 " + (show_lyrics_index + 1).ToString() + " 首, " + str_author + " " + str_title + ", 長度 " + lines_in_this_lyrics.ToString() + " 行\n";

            richTextBox1.Text += "目前字型為 " + font_size_current.ToString() + "\n";

            richTextBox1.Text += "內容:\n";

            for (int i = 0; i < current_strings.Count; i++)
            {
                richTextBox1.Text += current_strings[i] + "\n";
            }


            reload_slide_show_string();


        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2_cnt++;
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox1.SelectionStart = richTextBox1.TextLength;
            richTextBox1.ScrollToCaret();

        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n顯示所有標題\n";

            int index = 0;
            for (int i = 0; i < all_strings.Count; i++)
            {
                if (all_strings[i][0] == '#')  //title
                {
                    index++;
                    richTextBox1.Text += index.ToString() + "\t" + all_strings[i].Remove(0, 1) + "\n";
                }
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }
    }
}

