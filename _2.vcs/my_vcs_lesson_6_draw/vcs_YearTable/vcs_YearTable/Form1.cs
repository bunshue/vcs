using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Globalization; //for CultureInfo

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
            richTextBox1.Clear();
            eraName.Clear();

            load_eraData();

            int offset_x = 50;
            int offset_y = 50;
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

            pictureBox1.Size = new System.Drawing.Size(offset_x * 2 + total_year * 10 + 10, offset_y * 2 + 190);

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
            int year_now = DateTime.Now.Year;

            h = 50;
            y_st = 0;
            total_year = 0;

            foreach (var showlist in eraName)
            {
                year = showlist.Year_SP - showlist.Year_ST + 1;
                if (showlist.EraName == "順治")
                    total_year = 0;
                total_year += year;
                showlist.Year_length = year;
                //richTextBox1.Text += showlist.EraName + "\t" + showlist.Year_ST.ToString() + "\t" + showlist.Year_SP.ToString() + "\t" + showlist.Year_length.ToString() + "\n";

                x_st = (showlist.Year_ST - era_start) * ratio;
                w = year * ratio;
                p = new Pen(Color.Red, 1);
                g.DrawRectangle(p, offset_x + x_st, offset_y + y_st, w, h);
                richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";

                f = new Font("標楷體", 12);
                g.DrawString((total_year - year + 1).ToString(), f, new SolidBrush(Color.Blue), new PointF(offset_x + x_st, offset_y + y_st + h));
                f = new Font("標楷體", 10);
                g.DrawString((showlist.Year_ST - year_now).ToString(), f, new SolidBrush(Color.Blue), new PointF(offset_x + x_st, offset_y + y_st + h + 20));

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

                g.DrawString(name, f, new SolidBrush(Color.Blue), new PointF(offset_x + x_st + (w - ww) / 2, offset_y + y_st + (h - hh) / 2));

                p = new Pen(Color.Green, 1);
                g.DrawRectangle(p, offset_x + x_st + (w - ww) / 2, offset_y + y_st + (h - hh) / 2, ww, hh);

                pictureBox1.Image = bitmap1;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //儲存圖檔
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\YearTable_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
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

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "現在年 " + DateTime.Now.Year.ToString() + "\n";
        }

        private const int EMPEROR_DATA_SUI = 0x00;      //emperor data 0, Sui
        private const int EMPEROR_DATA_TANG = 0x01;     //emperor data 1, Tang
        private const int EMPEROR_DATA_CHING = 0x02;    //emperor data 2, Ching

        private const int PERSON_DATA_1 = 0x11;   //person data 1, Sung
        private const int PERSON_DATA_2 = 0x12;   //person data 2, Ming
        private const int PERSON_DATA_3 = 0x13;   //person data 3, Ching

        string[,] person = null;

        void load_personData(int index)
        {
            if (index == PERSON_DATA_1)
            {
                person = new string[19, 4] { 
                { "寇準", "961年", "1023年10月24日" , "1"},
                { "范仲淹", "989年10月1日", "1052年6月19日" , "2"},
                { "包拯", "999年3月5日", "1062年7月3日" , "3"},
                { "歐陽修", "1007年8月1日", "1072年9月22日" , "4"},
                { "司馬光", "1019年11月17日", "1086年10月11日" , "5"},
                { "王安石", "1021年12月18日", "1086年5月21日" , "6"},
                { "蘇軾", "1037年1月8日", "1101年8月24日" , "7"},
                { "黃庭堅", "1045年", "1105年" , "8"},
                { "秦觀", "1049年", "1100年9月17日" , "9"},
                { "宋徽宗", "1082年6月7日", "1135年6月4日" , "10"},
                { "李清照", "1084年3月13日", "1155年5月12日" , "11"},
                { "宋欽宗", "1100年5月23日", "1161年6月14日" , "12"},
                { "岳飛", "1103年3月24日", "1142年1月27日" , "13"},
                { "宋高宗", "1107年5月21日", "1187年11月9日" , "14"},
                { "朱熹", "1130年10月22日", "1200年4月23日" , "15"},
                { "辛棄疾", "1140年5月28日", "1207年10月3日" , "16"},
                { "宋理宗", "1205年1月26日", "1264年11月16日" , "17"},
                { "文天祥", "1236年6月6日", "1283年1月9日" , "18"},
                { "宋度宗", "1240年5月2日", "1274年8月12日" , "19"},
                };
            }
            else if (index == PERSON_DATA_2)
            {
                person = new string[3, 4] { 
                { "湯顯祖", "1550年9月24日", "1616年7月29日" , "1"},
                { "莎士比亞", "1564年4月26日", "1616年4月23日" , "2"},
                { "伊莉莎白一世", "1533年9月7日", "1603年3月24日" , "3"},
                };
            }
            else if (index == PERSON_DATA_3)
            {
                //TBD
                person = new string[3, 4] { 
                { "ccc", "1550年9月24日", "1616年7月29日" , "1"},
                { "cccc", "1564年4月26日", "1616年4月23日" , "2"},
                { "ccccc", "1533年9月7日", "1603年3月24日" , "3"},
                };
            }
            else
            {
                person = new string[1, 4] { 
                { "xxx", "1550年9月24日", "1616年7月29日" , "1"},
                };
            }
        }

        void load_emperorData(int index)
        {
            if (index == EMPEROR_DATA_SUI)
            {
                person = new string[3, 6] {
                { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
                { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
                };
            }
            else if (index == EMPEROR_DATA_TANG)
            {
                person = new string[23, 6] { 
                { "1", "唐高祖", "566年4月7日", "635年6月25日", "618年6月18日", "626年9月4日"},
                { "2", "唐太宗", "598年1月23日", "649年7月10日", "626年9月4日", "649年7月10日"},
                { "3", "唐高宗", "628年7月21日", "683年12月27日", "649年7月15日", "683年12月27日"},
                { "4", "唐中宗", "656年11月26日", "710年7月3日", "684年1月3日","684年2月26日"},
                { "5", "唐睿宗", "662年6月22日", "716年7月13日", "684年2月27日","690年10月16日"},
                { "6", "則天后", "624年2月17日", "705年12月16日", "690年10月16日", "705年2月21日"},
                { "7", "唐中宗", "656年11月26日", "710年7月3日", "705年2月23日","710年7月3日"},
                { "8", "唐睿宗", "662年6月22日", "716年7月13日", "710年7月25日","712年9月8日"},
                { "9", "唐玄宗", "685年9月8日", "762年5月3日", "712年9月8日", "756年8月1日"},
                { "10", "唐肅宗", "711年1月21日","762年5月16日", "756年8月12日", "762年5月16日"},
                { "11", "唐代宗", "726年11月11日", "779年6月10日", "762年5月18日", "779年6月10日"},
                { "12", "唐德宗", "742年5月27日", "805年2月25日", "779年6月12日", "805年2月25日"},
                { "13", "唐順宗", "761年2月21日", "806年2月11日", "805年2月28日", "805年8月31日"},
                { "14", "唐憲宗", "778年3月17日", "820年2月14日", "805年9月5日", "820年2月14日"},
                { "15", "唐穆宗", "795年7月26日", "824年2月25日", "820年2月20日", "824年2月25日"},
                { "16", "唐敬宗", "809年7月22日", "827年1月9日", "824年2月29日", "827年1月9日"},
                { "17", "唐文宗", "809年11月20日", "840年2月10日", "827年1月13日", "840年2月10日"},
                { "18", "唐武宗", "814年7月2日", "846年4月22日", "840年2月20日", "846年4月22日"},
                { "19", "唐宣宗", "810年7月27日", "859年9月10日", "846年4月22日", "859年9月10日"},
                { "20", "唐懿宗", "833年12月28日", "873年8月15日", "859年9月13日", "873年8月15日"},
                { "21", "唐僖宗", "862年6月8日", "888年4月20日", "873年8月16日", "888年4月20日"},
                { "22", "唐昭宗", "867年3月31日", "904年9月22日", "888年4月22日", "904年9月22日"},
                { "23", "唐哀帝", "892年10月27日", "908年3月26日", "904年9月27日", "907年5月12日"},
                };
            }
            else if (index == EMPEROR_DATA_CHING)
            {
                person = new string[12, 6] { 
                { "1", "清太祖", "1559年2月21日", "1626年9月30日", "1616年2月17日", "1626年9月30日"},
                { "2", "清太宗", "1592年11月28日", "1643年9月21日", "1626年10月20日", "1643年9月21日"},
                { "3", "順治", "1638年3月15日", "1661年2月5日", "1643年10月8日", "1661年2月5日"},
                { "4", "康熙", "1654年5月4日", "1722年12月20日", "1661年2月5日", "1722年12月20日"},
                { "5", "雍正", "1678年12月13日", "1735年10月8日", "1722年12月20日", "1735年10月7日"},
                { "6", "乾隆", "1711年9月25日", "1799年2月7日", "1735年10月18日", "1796年2月9日"},
                { "7", "嘉慶", "1760年11月14日", "1820年9月2日", "1796年2月9日", "1820年9月2日"},
                { "8", "道光", "1782年9月16日", "1850年2月26日", "1820年10月3日", "1850年2月26日"},
                { "9", "咸豐", "1831年7月17日", "1861年8月22日", "1850年3月9日", "1861年8月22日"},
                { "10", "同治", "1856年4月27日", "1875年1月12日", "1861年11月11日", "1875年1月12日"},
                { "11", "光緒", "1871年8月14日", "1908年11月14日", "1875年2月25日", "1908年11月14日"},
                { "12", "宣統", "1906年2月7日", "1967年10月17日", "1908年12月2日", "1912年2月12日"},
                };
            }
            else
            {
                person = new string[1, 6] {
                { "1", "xxx", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                };
            }
        }

        void draw_person_data(int index)
        {
            richTextBox1.Clear();

            load_personData(index);

            DateTime lifeEarliest = DateTime.Now;
            DateTime lifeLatest = new DateTime(1, 1, 1);

            int i;
            int total_persons = person.GetUpperBound(0) + 1;
            //richTextBox1.Text += "total_persons = " + total_persons.ToString() + "\n";

            for (i = 0; i < total_persons; i++)
            {
                DateTime lifeStart = DateTime.Parse(person[i, 1]);
                DateTime lifeEnd = DateTime.Parse(person[i, 2]);

                if (lifeEarliest > lifeStart)
                    lifeEarliest = lifeStart;

                if (lifeLatest < lifeEnd)
                    lifeLatest = lifeEnd;

                // 計算差異天數
                TimeSpan lifeDay = lifeEnd - lifeStart;
                int lifedayCount = (int)lifeDay.TotalDays;
                richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";
            }

            richTextBox1.Text += "壽命最早" + lifeEarliest.ToString() + "\n";
            richTextBox1.Text += "壽命最晚" + lifeLatest.ToString() + "\n";
            TimeSpan totalLife = lifeLatest - lifeEarliest;
            int totalLifeDaysCount = (int)totalLife.TotalDays;
            richTextBox1.Text += "壽命全長 " + totalLifeDaysCount.ToString() + " 天" + "\t" + DayConversionYMD(totalLifeDaysCount) + "\n";

            //int age;
            //int position;
            int BORDER = 50;
            int HEIGHT = 50;
            int offset_x = 100;
            int offset_y = 0;
            int x_st;
            int y_st;
            int w;
            int h;
            Font f;
            int ratio = 40;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";
            pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT + BORDER * 2);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            for (i = 0; i < total_persons; i++)
            {
                int num;
                num = int.Parse(person[i, 3]);
                richTextBox1.Text += "第 " + num.ToString() + " 行 " + person[i, 1] + "\n";

                DateTime lifeStart = DateTime.Parse(person[i, 1]);
                DateTime lifeEnd = DateTime.Parse(person[i, 2]);

                // 計算差異天數
                TimeSpan lifeDay = lifeEnd - lifeStart;
                int lifedayCount = (int)lifeDay.TotalDays;
                richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + 50 * (num - 1) + offset_y;

                w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
                h = 40;

                g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));
                g.DrawRectangle(p, x_st, y_st, w, h);

                f = new Font("標楷體", 22);
                string str = person[i, 0] + " (" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")";

                g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));
            }
            pictureBox1.Image = bitmap1;
        }

        void draw_emperor_data(int index)
        {
            richTextBox1.Clear();

            load_emperorData(index);

            DateTime lifeEarliest = DateTime.Now;
            DateTime lifeLatest = new DateTime(1, 1, 1);
            DateTime workEarliest = DateTime.Now;
            DateTime workLatest = new DateTime(1, 1, 1);

            int i;

            int row = person.Rank;//獲取行數
            int col1 = person.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = person.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = person.Length;//獲取整個二維陣列的長度，即所有元 的個數

            /*
            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";
            */

            int total_persons = person.GetUpperBound(0) + 1;
            //richTextBox1.Text += "total_persons = " + total_persons.ToString() + "\n";

            for (i = 0; i < total_persons; i++)
            {
                int num;
                num = int.Parse(person[i, 0]);
                richTextBox1.Text += "第 " + num.ToString() + " 任 " + person[i, 1] + "\n";

                DateTime lifeStart = DateTime.Parse(person[i, 2]);
                DateTime lifeEnd = DateTime.Parse(person[i, 3]);
                DateTime workStart = DateTime.Parse(person[i, 4]);
                DateTime workEnd = DateTime.Parse(person[i, 5]);

                if (lifeEarliest > lifeStart)
                    lifeEarliest = lifeStart;

                if (lifeLatest < lifeEnd)
                    lifeLatest = lifeEnd;

                if (workEarliest > workStart)
                    workEarliest = workStart;

                if (workLatest < workEnd)
                    workLatest = workEnd;

                // 計算差異天數
                TimeSpan lifeDay = lifeEnd - lifeStart;
                int lifedayCount = (int)lifeDay.TotalDays;
                richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                TimeSpan workDay = workEnd - workStart;
                int workdayCount = (int)workDay.TotalDays;
                richTextBox1.Text += "在位 " + workdayCount.ToString() + " 天" + "\t" + DayConversionYMD(workdayCount) + "\n";
            }

            richTextBox1.Text += "壽命最早" + lifeEarliest.ToString() + "\n";
            richTextBox1.Text += "壽命最晚" + lifeLatest.ToString() + "\n";
            TimeSpan totalLife = lifeLatest - lifeEarliest;
            int totalLifeDaysCount = (int)totalLife.TotalDays;
            richTextBox1.Text += "壽命全長 " + totalLifeDaysCount.ToString() + " 天" + "\t" + DayConversionYMD(totalLifeDaysCount) + "\n";

            richTextBox1.Text += "在位最早" + workEarliest.ToString() + "\n";
            richTextBox1.Text += "在位最晚" + workLatest.ToString() + "\n";
            TimeSpan totalWork = workLatest - workEarliest;
            int totalWorkDaysCount = (int)totalWork.TotalDays;
            richTextBox1.Text += "在位全長 " + totalWorkDaysCount.ToString() + " 天" + "\t" + DayConversionYMD(totalWorkDaysCount) + "\n";

            //int age;
            //int position;
            int BORDER = 50;
            int HEIGHT = 50;
            int offset_x = 100;
            int offset_y = 0;
            int x_st;
            int y_st;
            int w;
            int h;
            Font f;
            int ratio = 40;
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";
            pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT + BORDER * 2);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            for (i = 0; i < total_persons; i++)
            {
                int num;
                num = int.Parse(person[i, 0]);
                richTextBox1.Text += "第 " + num.ToString() + " 任 " + person[i, 1] + "\n";

                DateTime lifeStart = DateTime.Parse(person[i, 2]);
                DateTime lifeEnd = DateTime.Parse(person[i, 3]);
                DateTime workStart = DateTime.Parse(person[i, 4]);
                DateTime workEnd = DateTime.Parse(person[i, 5]);

                // 計算差異天數
                TimeSpan lifeDay = lifeEnd - lifeStart;
                int lifedayCount = (int)lifeDay.TotalDays;
                richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                TimeSpan workDay = workEnd - workStart;
                int workdayCount = (int)workDay.TotalDays;
                richTextBox1.Text += "在位 " + workdayCount.ToString() + " 天" + "\t" + DayConversionYMD(workdayCount) + "\n";

                x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + 50 * (num - 1) + offset_y;

                w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
                h = 40;

                g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));
                g.DrawRectangle(p, x_st, y_st, w, h);

                f = new Font("標楷體", 22);
                int tmp_width = 0;
                string str = string.Empty;

                str = num.ToString() + "." + person[i, 1];

                tmp_width = g.MeasureString(str, f).ToSize().Width;
                //richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "\n";

                g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st - tmp_width, y_st + 5));

                x_st = BORDER + ((int)(lifeEnd - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + 50 * (num - 1);
                g.DrawString("(" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) +
                             ", " + ((double)(workdayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")",
                    f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));

                x_st = BORDER + ((int)(workStart - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + HEIGHT * (num - 1);
                w = ((int)(workEnd - workStart).TotalDays) / ratio;
                h = HEIGHT * 4 / 5;
                if (w == 0)
                    w = 1;
                g.FillRectangle(new SolidBrush(Color.Red), new Rectangle(x_st, y_st, w, h));
                g.DrawRectangle(p, x_st, y_st, w, h);
                //richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";
            }
            pictureBox1.Image = bitmap1;
        }

        public string DayConversionYMD(int day)
        {
            if (day > 365)
                return (day / 365).ToString() + " 年" + ((day % 365) / 30).ToString() + " 月" + ((day % 365) % 30).ToString() + " 日";
            else if (day > 30)
                return (day / 30).ToString() + " 月" + ((day % 365) % 30).ToString() + " 日";
            else
                return day.ToString() + " 日";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            draw_emperor_data(EMPEROR_DATA_TANG);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            draw_emperor_data(EMPEROR_DATA_CHING);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            draw_emperor_data(EMPEROR_DATA_SUI);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            draw_person_data(PERSON_DATA_1);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            draw_person_data(PERSON_DATA_2);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            draw_person_data(PERSON_DATA_3);
        }
    }
}
