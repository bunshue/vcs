using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Stream reader = File.Open(openFileDialog1.FileName, FileMode.Open, FileAccess.Read);
                Encoding encoder = null;
                byte[] header = new byte[4];
                // 讀取前四個Byte
                reader.Read(header, 0, 4);
                if (header[0] == 0xFF && header[1] == 0xFE)
                {
                    richTextBox1.Text += "get UniCode File\n";
                    // UniCode File
                    reader.Position = 2;
                    encoder = Encoding.Unicode;
                }
                else if (header[0] == 0xEF && header[1] == 0xBB && header[2] == 0xBF)
                {
                    richTextBox1.Text += "get UTF-8 File\n";
                    // UTF-8 File
                    reader.Position = 3;
                    encoder = Encoding.UTF8;
                }
                else
                {
                    richTextBox1.Text += "get Default Encoding File\n";
                    // Default Encoding File
                    reader.Position = 0;
                    encoder = Encoding.Default;
                }
                byte[] buffer = new byte[32];
                int source = reader.Read(buffer, 0, 32);
                richTextBox1.Text += "source = " + source.ToString() + "\n";
                string sSource = string.Empty;
                int i;

                if (source > 0)
                {
                    if (encoder != Encoding.Default)
                    {
                        sSource += encoder.GetString(buffer, 0, source);
                        //reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "\ntry default\n";
                        encoder = Encoding.Default;
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry big5\n";
                        encoder = Encoding.GetEncoding("big5");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry gb2312\n";
                        encoder = Encoding.GetEncoding("gb2312");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry shift_JIS\n";
                        encoder = Encoding.GetEncoding("shift_jis");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";



                    }
                }
                reader.Close();

                //richTextBox1.Text += "文件內容: " + sSource + "\n";


            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

            richTextBox1.Text += "\n文字編碼都是Unicode編碼\n";


        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            var badstringFromDatabase = "ƒ`ƒƒƒlƒ‹ƒp[ƒgƒi[‚Ì‘I‘ð";
            var hopefullyRecovered = Encoding.GetEncoding(1252).GetBytes(badstringFromDatabase);
            var oughtToBeJapanese = Encoding.GetEncoding("shift_jis").GetString(hopefullyRecovered);
            richTextBox1.Text += "result : " + oughtToBeJapanese + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string tt = "唐王";
            int i;
            richTextBox1.Text += "len = " + tt.Length.ToString() + "\n";
            for (i = 0; i < tt.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + tt[i] + "\tvalue\t" + ((int)tt[i]).ToString("X4") + "\n";


            }
            richTextBox1.Text += "\n文字編碼都是Unicode編碼\n";
        }
    }
}
