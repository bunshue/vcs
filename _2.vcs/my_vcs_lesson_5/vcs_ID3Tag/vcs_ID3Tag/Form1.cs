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

        string[,] frame_data = new string[,] { 
        { "TSIZ", "大小", "Size"},
        { "AENC", "音訊加密", "Audio encryption"},
        { "APIC", "附圖", "Attached picture"},
        { "ASPI", "音訊搜尋點索引", "Audio seek point index"},
        { "COMM", "評論", "Comments"},
        { "COMR", "商業用資料框架", "Commercial frame"},
        { "ENCR", "加密方式註冊", "Encryption method registration"},
        { "EQUA", "等化", "Equalization"},
        { "EQU2", "等化", "Equalization"},
        { "ETCO", "事件時間代碼", "Event timing codes"},
        { "GEOB", "一般封裝物件", "General encapsulated object"},
        { "GRID", "組織識別註冊", "Group identification registration"},
        { "LINK", "連結資訊", "Linked information"},
        { "MCDI", "音樂光碟識別碼", "Music CD identifier"},
        { "MLLT", "MPEG位置查詢表", "MPEG location lookup table"},
        { "OWNE", "所有權", "Ownership frame"},
        { "PCNT", "播放次數", "Play counter"},
        { "POPM", "評等", "Popularimeter"},
        { "POSS", "位置同步", "Position synchronisation frame"},
        { "PRIV", "隱私權", "Private frame"},
        { "RBUF", "推薦緩衝區大小", "Recommended buffer size"},
        { "RVAD", "相對音量調整", "Relative volume adjustment"},
        { "RVA2", "相對音量調整", "Relative volume adjustment"},
        { "RVRB", "混響", "Reverb"},
        { "SEEK", "搜尋用", "Seek frame"},
        { "SIGN", "簽名用", "Signature frame"},
        { "SYLT", "同步歌詞、文字", "Synchronized lyric/text"},
        { "SYTC", "同步節拍代碼", "Synchronized tempo codes"},
        { "TALB", "專輯/電影/節目標題", "Album/Movie/Show title"},
        { "TBPM", "量度音樂速度", "Beats per minute (BPM)"},
        { "TCOM", "作曲者", "Composer"},
        { "TCON", "內容類型", "Content type"},
        { "TCOP", "著作權資訊", "Copyright message"},
        { "TDEN", "編碼時間", "Encoding time"},
        { "TDLY", "播放清單中的間隔時間", "Playlist delay"},
        { "TORY", "年分", "Original release year"},
        { "TDOR", "年分", "Original release year"},
        { "TDAT", "日期", "Date"},
        { "TDRC", "日期", "Date"},
        { "TRDA", "建立日期", "Recording dates"},
        { "TDRC", "建立日期", "Recording dates"},
        { "TDRC", "音訊紀錄時間", "Recording time"},
        { "TIME", "包含記錄用的時間", "Time"},
        { "TDRC", "包含記錄用的時間", "Time"},
        { "TYER", "年分", "Year"},
        { "TDRC", "年分", "Year"},
        { "TDRL", "音訊發行時間", "Release time"},
        { "TDTG", "音訊被標記時間", "Tagging time"},
        { "TENC", "編碼者", "Encoded by"},
        { "TEXT", "作詞者", "Lyricist/Text writer"},
        { "TFLT", "檔案類型", "File type"},
        { "IPLS", "相關人員列表", "Involved people list"},
        { "TIPL", "相關人員列表", "Involved people list"},
        { "TIT1", "群組描述", "Content group description"},
        { "TIT2", "標題", "Title/songname/content description"},
        { "TIT3", "字幕", "Subtitle/Description refinement"},
        { "TKEY", "初始調", "Initial key"},
        { "TLAN", "語言", "Language(s)"},
        { "TLEN", "長度", "Length"},
        { "TMCL", "音樂家與樂器對照", "Musician credits list"},
        { "TMED", "屬性", "Media type"},
        { "TMOO", "情境", "Mood"},
        { "TOAL", "原始標題", "Original album/movie/show title"},
        { "TOFN", "原始檔案名稱", "Original filename"},
        { "TOLY", "原始作詞者", "Original lyricist(s)/text writer(s)"},
        { "TOPE", "原始演唱者", "Original artist(s)/performer(s)"},
        { "TOWN", "著作權", "File owner/licensee"},
        { "TPE1", "指揮", "Lead performer(s)/Soloist(s)"},
        { "TPE2", "樂團/樂隊/伴奏", "Band/orchestra/accompaniment"},
        { "TPE3", "詳細參與演出者", "Conductor/performer refinement"},
        { "TPE4", "後製", "Interpreted, remixed, or otherwise modified by"},
        { "TPOS", "Part of a set", "Part of a set"},
        { "TPRO", "Produced notice", "Produced notice"},
        { "TPUB", "發行者", "Publisher"},
        { "TRCK", "曲目", "Track number/Position in set"},
        { "TRSN", "Internet radio station name", "Internet radio station name"},
        { "TRSO", "Internet radio station owner", "Internet radio station owner"},
        { "TSOA", "依專輯排序", "Album sort order"},
        { "TSOP", "依演出者排序", "Performer sort order"},
        { "TSOT", "依標題排序", "Title sort order"},
        { "TSRC", "國際標準音像製品編碼", "International Standard Recording Code (ISRC)"},
        { "TSSE", "編碼環境設定", "Software/Hardware and settings used for encoding"},
        { "TSST", "設定字幕", "Set subtitle"},
        { "TXXX", "自訂文字", "User defined text information frame"},
        { "UFID", "檔案識別碼", "Unique file identifier"},
        { "USER", "使用條款", "Terms of use"},
        { "USLT", "非同步歌詞轉錄", "Unsynchronized lyric/text transcription"},
        { "WCOM", "商業資訊", "Commercial information"},
        { "WCOP", "著作權資訊", "Copyright/Legal information"},
        { "WOAF", "官方音訊檔案網站", "Official audio file webpage"},
        { "WOAR", "作者URL", "Official artist/performer webpage"},
        { "WOAS", "官方音源URL", "Official audio source webpage"},
        { "WORS", "Official internet radio station homepage", "Official internet radio station homepage"},
        { "WPAY", "付費URL", "Payment"},
        { "WPUB", "發行者官網", "Publishers official webpage"},
        { "WXXX", "自訂URL", "User defined URL link frame"},
        };

        public struct Mp3InfoV1
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

        public struct Mp3InfoV2
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
                else if (i != (len - 1))
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        void print_data(byte[] data, int start, int len)
        {
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[start + i].ToString("X2");
                if ((i % 16) == 15)
                    richTextBox1.Text += "\n";
                else if (i != (len - 1))
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        private byte[] getID3v2Header(string filename)
        {
            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(0, SeekOrigin.Begin);
            const int seekPos = 10;
            int rl = 0;
            byte[] Info = new byte[seekPos];
            rl = stream.Read(Info, 0, seekPos);
            fs.Close();
            stream.Close();

            if (cb_raw_data.Checked == true)
            {
                richTextBox1.Text += "印出此檔案之前10拜資料(ID3 header)\n";
                print_data(Info);
            }
            return Info;
        }

        private byte[] getID3v2Data(string filename, int len)
        {
            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(10, SeekOrigin.Begin);  //從offset=10開始, 讀len長度資料
            int seekPos = len;
            int rl = 0;
            byte[] Info = new byte[seekPos];
            rl = stream.Read(Info, 0, seekPos);
            fs.Close();
            stream.Close();

            if (cb_raw_data.Checked == true)
            {
                richTextBox1.Text += "印出此檔案之前 " + len.ToString() + " 拜資料\n";
                print_data(Info);
            }
            return Info;
        }

        //再對上面返回的位元組陣列分段取出，並保存到Mp3InfoV2結構中返回:
        void getMp3InfoV2(byte[] Info)
        {
            Mp3InfoV2 mp3InfoV2 = new Mp3InfoV2();
            string str = null;
            int i;
            int position = 0;//迴圈的起始值
            int currentIndex = 0;//Info的當前索引值
            //獲取Frame ID標識(陣列前4個)

            int k = 0;
            while(true)
            {
                k++;
                //richTextBox1.Text += "\n第 " + k.ToString() + " 筆資料\t";
                //print_data(Info, currentIndex, 10);

                if ((Info[currentIndex] == 0x00) && (Info[currentIndex + 1] == 0x00) && (Info[currentIndex + 2] == 0x00) && (Info[currentIndex + 3] == 0x00))
                {
                    //richTextBox1.Text += "資料已到盡頭\n";
                    break;
                }

                for (position = currentIndex; position < currentIndex + 4; position++)
                {
                    str = str + (char)Info[position];
                }
                currentIndex = position;
                mp3InfoV2.identify = str;

                int tag_size = (((Info[currentIndex++] & 0xff) << 24) + ((Info[currentIndex++] & 0xff) << 16) + ((Info[currentIndex++] & 0xff) << 8) + (Info[currentIndex++] & 0xff));
                //richTextBox1.Text += "tag_size = " + tag_size.ToString() + "\n";

                //richTextBox1.Text += mp3InfoV2.identify + "\t";
                currentIndex += 2;  //skip flags


                //richTextBox1.Text += "currentIndex = " + currentIndex.ToString() + "\n";
                //richTextBox1.Text += "position = " + position.ToString() + "\n";

                bool skip = false;

                if (mp3InfoV2.identify == "MCDI")
                {
                    skip = true;
                    //richTextBox1.Text += "\tskip\n";
                    str = null;
                }

                if (skip == false)
                {
                    //獲取字串資料
                    str = null;
                    byte[] data = new byte[tag_size];//將歌名部分讀到一個單獨的陣列中
                    int j = 0;
                    for (i = currentIndex; i < currentIndex + tag_size; i++)
                    {
                        if (Info[i] == 0x00)
                        {
                        }
                        else
                        {
                            data[j] = Info[i];
                            j++;
                        }
                    }

                    /* test
                    print_data(data);
                    string str2 = Encoding.GetEncoding("big5").GetString(data);
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "------" + str2 + "-----------";
                    richTextBox1.Text += "\n";
                    */

                    mp3InfoV2.Title = this.byteToString(data);
                    print_data_frame(mp3InfoV2.identify, mp3InfoV2.Title);

                    /*
                    richTextBox1.Text += "data : " + mp3InfoV2.Title + "\n";

                    richTextBox1.Text += "hex data : \n";
                    for (i = 0; i < tag_size; i++)
                    {
                        richTextBox1.Text += data[i].ToString("X2") + " ";
                    }
                    richTextBox1.Text += "\n";

                    richTextBox1.Text += "byteArray 資料\t";
                    for (i = 0; i < tag_size; i++)
                    {
                        //richTextBox7.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                        //richTextBox7.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                        richTextBox1.Text += data[i].ToString("X2") + " ";
                    }
                    richTextBox1.Text += "\n";
                    */
                    //string str2 = Encoding.GetEncoding("big5").GetString(data);
                    //richTextBox1.Text += str2;
                    //richTextBox1.Text += "\n";
                }
                currentIndex += tag_size;
                //richTextBox1.Text += "\ncurrentIndex = " + currentIndex.ToString() + "\n";
            }
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
        //再對上面返回的位元組陣列分段取出，並保存到Mp3InfoV1結構中返回:
        private Mp3InfoV1 getMp3InfoV1(byte[] Info)
        {
            Mp3InfoV1 mp3InfoV1 = new Mp3InfoV1();
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
            mp3InfoV1.identify = str;
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
            mp3InfoV1.Title = this.byteToString(bytTitle);
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
            mp3InfoV1.Artist = this.byteToString(bytArtist);
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
            mp3InfoV1.Album = this.byteToString(bytAlbum);
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
            mp3InfoV1.Year = this.byteToString(bytYear);
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
            mp3InfoV1.Comment = this.byteToString(bytComment);
            //以下獲取保留位（陣列125-127）
            mp3InfoV1.Zero = Info[++position];
            mp3InfoV1.Track = Info[++position];
            mp3InfoV1.Genre = Info[++position];
            return mp3InfoV1;
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
            clear_textbox_id3_data();
            textBox_filename.Text = filename;
            get_ID3v1Tag(filename, encoding);
            get_ID3v2Tag(filename, encoding);
        }

        void get_ID3v1Tag(string filename, string encoding)
        {
            Mp3InfoV1 mp3_information;
            byte[] Info = getLast128(filename);

            if ((Info[0] == 'T') && (Info[1] == 'A') && (Info[2] == 'G'))
            {
                mp3_information = getMp3InfoV1(Info);

                /*
                richTextBox1.Text += "有ID3 v1資料\n";
                richTextBox1.Text += "identify : " + mp3_information.identify + "\n";
                richTextBox1.Text += "Title : " + mp3_information.Title + "\n";
                richTextBox1.Text += "Artist : " + mp3_information.Artist + "\n";
                richTextBox1.Text += "Album : " + mp3_information.Album + "\n";
                richTextBox1.Text += "Year : " + mp3_information.Year + "\n";
                richTextBox1.Text += "Comment : " + mp3_information.Comment + "\n";
                richTextBox1.Text += "Zero : " + mp3_information.Zero.ToString() + "\n";
                if (mp3_information.Zero == 0)
                    richTextBox1.Text += "Track : " + mp3_information.Track.ToString() + "\n";
                else
                    richTextBox1.Text += "Track : 無資料\n";
                richTextBox1.Text += "Genre : " + mp3_information.Genre.ToString() + "\n";
                richTextBox1.Text += "\n";
                */

                textBox1.Text = mp3_information.identify;
                textBox2.Text = mp3_information.Title;
                textBox3.Text = mp3_information.Artist;
                textBox4.Text = mp3_information.Album;
                textBox5.Text = mp3_information.Year;
                textBox6.Text = mp3_information.Comment;
                if (mp3_information.Zero == 0)
                    textBox7.Text = mp3_information.Track.ToString();
                else
                    textBox7.Text = "無資料";
                textBox8.Text = mp3_information.Genre.ToString();

                print_genre(mp3_information.Genre);
            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\n";
            }
        }

        void get_ID3v2Tag(string filename, string encoding)
        {
            byte[] header = getID3v2Header(filename);
            if ((header[0] == 'I') && (header[1] == 'D') && (header[2] == '3'))
            {
                textBox1b.Text = "ID3";
                /*
                richTextBox1.Text += "印出此檔案之前10拜資料(ID3 header)\n";
                print_data(header);

                richTextBox1.Text += "有ID3 v2資料\n";
                richTextBox1.Text += "Major version : " + header[3].ToString() + "\n";
                richTextBox1.Text += "minor version : " + header[4].ToString() + "\n";
                richTextBox1.Text += "flags : " + header[5].ToString("X2") + "\n";
                */

                int tag_size = (((header[6] & 0x7f) << 21) + ((header[7] & 0x7f) << 14) + ((header[8] & 0x7f) << 7) + (header[9] & 0x7f));
                //richTextBox1.Text += "tag_size = " + tag_size.ToString() + "\n";

                byte[] Info = getID3v2Data(filename, tag_size);
                getMp3InfoV2(Info);
            }
            else
            {
                richTextBox1.Text += "無ID3 v2資料\n";
            }
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

        void clear_textbox_id3_data()
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
            textBox5.Clear();
            textBox6.Clear();
            textBox7.Clear();
            textBox8.Clear();
            textBox1b.Clear();
            textBox2b.Clear();
            textBox3b.Clear();
            textBox4b.Clear();
            textBox5b.Clear();
            textBox6b.Clear();
            textBox7b.Clear();
            textBox8b.Clear();
            textBox9b.Clear();
            textBox_filename.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            clear_textbox_id3_data();
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
                    //richTextBox1.Text += "檔名:\t" + strFilename + "\n";
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

        void print_data_frame(string id, string data)
        {
            int i;
            int total_frame_ids = frame_data.GetUpperBound(0) + 1;
            bool found_frame_id = false;
            for (i = 0; i < total_frame_ids; i++)
            {
                if (id == "TIT2")
                {
                    textBox2b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TPE1")
                {
                    textBox3b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TALB")
                {
                    textBox4b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TYER")
                {
                    textBox5b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "COMM")
                {
                    textBox6b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TRCK")
                {
                    textBox7b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TCON")
                {
                    textBox8b.Text = data;
                    found_frame_id = true;
                }
                else if (id == "TLEN")
                {
                    textBox9b.Text = data;
                    found_frame_id = true;
                }
                else if (id == frame_data[i, 0])
                {
                    richTextBox1.Text += frame_data[i, 0] + "\t" + frame_data[i, 1] + "\t" + data + "\n";
                    found_frame_id = true;
                    break;
                }
            }
            if (found_frame_id == false)
            {
                richTextBox1.Text += "\n\nXXXXXXXXXXXX 找不到 id = " + id + "\n";
                richTextBox1.Text += "XXXXXXXXXXXX 找不到 id = " + id + "\n";
                richTextBox1.Text += "XXXXXXXXXXXX 找不到 id = " + id + "\n\n\n";
            }
        }
    }
}
