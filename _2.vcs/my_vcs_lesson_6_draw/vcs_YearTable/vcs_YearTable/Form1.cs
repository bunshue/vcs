using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_YearTable
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

            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            button5.Enabled = false;
            button7.Enabled = false;

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            button2.Enabled = true;
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            button7.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //載入圖片至畫布
            string filename = string.Empty;
            filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";
            bitmap1 = new Bitmap(filename);

            int width;
            int height;

            width = bitmap1.Width;
            height = bitmap1.Height;

            richTextBox1.Text += "畫布大小 : W = " + width.ToString() + " H = " + height.ToString() + "\n";

            //pictureBox1.Size = new Size(width, height);   //改變圖框大小
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Image = bitmap1;

            g = Graphics.FromImage(bitmap1);

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //畫東西
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));
            g.DrawRectangle(new Pen(Color.Red, 5), new Rectangle(100, 100, 300, 300));

            int width = 200;
            int height = 200;
            Point[] points = new Point[3];
            points[0] = new Point(width / 2, height / 8);
            points[1] = new Point(width * 7 / 8, height * 7 / 8);
            points[2] = new Point(width * 1 / 8, height * 7 / 8);
            g.FillPolygon(sb, points);
            
            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //清除畫布
            //g.Clear(Color.White);
            g.Clear(BackColor);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //逐點繪圖
            int width = bitmap1.Width;
            int height = bitmap1.Height;
            int xx;
            int yy;
            Color pt;

            //讀取/修改每一的的RGB值
            for (yy = 0; yy < height / 2; yy += 1)
            {
                for (xx = 0; xx < width / 2; xx += 1)
                {
                    pt = bitmap1.GetPixel(xx, yy);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 255 - pt.R, 255 - pt.G, 255 - pt.B));
                    //bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x11, 0x33, 0x55));
                    //bitmap1.SetPixel(xx, yy, Color.White);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //儲存圖檔
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\draw_test_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                //string filename3 = filename + ".png";

                //bitmap1.Save(@filename1, ImageFormat.Jpeg);
                bitmap1.Save(@filename2, ImageFormat.Bmp);
                //bitmap1.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }



        private class eraNameList
        {
            public string EraName { get; set; }
            public int Year_ST { get; set; }
            public int Year_SP { get; set; }
            public int Year_length { get; set; }
        }

        List<eraNameList> eraName = new List<eraNameList>();


        void load_eraData()
        {
            eraName.Add(new eraNameList { EraName = "洪武", Year_ST = 1368, Year_SP = 1398 });
            eraName.Add(new eraNameList { EraName = "建文", Year_ST = 1399, Year_SP = 1402 });
            eraName.Add(new eraNameList { EraName = "永樂", Year_ST = 1403, Year_SP = 1424 });
            eraName.Add(new eraNameList { EraName = "洪熙", Year_ST = 1425, Year_SP = 1425 });
            eraName.Add(new eraNameList { EraName = "宣德", Year_ST = 1426, Year_SP = 1435 });
            eraName.Add(new eraNameList { EraName = "正統", Year_ST = 1436, Year_SP = 1449 });
            eraName.Add(new eraNameList { EraName = "景泰", Year_ST = 1450, Year_SP = 1456 });
            eraName.Add(new eraNameList { EraName = "天順", Year_ST = 1457, Year_SP = 1464 });
            eraName.Add(new eraNameList { EraName = "成化", Year_ST = 1465, Year_SP = 1487 });
            eraName.Add(new eraNameList { EraName = "弘治", Year_ST = 1488, Year_SP = 1505 });
            eraName.Add(new eraNameList { EraName = "正德", Year_ST = 1506, Year_SP = 1521 });
            eraName.Add(new eraNameList { EraName = "嘉靖", Year_ST = 1522, Year_SP = 1566 });
            eraName.Add(new eraNameList { EraName = "隆慶", Year_ST = 1567, Year_SP = 1572 });
            eraName.Add(new eraNameList { EraName = "萬曆", Year_ST = 1573, Year_SP = 1620 });
            eraName.Add(new eraNameList { EraName = "泰昌", Year_ST = 1620, Year_SP = 1620 });
            eraName.Add(new eraNameList { EraName = "天啟", Year_ST = 1621, Year_SP = 1627 });
            eraName.Add(new eraNameList { EraName = "崇禎", Year_ST = 1628, Year_SP = 1644 });

            eraName.Add(new eraNameList { EraName = "順治", Year_ST = 1644, Year_SP = 1661 });
            eraName.Add(new eraNameList { EraName = "康熙", Year_ST = 1662, Year_SP = 1722 });
            eraName.Add(new eraNameList { EraName = "雍正", Year_ST = 1723, Year_SP = 1735 });
            eraName.Add(new eraNameList { EraName = "乾隆", Year_ST = 1736, Year_SP = 1795 });
            eraName.Add(new eraNameList { EraName = "嘉慶", Year_ST = 1796, Year_SP = 1820 });
            eraName.Add(new eraNameList { EraName = "道光", Year_ST = 1821, Year_SP = 1850 });
            eraName.Add(new eraNameList { EraName = "咸豐", Year_ST = 1851, Year_SP = 1861 });
            eraName.Add(new eraNameList { EraName = "同治", Year_ST = 1862, Year_SP = 1874 });
            eraName.Add(new eraNameList { EraName = "光緒", Year_ST = 1875, Year_SP = 1908 });
            eraName.Add(new eraNameList { EraName = "宣統", Year_ST = 1909, Year_SP = 1911 });
        }

        private void button8_Click(object sender, EventArgs e)
        {
            load_eraData();

            int year;
            int era_start = 0;
            int total_year = 0;
            richTextBox1.Text += "年號\t起\t迄\t年\n";
            foreach (var showlist in eraName)
            {
                if (era_start == 0)
                    era_start = showlist.Year_ST;
                year = showlist.Year_SP - showlist.Year_ST + 1;
                total_year += year;
                showlist.Year_length = year;
                richTextBox1.Text += showlist.EraName + "\t" + showlist.Year_ST.ToString() + "\t" + showlist.Year_SP.ToString() + "\t" + showlist.Year_length.ToString() + "\n";
            }
            richTextBox1.Text += "總年數 : " + total_year.ToString() + "\n";

            pictureBox1.Size = new System.Drawing.Size(total_year * 10 + 10, 190);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            int ratio;
            ratio = W / total_year;

            richTextBox1.Text += "W : " + W.ToString() + "\n";
            richTextBox1.Text += "H : " + H.ToString() + "\n";
            richTextBox1.Text += "ratio : " + ratio.ToString() + "\n";

            //Graphics g = pictureBox1.CreateGraphics();
            Pen p = new Pen(Color.Red, 1);
            Font f;

            int x_st = 0;
            int y_st = 0;
            int w = 0;
            int h = 0;

            h = 50;
            y_st = 0;
            total_year = 0;

            foreach (var showlist in eraName)
            {
                year = showlist.Year_SP - showlist.Year_ST + 1;
                total_year += year;
                showlist.Year_length = year;
                //richTextBox1.Text += showlist.EraName + "\t" + showlist.Year_ST.ToString() + "\t" + showlist.Year_SP.ToString() + "\t" + showlist.Year_length.ToString() + "\n";

                x_st = (showlist.Year_ST - era_start) * ratio;
                w = year * ratio;
                p = new Pen(Color.Red, 1);
                g.DrawRectangle(p, x_st, y_st, w, h);
                richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";

                f = new Font("標楷體", 12);
                g.DrawString((total_year - year + 1).ToString(), f, new SolidBrush(Color.Blue), new PointF(x_st, y_st + h));

                string name = showlist.EraName + "(" + year.ToString() + ")";
                int font_size = 20;
                int ww = 0;
                int hh = 0;

                bool flag_font_size_ok = false;

                f = new Font("標楷體", font_size);
                while (flag_font_size_ok == false)
                {
                    ww = g.MeasureString(name, f).ToSize().Width;
                    hh = g.MeasureString(name, f).ToSize().Height;
                    if ((ww > w) || (hh > h))
                    {
                        font_size--;
                        richTextBox1.Text += "font太大, 減為" + font_size.ToString() + "\n";
                        f = new Font("標楷體", font_size);
                    }
                    else
                    {
                        flag_font_size_ok = true;
                    }
                }

                richTextBox1.Text += "ww = " + ww.ToString() + "  hh = " + hh.ToString() + "\n";

                g.DrawString(name, f, new SolidBrush(Color.Blue), new PointF(x_st + (w - ww) / 2, y_st + (h - hh) / 2));

                p = new Pen(Color.Green, 1);
                g.DrawRectangle(p, x_st + (w - ww) / 2, y_st + (h - hh) / 2, ww, hh);


                pictureBox1.Image = bitmap1;
            }


        }

        private void button9_Click(object sender, EventArgs e)
        {
            //儲存圖檔
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\draw_test_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                //string filename3 = filename + ".png";

                //bitmap1.Save(@filename1, ImageFormat.Jpeg);
                bitmap1.Save(@filename2, ImageFormat.Bmp);
                //bitmap1.Save(@filename3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + filename3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";

        }

        int life_st = 0;
        int life_sp = 0;
        int year_min = 10000;
        int year_max = 0;
        int position_st = 1;

        void find_position_st(int position)
        {
            if (position > position_st)
                position_st = position;
        }

        void find_max_min(int year)
        {
            if (year < year_min)
                year_min = year;
            if (year > year_max)
                year_max = year;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //load_personData();    //TBD

            string[,] person = new string[19, 4] { 
            { "寇準", "961", "1023" , "0"},
            { "范仲淹", "989", "1052" , "2"},
            { "包拯", "999", "1062" , "4"},
            { "司馬光", "1019", "1086" , "3"},
            { "王安石", "1021", "1086" , "5"},
            { "歐陽修", "1007", "1072" , "1"},
            { "秦觀", "1049", "1100" , "-1"},
            { "黃庭堅", "1045", "1105" , "6"},
            { "宋高宗", "1107", "1187" , "6"},
            { "宋理宗", "1205", "1264" , "6"},
            { "宋度宗", "1240", "1274" , "3"},
            { "蘇軾", "1037", "1101" , "0"},
            { "岳飛", "1103", "1142" , "0"},
            { "李清照", "1084", "1155" , "1"},
            { "朱熹", "1130", "1200" , "3"},
            { "辛棄疾", "1140", "1207" , "4"},
            { "文天祥", "1236", "1283" , "4"},
            { "宋徽宗", "1082", "1135" , "2"},
            { "宋欽宗", "1100", "1156" , "5"}
            };
            int[,] data = new int[19, 4];

            int i;
            int age;
            int position;
            int BORDER = 50;
            int HEIGHT = 50;

            for (i = 0; i < 19; i++)
            {
                life_st = int.Parse(person[i, 1]);
                find_max_min(life_st);
                data[i, 0] = life_st;
                life_sp = int.Parse(person[i, 2]);
                find_max_min(life_sp);
                data[i, 1] = life_sp;
                age = life_sp - life_st;
                data[i, 2] = age;
                position = int.Parse(person[i, 3]);
                find_position_st(position);
                data[i, 3] = position;
                richTextBox1.Text += person[i, 0] + "\t" + life_st.ToString() + "\t" + life_sp.ToString() + "\t" + age.ToString() + "\t" + position.ToString() + "\n";
            }
            richTextBox1.Text += "min = " + year_min.ToString() + "\tmax = " + year_max.ToString() + "\n";
            richTextBox1.Text += "W = " + pictureBox1.Width.ToString() + "\tH = " + pictureBox1.Height.ToString() + "\n";

            pictureBox1.Size = new System.Drawing.Size(1200, 800);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";


            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, BORDER, BORDER));
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 10, pictureBox1.Height - 10));

            int total_width = pictureBox1.Width;
            int total_length = year_max - year_min;
            int ratio = (total_width - 200) / total_length;

            richTextBox1.Text += "total_width = " + total_width.ToString() + "\ttotal_length = " + total_length.ToString() + "\n";
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            int offset = year_min - BORDER;

            //int position_st = 8;

            g.DrawRectangle(new Pen(Color.Green), new Rectangle(BORDER, 10, total_length * ratio, 30));


            int x;
            int y;
            int w;
            int h;
            for (i = 0; i < 19; i++)
            {
                if (data[i, 3] != -1)
                {
                    richTextBox1.Text += "AAA" + person[i, 0] + "\n";

                    x = (data[i, 0] - year_min) * ratio + BORDER;
                    y = BORDER + HEIGHT * data[i, 3];
                    w = data[i, 2] * ratio;
                    h = HEIGHT - 10;
                    g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x, y, w, h));
                    g.DrawRectangle(new Pen(Color.Black), new Rectangle(x, y, w, h));
                    g.DrawString(person[i, 0], this.Font, new SolidBrush(Color.Black), (data[i, 0] - year_min) * ratio + data[i, 2] * ratio / 2 + BORDER, BORDER + HEIGHT * data[i, 3] + 20);
                }
                else
                {
                    position_st++;
                    richTextBox1.Text += "BBB" + person[i, 0] + "\n";
                    x = (data[i, 0] - year_min) * ratio + BORDER;
                    y = BORDER + HEIGHT * position_st;
                    w = data[i, 2] * ratio;
                    h = HEIGHT - 10;
                    g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x, y, w, h));
                    g.DrawRectangle(new Pen(Color.Black), new Rectangle(x, y, w, h));
                    g.DrawString(person[i, 0], this.Font, new SolidBrush(Color.Black), (data[i, 0] - year_min) * ratio + data[i, 2] * ratio / 2 + BORDER, BORDER + HEIGHT * position_st + 20);
                }
            }

            //g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 100, 100);
            
            pictureBox1.Image = bitmap1;

        }
    }
}
