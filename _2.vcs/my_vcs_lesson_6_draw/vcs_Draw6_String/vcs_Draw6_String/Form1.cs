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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1100;
            y_st = 40;
            dx = 150;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button28.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button29.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            //bt_clear.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_save.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            bt_exit.Location = new Point(x_st + dx * 4, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width-100, this.Height - richTextBox1.Location.Y + 200);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Location = new Point(40, 40);

            x_st = 40;
            y_st = 600;
            dx = 450;
            dy = 150;
            int W = 440;
            int H = 150;

            pictureBox2.Location = new Point(x_st, y_st);

            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.BackColor = Color.Pink;

            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox4.Size = new Size(W, H);

            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox5.Size = new Size(W, H);

            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox6.Size = new Size(W, H);

            pictureBox7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox7.Size = new Size(W, H);

            pictureBox8.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox8.Size = new Size(W, H);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            open_new_file();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

            // Print some text left justified, right justified, and centered.
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
            if (bitmap1 == null)
            {
                open_new_file();
            }

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

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

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

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DrawTranslucentText();
        }

        void DrawTranslucentText()
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bm = new Bitmap(filename);

            using (Graphics gr = Graphics.FromImage(bm))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;

                    int dy = (int)(gr.MeasureString("X", this.Font).Height * 1.5);
                    int x = bm.Width / 2;
                    int y = 30;

                    for (int opacity = 20; opacity <= 80; opacity += 10)
                    {
                        string txt = "透明度 " + opacity.ToString();
                        using (Brush brush = new SolidBrush(Color.FromArgb(opacity, 0, 0, 0)))
                        {
                            gr.DrawString(txt, this.Font, brush, x, y, string_format);
                        }
                        using (Brush brush = new SolidBrush(Color.FromArgb(opacity, 255, 255, 255)))
                        {
                            gr.DrawString(txt, this.Font, brush, x - 2, y - 2, string_format);
                        }
                        y += dy;
                    }
                }
                pictureBox1.Image = bm;
            }
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
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            Font f = new Font("標楷體", 18, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Black);
            g.DrawString("生日快樂!", f, sb, 10, 10);
            pictureBox1.Image = bitmap1;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            DrawVerticalString();
        }

        int dd = 0;
        public void DrawVerticalString()
        {
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            string str = "imsLink每次影像重抓 像是會慢一陣子";
            Font f = new Font("Arial", 16);
            SolidBrush sb = new SolidBrush(Color.Black);
            StringFormat drawFormat = new StringFormat();

            dd++;
            float x = 150.0F + dd;
            float y = 50.0F + dd;


            //richTextBox1.Text += "111\t" + drawFormat.FormatFlags.ToString() + "\n";
            //drawFormat.FormatFlags = StringFormatFlags.
            g.DrawString(str, f, sb, x, y, drawFormat);

            //richTextBox1.Text += "222\t" + drawFormat.FormatFlags.ToString() + "\n";
            //drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString(str, f, sb, x, y + 100, drawFormat);

            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            //richTextBox1.Text += "333\t" + drawFormat.FormatFlags.ToString() + "\n";
            g.DrawString(str, f, sb, x, y, drawFormat);

            f.Dispose();
            sb.Dispose();
            g.Dispose();

            pictureBox1.Image = bitmap1;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            // Construct a new Rectangle.
            Rectangle r = new Rectangle(new Point(50, 50), new Size(300, 300));
            Font f = new Font("標楷體", 12, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Black);

            StringFormat fmt = new StringFormat(StringFormatFlags.NoClip);

            // Draw the bounding rectangle
            g.DrawRectangle(Pens.Black, r);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊上左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊上中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Far;      //水平靠右
            g.DrawString("對齊上右方", f, sb, (RectangleF)r, fmt);


            fmt.LineAlignment = StringAlignment.Center;    //向中對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊中左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;    //向中對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊中中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;  //向中對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            g.DrawString("對齊中右方", f, sb, (RectangleF)r, fmt);


            fmt.LineAlignment = StringAlignment.Far;    //向下對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊下左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Far;    //向下對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊下中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Far;  //向下對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            g.DrawString("對齊下右方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;  //向中對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            fmt.FormatFlags = StringFormatFlags.DirectionVertical;  //直書
            g.DrawString("向中對齊+水平靠右+直書", f, Brushes.Red, (RectangleF)r, fmt);

            pictureBox1.Image = bitmap1;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //使用StringFormat與適當DrawString方法來指定置中對齊的文字。
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            string text1 = "Use StringFormat and Rectangle objects to center text in a rectangle.";
            using (Font font1 = new Font("Arial", 22, FontStyle.Bold, GraphicsUnit.Point))
            {
                Rectangle rect1 = new Rectangle(10, 10, 130, 140);

                // Create a StringFormat object with the each line of text, and the block
                // of text centered on the page.
                StringFormat stringFormat = new StringFormat();
                stringFormat.Alignment = StringAlignment.Center;
                stringFormat.LineAlignment = StringAlignment.Center;

                // Draw the text and the surrounding rectangle.
                g.DrawString(text1, font1, Brushes.Blue, rect1, stringFormat);
                g.DrawRectangle(Pens.Black, rect1);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //使用TextFormatFlags列舉型別換行，以及以垂直和水平置中與適當的文字DrawText方法。
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            string text2 = "Use TextFormatFlags and Rectangle objects to center text in a rectangle.";

            using (Font font2 = new Font("Arial", 12, FontStyle.Bold, GraphicsUnit.Point))
            {
                Rectangle rect2 = new Rectangle(150, 10, 130, 140);

                // Create a TextFormatFlags with word wrapping, horizontal center and
                // vertical center specified.
                TextFormatFlags flags = TextFormatFlags.HorizontalCenter |
                    TextFormatFlags.VerticalCenter | TextFormatFlags.WordBreak;

                // Draw the text and the surrounding rectangle.
                TextRenderer.DrawText(g, text2, font2, rect2, Color.Blue, flags);
                g.DrawRectangle(Pens.Black, rect2);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

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

        private void button16_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                open_new_file();
            }

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
                // These just make things weird:
                //string_format.Alignment = StringAlignment.Center;
                //string_format.LineAlignment = StringAlignment.Center;

                // Define the tab stops.
                float[] tabs = { 250, 75, 75 };
                string_format.SetTabStops(0, tabs);

                // Draw the headings.
                float margin = 10;
                float y = 10;
                using (Font font = new Font("Times New Roman", 13, FontStyle.Bold))
                {
                    g.DrawString(headings, font, Brushes.Blue, margin, y, string_format);
                }

                // Draw a horizontal line.
                y += 1.4f * Font.Height;
                g.DrawLine(Pens.Blue, margin, y, margin + tabs.Sum() + 50, y);
                y += 5;

                // Draw the book entries.
                using (Font font = new Font("Times New Roman", 11))
                {
                    foreach (string line in lines)
                    {
                        g.DrawString(line, font, Brushes.Black, margin, y, string_format);
                        y += 1.2f * this.Font.Height;
                    }
                }
            }
            pictureBox1.Image = bitmap1;
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

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void open_new_file()
        {
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            // Draw text aligned in various ways.
            Rectangle rect = new Rectangle(5, 5, this.pictureBox2.ClientSize.Width - 10, this.pictureBox2.ClientSize.Height - 10);
            e.Graphics.DrawRectangle(Pens.Red, rect);

            using (Font font = new Font("Times New Roman", 16, GraphicsUnit.Pixel))
            {
                using (StringFormat sf = new StringFormat())
                {
                    // Top.
                    sf.LineAlignment = StringAlignment.Near;    // Top.

                    // Top/Left.
                    sf.Alignment = StringAlignment.Near;        // Left.
                    e.Graphics.DrawString("Top/Left", font, Brushes.Black, rect, sf);

                    // Top/Center.
                    sf.Alignment = StringAlignment.Center;      // Center.
                    e.Graphics.DrawString("Top/Center", font, Brushes.Black, rect, sf);

                    // Top/Right.
                    sf.Alignment = StringAlignment.Far;         // Right.
                    e.Graphics.DrawString("Top/Right", font, Brushes.Black, rect, sf);

                    // Middle.
                    sf.LineAlignment = StringAlignment.Center;  // Middle.

                    // Middle/Left.
                    sf.Alignment = StringAlignment.Near;        // Left.
                    e.Graphics.DrawString("Middle/Left", font, Brushes.Black, rect, sf);

                    // Middle/Center.
                    sf.Alignment = StringAlignment.Center;      // Center.
                    e.Graphics.DrawString("Middle/Center", font, Brushes.Black, rect, sf);

                    // Middle/Right.
                    sf.Alignment = StringAlignment.Far;         // Right.
                    e.Graphics.DrawString("Middle/Right", font, Brushes.Black, rect, sf);

                    // Bottom.
                    sf.LineAlignment = StringAlignment.Far;     // Bottom.

                    // Bottom/Left.
                    sf.Alignment = StringAlignment.Near;        // Left.
                    e.Graphics.DrawString("Bottom/Left", font, Brushes.Black, rect, sf);

                    // Bottom/Center.
                    sf.Alignment = StringAlignment.Center;      // Center.
                    e.Graphics.DrawString("Bottom/Center", font, Brushes.Black, rect, sf);

                    // Bottom/Right.
                    sf.Alignment = StringAlignment.Far;         // Right.
                    e.Graphics.DrawString("Bottom/Right", font, Brushes.Black, rect, sf);
                }
            }


        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            /*
            Bitmap bm = new Bitmap(280, 100);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
                gr.ScaleTransform(-1, 1);
                using (Font the_font = new Font("Comic Sans MS", 40))
                {
                    gr.DrawString("Backward", the_font, Brushes.Black, -280, 0);
                    pictureBox3.Image = bm;
                }
            }
            */

            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            e.Graphics.ScaleTransform(-1, 1);
            using (Font the_font = new Font("Comic Sans MS", 40))
            {
                e.Graphics.DrawString("Backward", the_font, Brushes.Black, -280, 0);

                e.Graphics.DrawString("反向字體", the_font, Brushes.Black, -280, 50);
            }
        }

        // 彩色字體 ST
        // Return a random color.
        private Random rand = new Random();
        private Color[] colors =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.LightGreen,
            Color.LightBlue,
            Color.Green,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.Purple,
        };
        private Color RandomColor()
        {
            return colors[rand.Next(0, colors.Length)];
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            // Draw the lined-filled text.

            const string TXT = "群曜醫電";

            // Make the result smoother.
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            //e.Graphics.Clear(this.BackColor);
            e.Graphics.Clear(Color.LightGray);

            // Make a font.
            using (Font the_font = new Font("Times New Roman", 85, FontStyle.Bold, GraphicsUnit.Pixel))
            {
                using (GraphicsPath path = new GraphicsPath())
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int cx = this.pictureBox4.ClientSize.Width / 2;
                        int cy = this.pictureBox4.ClientSize.Height / 2;
                        path.AddString(TXT, the_font.FontFamily,
                            (int)the_font.Style, the_font.Size,
                            new Point(cx, cy), string_format);
                    }

                    // Restrict drawing to the path.
                    using (Region clip_region = new Region(path))
                    {
                        e.Graphics.Clip = clip_region;

                        // Fill the path with circles.
                        Random rand = new Random();
                        for (int i = 1; i < 200; i++)
                        {
                            int radius = rand.Next(5, 50);
                            int cx = rand.Next(0, this.pictureBox4.ClientSize.Width);
                            int cy = rand.Next(0, this.pictureBox4.ClientSize.Height);
                            using (Brush colored_brush = new SolidBrush(RandomColor()))
                            {
                                e.Graphics.FillEllipse(colored_brush,
                                    cx - radius, cy - radius, 2 * radius, 2 * radius);
                            }
                        }

                        // Reset the clipping region.
                        e.Graphics.ResetClip();
                    }
                }
            }
        }

        // 彩色字體 SP

        // 鉛筆彩色字體 ST

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            // Draw the lined-filled text.
            const string TXT = "群曜醫電";

            // Make the result smoother.
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            e.Graphics.Clear(this.BackColor);

            // Make a font.
            using (Font the_font = new Font("Times New Roman", 85, FontStyle.Bold, GraphicsUnit.Pixel))
            {
                using (GraphicsPath path = new GraphicsPath())
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int cx = this.pictureBox5.ClientSize.Width / 2;
                        int cy = this.pictureBox5.ClientSize.Height / 2;
                        path.AddString(TXT, the_font.FontFamily,
                            (int)the_font.Style, the_font.Size,
                            new Point(cx, cy), string_format);
                    }

                    // Restrict drawing to the path.
                    using (Region clip_region = new Region(path))
                    {
                        e.Graphics.Clip = clip_region;

                        // Fill the path with lines.
                        Random rand = new Random();
                        int x0, y0, x1, y1;
                        x0 = 0;
                        x1 = this.pictureBox5.ClientSize.Width;
                        for (int i = 1; i < 75; i++)
                        {
                            y0 = rand.Next(0, this.pictureBox5.ClientSize.Height);
                            y1 = rand.Next(0, this.pictureBox5.ClientSize.Height);
                            using (Pen colored_pen = new Pen(RandomColor()))
                            {
                                e.Graphics.DrawLine(colored_pen, x0, y0, x1, y1);
                            }
                        }
                        y0 = 0;
                        y1 = this.pictureBox5.ClientSize.Height;
                        for (int i = 1; i < 75; i++)
                        {
                            x0 = rand.Next(0, this.pictureBox5.ClientSize.Width);
                            x1 = rand.Next(0, this.pictureBox5.ClientSize.Width);
                            using (Pen colored_pen = new Pen(RandomColor()))
                            {
                                e.Graphics.DrawLine(colored_pen, x0, y0, x1, y1);
                            }
                        }

                        // Reset the clipping region.
                        e.Graphics.ResetClip();
                    }
                }
            }

        }
        // 鉛筆彩色字體 SP

        // 字體外框顏色改變 ST
        private void pictureBox6_Paint(object sender, PaintEventArgs e)
        {
            // Make things smoother.
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Create the text path.
            GraphicsPath path = new GraphicsPath(FillMode.Alternate);

            // Draw text using a StringFormat to center it on the form.
            using (FontFamily font_family = new FontFamily("Times New Roman"))
            {
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;
                    sf.LineAlignment = StringAlignment.Center;
                    path.AddString("群曜醫電", font_family, (int)FontStyle.Bold, 85, this.pictureBox6.ClientRectangle, sf);
                }
            }

            // Fill and draw the path.
            e.Graphics.FillPath(Brushes.Blue, path);
            using (Pen pen = new Pen(Color.Red, 3))
            {
                e.Graphics.DrawPath(pen, path);
            }
        }
        // 字體外框顏色改變 SP

        private void pictureBox7_Paint(object sender, PaintEventArgs e)
        {

        }

        // 單色鉛筆彩色字體 ST
        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {
            // Draw the lined-filled text.
            const string TXT = "群曜醫電";

            // Make the result smoother.
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            e.Graphics.Clear(this.BackColor);

            // Make a font.
            using (Font the_font = new Font("Times New Roman", 85, FontStyle.Bold, GraphicsUnit.Pixel))
            {
                using (GraphicsPath path = new GraphicsPath())
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int cx = this.pictureBox8.ClientSize.Width / 2;
                        int cy = this.pictureBox8.ClientSize.Height / 2;
                        path.AddString(TXT, the_font.FontFamily,
                            (int)the_font.Style, the_font.Size,
                            new Point(cx, cy), string_format);
                    }

                    // Restrict drawing to the path.
                    using (Region clip_region = new Region(path))
                    {
                        e.Graphics.Clip = clip_region;

                        // Fill the path with lines.
                        Random rand = new Random();
                        int x0, y0, x1, y1;
                        x0 = 0;
                        x1 = this.pictureBox8.ClientSize.Width;
                        for (int i = 1; i < 75; i++)
                        {
                            y0 = rand.Next(0, this.pictureBox8.ClientSize.Height);
                            y1 = rand.Next(0, this.pictureBox8.ClientSize.Height);
                            e.Graphics.DrawLine(Pens.Black, x0, y0, x1, y1);
                        }
                        y0 = 0;
                        y1 = this.pictureBox8.ClientSize.Height;
                        for (int i = 1; i < 75; i++)
                        {
                            x0 = rand.Next(0, this.pictureBox8.ClientSize.Width);
                            x1 = rand.Next(0, this.pictureBox8.ClientSize.Width);
                            e.Graphics.DrawLine(Pens.Black, x0, y0, x1, y1);
                        }

                        // Reset the clipping region.
                        e.Graphics.ResetClip();
                    }
                }
            }
        }

        // 單色鉛筆彩色字體 SP

    }
}
