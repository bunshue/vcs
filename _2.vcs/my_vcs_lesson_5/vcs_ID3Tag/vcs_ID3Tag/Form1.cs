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
            public byte Zero;//保留位，一個位元組, byte 125, 零位元組
            public byte Track;//保留位，一個位元組, byte 126, 曲目
            public byte Genre;//保留位，一個位元組, byte 127, 藝術類型
        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 16) == 15)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
        private byte[] getLast128(string filename)
        {
            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(-128, SeekOrigin.End);
            const int seekPos = 128;
            int rl = 0;
            byte[] Info = new byte[seekPos];
            rl = stream.Read(Info, 0, seekPos);
            fs.Close();
            stream.Close();

            if (cb_raw_data.Checked == true)
            {
                richTextBox1.Text += "印出此檔案之末128拜資料\n";
                print_data(Info);
            }

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
            for (i = currentIndex; i < currentIndex + 27; i++)
            {
                bytComment[j] = Info[i];
                position++;
                j++;
            }
            currentIndex = position;
            mp3Info.Comment = this.byteToString(bytComment);
            //以下獲取保留位（陣列125-127）
            mp3Info.Zero = Info[++position];
            mp3Info.Track = Info[++position];
            mp3Info.Genre = Info[++position];
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
                foreach (var filename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "檔名:\t" + filename + "\n";
                    get_ID3Tag(filename, encoding);
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
            richTextBox1.Text += "Zero : " + mp3_information.Zero.ToString() + "\n";
            richTextBox1.Text += "Track : " + mp3_information.Track.ToString() + "\n";
            richTextBox1.Text += "Genre : " + mp3_information.Genre.ToString() + "\n";
            richTextBox1.Text += "\n";

            textBox1.Text = mp3_information.identify;
            textBox2.Text = mp3_information.Title;
            textBox3.Text = mp3_information.Artist;
            textBox4.Text = mp3_information.Album;
            textBox5.Text = mp3_information.Year;
            textBox6.Text = mp3_information.Comment;
            textBox7.Text = mp3_information.Track.ToString();
            textBox8.Text = mp3_information.Genre.ToString();

            print_genre(mp3_information.Genre);
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
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
            textBox5.Clear();
            textBox6.Clear();
            textBox7.Clear();
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

        void print_genre(byte genre)
        {

            string[,] genre_data = new string[,] {
            { "0", "Blues", "藍調"},
            { "1", "Classic Rock", "古典搖滾樂"},
            { "2", "Country", "鄉村音樂"},
            { "3", "Dance", "舞曲"},
            { "4", "Disco", "迪斯科"},
            { "5", "Funk", "放克"},
            { "6", "Grunge", "油漬搖滾"},
            { "7", "Hip-Hop", "嘻哈"},
            { "8", "Jazz", "爵士樂"},
            { "9", "Metal", "重金屬音樂"},
            { "10", "New Age", "新世紀音樂"},
            { "11", "Oldies", "Oldies"},
            { "12", "Other", "Other"},
            { "13", "Pop", "流行 (音樂類型)"},
            { "14", "R&B", "節奏布魯斯"},
            { "15", "Rap", "饒舌"},
            { "16", "Reggae", "雷鬼音樂"},
            { "17", "Rock", "搖滾樂"},
            { "18", "Techno", "鐵克諾音樂"},
            { "19", "Industrial", "Industrial"},
            { "20", "Alternative", "另類搖滾"},
            { "21", "Ska", "斯卡曲風"},
            { "22", "Death Metal", "死亡金屬音樂"},
            { "23", "Pranks", "Pranks"},
            { "24", "Soundtrack", "原聲音樂"},
            { "25", "Euro-Techno", "Euro-Techno"},
            { "26", "Ambient", "氛圍音樂"},
            { "27", "Trip-Hop", "神遊舞曲"},
            { "28", "Vocal", "聲樂"},
            { "29", "Jazz+Funk", "爵士樂+放克"},
            { "30", "Fusion", "融合爵士樂"},
            { "31", "Trance", "出神音樂"},
            { "32", "Classical", "古典音樂"},
            { "33", "Instrumental", "器樂"},
            { "34", "Acid", "Acid"},
            { "35", "House", "浩室音樂"},
            { "36", "Game", "Game"},
            { "37", "Sound Clip", "音效及聲音片段"},
            { "38", "Gospel", "福音音樂"},
            { "39", "Noise", "噪音音樂"},
            { "40", "AlternRock", "AlternRock"},
            { "41", "Bass", "電貝斯"},
            { "42", "Soul", "靈魂樂"},
            { "43", "Punk", "龐克文化"},
            { "44", "Space", "Space"},
            { "45", "Meditative", "冥想音樂"},
            { "46", "Instrumental Pop", "Instrumental Pop"},
            { "47", "Instrumental Rock", "Instrumental Rock"},
            { "48", "Ethnic", "Ethnic"},
            { "49", "Gothic", "Gothic"},
            { "50", "Darkwave", "Darkwave"},
            { "51", "Techno-Industrial", "Techno-Industrial"},
            { "52", "Electronic", "電子音樂"},
            { "53", "Pop-Folk", "Pop-Folk"},
            { "54", "Eurodance", "歐陸舞曲"},
            { "55", "Dream", "Dream"},
            { "56", "Southern Rock", "Southern Rock"},
            { "57", "Comedy", "喜劇"},
            { "58", "Cult", "Cult"},
            { "59", "Gangsta", "Gangsta"},
            { "60", "Top 40", "Top 40"},
            { "61", "Christian Rap", "Christian Rap"},
            { "62", "Pop/Funk", "流行 (音樂類型)/放克"},
            { "63", "Jungle", "早期叢林舞曲"},
            { "64", "Native American", "Native American"},
            { "65", "Cabaret", "卡巴萊"},
            { "66", "New Wave", "新浪潮"},
            { "67", "Psychadelic", "Psychadelic"},
            { "68", "Rave", "銳舞"},
            { "69", "Showtunes", "Showtunes"},
            { "70", "Trailer", "Trailer"},
            { "71", "Lo-Fi", "Lo-Fi"},
            { "72", "Tribal", "Tribal"},
            { "73", "Acid Punk", "Acid Punk"},
            { "74", "Acid Jazz", "酸爵士"},
            { "75", "Polka", "波爾卡"},
            { "76", "Retro", "Retro"},
            { "77", "Musical", "Musical"},
            { "78", "Rock & Roll", "搖滾"},
            { "79", "Hard Rock", "硬式搖滾"},
            { "80", "Folk", "民俗音樂"},
            { "81", "Folk-Rock", "民謠搖滾"},
            { "82", "National Folk", "National Folk"},
            { "83", "Swing", "Swing"},
            { "84", "Fast Fusion", "Fast Fusion"},
            { "85", "Bebob", "咆勃爵士樂"},
            { "86", "Latin", "拉丁舞"},
            { "87", "Revival", "Revival"},
            { "88", "Celtic", "凱爾特音樂"},
            { "89", "Bluegrass", "藍草音樂"},
            { "90", "Avantgarde", "前衛"},
            { "91", "Gothic Rock", "哥德搖滾"},
            { "92", "Progressive Rock", "前衛搖滾"},
            { "93", "Psychedelic Rock", "迷幻搖滾"},
            { "94", "Symphonic Rock", "前衛搖滾"},
            { "95", "Slow Rock", "Slow Rock"},
            { "96", "Big Band", "大樂團"},
            { "97", "Chorus", "副歌"},
            { "98", "Easy Listening", "Easy Listening"},
            { "99", "Acoustic", "原音樂"},
            { "100", "Humour", "幽默"},
            { "101", "Speech", "語音"},
            { "102", "Chanson", "香頌"},
            { "103", "Opera", "歌劇"},
            { "104", "Chamber Music", "室內樂"},
            { "105", "Sonata", "奏鳴曲"},
            { "106", "Symphony", "交響曲"},
            { "107", "Booty Bass", "Booty Bass"},
            { "108", "Primus", "諷刺"},
            { "109", "Porn Groove", "Porn Groove"},
            { "110", "Satire", "Satire"},
            { "111", "Slow Jam", "Slow Jam"},
            { "112", "Club", "電子舞曲"},
            { "113", "Tango", "探戈"},
            { "114", "Samba", "桑巴"},
            { "115", "Folklore", "民俗學"},
            { "116", "Ballad", "謠曲"},
            { "117", "Power Ballad", "Power Ballad"},
            { "118", "Rhythmic Soul", "Rhythmic Soul"},
            { "119", "Freestyle", "Freestyle"},
            { "120", "Duet", "Duet"},
            { "121", "Punk Rock", "朋克搖滾"},
            { "122", "Drum Solo", "Drum Solo"},
            { "123", "A capella", "無伴奏合唱"},
            { "124", "Euro-House", "浩室音樂"},
            { "125", "Dance Hall", "Dance Hall"},
            };

            if (genre <= 125)
            {
                textBox8.Text = genre.ToString() + "  " + genre_data[genre, 1] + "  " + genre_data[genre, 2];
            }
            else
            {
                textBox8.Text = genre.ToString() + "  無資料";
            }
        }
    }
}
