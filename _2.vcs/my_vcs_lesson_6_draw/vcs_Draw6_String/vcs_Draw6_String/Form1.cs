using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for LinearGradientBrush
using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw6_String
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 950;
            y_st = 40;
            dx = 130;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            button4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            button8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 3, y_st + dy * 2);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button15.Location = new Point(x_st + dx * 3, y_st + dy * 3);

            button16.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button19.Location = new Point(x_st + dx * 3, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 5);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 6);

            button28.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 7);

            //bt_clear.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_save.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            bt_exit.Location = new Point(x_st + dx * 3, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 80);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Location = new Point(40, 40);

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Print some text left justified, right justified, and centered.
            if (bitmap1 != null)
            {
                const int gap = 10;
                g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAlias;
                g.Clear(this.BackColor);

                string text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
                int wid = (this.pictureBox1.ClientSize.Width - 4 * gap) / 3;
                int hgt = this.pictureBox1.ClientSize.Height - 2 * gap;

                // Left alignment.
                Rectangle rect = new Rectangle(gap, gap, wid, hgt);
                g.DrawRectangle(Pens.Blue, rect);
                DrawText(g, text, rect, StringAlignment.Near);

                // Right alignment.
                rect.X += wid + gap;
                g.DrawRectangle(Pens.Blue, rect);
                DrawText(g, text, rect, StringAlignment.Far);

                // Center alignment.
                rect.X += wid + gap;
                g.DrawRectangle(Pens.Blue, rect);
                DrawText(g, text, rect, StringAlignment.Center);

                pictureBox1.Image = bitmap1;
            }
            else
            {
                richTextBox1.Text += "未開啟檔案\n";
            }
        }

        private void DrawText(Graphics gr, string text, Rectangle rect, StringAlignment alignment)
        {
            gr.DrawRectangle(Pens.Blue, rect);
            using (StringFormat string_format = new StringFormat())
            {
                // Center alignment.
                string_format.Alignment = alignment;
                string_format.FormatFlags = StringFormatFlags.LineLimit;
                string_format.Trimming = StringTrimming.Word;

                gr.DrawString(text, this.Font, Brushes.Black, rect, string_format);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                // A Mark Twain quote:
                const string quote = "The trouble ain't that there is too many fools, but that the lightning ain't distributed right.";
                const int margin = 20;
                StringFormatFlags[] flags =
                {
                    StringFormatFlags.FitBlackBox,
                    StringFormatFlags.LineLimit,
                    StringFormatFlags.NoClip,
                    StringFormatFlags.NoWrap
                };
                int height = (this.pictureBox1.ClientSize.Height - (flags.Length + 1) * margin) / flags.Length;
                int width = this.pictureBox1.ClientSize.Width - 2 * margin;

                using (Font font = new Font("Times New Roman", 20))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        int y = margin;
                        foreach (StringFormatFlags flag in flags)
                        {
                            Rectangle rect = new Rectangle(margin, y, width, height);
                            g.DrawRectangle(Pens.Black, rect);
                            string_format.FormatFlags = flag;
                            g.DrawString(flag.ToString() + "  :  " + quote, font, Brushes.Blue, rect, string_format);
                            y += height + margin;
                            richTextBox1.Text += "flag : " + flag.ToString() + "\n";
                        }
                    }
                }

                pictureBox1.Image = bitmap1;
            }
            else
            {
                richTextBox1.Text += "未開啟檔案\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                // A Mark Twain quote:
                const string quote =
                    "The trouble ain't that there is too many fools, " +
                    "but that the lightning ain't distributed right.";
                const int margin = 5;
                StringTrimming[] values =
                    (StringTrimming[])Enum.GetValues(typeof(StringTrimming));
                int height = (this.pictureBox1.ClientSize.Height - (values.Length + 1) * margin) / values.Length;
                int width = this.pictureBox1.ClientSize.Width - 2 * margin;

                using (Font font = new Font("Times New Roman", 16))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        int y = margin;
                        foreach (StringTrimming trimmming in values)
                        {
                            Rectangle rect = new Rectangle(margin, y, width, height);
                            g.DrawRectangle(Pens.Black, rect);
                            string_format.Trimming = trimmming;
                            g.DrawString(trimmming.ToString() + "  :  " + quote, font, Brushes.Blue, rect, string_format);
                            y += height + margin;
                            richTextBox1.Text += "trimmming : " + trimmming.ToString() + "\n";
                        }
                    }
                }
                pictureBox1.Image = bitmap1;
            }
            else
            {
                richTextBox1.Text += "未開啟檔案\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                // Draw some text aligned in columns.

                g.TextRenderingHint = TextRenderingHint.AntiAlias;

                string headings = "Title\tPrice\t# Pages\tYear";
                string[] lines =
                {
                "WPF 3d\t$34.95\t430\t2018",
                "The C# Helper Top 100\t$24.95\t380\t2017",
                "Interview Puzzles Dissected\t$15.95\t300\t2016",
                "C# 24-Hour Trainer, Second Edition\t$45.00\t600\t2015",
                "Beginning Software Engineering\t$45.00\t480\t2015",
                "Essential Algorithms\t$60.00\t624\t2013",
                "Beginning Database Design Solutions\t$44.99\t552\t2008",
                "Powers of Two\t$2.04\t8\t16",
                };

                // Prepare a StringFormat to use the tabs.
                using (StringFormat string_format = new StringFormat())
                {
                    // Define the columns' X coordinates.
                    float[] xpos = { 10, 310, 400, 475 };

                    // Define the column alignments.
                    StringAlignment[] alignments =
                    {
                    StringAlignment.Near,
                    StringAlignment.Far,
                    StringAlignment.Far,
                    StringAlignment.Far,
                    };

                    // Draw the headings.
                    float margin = 10;
                    float y = 10;
                    using (Font font = new Font("Times New Roman", 13, FontStyle.Bold))
                    {
                        string[] strings = headings.Split('\t');
                        for (int i = 0; i < strings.Length; i++)
                        {
                            string_format.Alignment = alignments[i];
                            g.DrawString(strings[i], font, Brushes.Blue, xpos[i], y, string_format);
                        }
                    }

                    // Draw a horizontal line.
                    y += 1.4f * Font.Height;
                    float width = xpos[xpos.Length - 1] + 5;
                    g.DrawLine(Pens.Blue, margin, y, width, y);
                    y += 5;

                    // Draw the book entries.
                    using (Font font = new Font("Times New Roman", 11))
                    {
                        foreach (string line in lines)
                        {
                            string[] strings = line.Split('\t');
                            for (int i = 0; i < strings.Length; i++)
                            {
                                string_format.Alignment = alignments[i];
                                g.DrawString(strings[i], font, Brushes.Black, xpos[i], y, string_format);
                            }
                            y += 1.2f * this.Font.Height;
                        }
                    }
                }
                pictureBox1.Image = bitmap1;
            }
            else
            {
                richTextBox1.Text += "未開啟檔案\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {


        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }
        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }


    }
}
