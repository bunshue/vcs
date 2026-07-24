using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode //提供畫高級二維，矢量圖形功能
using System.Drawing.Imaging;   //for ImageFormat   //提供畫GDI+圖形的高級功能

using System.Runtime.InteropServices;   //for Marshal

using System.Drawing.Text;      //for TextRenderingHint //提供畫GDI+圖形的高級功能

using System.Diagnostics;       //for Debug
using System.Reflection;    //PropertyInfo
using System.Threading;

using System.IO;

namespace vcs_Draw_Example2
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

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);     // 設定畫筆為紅色、粗細為 2 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(1024, 400);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            bt_save.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_save.Size.Width * 2, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_save.Size.Height);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_reset.Size.Height);

            ucOscilloscope1.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            ucOscilloscope1.Size = new Size(1024, 200);
            ucOscilloscope1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(1024, 200);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 900);
            this.Text = "vcs_Draw_Example2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(900, 400);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        //沒用到????
        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

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

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        //實現wav波形圖 ST
        const int byteSample = 2;
        const int dataPosition = 40;
        //0x16 2byte 0002  雙聲道
        //0x22 2byte 0010  16位
        //0x18 4byte 0000AC44   44100采樣率

        const bool leftStatus = false;

        private void button2_Click(object sender, EventArgs e)
        {
            //wave轉txt
            richTextBox1.Text += "wave轉txt ST\n";
            Application.DoEvents();

            //讀取wav，保存音頻數據到txt
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\_wav\start.wav";
            string filename2 = @"start.txt";

            byte[] length = new byte[4];
            FileStream fs = new FileStream(filename1, FileMode.Open, FileAccess.Read);
            fs.Position = dataPosition;
            fs.Read(length, 0, 4);
            byte[] content = new byte[getHexToInt(length)];
            string[] sample = new string[content.Length / byteSample];
            fs.Read(content, 0, content.Length);
            getHex(content);
            sample = getSample(content);
            StreamWriter sw = new StreamWriter(filename2, true, Encoding.Default);
            foreach (string i in sample)
            {
                sw.Flush();
                sw.WriteLine(i);
            }
            sw.Close();
            richTextBox1.Text += "wave轉txt SP\n";
        }

        static int getHexToInt(byte[] x)
        {
            string retValue = "";
            for (int i = x.Length - 1; i >= 0; i--)
            {
                retValue += x[i].ToString("X");
            }
            return Convert.ToInt32(retValue, 16);
        }

        static void getHex(byte[] x)
        {
            byte tmp;
            for (int i = 0; i < x.Length; i++)
            {
                tmp = Convert.ToByte(x[i].ToString("X"), 16);
                x[i] = tmp;
            }
        }

        static string[] getSample(byte[] x)
        {
            string[] retValue = new string[x.Length / byteSample];

            for (int i = 0; i < retValue.Length; i++)
            {
                for (int j = (i + 1) * byteSample - 1; j >= i * byteSample; j--)
                {
                    retValue[i] += x[j].ToString("X");
                }
                retValue[i] = ((double)Convert.ToInt16(retValue[i], 16) / 32768).ToString("F4");
            }
            return retValue;
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //顯示wave 1
            string filename2 = @"start.txt";

            new Thread(new ThreadStart(() =>
            {
                this.Invoke(new MethodInvoker(() => { richTextBox1.Text += leftStatus ? "左聲道" : "右聲道"; }));
                List<double> list = new List<double>();
                StreamReader sr = new StreamReader(filename2, Encoding.Default);
                int m = 0;
                while (!sr.EndOfStream)
                {
                    if (leftStatus)
                    {
                        if (m % 2 == 0)
                        {
                            list.Add(double.Parse(sr.ReadLine()));
                        }
                    }
                    else
                    {
                        if (m % 2 != 0)
                        {
                            list.Add(double.Parse(sr.ReadLine()));
                        }
                    }
                    m++;
                }
                sr.Close();
                Bitmap bitmap = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                Graphics g = Graphics.FromImage(bitmap);
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 20), new Point(20, 540));
                g.DrawLine(new Pen(Color.Black, 5), new Point(20, 290), new Point(1600, 290));

                int k = list.Count / 1550;

                for (int i = 0; i < list.Count; i++)
                {
                    g.DrawLine(new Pen(Color.Green, 1), new Point(20 + i / k, 290), new Point(20 + i / k, 290 + (int)(list[i] * 250 * 2)));
                }
                this.pictureBox1.Image = bitmap;
            })).Start();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //顯示wave 2
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_wav\start.wav";

            WAVReader wr = new WAVReader();
            wr.ReadWAVFile(filename);
            int ww = pictureBox1.Width;
            int hh = pictureBox1.Height;
            Graphics g = pictureBox1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.DrawLine(new Pen(Color.DarkSeaGreen, 1), new Point(0, hh / 2), new Point(ww, hh / 2));
            int prex = 0, prey = 0; //上一個座標  
            int x = 0, y = 0;
            double k = hh / 2.0 / 32768.0;
            for (int i = 0; i < ww; i++)
            {
                x = i;
                y = hh - (int)(wr.wavdata[i * 3] * k + hh / 2);
                if (i != 0)
                {
                    g.DrawLine(new Pen(Color.Red, 1), x, y, prex, prey);
                }
                prex = x;
                prey = y;
            }
        }
        //實現wav波形圖 SP

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        void draw_Oscilloscope(string filename)
        {
            ucOscilloscope1.LineColor = Color.Red;

            string data;
            string[] splitData;
            using (TextReader reader = File.OpenText(filename))
            {
                data = reader.ReadToEnd();
                splitData = data.Split(new char[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }
            List<int> mapData = new List<int>();
            foreach (string info in splitData)
            {
                try
                {
                    int xxx = Convert.ToInt32(info);
                    if (xxx > 0)
                    {
                        mapData.Add(xxx);
                    }
                }
                catch (System.Exception ex)
                {
                }
            }
            ucOscilloscope1.MappingDatas = mapData;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //畫 Oscilloscope 1
            string filename = @"..\..\data\MappingData1.txt";
            draw_Oscilloscope(filename);
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //畫 Oscilloscope 2
            string filename = @"..\..\data\MappingData2.txt";
            draw_Oscilloscope(filename);
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
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
    }

    class WAVReader //wav 文件讀取類
    {
        private string Id; //文件標識
        private double Size;  //文件大小
        private string Type; //文件類型
        private string formatId;
        private double formatSize;      //數值爲16或18，18則最後又附加信息
        private int formatTag;
        private int num_Channels;       //聲道數目
        private int SamplesPerSec;      //採樣率
        private int AvgBytesPerSec;     //每秒所需字節數 
        private int BlockAlign;         //數據塊對齊單位(每個採樣需要的字節數) 
        private int BitsPerSample;      //每個採樣需要的bit數
        private string additionalInfo;  //附加信息
        private string dataId;
        private int dataSize;
        public List<double> wavdata = new List<double>();
        public void ReadWAVFile(string filename)  //讀取波形文件並顯示
        {
            if (filename == "")
            {
                return;
            }
            byte[] id = new byte[4];
            byte[] size = new byte[4];
            byte[] type = new byte[4];
            byte[] formatid = new byte[4];
            byte[] formatsize = new byte[4];
            byte[] formattag = new byte[2];
            byte[] numchannels = new byte[2];
            byte[] samplespersec = new byte[4];
            byte[] avgbytespersec = new byte[4];
            byte[] blockalign = new byte[2];
            byte[] bitspersample = new byte[2];
            byte[] additionalinfo = new byte[2];    //可選
            byte[] factid = new byte[4];
            byte[] factsize = new byte[4];
            byte[] factdata = new byte[4];
            byte[] dataid = new byte[4];
            byte[] datasize = new byte[4];
            using (FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read))
            {
                using (BinaryReader br = new BinaryReader(fs, Encoding.UTF8))
                {
                    //#region  RIFF WAVE Chunk
                    br.Read(id, 0, 4);
                    br.Read(size, 0, 4);
                    br.Read(type, 0, 4);
                    Id = getString(id, 4);
                    long longsize = bytArray2Int(size);//十六進制轉爲十進制
                    Size = longsize * 1.0;
                    Type = getString(type, 4);
                    //#endregion
                    //#region Format Chunk
                    br.Read(formatid, 0, 4);
                    br.Read(formatsize, 0, 4);
                    br.Read(formattag, 0, 2);
                    br.Read(numchannels, 0, 2);
                    br.Read(samplespersec, 0, 4);
                    br.Read(avgbytespersec, 0, 4);
                    br.Read(blockalign, 0, 2);
                    br.Read(bitspersample, 0, 2);
                    if (getString(formatsize, 2) == "18")
                    {
                        br.Read(additionalinfo, 0, 2);
                        additionalInfo = getString(additionalinfo, 2);  //附加信息
                    }
                    formatId = getString(formatid, 4);
                    formatSize = bytArray2Int(formatsize);
                    byte[] tmptag = composeByteArray(formattag);
                    formatTag = bytArray2Int(tmptag);
                    byte[] tmpchanels = composeByteArray(numchannels);
                    num_Channels = bytArray2Int(tmpchanels);                //聲道數目
                    SamplesPerSec = bytArray2Int(samplespersec);            //採樣率
                    AvgBytesPerSec = bytArray2Int(avgbytespersec);          //每秒所需字節數   
                    byte[] tmpblockalign = composeByteArray(blockalign);
                    BlockAlign = bytArray2Int(tmpblockalign);              //數據塊對齊單位(每個採樣需要的字節數)
                    byte[] tmpbitspersample = composeByteArray(bitspersample);
                    BitsPerSample = bytArray2Int(tmpbitspersample);        // 每個採樣需要的bit數     
                    //#endregion
                    //#region Data Chunk
                    byte[] d_flag = new byte[1];
                    while (true)
                    {
                        br.Read(d_flag, 0, 1);
                        if (getString(d_flag, 1) == "d")
                        {
                            break;
                        }
                    }
                    byte[] dt_id = new byte[4];
                    dt_id[0] = d_flag[0];
                    br.Read(dt_id, 1, 3);
                    dataId = getString(dt_id, 4);
                    br.Read(datasize, 0, 4);
                    dataSize = bytArray2Int(datasize);
                    List<string> testl = new List<string>();
                    if (BitsPerSample == 8)
                    {
                        for (int i = 0; i < dataSize; i++)
                        {
                            byte wavdt = br.ReadByte();  // 讀一拜
                            wavdata.Add(wavdt);
                        }
                    }
                    else if (BitsPerSample == 16)
                    {
                        for (int i = 0; i < dataSize / 2; i++)
                        {
                            short wavdt = br.ReadInt16();
                            wavdata.Add(wavdt);
                        }
                    }
                    //#endregion
                }
            } //wavdata
        }

        // 數字節數組轉換爲int
        private int bytArray2Int(byte[] bytArray)
        {
            return bytArray[0] | (bytArray[1] << 8) | (bytArray[2] << 16) | (bytArray[3] << 24);
        }

        // 將字節數組轉換爲字符串
        private string getString(byte[] bts, int len)
        {
            char[] tmp = new char[len];
            for (int i = 0; i < len; i++)
            {
                tmp[i] = (char)bts[i];
            }
            return new string(tmp);
        }

        // 組成4個元素的字節數組
        private byte[] composeByteArray(byte[] bt)
        {
            byte[] tmptag = new byte[4] { 0, 0, 0, 0 };
            tmptag[0] = bt[0];
            tmptag[1] = bt[1];
            return tmptag;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


