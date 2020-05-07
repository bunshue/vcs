using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileStream, path

namespace vcs_ID3Tag
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string encoding = "big5";

        public struct Mp3Info
        {
            public string identify;//TAG，三個位元組
            public string Title;//歌曲名,30個位元組
            public string Artist;//歌手名,30個位元組
            public string Album;//所屬唱片,30個位元組
            public string Year;//年,4個字元
            public string Comment;//注釋,28個位元組
            public char reserved1;//保留位，一個位元組
            public char reserved2;//保留位，一個位元組
            public char reserved3;//保留位，一個位元組
        }

        //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
        private byte[] getLast128(string FileName)
        {
            FileStream fs = new FileStream(FileName, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(-128, SeekOrigin.End);
            const int seekPos = 128;
            int rl = 0;
            byte[] Info = new byte[seekPos];
            rl = stream.Read(Info, 0, seekPos);
            fs.Close();
            stream.Close();
            /*
            richTextBox1.Text += "印出此檔案之末128拜資料\n";
            int i;
            for (i = 0; i < 128; i++)
            {
                richTextBox1.Text += Info[i].ToString("X2");
                if ((i % 16) == 15)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
            */
            return Info;
        }
        //再對上面返回的位元組陣列分段取出，並保存到Mp3Info結構中返回:
        private Mp3Info getMp3Info(byte[] Info)
        {
            Mp3Info mp3Info = new Mp3Info();
            string str = null;
            int i;
            int position = 0;//迴圈的起始值
            int currentIndex = 0;//Info的當前索引值
            //獲取TAG標識(陣列前3個)
            for (i = currentIndex; i < currentIndex + 3; i++)
            {
                str = str + (char)Info[i];
                position++;
            }
            currentIndex = position;
            mp3Info.identify = str;
            //獲取歌名（陣列3-32）
            str = null;
            byte[] bytTitle = new byte[30];//將歌名部分讀到一個單獨的陣列中
            int j = 0;
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytTitle[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Title = this.byteToString(bytTitle);
            //獲取歌手名（陣列33-62）
            str = null;
            j = 0;
            byte[] bytArtist = new byte[30];//將歌手名部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytArtist[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Artist = this.byteToString(bytArtist);
            //獲取唱片名（陣列63-92）
            str = null;
            j = 0;
            byte[] bytAlbum = new byte[30];//將唱片名部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 30; i++)
            {
                bytAlbum[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Album = this.byteToString(bytAlbum);
            //獲取年 （陣列93-96）
            str = null;
            j = 0;
            byte[] bytYear = new byte[4];//將年部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 4; i++)
            {
                bytYear[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Year = this.byteToString(bytYear);
            //獲取注釋（陣列97-124）
            str = null;
            j = 0;
            byte[] bytComment = new byte[28];//將注釋部分讀到一個單獨的陣列中
            for (i = currentIndex; i < currentIndex + 25; i++)
            {
                bytComment[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Comment = this.byteToString(bytComment);
            //以下獲取保留位（陣列125-127）
            mp3Info.reserved1 = (char)Info[++position];
            mp3Info.reserved2 = (char)Info[++position];
            mp3Info.reserved3 = (char)Info[++position];
            return mp3Info;

        }

        //上面程式用到下面的方法：
        /// <summary>
        /// 將位元組陣列轉換成字串
        /// </summary>
        /// <param name = "b">位元組陣列</param>
        /// <returns>返回轉換後的字串</returns>
        private string byteToString(byte[] b)
        {
            //Encoding enc = Encoding.GetEncoding("GB2312");
            Encoding enc = Encoding.GetEncoding(encoding);
            string str = enc.GetString(b);
            str = str.Substring(0, str.IndexOf('\0') >= 0 ? str.IndexOf('\0') : str.Length);//去掉無用字元
            return str;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
                encoding = "big5";
            else if (radioButton2.Checked == true)
                encoding = "gb2312";
            else if (radioButton3.Checked == true)
                encoding = "shift_jis";
            else
                encoding = "unicode";

            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = "c:\\______test_files_mp3";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n\n";
                foreach (var strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "檔名:\t" + strFilename + "\n";
                    get_ID3Tag(strFilename, encoding);
                }
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void get_ID3Tag(string filename, string encoding)
        {
            Mp3Info mp3_information;
            byte[] Info = getLast128(filename);
            mp3_information = getMp3Info(Info);

            richTextBox1.Text += "identify : " + mp3_information.identify + "\n";
            richTextBox1.Text += "Title : " + mp3_information.Title + "\n";
            richTextBox1.Text += "Artist : " + mp3_information.Artist + "\n";
            richTextBox1.Text += "Album : " + mp3_information.Album + "\n";
            richTextBox1.Text += "Year : " + mp3_information.Year + "\n";
            richTextBox1.Text += "Comment : " + mp3_information.Comment + "\n";
            richTextBox1.Text += "reserved1 : " + mp3_information.reserved1 + "\n";
            richTextBox1.Text += "reserved2 : " + mp3_information.reserved2 + "\n";
            richTextBox1.Text += "reserved3 : " + mp3_information.reserved3 + "\n";
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\aaaa.mp3";       //一定要有@
            encoding = "big5";
            get_ID3Tag(filename, encoding);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\uramachi.mp3";       //一定要有@
            encoding = "gb2312";
            get_ID3Tag(filename, encoding);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\harumi.mp3";       //一定要有@
            encoding = "shift_jis";
            get_ID3Tag(filename, encoding);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
                encoding = "big5";
            else if (radioButton2.Checked == true)
                encoding = "gb2312";
            else if (radioButton3.Checked == true)
                encoding = "shift_jis";
            else
                encoding = "unicode";

            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = "c:\\______test_files_mp3";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n\n";
                foreach (var strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "檔名:\t" + strFilename + "\n";
                    richTextBox1.Text += "正中編碼\n";
                    encoding = "big5";
                    get_ID3Tag(strFilename, encoding);
                    richTextBox1.Text += "\n簡中編碼\n";
                    encoding = "gb2312";
                    get_ID3Tag(strFilename, encoding);
                    richTextBox1.Text += "\n日文編碼\n";
                    encoding = "shift_jis";
                    get_ID3Tag(strFilename, encoding);
                    richTextBox1.Text += "\n";
                }
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

    }
}
