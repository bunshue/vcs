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

            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Normal;
            this.Size = new Size(1920, 1080);
            this.Location = new Point(0, 0);
            this.BackColor = Color.Pink;

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1200;
            y_st = 10;
            dx = 100;
            dy = 42;

            //row 0
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            //row 1
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            //row 2
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);

            //row 3
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            //row 4
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button2.Location = new Point(x_st + dx * 1, y_st + dy * 4);

            //row 5
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            //row 6
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);



            //row 7
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button9.Location = new Point(x_st + dx * 1 - dx / 4 + 5, y_st + dy * 7);
            button5.Location = new Point(x_st + dx * 1 + dx / 3 + 10, y_st + dy * 7);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (g != null)
            {
                //清除畫布
                //g.Clear(Color.White);
                g.Clear(BackColor);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。

                pictureBox1.Image = bitmap1;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
        private const int PERSON_DATA_GREAT = 0x20;   //person data, 有名的人
        private const int PERSON_DATA_MODERN = 0x21;   //person data, 近現人物

        private const int LEADER_DATA_0 = 0x00;      //leader data 0, 隋唐
        private const int LEADER_DATA_1 = 0x01;      //leader data 1, 明末
        private const int LEADER_DATA_2 = 0x02;      //leader data 2, 清末
        private const int LEADER_DATA_3 = 0x03;      //leader data 3

        string[,] person = null;

        void load_personData(int index)
        {
            if (index == PERSON_DATA_1)
            {
                person = new string[,] { 
                { "寇準", "961年", "1023年10月24日"},
                { "范仲淹", "989年10月1日", "1052年6月19日"},
                { "包拯", "999年3月5日", "1062年7月3日"},
                { "歐陽修", "1007年8月1日", "1072年9月22日"},
                { "司馬光", "1019年11月17日", "1086年10月11日"},
                { "王安石", "1021年12月18日", "1086年5月21日"},
                { "蘇軾", "1037年1月8日", "1101年8月24日"},
                { "黃庭堅", "1045年", "1105年"},
                { "秦觀", "1049年", "1100年9月17日"},
                { "宋徽宗", "1082年6月7日", "1135年6月4日"},
                { "李清照", "1084年3月13日", "1155年5月12日"},
                { "宋欽宗", "1100年5月23日", "1161年6月14日"},
                { "岳飛", "1103年3月24日", "1142年1月27日"},
                { "宋高宗", "1107年5月21日", "1187年11月9日"},
                { "朱熹", "1130年10月22日", "1200年4月23日"},
                { "辛棄疾", "1140年5月28日", "1207年10月3日"},
                { "宋理宗", "1205年1月26日", "1264年11月16日"},
                { "文天祥", "1236年6月6日", "1283年1月9日"},
                { "宋度宗", "1240年5月2日", "1274年8月12日"},
                };
            }
            else if (index == PERSON_DATA_2)
            {
                person = new string[,] { 
                { "嘉靖帝", "1507年9月16日", "1567年1月23日"},
                { "隆慶帝", "1537年3月4日", "1572年7月5日"},
                { "萬曆帝", "1563年9月4日", "1620年8月18日"},
                { "泰昌帝", "1582年8月28日", "1620年9月26日"},
                { "天啟帝", "1605年12月23日", "1627年9月30日"},
                { "崇禎帝", "1611年2月6日", "1644年4月25日"},
                { "哥倫布", "1451年", "1506年5月20日"},
                { "哥白尼", "1473年2月19日", "1543年5月24日"},
                { "湯顯祖", "1550年9月24日", "1616年7月29日"},
                { "莎士比亞", "1564年4月26日", "1616年4月23日"},
                { "伊莉莎白一世", "1533年9月7日", "1603年3月24日"},
                { "努爾哈赤", "1559年2月21日", "1626年9月30日"},
                { "皇太極", "1592年11月28日", "1643年9月21日"},
                { "牛頓", "1643年1月4日", "1727年3月31日"},
                { "萊布尼茲", "1646年7月1日", "1716年11月14日"},
                { "徐霞客", "1587年1月5日", "1641年3月8日"},
                { "吳三桂", "1612年6月8日", "1678年10月2日"},
                { "宋應星", "1587年", "1666年"},
                { "魏忠賢", "1568年2月27日", "1627年12月11日"},
                { "張居正", "1525年5月26日", "1582年7月9日"},
                { "王守仁", "1472年10月31日", "1529年1月9日"},
                { "袁崇煥", "1584年6月6日", "1630年9月22日"},
                { "戚繼光", "1528年11月12日", "1588年1月17日"},
                { "徐渭", "1521年3月12日", "1593年"},
                { "唐寅", "1470年3月6日", "1524年1月7日"},
                { "豐臣秀吉", "1537年3月17日", "1598年9月18日"},
                { "織田信長", "1534年5月24日", "1582年6月21日"},
                { "德川家康", "1542年1月31日", "1616年6月1日"},
                { "李時珍", "1518年7月3日", "1593年"},
                { "顧炎武", "1613年7月15日", "1682年2月15日"},
                };
            }
            else if (index == PERSON_DATA_3)
            {
                person = new String[,] { 
                { "雍正帝", "1678年12月13日", "1735年10月8日"},
                { "年羹堯", "1679年", "1726年1月15日"},
                { "乾隆帝", "1711年9月25日", "1799年2月7日"},
                { "嘉慶帝", "1760年11月13日", "1820年9月2日"},
                { "紀昀", "1724年8月3日", "1805年3月14日"},
                { "和珅", "1750年7月1日", "1799年2月22日"},
                { "道光帝", "1782年9月16日", "1850年2月26日"},
                { "咸豐帝", "1831年7月17日", "1861年8月22日"},
                { "同治帝", "1856年4月27日", "1875年1月12日"},
                { "光緒帝", "1871年8月14日", "1908年11月14日"},
                { "奕訢", "1833年1月11日", "1898年5月29日"},
                { "奕譞", "1840年10月16日", "1891年1月1日"},
                { "慈禧", "1835年11月29日", "1908年11月15日"},
                { "隆裕", "1868年1月28日", "1913年2月22日"},
                { "袁世凱", "1859年9月16日", "1916年6月6日"},
                { "曾國藩", "1811年11月26日", "1872年3月12日"},
                { "左宗棠", "1812年11月10日", "1885年9月5日"},
                { "張之洞", "1837年9月2日", "1909年10月4日"},
                { "榮祿", "1836年4月6日", "1903年4月11日"},
                { "李鴻章", "1823年2月15日", "1901年11月7日"},
                { "華盛頓", "1732年2月22日", "1799年12月14日"},
                { "拿破崙", "1769年8月15日", "1821年5月5日"},
                { "路易十四", "1638年9月5日", "1715年9月1日"},
                { "路易十六", "1754年8月23日", "1793年1月21日"},
                { "林肯", "1809年2月12日", "1865年4月15日"},
                { "莫札特", "1756年1月27日", "1791年12月5日"},
                { "貝多芬", "1770年12月16日", "1827年3月26日"},
                { "維多利亞女王", "1819年5月24日", "1901年1月22日"},
                { "俾斯麥", "1815年4月1日", "1898年7月30日"},
                { "伊藤博文", "1841年10月16日", "1909年10月26日"},
                { "明治天皇", "1852年11月3日", "1912年7月30日"},
                };
            }
            else if (index == PERSON_DATA_GREAT)
            {
                person = new string[,] { 
                { "哥白尼", "1473年2月19日", "1543年5月24日",  "波蘭"},
                { "伽利略", "1564年2月15日", "1642年1月8日" , "義大利"},
                { "克卜勒", "1571年12月27日", "1630年11月15日" , "德國"},
                { "牛頓", "1643年1月4日", "1727年3月31日" , "英國"},
                { "哈雷", "1656年11月8日", "1742年1月14日" , "英國"},
                { "萊布尼茲", "1646年7月1日", "1716年11月14日" , "德國"},
                { "伏爾泰", "1694年11月21日", "1778年5月30日" , "法國"},
                { "雨果", "1802年2月26日", "1885年5月22日" , "法國"},
                { "馬克士威", "1831年6月13日", "1879年11月5日" , "蘇格蘭"},
                { "尼采", "1844年10月15日", "1900年8月25日" , "德國"},
                { "愛迪生", "1847年2月11日", "1931年10月18日" , "美國"},
                { "亨利·福特", "1863年7月30日", "1947年4月7日" , "美國"},
                { "普朗克(Planck)", "1858年4月23日", "1947年10月4日" , "德國"},
                { "居禮夫人", "1867年11月7日", "1934年7月4日" , "波蘭裔法國"},
                { "愛因斯坦", "1879年3月14日", "1955年4月18日" , "猶太裔"},
                { "海森堡", "1901年12月5日", "1976年2月1日" , "德國"},
                { "傅立葉", "1768年3月21日", "1830年5月16日" ,  "法國"},
                { "法拉第", "1791年9月22日", "1867年8月25日" , "英國"},
                { "達爾文", "1809年2月12日", "1882年4月19日" , "英國"},
                { "亨利", "1797年12月17日", "1878年5月13日" , "美國"},
                { "笛卡兒", "1596年3月31日", "1650年2月11日" , "法國"},
                { "達文西", "1452年4月15日", "1519年5月2日" , "義大利"},
                { "米開朗基羅", "1475年3月6日", "1564年2月18日" , "義大利"},
                { "拉斐爾", "1483年3月28日", "1520年4月6日" , "義大利"},
                { "安培", "1775年1月20日", "1836年6月10日","法國"},
                { "拉普拉斯", "1749年3月23日", "1827年3月5日","法國"},
                { "白努利", "1700年2月8日", "1782年3月17日","荷蘭"},
                { "歐拉", "1707年4月15日", "1783年9月18日","瑞士"},
                { "庫侖", "1736年", "1806年","法國"},
                { "高斯", "1777年4月30日", "1855年2月23日", "德國"},
                { "韋伯", "1804年10月24日", "1891年6月23日", "德國"},
                { "厄斯特", "1777年8月14日", "1851年3月9日", "丹麥"},
                { "赫茲", "1857年2月22日", "1894年1月1日", "德國"},
                { "伏打", "1745年2月18日", "1827年3月5日", "義大利"},
                { "波以耳", "1627年1月25日", "1691年12月30日", "愛爾蘭"},
                { "虎克", "1635年7月28日", "1703年3月3日", "英國"},
                { "給呂薩克", "1778年12月6日", "1850年5月10日", "法國"},
                { "歐姆", "1789年3月16日", "1854年7月6日", "德國"},
                { "帕松(Poisson)", "1781年6月21日", "1840年4月25日", "法國"},
                { "馬可尼", "1874年4月25日", "1937年7月20日", "義大利"},
                { "特斯拉", "1856年7月10日", "1943年1月7日", "塞爾維亞裔美籍"},
                { "班傑明·富蘭克林", "1706年1月17日", "1790年4月17日", "美國"},
                { "惠更斯", "1629年4月14日", "1695年7月8日", "荷蘭"},
                { "莫札特", "1756年1月27日", "1791年12月5日", "奧地利"},
                { "貝多芬", "1770年12月16日", "1827年3月26日", "德國"},
                { "柴可夫斯基", "1840年5月7日", "1893年11月6日" , "俄羅斯"},
                { "湯顯祖", "1550年9月24日", "1616年7月29日" , "中國"},
                { "莎士比亞", "1564年4月26日", "1616年4月23日" , "英國"},
                { "喬治·伊士曼", "1854年7月12日", "1932年3月14日", "美國"},
                { "司乃耳", "1580年6月13日", "1626年10月30日", "荷蘭"},
                { "徐光啟", "1562年4月24日", "1633年11月8日", "中國"},
                { "利瑪竇", "1552年10月6日", "1610年5月11日", "義大利"},
                { "摩斯", "1791年4月27日", "1872年4月2日", "美國"},
                { "郎世寧", "1688年7月19日", "1766年7月17日", "義大利"},
                { "南懷仁", "1623年10月9日", "1688年1月28日", "比利時"},
                { "約翰·史蒂斯·彭伯頓(John Stith Pemberton)", "1831年7月8日", "1888年8月16日", "美國"},
                { "諾貝爾(Alfred Bernhard Nobel)", "1833年10月21日", "1896年12月10日", "瑞典"},
                { "詹姆斯·瓦特(James Watt)", "1736年1月19日", "1819年8月25日", "英國"},
                { "約瑟夫·湯姆森(Joseph John Thomson)", "1856年12月18日", "1940年8月30日", "英國"},
                { "德布羅意(Broglie)", "1892年8月15日", "1987年3月19日", "法國"},
                { "薛丁格(Schrödinger)", "1887年8月12日", "1961年1月4日", "奧地利"},
                { "南丁格爾", "1820年5月12日", "1910年8月13日", "英國"},
                { "克希荷夫(Kirchhoff)", "1824年3月12日", "1887年10月17日", "德國"},
                { "喬治·史蒂文生(George Stephenson)", "1781年6月9日", "1848年8月12日", "英國"},
                { "歐尼斯特·拉塞福(Ernest Rutherford)", "1871年8月30日", "1937年10月19日", "紐西蘭"},
                { "羅伯特·威廉·本生(Robert Wilhelm Bunsen)", "1811年3月30日", "1899年8月16日", "德國"},
                { "戴維寧(Thévenin)", "1857年3月30日", "1926年9月21日", "法國"},
                { "恩斯特·馬赫(Ernst Mach)", "1838年2月18日", "1916年2月19日", "奧地利-捷克"},
                { "諾頓(Norton)", "1898年7月28日", "1983年1月28日", "美國"},
                { "霍爾(Hall)", "1855年11月7日", "1938年11月20日", "美國"},
                { "倫琴(Röntgen)", "1845年3月27日", "1923年2月10日", "德國"},
                { "波茲曼(Boltzmann)", "1844年2月20日", "1906年9月5日", "奧地利"},
                { "波耳(Bohr)", "1885年10月7日", "1962年11月18日", "丹麥"},
                { "哥倫布", "1451年10月31日", "1506年5月20日", "義大利"},
                { "達伽馬", "1460年", "1524年12月24日", "葡萄牙"},
                { "麥哲倫", "1480年10月17日", "1521年4月27日", "葡萄牙"},
                { "路易·巴斯德", "1822年12月27日", "1895年9月28日", "法國"},
                { "拉瓦節", "1743年8月26日", "1794年5月8日", "法國"},
                { "卡爾·馬克思(Karl Marx)", "1818年5月5日", "1883年3月14日", "猶太裔德國"},
                { "恩格斯", "1820年11月28日", "1895年8月5日" , "德國"},
                { "亞當·史密斯(Adam Smith)", "1723年6月16日", "1790年7月17日", "蘇格蘭"},
                { "約翰·道耳頓(John Dalton)", "1766年9月6日", "1844年7月27日", "英國"},
                { "焦耳(Joule)", "1818年12月24日", "1889年10月12日", "英國"},
                { "弗萊明", "1881年8月6日", "1955年3月11日", "蘇格蘭"},
                { "貝爾", "1847年3月3日", "1922年8月2日", "加拿大"},
                { "孟德爾", "1822年7月20日", "1884年1月6日", "奧地利"},
                { "佛洛伊德", "1856年5月6日", "1939年9月23日", "奧地利"},
                { "愛德華·詹納", "1749年5月17日", "1823年1月26日", "英國"},
                { "巴哈", "1685年3月31日", "1750年7月28日", "德國"},
                { "恩里科·費米(Enrico Fermi)", "1901年9月29日", "1954年11月28日", "義大利裔美籍"},
                { "盧梭", "1712年6月28日", "1778年7月2日", "法國"},
                { "馬基維利", "1469年5月3日", "1527年6月21日", "義大利"},
                { "馬爾薩斯", "1766年2月13日", "1834年12月29日", "英國"},
                { "都卜勒", "1803年11月29日", "1853年3月17日", "奧地利"},
                { "雷諾瓦", "1841年2月25日", "1919年12月3日", "法國"},
                { "文森·威廉·梵谷(Vincent Willem van Gogh)", "1853年3月30日", "1890年7月29日", "荷蘭"},
                { "畢卡索", "1881年10月25日", "1973年4月8日", "西班牙"},
                { "開利(Carrier)", "1876年11月26日", "1950年10月7日", "美國"},
                { "曹雪芹", "1715年6月4日", "1763年", "中國"},
                { "洪昇", "1645年8月21日", "1704年7月2日", "中國"},
                { "孔尚任", "1648年11月1日", "1718年2月14日", "中國"},
                { "錢謙益", "1582年10月22日", "1664年6月17日" , "中國"},
                { "柳如是", "1618年", "1664年6月28日" , "中國"},
                { "紀曉嵐", "1724年8月3日", "1805年3月14日" , "中國"},
                { "胡適", "1891年12月17日", "1962年2月24日", "中國"},

                { "約翰·杜威(John Dewey)", "1859年10月20日", "1952年6月1日", "美國"},

                //{ "xxxxx", "xxxxx", "xxxxx" , "xxxxxx"},
                //{ "xxxxx", "xxxxx", "xxxxx" , "xxxxxx"},
                };

            }
            else if (index == PERSON_DATA_MODERN)
            {
                person = new string[,] { 
                { "卡爾·馬克思(Karl Marx)", "1818年5月5日", "1883年3月14日", "猶太裔德國"},
                { "恩格斯", "1820年11月28日", "1895年8月5日" , "德國"},
                { "胡適", "1891年12月17日", "1962年2月24日", "中國"},

                //中方 溥儀載灃奕劻汪精衛胡漢民
                //國方 蔣介石陳誠孫文何應欽蔣經國四大家族
                //共方 毛澤東十大元帥江青 附共者
                //蘇聯 列寧 史達林 赫魯雪夫
                //美國
                //其他國

                { "約翰·杜威(John Dewey)", "1859年10月20日", "1952年6月1日", "美國"},

                //{ "xxxxx", "xxxxx", "xxxxx" , "xxxxxx"},
                //{ "xxxxx", "xxxxx", "xxxxx" , "xxxxxx"},
                };


            }
            else
            {
                person = new string[,] { 
                { "xxx", "1550年9月24日", "1616年7月29日" , "country"},
                };
            }
        }

        void load_emperorData(int index)
        {
            if (index == EMPEROR_DATA_SUI)
            {
                person = new string[,] {
                { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
                { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
                };
            }
            else if (index == EMPEROR_DATA_TANG)
            {
                person = new string[,] { 
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
                person = new string[,] { 
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
                person = new string[,] {
                { "1", "xxx", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                };
            }
        }

        void load_leaderData(int index)
        {
            if (index == LEADER_DATA_0)
            {
                person = new string[,] {
                { "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                { "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
                { "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
                };
            }
            else if (index == LEADER_DATA_1)
            {
                person = new string[,] { 
                { "唐高祖", "566年4月7日", "635年6月25日", "618年6月18日", "626年9月4日"},
                { "唐太宗", "598年1月23日", "649年7月10日", "626年9月4日", "649年7月10日"},
                { "唐高宗", "628年7月21日", "683年12月27日", "649年7月15日", "683年12月27日"},
                { "唐中宗", "656年11月26日", "710年7月3日", "684年1月3日","684年2月26日"},
                { "唐睿宗", "662年6月22日", "716年7月13日", "684年2月27日","690年10月16日"},
                { "則天后", "624年2月17日", "705年12月16日", "690年10月16日", "705年2月21日"},
                { "唐中宗", "656年11月26日", "710年7月3日", "705年2月23日","710年7月3日"},
                { "唐睿宗", "662年6月22日", "716年7月13日", "710年7月25日","712年9月8日"},
                { "唐玄宗", "685年9月8日", "762年5月3日", "712年9月8日", "756年8月1日"},
                { "唐肅宗", "711年1月21日","762年5月16日", "756年8月12日", "762年5月16日"},
                { "唐代宗", "726年11月11日", "779年6月10日", "762年5月18日", "779年6月10日"},
                { "唐德宗", "742年5月27日", "805年2月25日", "779年6月12日", "805年2月25日"},
                { "唐順宗", "761年2月21日", "806年2月11日", "805年2月28日", "805年8月31日"},
                { "唐憲宗", "778年3月17日", "820年2月14日", "805年9月5日", "820年2月14日"},
                { "唐穆宗", "795年7月26日", "824年2月25日", "820年2月20日", "824年2月25日"},
                { "唐敬宗", "809年7月22日", "827年1月9日", "824年2月29日", "827年1月9日"},
                { "唐文宗", "809年11月20日", "840年2月10日", "827年1月13日", "840年2月10日"},
                { "唐武宗", "814年7月2日", "846年4月22日", "840年2月20日", "846年4月22日"},
                { "唐宣宗", "810年7月27日", "859年9月10日", "846年4月22日", "859年9月10日"},
                { "唐懿宗", "833年12月28日", "873年8月15日", "859年9月13日", "873年8月15日"},
                { "唐僖宗", "862年6月8日", "888年4月20日", "873年8月16日", "888年4月20日"},
                { "唐昭宗", "867年3月31日", "904年9月22日", "888年4月22日", "904年9月22日"},
                { "唐哀帝", "892年10月27日", "908年3月26日", "904年9月27日", "907年5月12日"},
                };
            }
            else if (index == LEADER_DATA_2)
            {
                person = new string[,] { 
                { "清太祖", "1559年2月21日", "1626年9月30日", "1616年2月17日", "1626年9月30日"},
                { "清太宗", "1592年11月28日", "1643年9月21日", "1626年10月20日", "1643年9月21日"},
                { "順治", "1638年3月15日", "1661年2月5日", "1643年10月8日", "1661年2月5日"},
                { "康熙", "1654年5月4日", "1722年12月20日", "1661年2月5日", "1722年12月20日"},
                { "雍正", "1678年12月13日", "1735年10月8日", "1722年12月20日", "1735年10月7日"},
                { "乾隆", "1711年9月25日", "1799年2月7日", "1735年10月18日", "1796年2月9日"},
                { "嘉慶", "1760年11月14日", "1820年9月2日", "1796年2月9日", "1820年9月2日"},
                { "道光", "1782年9月16日", "1850年2月26日", "1820年10月3日", "1850年2月26日"},
                { "咸豐", "1831年7月17日", "1861年8月22日", "1850年3月9日", "1861年8月22日"},
                { "同治", "1856年4月27日", "1875年1月12日", "1861年11月11日", "1875年1月12日"},
                { "光緒", "1871年8月14日", "1908年11月14日", "1875年2月25日", "1908年11月14日"},
                { "宣統", "1906年2月7日", "1967年10月17日", "1908年12月2日", "1912年2月12日"},
                };
            }
            else
            {
                person = new string[,] {
                { "xxx", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                };
            }
        }

        void draw_person_data(int index)
        {
            richTextBox1.Clear();

            load_personData(index);

            DateTime lifeEarliest = DateTime.Now;
            DateTime lifeEarliest2 = DateTime.Now;
            DateTime lifeLatest = new DateTime(1, 1, 1);
            DateTime lifeStart;
            DateTime lifeEnd;
            TimeSpan lifeDay;
            int lifedayCount;
            int row = 0;
            string str;


            int i;
            int total_persons = person.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_persons = " + total_persons.ToString() + "\n";
            int current_index = 0;
            int next_index = 0;
            DateTime current_life_sp;

            int[] person_used = new int[total_persons];
            for (i = 0; i < total_persons; i++)
            {
                person_used[i] = 0;
            }

            for (i = 0; i < total_persons; i++)
            {
                lifeStart = DateTime.Parse(person[i, 1]);
                lifeEnd = DateTime.Parse(person[i, 2]);

                if (lifeEarliest > lifeStart)
                {
                    lifeEarliest = lifeStart;
                    //current_index = i;
                }

                if (lifeLatest < lifeEnd)
                    lifeLatest = lifeEnd;

                // 計算差異天數
                lifeDay = lifeEnd - lifeStart;
                lifedayCount = (int)lifeDay.TotalDays;
                //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";
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
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT + BORDER * 2);
            pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT / 2 + BORDER * 2);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            g.DrawRectangle(new Pen(Color.Lime), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            //找出最早的時間
            lifeEarliest2 = DateTime.Now;
            for (i = 0; i < total_persons; i++)
            {
                if (person_used[i] == 0)
                {
                    lifeStart = DateTime.Parse(person[i, 1]);

                    if (lifeEarliest2 > lifeStart)
                    {
                        lifeEarliest2 = lifeStart;
                        current_index = i;
                    }
                }
            }

            current_life_sp = DateTime.Parse(person[current_index, 2]);

            /*
            richTextBox1.Text += "取得時間最早的項目, index = " + current_index.ToString() + "\n";
            richTextBox1.Text += "此項目的名字 = " + person[current_index, 0] + "\n";
            richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[current_index, 1]).ToString() + "\n";
            richTextBox1.Text += "此項目的壽命結束時間 = " + current_life_sp.ToString() + "\n";
            richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
            */

            lifeStart = DateTime.Parse(person[current_index, 1]);
            lifeEnd = DateTime.Parse(person[current_index, 2]);

            // 計算差異天數
            lifeDay = lifeEnd - lifeStart;
            lifedayCount = (int)lifeDay.TotalDays;
            //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

            x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;

            y_st = BORDER + 50 * row + offset_y;

            w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
            h = 40;

            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

            g.DrawRectangle(p, x_st, y_st, w, h);

            f = new Font("標楷體", 22);
            str = person[current_index, 0] + " (" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")";

            g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));

            person_used[current_index] = 1;

            TimeSpan time_diff;
            int smallest_diff;

            for (int k = 0; k < (total_persons - 1); k++)
            {
                //richTextBox1.Text += "\nk = " + k.ToString() + "\n\n";
                smallest_diff = 500 * 365;  //500年

                for (i = 0; i < total_persons; i++)
                {
                    if (person_used[i] == 0)
                    {
                        if (DateTime.Parse(person[i, 1]) > current_life_sp)
                        {
                            time_diff = DateTime.Parse(person[i, 1]) - current_life_sp;
                            if ((time_diff.TotalDays > 365) && ((int)time_diff.TotalDays < smallest_diff))
                            {
                                smallest_diff = (int)time_diff.TotalDays;
                                next_index = i;
                            }
                        }
                    }
                }
                //richTextBox1.Text += "smallest_diff = " + smallest_diff.ToString() + "\n";
                if (smallest_diff == 500 * 365)
                {
                    //richTextBox1.Text += "已搜尋到底，要畫下一行。\n";
                    row++;
                    //從剩下的項目，找出最早的時間
                    //找出最早的時間
                    lifeEarliest2 = DateTime.Now;
                    for (i = 0; i < total_persons; i++)
                    {
                        if (person_used[i] == 0)
                        {
                            lifeStart = DateTime.Parse(person[i, 1]);

                            if (lifeEarliest2 > lifeStart)
                            {
                                lifeEarliest2 = lifeStart;
                                current_index = i;
                            }
                        }
                    }
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    /*
                    richTextBox1.Text += "取得剩下的項目裡面時間最早的項目, index = " + current_index.ToString() + "\n";
                    richTextBox1.Text += "此項目的名字 = " + person[current_index, 0] + "\n";
                    richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[current_index, 1]).ToString() + "\n";
                    richTextBox1.Text += "此項目的壽命結束時間 = " + current_life_sp.ToString() + "\n";
                    richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
                    */
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    person_used[current_index] = 1;
                }
                else
                {
                    current_index = next_index;
                    /*
                    richTextBox1.Text += "取得下一個項目, index = " + next_index.ToString() + "\n";
                    richTextBox1.Text += "此項目的名字 = " + person[next_index, 0] + "\n";
                    richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[next_index, 1]).ToString() + "\n";
                    richTextBox1.Text += "此項目的壽命結束時間 = " + DateTime.Parse(person[next_index, 2]).ToString() + "\n";
                    richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
                    */
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    person_used[current_index] = 1;
                }

                lifeStart = DateTime.Parse(person[current_index, 1]);
                lifeEnd = DateTime.Parse(person[current_index, 2]);

                // 計算差異天數
                lifeDay = lifeEnd - lifeStart;
                lifedayCount = (int)lifeDay.TotalDays;
                //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + 50 * row + offset_y;

                w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
                h = 40;

                g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

                g.DrawRectangle(p, x_st, y_st, w, h);

                f = new Font("標楷體", 22);
                str = person[current_index, 0] + " (" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")";

                g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));
            }
            richTextBox1.Text += "row = " + row.ToString() + "\n";
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, (row + 2) * HEIGHT + BORDER * 2);  ????
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, 200);  ????

            pictureBox1.Image = bitmap1;
        }

        void draw_leader_data(int index)
        {
            richTextBox1.Clear();

            load_leaderData(index);

            DateTime lifeEarliest = DateTime.Now;
            DateTime lifeEarliest2 = DateTime.Now;
            DateTime lifeLatest = new DateTime(1, 1, 1);
            DateTime lifeStart;
            DateTime lifeEnd;
            DateTime workStart;
            DateTime workEnd;
            TimeSpan lifeDay;
            TimeSpan workDay;
            DateTime workEarliest = DateTime.Now;
            DateTime workLatest = new DateTime(1, 1, 1);

            int lifedayCount;
            int workdayCount;
            int row = 0;
            string str;

            int i;
            int total_persons = person.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_persons = " + total_persons.ToString() + "\n";
            int current_index = 0;
            int next_index = 0;
            DateTime current_life_sp;

            int[] person_used = new int[total_persons];
            for (i = 0; i < total_persons; i++)
            {
                person_used[i] = 0;
            }

            for (i = 0; i < total_persons; i++)
            {
                lifeStart = DateTime.Parse(person[i, 1]);
                lifeEnd = DateTime.Parse(person[i, 2]);
                workStart = DateTime.Parse(person[i, 3]);
                workEnd = DateTime.Parse(person[i, 4]);

                if (lifeEarliest > lifeStart)
                {
                    lifeEarliest = lifeStart;
                    //current_index = i;
                }

                if (lifeLatest < lifeEnd)
                    lifeLatest = lifeEnd;

                if (workEarliest > workStart)
                    workEarliest = workStart;

                if (workLatest < workEnd)
                    workLatest = workEnd;

                // 計算差異天數
                lifeDay = lifeEnd - lifeStart;
                lifedayCount = (int)lifeDay.TotalDays;
                //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                // 計算差異天數
                lifeDay = lifeEnd - lifeStart;
                lifedayCount = (int)lifeDay.TotalDays;
                //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                workDay = workEnd - workStart;
                workdayCount = (int)workDay.TotalDays;
                //richTextBox1.Text += "在位 " + workdayCount.ToString() + " 天" + "\t" + DayConversionYMD(workdayCount) + "\n";
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
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT + BORDER * 2);
            pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, total_persons * HEIGHT / 2 + BORDER * 2);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            g.DrawRectangle(new Pen(Color.Lime), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            //找出最早的時間
            lifeEarliest2 = DateTime.Now;
            for (i = 0; i < total_persons; i++)
            {
                if (person_used[i] == 0)
                {
                    lifeStart = DateTime.Parse(person[i, 1]);

                    if (lifeEarliest2 > lifeStart)
                    {
                        lifeEarliest2 = lifeStart;
                        current_index = i;
                    }
                }
            }

            current_life_sp = DateTime.Parse(person[current_index, 2]);

            /*
            richTextBox1.Text += "取得時間最早的項目, index = " + current_index.ToString() + "\n";
            richTextBox1.Text += "此項目的名字 = " + person[current_index, 0] + "\n";
            richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[current_index, 1]).ToString() + "\n";
            richTextBox1.Text += "此項目的壽命結束時間 = " + current_life_sp.ToString() + "\n";
            richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
            */

            lifeStart = DateTime.Parse(person[current_index, 1]);
            lifeEnd = DateTime.Parse(person[current_index, 2]);
            workStart = DateTime.Parse(person[current_index, 3]);
            workEnd = DateTime.Parse(person[current_index, 4]);

            // 計算差異天數
            lifeDay = lifeEnd - lifeStart;
            lifedayCount = (int)lifeDay.TotalDays;
            //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

            workDay = workEnd - workStart;
            workdayCount = (int)workDay.TotalDays;
            //richTextBox1.Text += "在位 " + workdayCount.ToString() + " 天" + "\t" + DayConversionYMD(workdayCount) + "\n";

            x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;
            y_st = BORDER + 50 * row + offset_y;

            w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
            h = 40;

            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

            g.DrawRectangle(p, x_st, y_st, w, h);

            f = new Font("標楷體", 22);
            str = person[current_index, 0] + " (" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")";
            g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));

            x_st = BORDER + ((int)(workStart - lifeEarliest).TotalDays) / ratio + offset_x;
            w = ((int)(workEnd - workStart).TotalDays) / ratio;
            h = HEIGHT * 4 / 5;
            if (w == 0)
                w = 1;
            g.FillRectangle(new SolidBrush(Color.Red), new Rectangle(x_st, y_st, w, h));
            g.DrawRectangle(p, x_st, y_st, w, h);
            //richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";

            person_used[current_index] = 1;

            TimeSpan time_diff;
            int smallest_diff;

            for (int k = 0; k < (total_persons - 1); k++)
            {
                //richTextBox1.Text += "\nk = " + k.ToString() + "\n\n";
                smallest_diff = 500 * 365;  //500年

                for (i = 0; i < total_persons; i++)
                {
                    if (person_used[i] == 0)
                    {
                        if (DateTime.Parse(person[i, 1]) > current_life_sp)
                        {
                            time_diff = DateTime.Parse(person[i, 1]) - current_life_sp;
                            if ((time_diff.TotalDays > 365) && ((int)time_diff.TotalDays < smallest_diff))
                            {
                                smallest_diff = (int)time_diff.TotalDays;
                                next_index = i;
                            }
                        }
                    }
                }
                //richTextBox1.Text += "smallest_diff = " + smallest_diff.ToString() + "\n";
                if (smallest_diff == 500 * 365)
                {
                    //richTextBox1.Text += "已搜尋到底，要畫下一行。\n";
                    row++;
                    //從剩下的項目，找出最早的時間
                    //找出最早的時間
                    lifeEarliest2 = DateTime.Now;
                    for (i = 0; i < total_persons; i++)
                    {
                        if (person_used[i] == 0)
                        {
                            lifeStart = DateTime.Parse(person[i, 1]);

                            if (lifeEarliest2 > lifeStart)
                            {
                                lifeEarliest2 = lifeStart;
                                current_index = i;
                            }
                        }
                    }
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    /*
                    richTextBox1.Text += "取得剩下的項目裡面時間最早的項目, index = " + current_index.ToString() + "\n";
                    richTextBox1.Text += "此項目的名字 = " + person[current_index, 0] + "\n";
                    richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[current_index, 1]).ToString() + "\n";
                    richTextBox1.Text += "此項目的壽命結束時間 = " + current_life_sp.ToString() + "\n";
                    richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
                    */
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    person_used[current_index] = 1;
                }
                else
                {
                    current_index = next_index;
                    /*
                    richTextBox1.Text += "取得下一個項目, index = " + next_index.ToString() + "\n";
                    richTextBox1.Text += "此項目的名字 = " + person[next_index, 0] + "\n";
                    richTextBox1.Text += "此項目的壽命開始時間 = " + DateTime.Parse(person[next_index, 1]).ToString() + "\n";
                    richTextBox1.Text += "此項目的壽命結束時間 = " + DateTime.Parse(person[next_index, 2]).ToString() + "\n";
                    richTextBox1.Text += "畫第 " + current_index.ToString() + " 項\n";
                    */
                    current_life_sp = DateTime.Parse(person[current_index, 2]);
                    person_used[current_index] = 1;
                }

                lifeStart = DateTime.Parse(person[current_index, 1]);
                lifeEnd = DateTime.Parse(person[current_index, 2]);
                workStart = DateTime.Parse(person[current_index, 3]);
                workEnd = DateTime.Parse(person[current_index, 4]);

                // 計算差異天數
                lifeDay = lifeEnd - lifeStart;
                lifedayCount = (int)lifeDay.TotalDays;
                //richTextBox1.Text += "壽命 " + lifedayCount.ToString() + " 天" + "\t" + DayConversionYMD(lifedayCount) + "\n";

                x_st = BORDER + ((int)(lifeStart - lifeEarliest).TotalDays) / ratio + offset_x;
                y_st = BORDER + 50 * row + offset_y;

                w = ((int)(lifeEnd - lifeStart).TotalDays) / ratio;
                h = 40;

                g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

                g.DrawRectangle(p, x_st, y_st, w, h);

                f = new Font("標楷體", 22);
                str = person[current_index, 0] + " (" + ((double)(lifedayCount) / (double)365).ToString("N1", CultureInfo.InvariantCulture) + ")";
                g.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(x_st + 5, y_st + 5));

                x_st = BORDER + ((int)(workStart - lifeEarliest).TotalDays) / ratio + offset_x;
                w = ((int)(workEnd - workStart).TotalDays) / ratio;
                h = HEIGHT * 4 / 5;
                if (w == 0)
                    w = 1;
                g.FillRectangle(new SolidBrush(Color.Red), new Rectangle(x_st, y_st, w, h));
                g.DrawRectangle(p, x_st, y_st, w, h);
                //richTextBox1.Text += "x_st = " + (x_st / ratio).ToString() + ", w = " + (w / ratio).ToString() + "\n";
            }
            richTextBox1.Text += "row = " + row.ToString() + "\n";
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, (row + 2) * HEIGHT + BORDER * 2);  ????
            //pictureBox1.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3, 200);  ????
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
            //this.Size = new System.Drawing.Size(totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3 + 10, total_persons * HEIGHT + BORDER * 2 + 10);
            richTextBox1.Text += "this size : W = " + (totalLifeDaysCount / ratio + BORDER * 2 + offset_x * 3).ToString() + ", H = " + (total_persons * HEIGHT + BORDER * 2).ToString() + "\n";

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

        private void button1_Click(object sender, EventArgs e)
        {
            draw_person_data(PERSON_DATA_GREAT);
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************

        #region 移動無邊框Form

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

        private void button5_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            draw_leader_data(LEADER_DATA_0);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            draw_person_data(PERSON_DATA_MODERN);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //生卒最接近

            richTextBox1.Clear();

            load_personData(PERSON_DATA_GREAT);

            DateTime lifeStart1;
            DateTime lifeStart2;
            DateTime lifeEnd1;
            DateTime lifeEnd2;

            int i;
            int j;
            int total_persons = person.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_persons = " + total_persons.ToString() + "\n";

            int threshold = 600;    //天

            for (i = 0; i < (total_persons - 1); i++)
            {
                for (j = (i + 1); j < total_persons; j++)
                {
                    lifeStart1 = DateTime.Parse(person[i, 1]);
                    lifeStart2 = DateTime.Parse(person[j, 1]);

                    lifeEnd1 = DateTime.Parse(person[i, 2]);
                    lifeEnd2 = DateTime.Parse(person[j, 2]);

                    TimeSpan diffLife1 = lifeStart1 - lifeStart2;
                    TimeSpan diffLife2 = lifeEnd1 - lifeEnd2;

                    int diffDays1 = (int)diffLife1.TotalDays;
                    int diffDays2 = (int)diffLife2.TotalDays;

                    //richTextBox1.Text += "diff1 = " + diffDays1.ToString() + "\tdiff2 = " + diffDays2.ToString() + "\n";

                    if ((Math.Abs(diffDays1) + Math.Abs(diffDays2)) < threshold)
                    {
                        richTextBox1.Text += "很相近 : " + person[i, 0] + "\t" + person[j, 0] + "\t差 " + (Math.Abs(diffDays1) + Math.Abs(diffDays2)).ToString() + " 天\n";
                    }
                }
            }
            richTextBox1.Text += "done\n";
        }
    }
}
