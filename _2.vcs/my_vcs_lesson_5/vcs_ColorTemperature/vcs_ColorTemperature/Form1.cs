using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ColorTemperature
{
    public partial class Form1 : Form
    {
        string filepath_color_data = "bbr_color.txt";

        public class RGBInfo
        {
            public string temperature;
            public int r;
            public int g;
            public int b;
            public RGBInfo(string t, int r, int g, int b)
            {
                this.temperature = t;
                this.r = r;
                this.g = g;
                this.b = b;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態

        List<RGBInfo> rgbinfos = new List<RGBInfo>();

        public Form1()
        {
            InitializeComponent();

            bool result;

            result = loadTextData();

            if (result == false)
                return;

            draw_color_temperature_all();
            pictureBox3.Image = vcs_ColorTemperature.Properties.Resources.color_temperature;
        }

        bool loadTextData()
        {
            int i;
            int value_r = 0;
            int value_g = 0;
            int value_b = 0;
            bool flag_skip_comment = false;
            if (System.IO.File.Exists(filepath_color_data) == false)
            {
                richTextBox1.Text += "color_data檔案 " + filepath_color_data + " 不存在，離開。\n";
                return false;
            }
            else
            {
                richTextBox1.Text += "color_data檔案 " + filepath_color_data + " 存在, 開啟，並讀入文字資料\n";

                rgbinfos.Clear();

                string line;
                StreamReader sr = new StreamReader(filepath_color_data, Encoding.Default);

                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
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
                    else if (line[0] == '#')
                    {
                        //comment
                        //richTextBox1.Text += "get comment" + line + "\n";
                        continue;
                    }
                    else if (line[0] == '%')
                    {
                        //comment
                        //richTextBox1.Text += "get comment" + line + "\n";
                        continue;
                    }


                    if (line.Contains("10deg"))
                    {
                        i++;
                        //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";

                        string temperature;
                        temperature = line.Substring(0, 7);
                        //richTextBox1.Text += "temperature = " + temperature + "\t";
                        /*
                        string r;
                        string g;
                        string b;
                        r = line.Substring(65, 3);
                        g = line.Substring(69, 3);
                        b = line.Substring(73, 3);
                        richTextBox1.Text += "R = " + r.ToString() + "  G = " + g.ToString() + "  B = " + b.ToString() + "\n";
                        */

                        value_r = int.Parse(line.Substring(65, 4));
                        value_g = int.Parse(line.Substring(69, 4));
                        value_b = int.Parse(line.Substring(73, 4));
                        //richTextBox1.Text += "R = " + value_r.ToString() + "  G = " + value_g.ToString() + "  B = " + value_b.ToString() + "\n";

                        //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length));
                        rgbinfos.Add(new RGBInfo(temperature, value_r, value_g, value_b));

                    }
                    else
                    {
                        continue;
                    }



                    //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";
                    //all_strings.Add(line);


                    //if (i >= 30)
                    //  break;
                }
                //strings_count = all_strings.Count;
                sr.Close();

                //richTextBox1.Text += "共有 " + lyrics_count.ToString() + " 首\n";
                //richTextBox1.Text += "可用行數 " + strings_count.ToString() + "\n";


                return true;
            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            trackBar1.Value = trackBar1.Value / 100 * 100;
            richTextBox1.Text += "new value = " + trackBar1.Value.ToString() + "\n";
            draw_color_temperature_rgb(trackBar1.Value);
            textBox1.Text = trackBar1.Value.ToString() + " K";
        }

        void draw_color_temperature_all()
        {
            //Graphics g;
            Bitmap bmp;
            //逐點製作圖檔
            int xx;
            int yy;

            int ww = pictureBox2.Width;
            int hh = pictureBox2.Height;

            bmp = new Bitmap(ww, hh);

            //richTextBox1.Text += "rgbinfos.Count = " + rgbinfos.Count.ToString() + "\n";
            for (int i = 0; i < rgbinfos.Count; i++)
            {
                //richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                //richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";
                //" R = " + rgbinfos[i].r.ToString() + " G = " + rgbinfos[i].g.ToString() + " B = " + rgbinfos[i].b.ToString() + "\n";

                //richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                //richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";


                for (yy = 0; yy < hh; yy++)
                {
                    for (xx = (i * 3); xx < (i * 3 + 3); xx++)
                    {
                        bmp.SetPixel(xx, yy, Color.FromArgb(255, rgbinfos[i].r, rgbinfos[i].g, rgbinfos[i].b));
                        //bitmap3.SetPixel(xx, yy, Color.Red);
                    }
                }



            }
            pictureBox2.Image = bmp;

        }


        void draw_color_temperature_rgb(int temp)
        {
            //Graphics g;
            Bitmap bmp;
            //逐點製作圖檔
            int xx;
            int yy;

            int ww = pictureBox1.Width;
            int hh = pictureBox1.Height;

            bmp = new Bitmap(ww, hh);

            //richTextBox1.Text += "rgbinfos.Count = " + rgbinfos.Count.ToString() + "\n";
            for (int i = 0; i < rgbinfos.Count; i++)
            {
                //richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                //richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";
                //" R = " + rgbinfos[i].r.ToString() + " G = " + rgbinfos[i].g.ToString() + " B = " + rgbinfos[i].b.ToString() + "\n";

                if(rgbinfos[i].temperature.Contains(temp.ToString()))
                {
                    richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                    richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";


                    for (yy = 0; yy < hh; yy++)
                    {
                        for (xx = 0; xx < ww; xx++)
                        {
                            bmp.SetPixel(xx, yy, Color.FromArgb(255, rgbinfos[i].r, rgbinfos[i].g, rgbinfos[i].b));
                            //bitmap3.SetPixel(xx, yy, Color.Red);
                        }
                    }
                    pictureBox1.Image = bmp;


                    break;
                }

            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int rgb_max = 0;
            int rgb_index = 0;
            int r_max = 0;
            int r_min = 255;
            int g_max = 0;
            int g_min = 255;
            int b_max = 0;
            int b_min = 255;
            for (int i = 0; i < rgbinfos.Count; i++)
            {
                if (r_max < rgbinfos[i].r)
                    r_max = rgbinfos[i].r;
                if (r_min > rgbinfos[i].r)
                    r_min = rgbinfos[i].r;
                if (g_max < rgbinfos[i].g)
                    g_max = rgbinfos[i].g;
                if (g_min > rgbinfos[i].g)
                    g_min = rgbinfos[i].g;
                if (b_max < rgbinfos[i].b)
                    b_max = rgbinfos[i].b;
                if (b_min > rgbinfos[i].b)
                    b_min = rgbinfos[i].b;

                if (rgb_max < (rgbinfos[i].r + rgbinfos[i].g + rgbinfos[i].b))
                {
                    rgb_max = rgbinfos[i].r + rgbinfos[i].g + rgbinfos[i].b;
                    rgb_index = i;
                }


                //richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                //richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";
                //" R = " + rgbinfos[i].r.ToString() + " G = " + rgbinfos[i].g.ToString() + " B = " + rgbinfos[i].b.ToString() + "\n";

                //richTextBox1.Text += "temperature = " + rgbinfos[i].temperature + "\t";
                //richTextBox1.Text += "R = " + rgbinfos[i].r.ToString() + "  G = " + rgbinfos[i].g.ToString() + "  B = " + rgbinfos[i].b.ToString() + "\n";

            }
            richTextBox1.Text += "r_max = " + r_max.ToString() + "  r_min = " + r_min.ToString() + "\n";
            richTextBox1.Text += "g_max = " + g_max.ToString() + "  g_min = " + g_min.ToString() + "\n";
            richTextBox1.Text += "b_max = " + b_max.ToString() + "  b_min = " + b_min.ToString() + "\n";

            richTextBox1.Text += "rgb_index = " + rgb_index.ToString() + "\n";
            richTextBox1.Text += "temperature = " + rgbinfos[rgb_index].temperature + "\n";
            richTextBox1.Text += "R = " + rgbinfos[rgb_index].r.ToString() + "  G = " + rgbinfos[rgb_index].g.ToString() + "  B = " + rgbinfos[rgb_index].b.ToString() + "\n";

            //Graphics g;
            Bitmap bmp;
            //逐點製作圖檔
            int xx;
            int yy;

            int ww = pictureBox1.Width;
            int hh = pictureBox1.Height;

            bmp = new Bitmap(ww, hh);


            Point[] pts_r = new Point[rgbinfos.Count * 3];
            Point[] pts_g = new Point[rgbinfos.Count * 3];
            Point[] pts_b = new Point[rgbinfos.Count * 3];


            for (int i = 0; i < (rgbinfos.Count * 3); i++)
            {
                pts_r[i].X = i;
                pts_r[i].Y = 255 - rgbinfos[i / 3].r;
                pts_g[i].X = i;
                pts_g[i].Y = 255 - rgbinfos[i / 3].g;
                pts_b[i].X = i;
                pts_b[i].Y = 255 - rgbinfos[i / 3].b;
            }



            richTextBox1.Text += "rgbinfos.Count = " + rgbinfos.Count.ToString() + "\n";
            richTextBox1.Text += "size of pts_r = " + pts_r.Length.ToString() + "\n";

            /*
            for (int i = 0; i < (rgbinfos.Count * 3); i++)
            {
                richTextBox1.Text += pts_r[i].X.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < (rgbinfos.Count * 3); i++)
            {
                richTextBox1.Text += pts_r[i].X.ToString() + " ";
            }
            richTextBox1.Text += "\n";
            */

            //g.DrawCurve(greenPen, curvePoints); //畫曲線
            Graphics g;
            g = Graphics.FromImage(bmp);
            g.DrawCurve(new Pen(Color.Red, 3), pts_r);
            g.DrawCurve(new Pen(Color.Green, 3), pts_g);
            g.DrawCurve(new Pen(Color.Blue, 3), pts_b);



            pictureBox1.Image = bmp;




        }


    }
}
