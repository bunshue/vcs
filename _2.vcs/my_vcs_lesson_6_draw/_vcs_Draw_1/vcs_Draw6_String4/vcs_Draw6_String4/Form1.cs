using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Gif;
using Gif.Components;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_Draw6_String4
{
    public partial class Form1 : Form
    {
        float font_size = 0;
        //int WordSize;
        int SelectFont;

        public Bitmap bitmap1 = null;

        bool flag_making_pictures = false;
        int making_pictures_count = 0;

        int moving_steps = 4;

        Font font = new Font("標楷體", 22);

        Color foreground_color = Color.Blue;
        Color background_color = Color.Pink;

        string showing_text = string.Empty;
        int xx = 20;
        int yy = 20;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            string Path;
            //檢查存圖的資料夾
            Path = Application.StartupPath + "\\png2gif";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }

            Path = Application.StartupPath + "\\pngfiles";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }

            //textBox1.Text = "世界和平統一家庭聯合會，簡稱統一教，原名世界基督教統一神靈協會，是由文鮮明於1954年在韓國創立的新興宗教。";
            textBox1.Text = "世界和平統一家庭聯合會";
            //textBox1.Text = "世界和平統一家庭聯合會，簡稱統一教，原名";
            showing_text = textBox1.Text;

            bitmap1 = (Bitmap)vcs_Draw6_String4.Properties.Resources.Unification_Church_symbol_svg;

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            xx = pictureBox1.Width;

            nud_x_st.Value = xx;
            nud_y_st.Value = yy;
            nud_w.Value = pictureBox1.Width;
            nud_h.Value = pictureBox1.Height;

            nud_x_st.ValueChanged += new EventHandler(setup_banner_profile);
            nud_y_st.ValueChanged += new EventHandler(setup_banner_profile);
            nud_w.ValueChanged += new EventHandler(setup_banner_profile);
            nud_h.ValueChanged += new EventHandler(setup_banner_profile);
            font_size = font.Size;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            //this.Size = new Size(1700, 960);
            this.Text = "vcs_Draw6_String4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            /* debug
            string text1 = "從顧客";
            string text2 = "從顧客、競";
            string text3 = "從顧客、競爭對";
            string text4 = "從顧客、競爭對手、自家公";
            string text5 = "從顧客、競爭對手、自家公司、";
            string text6 = "從顧客、競爭對手、自家公司、通路找";
            string text7 = "從顧客、競爭對手、自家公司、通路找出成功因素，";

            string text = "從顧客、競爭對手、自家公司、通路找出成功因素，建立戰略的手法。";

            //text = text2;
            richTextBox1.Text += text + "\n";

            int len = text.Length;
            for (int i = 0; i < len; i++)
            {
                string tt = text.Substring(0, i + 1);
                richTextBox1.Text += tt + "\n";
                get_string_size(tt);
            }
            //richTextBox1.Text += text1(0:10);
            */
        }

        //------------------------------------------------------------  # 60個

        private void setup_banner_profile(object sender, EventArgs e)
        {
            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            yy = y_st;

            pictureBox1.Size = new Size(w, h);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();

            if (flag_making_pictures == true)
            {
                making_pictures_count += timer1.Interval;
                if (making_pictures_count > 1000)
                {
                    making_pictures_count = 0;
                    richTextBox1.Text += "X";

                    save_picturebox_to_image();
                }
            }
        }

        int cnt = 0;
        void save_picturebox_to_image()
        {
            Bitmap bmp = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
            Graphics g = Graphics.FromImage(bmp);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, Size blockRegionSize);
            //g.CopyFromScreen(this.pictureBox1.Location, new Point(0, 0), new Size(this.pictureBox1.Width, this.pictureBox1.Height));

            int x_st = 5 + 3;
            int y_st = 10 + 5 + 5 + 5 + 5;
            int W = pictureBox1.Width + x_st;
            int H = pictureBox1.Height + y_st;
            g.CopyFromScreen(this.Location.X + pictureBox1.Location.X + (int)x_st, this.Location.Y + pictureBox1.Location.Y + (int)y_st, 0, 0, new Size(W, H));

            //richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            //richTextBox1.Text += "H = " + this.Height.ToString() + "\n";

            string filename = Application.StartupPath + "\\pngfiles\\png_" + cnt.ToString("D4") + ".png";

            bmp.Save(filename, ImageFormat.Png);

            //存成jpg檔
            //String filename = Application.StartupPath + "\\picture\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //myImage.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
            cnt++;
        }

        //6060

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += textBox1.Text + "\n";
            timer1.Enabled = false;

            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            xx = pictureBox1.Width;
            yy = y_st;

            making_pictures_count = 0;
            flag_making_pictures = true;

            timer1.Enabled = true;
            button1.BackColor = Color.Red;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀PNG 做成GIF\n";
            string dirname = @"png2gif";
            string filename = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

            PngsToGif(dirname, filename, 500, true);

            richTextBox1.Text += "資料夾 : " + dirname + "\n製成 : " + filename + "\n";
            richTextBox1.Text += "完成\n";
        }

        /// 把directory文件夹里的png文件生成为gif文件，放在giffile
        /// <param name="directory">png文件夹</param>
        /// <param name="giffile">gif保存路径</param>
        /// <param name="time">每帧的时间/ms</param>
        /// <param name="repeat">是否重复</param>
        public static void PngsToGif(string directory, string giffile, int time, bool repeat)
        {
            //把多张Png文件转成Gif文件

            //一般文件名按顺序排
            string[] pngfiles = Directory.GetFileSystemEntries(directory, "*.png");

            AnimatedGifEncoder e = new AnimatedGifEncoder();
            e.Start(giffile);

            //每帧播放时间
            e.SetDelay(time);

            //-1：不重复，0：重复
            e.SetRepeat(repeat ? 0 : -1);
            for (int i = 0, count = pngfiles.Length; i < count; i++)
            {
                e.AddFrame(Image.FromFile(pngfiles[i]));
            }
            e.Finish();
        }

        private void bt_font_setup_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = font;
            fontDialog1.Color = foreground_color;

            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                font = fontDialog1.Font;
                foreground_color = fontDialog1.Color;
            }
        }

        private void cb_font_style_CheckedChanged(object sender, EventArgs e)
        {
            if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
                }
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Bold | FontStyle.Italic);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Bold | FontStyle.Italic);
                }
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Bold | FontStyle.Underline);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Bold | FontStyle.Underline);
                }
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Italic | FontStyle.Underline);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Italic | FontStyle.Underline);
                }
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Bold);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Bold);
                }
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Underline);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Underline);
                }
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Italic);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Italic);
                }
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                {
                    font = new Font("標楷體", font_size, FontStyle.Regular);
                }
                else if (SelectFont == 2)
                {
                    font = new Font("新細明體", font_size, FontStyle.Regular);
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            showing_text = textBox1.Text;
        }

        void get_string_size(string text)
        {
            Font font = new Font("標楷體", 60);
            /*
            richTextBox1.Text += font + "\n";
            richTextBox1.Text += font.Name + "\n";
            richTextBox1.Text += font.Size + "\n";
            richTextBox1.Text += "len = " + text.Length + "\n";
            */
            int tmp_width = 0;
            int tmp_height = 0;
            string str = text;

            Graphics g = this.pictureBox1.CreateGraphics();
            tmp_width = g.MeasureString(str, font).ToSize().Width;
            tmp_height = g.MeasureString(str, font).ToSize().Height;
            richTextBox1.Text += "len = " + str.Length + "\t";
            richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";

            return;
        }

        private void bt_open_picture_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            //openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\__pic\_ntuh";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                //filename = openFileDialog1.FileName;

                //reset_picture();

                //讀取圖檔, 先放在Bitmap裏
                string filename = openFileDialog1.FileName;
                bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                //pictureBox1.Image = bitmap1;
                bt_open_picture.BackgroundImage = bitmap1;
                this.pictureBox1.Invalidate();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        int dx = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = bitmap1.Width;
            int h = bitmap1.Height;
            //richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            //richTextBox1.Text += "w = " + h.ToString() + ", W = " + h.ToString() + "\n";

            /*
            //bm_contrast = new Bitmap(ww2, hh2);
            Bitmap bmp = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);

            //pictureBox1.BackgroundImage = bmp;
            */

            int ww = 100;
            int hh = 100;
            int x_st = (W - ww) / 2;
            int y_st = 0;
            int left = (W - ww) / 2;

            //原圖貼上
            //                      貼上位置x      貼上位置y      貼上大小W            貼上大小H
            //e.Graphics.DrawImage(bitmap1, x_st, y_st, bitmap1.Width * 12 / 10, bitmap1.Height * 12 / 10);
            e.Graphics.DrawImage(bitmap1, x_st, y_st, ww, hh);

            Pen pen = new Pen(Color.Red, 2);
            //Rectangle rect = SelectionRectangle(true);
            //e.Graphics.DrawRectangle(pen, 0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);

            pen.Color = Color.Green;
            pen.DashPattern = new float[] { 5, 5 };
            //e.Graphics.DrawRectangle(pen, 5, 5, pictureBox1.Size.Width - 10, pictureBox1.Size.Height - 10);

            string text = textBox1.Text;
            /*
            richTextBox1.Text += font + "\n";
            richTextBox1.Text += font.Name + "\n";
            richTextBox1.Text += font.Size + "\n";
            richTextBox1.Text += "len = " + text.Length + "\n";
            */
            int tmp_width = 0;
            int tmp_height = 0;

            tmp_width = e.Graphics.MeasureString(text, font).ToSize().Width;
            tmp_height = e.Graphics.MeasureString(text, font).ToSize().Height;
            //richTextBox1.Text += "len = " + text.Length + "\t";
            //richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\t";

            xx -= moving_steps;

            if (xx < left + ww)
            {
                dx = 100;
            }
            else
            {
                dx = 0;
            }

            SolidBrush sb = new SolidBrush(foreground_color);
            if ((xx + tmp_width) < (left + dx))
            {
                e.Graphics.DrawString(text, font, sb, xx - dx, yy);
            }
            else if (xx > (left + ww))
            {
                e.Graphics.DrawString(text, font, sb, xx - dx, yy);
            }
            else
            {
                //e.Graphics.DrawString(text, font, Brushes.Red, xx - dx, yy);
                int len = text.Length;
                int every_word_width = tmp_width / len;

                int over = left + ww - xx;
                int left_word = over / every_word_width;
                if (left_word == 0)
                {
                    left_word = 1;
                }

                string left_string = text.Substring(0, left_word);
                //richTextBox1.Text += left_word.ToString() + " ";
                if (left_word == 1)
                {
                    e.Graphics.DrawString(left_string, font, sb, xx - dx - 10, yy);
                }
                else
                {
                    e.Graphics.DrawString(left_string, font, sb, xx - dx - 10, yy);
                }

                int dd = left_word * every_word_width + ww + 40;

                string right_string = text.Substring(left_word, len - left_word);
                e.Graphics.DrawString(right_string, font, sb, xx - dx + dd, yy);
                //string tt = text.Substring(0, i + 1);
            }

            //e.Graphics.DrawString(text, font, sb, xx - dx, yy);

            //e.Graphics.DrawRectangle(Pens.Red, xx, yy, tmp_width, tmp_height);
            //richTextBox1.Text += xx.ToString() + " ";
            if ((xx + tmp_width) < 0)
            {
                xx = pictureBox1.Width;

                if (flag_making_pictures == true)
                {
                    flag_making_pictures = false;
                    richTextBox1.Text += "製作完成";
                    button1.BackColor = SystemColors.ControlLight;
                }
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//lb_moving1.Font.Size = 10F;
//this.comboBox_drive.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));


