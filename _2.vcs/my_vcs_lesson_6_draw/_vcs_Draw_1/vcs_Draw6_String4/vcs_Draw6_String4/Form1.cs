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

using System.Drawing.Text;  //for InstalledFontCollection, PrivateFontCollection

namespace vcs_Draw6_String4
{
    public partial class Form1 : Form
    {
        int WordSize;
        int SelectFont;

        Label lb_moving = new Label();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = "世界和平統一家庭聯合會，簡稱統一教，原名世界基督教統一神靈協會，是由文鮮明於1954年在韓國創立的新興宗教。";

            // 實例化控件

            lb_moving.Text = textBox1.Text;
            lb_moving.Font = new Font("標楷體", 22);
            lb_moving.ForeColor = Color.Black;
            lb_moving.Location = new Point(20, 20);
            lb_moving.AutoSize = true;
            this.pictureBox1.Controls.Add(lb_moving);     // 將控件加入表單

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            lb_moving.Left -= 4;
            if (lb_moving.Right < 0)
            {
                lb_moving.Left = this.Width;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += textBox1.Text + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀PNG 做成GIF\n";
            string dirname = @"png2gif";
            string filename = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

            PngsToGif(dirname, filename, 500, true);

            richTextBox1.Text += "資料夾 : " + dirname + "\n製成 : " + filename + "\n";
            richTextBox1.Text += "完成\n\n";

        }

        /// <summary>
        /// 把directory文件夹里的png文件生成为gif文件，放在giffile
        /// </summary>
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

        private void bt_font_size_10_Click(object sender, EventArgs e)
        {
            WordSize = 10;
            lb_moving.Font = new Font("標楷體", WordSize);
            //lb_moving.Font.Size = 10F;
            //this.comboBox_drive.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));

        }

        private void bt_font_size_20_Click(object sender, EventArgs e)
        {
            WordSize = 20;
            lb_moving.Font = new Font("標楷體", WordSize);

        }

        private void bt_font_size_30_Click(object sender, EventArgs e)
        {
            WordSize = 30;
            lb_moving.Font = new Font("標楷體", WordSize);

        }

        private void bt_font_size_40_Click(object sender, EventArgs e)
        {
            WordSize = 40;
            lb_moving.Font = new Font("標楷體", WordSize);

        }

        private void bt_font_size_50_Click(object sender, EventArgs e)
        {
            WordSize = 50;
            lb_moving.Font = new Font("標楷體", WordSize);
        }

        private void bt_font_size_minus_Click(object sender, EventArgs e)
        {
            float font_size = lb_moving.Font.Size;
            if (font_size > 5)
            {
                font_size--;
                //字體變小
                lb_moving.Font = new Font("新細明體", font_size);
            }

        }

        private void bt_font_size_plus_Click(object sender, EventArgs e)
        {
            float font_size = lb_moving.Font.Size;
            if (font_size < 100)
            {
                font_size++;
                //字體變大
                lb_moving.Font = new Font("新細明體", font_size);
            }

        }

        private void bt_fontname1_Click(object sender, EventArgs e)
        {
            SelectFont = 1;
            lb_moving.Font = new Font("標楷體", WordSize);

        }

        private void bt_fontname2_Click(object sender, EventArgs e)
        {
            SelectFont = 2;
            lb_moving.Font = new Font("新細明體", WordSize);

        }

        private void bt_font_setup_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = lb_moving.Font;
            fontDialog1.Color = lb_moving.ForeColor;

            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                lb_moving.Font = fontDialog1.Font;
                lb_moving.ForeColor = fontDialog1.Color;
            }

        }

        private void cb_font_style_CheckedChanged(object sender, EventArgs e)
        {



            if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Italic);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Italic);
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Bold | FontStyle.Underline);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Bold | FontStyle.Underline);
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Italic | FontStyle.Underline);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Italic | FontStyle.Underline);
            }
            else if ((cb_font_style1.Checked == true) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Bold);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Bold);
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == true))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Underline);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Underline);
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == true) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Italic);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Italic);
            }
            else if ((cb_font_style1.Checked == false) && (cb_font_style2.Checked == false) && (cb_font_style3.Checked == false))
            {
                if (SelectFont == 1)
                    lb_moving.Font = new Font("標楷體", WordSize, FontStyle.Regular);
                else if (SelectFont == 2)
                    lb_moving.Font = new Font("新細明體", WordSize, FontStyle.Regular);
            }

        }

        private void bt_speed_minus_Click(object sender, EventArgs e)
        {
            timer1.Interval += 5;
        }

        private void bt_speed_plus_Click(object sender, EventArgs e)
        {
            if (timer1.Interval > 5)
                timer1.Interval -= 5;

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            lb_moving.Text = textBox1.Text;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_background_color_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            colorDialog1.AnyColor = true;      			//顯示基本顏色集中可用的所有顏色
            colorDialog1.FullOpen = true;      //創建自定義顏色的控件在對話框打開時是可見的
            colorDialog1.SolidColorOnly = false;			//不限制只選擇純色
            if (colorDialog1.ShowDialog() == DialogResult.OK)   //彈出對話框
            {
                pictureBox1.BackColor = colorDialog1.Color;
                //richTextBox1.SelectionBackColor = colorDialog1.Color;
            }

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
            //openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            //openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\__pic\_ntuh";  //預設開啟的路徑
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
                Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
                //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
                //pictureBox1.Image = bitmap1;
                bt_open_picture.BackgroundImage = bitmap1;
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }
    }
}

