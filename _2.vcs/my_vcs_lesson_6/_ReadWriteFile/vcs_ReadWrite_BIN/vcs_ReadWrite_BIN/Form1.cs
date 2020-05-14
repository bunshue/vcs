using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

namespace vcs_ReadWrite_BIN
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\bin_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bin";
            richTextBox1.Text += "寫入檔案\n";

            byte[] data = new byte[256];

            //設定資料內容
            for (int i = 0; i < data.Length; i++)
            {
                data[i] = (byte)i;
                /*
                if ((i % 2) == 0)
                {
                    data[i] = 0xA1;
                }
                else
                    data[i] = 0x42;
                */
            }

            //打印資料
            print_data(data, data.Length);

            /*
            //打印資料, 另法
            string data_result = string.Empty;
            foreach (byte b in data)
            {
                data_result += b.ToString("X2");
            }
            richTextBox1.Text += data_result;
            */

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename1 = Application.StartupPath + "\\BGR5706.bin";
            string filename2 = Application.StartupPath + "\\bin_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //讀取資料
            byte[] dataa = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + dataa.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */
            int i;
            for (i = 0; i < 1000; i++)
            {
                richTextBox1.Text += dataa[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 4) == 3)
                {
                    richTextBox1.Text += "  ";
                }

            }

            /*
            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
            }
            */
            //修改資料

            //int ww = 2048*4/16;
            //int hh = 640*500/2048/4*16/2;

            int ww = 640;
            //int hh = 640 * 500 / 2048 / 4 * 16 / 2; //312.5
            int hh = 480;

           
            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;
            richTextBox1.Text += "ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            for (i = 0; i < ww * hh; i++)
            {
                //data[54 + i * 4 + 0] = 0xCC;
                //data[54 + i * 4 + 1] = 0xBB;
                //data[54 + i * 4 + 2] = 0xAA;
                //data[54 + i * 4 + 3] = 0xFF;

                data[54 + i * 4 + 0] = dataa[i * 4 + 0];
                data[54 + i * 4 + 1] = dataa[i * 4 + 1];
                data[54 + i * 4 + 2] = dataa[i * 4 + 2];
                data[54 + i * 4 + 3] = dataa[i * 4 + 3];
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "寫成檔案" + filename + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename1 = Application.StartupPath + "\\bgr.bin";
            string filename2 = Application.StartupPath + "\\bin_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //讀取資料
            byte[] dataa = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + dataa.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */
            int i;
            for (i = 0; i < 500; i++)
            {
                richTextBox1.Text += dataa[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 4) == 3)
                {
                    richTextBox1.Text += "  ";
                }

            }
            richTextBox1.Text += "\n";

            /*
            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
            }
            */
            //修改資料

            //int ww = 2048*4/16;
            //int hh = 640*500/2048/4*16/2;

            int ww = 2048 * 4 / 16;
            int hh = 640 * 500 / 2048 / 4 * 16 / 2;

            int size = ww * hh * 4 + 0x36;
            int h_res = 0x0EC4;
            int v_res = 0x0EC4;
            richTextBox1.Text += "ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";

            byte[] data = new byte[size];

            for (i = 0; i < size; i++)
            {
                data[i] = 0;
            }
            data[0] = (byte)'B';
            data[1] = (byte)'M';
            data[2] = (byte)(size % 256);
            data[3] = (byte)((size / 256) % 256);
            data[4] = (byte)((size / 256 / 256) % 256);
            data[5] = (byte)((size / 256 / 256) % 256);
            data[10] = 0x36;
            data[14] = 0x28;

            data[18] = (byte)(ww % 256);
            data[19] = (byte)((ww / 256) % 256);
            data[20] = (byte)((ww / 256 / 256) % 256);
            data[21] = (byte)((ww / 256 / 256) % 256);

            data[22] = (byte)(hh % 256);
            data[23] = (byte)((hh / 256) % 256);
            data[24] = (byte)((hh / 256 / 256) % 256);
            data[25] = (byte)((hh / 256 / 256) % 256);

            data[26] = 0x01;
            data[28] = 0x20;

            data[38] = (byte)(h_res % 256);
            data[39] = (byte)((h_res / 256) % 256);
            data[40] = (byte)((h_res / 256 / 256) % 256);
            data[41] = (byte)((h_res / 256 / 256) % 256);

            data[42] = (byte)(v_res % 256);
            data[43] = (byte)((v_res / 256) % 256);
            data[44] = (byte)((v_res / 256 / 256) % 256);
            data[45] = (byte)((v_res / 256 / 256) % 256);

            int Y;
            int U;
            int V;
            int R;
            int G;
            int B;

            for (i = 0; i < ww * hh; i++)
            {
                //data[54 + i * 4 + 0] = 0xCC;
                //data[54 + i * 4 + 1] = 0xBB;
                //data[54 + i * 4 + 2] = 0xAA;
                //data[54 + i * 4 + 3] = 0xFF;

                Y = dataa[i * 4 + 0];
                V = dataa[i * 4 + 1];
                U = dataa[i * 4 + 2];

                R = (int)((double)Y + 1.4075 * ((double)V - 128));
                G = (int)((double)Y - 0.3455 * ((double)U - 128) - (0.7169 * ((double)V - 128)));
                B = (int)((double)Y + 1.7790 * ((double)U - 128));
                if (R > 255)
                    R = 255;
                else if (R < 0)
                    R = 0;
                if (G > 255)
                    G = 255;
                else if (G < 0)
                    G = 0;
                if (B > 255)
                    B = 255;
                else if (B < 0)
                    B = 0;

                data[54 + i * 4 + 0] = (byte)B;
                data[54 + i * 4 + 1] = (byte)G;
                data[54 + i * 4 + 2] = (byte)R;
                data[54 + i * 4 + 3] = dataa[i * 4 + 3];
                if (i < 100)
                {
                    richTextBox1.Text += "Y = 0x" + Y.ToString("X2") + " U = 0x" + U.ToString("X2") + " V = 0x" + V.ToString("X2") + "  ";
                    richTextBox1.Text += "R = 0x" + R.ToString("X2") + "=" + R.ToString() + " R = 0x" + G.ToString("X2") + "=" + G.ToString() + " B = 0x" + B.ToString("X2") + "=" + B.ToString() + "\n";
                }
            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */
            for (i = 0; i < 500; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 4) == 3)
                {
                    richTextBox1.Text += "  ";
                }

            }
            richTextBox1.Text += "\n";

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "寫成檔案" + filename + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename1 = "C:\\______test_files\\__RW\\_txt\\poetry.txt";
            string filename2 = Application.StartupPath + "\\hex_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            //讀取資料
            byte[] dataa = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + dataa.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            FileStream fs = new FileStream(filename2, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));   //指名編碼格式

            int i;
            for (i = 0; i < dataa.Length; i++)
            {
                sw.Write(dataa[i].ToString("X2"));
                //richTextBox1.Text += dataa[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    //richTextBox1.Text += "\n";
                    sw.Write('\n');
                }
                else
                {
                    sw.Write(' ');
                }
            }
            sw.Close();
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename2 + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename1 = "C:\\______test_files\\__RW\\_txt\\poetry.txt";
            string filename2 = Application.StartupPath + "\\hex_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            //讀取資料
            byte[] dataa = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + dataa.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            FileStream fs = new FileStream(filename2, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));   //指名編碼格式

            int max = 0;
            int min = 255;
            int i;
            //for (i = 0; i < dataa.Length; i++)
            for (i = 0; i < 100; i++)
            {
                sw.Write(dataa[i].ToString("X2"));
                richTextBox1.Text += dataa[i].ToString("X2");
                if ((i % 32) == 31)
                {
                    richTextBox1.Text += "\n";
                    sw.Write('\n');
                }
                else
                {
                    richTextBox1.Text += " ";
                    sw.Write(' ');
                }
            }

            for (i = 0; i < dataa.Length; i++)
            {
                if ((i % 2) == 0)
                {
                    if (dataa[i] > max)
                        max = dataa[i];
                    if (dataa[i] < min)
                        min = dataa[i];
                }
            }
            richTextBox1.Text += "max = " + max.ToString("X2") + "\n";
            richTextBox1.Text += "min = " + min.ToString("X2") + "\n";

            sw.Close();
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename2 + "\n";
        }

        string filename = "C:\\______test_files\\__RW\\_bin\\sample.bin";

        void print_data(byte[] data, int len)
        {
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //讀取資料
            byte[] data = File.ReadAllBytes(filename);
            int len = data.Length;
            richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";

            //打印資料
            print_data(data, len);

            /*
            //打印資料, 另法
            string data_read_result = string.Empty;
            foreach (byte b in data)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            richTextBox1.Text += "\n";
            */
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //隨機binary讀取
            FileStream fs = File.Open(filename, FileMode.OpenOrCreate, FileAccess.ReadWrite);
            BinaryReader br = new BinaryReader(fs);
            int len = (int)fs.Length;
            richTextBox1.Text += "讀取檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";

            len = 7;
            byte[] data = new byte[7];

            int i;
            for (i = 0; i < 8; i++)
            {
                //讀取位元陣列
                fs.Seek(32 * i, SeekOrigin.Begin);  //從Begin開始 32 *i 拜
                data = br.ReadBytes(len);           //用ReadBytes從目前位置開始讀len拜
                print_data(data, len);
            }

            //釋放資源
            br.Close();
            fs.Close();

            richTextBox1.Text += "讀一個mp3檔的末128拜\n";
            string filename2 = "C:\\______test_files\\aaaa.mp3";
            //隨機binary讀取
            fs = File.Open(filename2, FileMode.OpenOrCreate, FileAccess.ReadWrite);
            br = new BinaryReader(fs);
            len = (int)fs.Length;
            richTextBox1.Text += "讀取檔案 : " + filename2 + "\n";
            richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";
            richTextBox1.Text += "讀末128拜\n";

            len = 128;
            byte[] data2 = new byte[len];
            fs.Seek(-len, SeekOrigin.End);  //從最後開始往回算 128 拜

            //讀取位元陣列
            data = br.ReadBytes(len);       //用ReadBytes從目前位置開始讀len拜
            print_data(data, len);

            //釋放資源
            br.Close();
            fs.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //循序binary讀取
            FileStream fs = File.Open(filename, FileMode.OpenOrCreate, FileAccess.ReadWrite);
            BinaryReader br = new BinaryReader(fs);
            int len = System.Convert.ToInt16(fs.Length);
            richTextBox1.Text += "讀取檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";

            richTextBox1.Text += "讀前面1/3\n";
            len /= 3;

            //讀取位元陣列
            byte[] data = br.ReadBytes(len);    //用ReadBytes讀取檔案的前幾拜(循序)

            //釋放資源
            br.Close();
            fs.Close();

            print_data(data, len);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}
