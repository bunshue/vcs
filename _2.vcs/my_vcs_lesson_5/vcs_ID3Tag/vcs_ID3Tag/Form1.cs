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
            public string identify;//ID3，三個位元組
            public string Title;//歌曲名,30個位元組
            public string Artist;//歌手名,30個位元組
            public string Album;//所屬唱片,30個位元組
            public string Year;//年,4個字元
            public string Comment;//注釋,28個位元組
            public string Track;//保留位，一個位元組, byte 126, 曲目
            public string Genre;//保留位，一個位元組, byte 127, 藝術類型
            public string Length;
        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            if (len > 50)
            {
                richTextBox1.Text += "print too long len = " + len.ToString() + "\n";
                len = 50;
            }
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
            if (len > 50)
            {
                richTextBox1.Text += "print too long len = " + len.ToString() + "\n";
                len = 50;
            }
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
        private Mp3InfoV2 getMp3InfoV2(byte[] Info)
        {
            Mp3InfoV2 mp3InfoV2 = new Mp3InfoV2();
            string frame_id = null;
            string frame_id_data = null;
            int i;
            int position = 0;//迴圈的起始值
            int currentIndex = 0;//Info的當前索引值

            int k = 0;
            while(true)
            {
                k++;
                if (cb_raw_data.Checked == true)
                {
                    richTextBox1.Text += "\n第 " + k.ToString() + " 筆資料\t";
                    //印出此frame id的檔頭(10拜)
                    print_data(Info, currentIndex, 10);
                }

                if ((Info[currentIndex] == 0x00) && (Info[currentIndex + 1] == 0x00) && (Info[currentIndex + 2] == 0x00) && (Info[currentIndex + 3] == 0x00))
                {
                    //richTextBox1.Text += "資料已到盡頭\n";
                    break;
                }

                for (position = currentIndex; position < currentIndex + 4; position++)
                {
                    frame_id += (char)Info[position];
                }

                if (cb_raw_data.Checked == true)
                {
                    richTextBox1.Text += "ID\t\tpos = 0x" + currentIndex.ToString("X2") + " = " + currentIndex.ToString() + "\t\t";
                    for (position = currentIndex; position < currentIndex + 4; position++)
                    {
                        richTextBox1.Text += Info[position].ToString("X2") + " ";
                    }
                    richTextBox1.Text += "\t\t";
                    for (position = currentIndex; position < currentIndex + 4; position++)
                    {
                        richTextBox1.Text += (char)Info[position];
                    }
                    richTextBox1.Text += "\t\t";
                }

                currentIndex = position;

                int tag_size = (((Info[currentIndex++] & 0xff) << 24) + ((Info[currentIndex++] & 0xff) << 16) + ((Info[currentIndex++] & 0xff) << 8) + (Info[currentIndex++] & 0xff));

                if (cb_raw_data.Checked == true)
                    richTextBox1.Text += "tag_size = 0x" + tag_size.ToString("X2") + " = " + tag_size.ToString() + "\n";

                currentIndex += 2;  //skip flags

                //richTextBox1.Text += "currentIndex = " + currentIndex.ToString() + "\n";
                //richTextBox1.Text += "position = " + position.ToString() + "\n";

                if (frame_id == "MCDI")
                {
                    richTextBox1.Text += frame_id + "\t\tlen = " + tag_size.ToString() + "\t\tskip\n";
                }
                else if (frame_id == "APIC")
                {
                    richTextBox1.Text += frame_id + "\t\tlen = " + tag_size.ToString() + "\t\tskip\n";
                }
                else if (frame_id == "GEOB")
                {
                    richTextBox1.Text += frame_id + "\t\tlen = " + tag_size.ToString() + "\t\tskip\n";
                }
                else
                {
                    //獲取字串資料
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

                    if (cb_raw_data.Checked == true)
                    {
                        richTextBox1.Text += frame_id + "\t\t";
                        int len = tag_size;
                        if (len > 100)
                            len = 100;
                        for (i = 0; i < len; i++)
                        {
                            richTextBox1.Text += data[i].ToString("X2");
                            if ((i % 32) == 31)
                                richTextBox1.Text += "\n";
                            else
                                richTextBox1.Text += " ";
                        }
                        richTextBox1.Text += "\n";
                    }

                    if (frame_id == "COMM")
                    {
                        frame_id_data = this.byteToString(data);
                    }
                    else
                    {
                        frame_id_data = check_frame_id_dataunicode(Info, currentIndex, tag_size);
                        if (frame_id_data == null)
                            frame_id_data = this.byteToString(data);
                    }

                    if (frame_id == "TIT2")
                    {
                        mp3InfoV2.Title = frame_id_data;
                    }
                    else if (frame_id == "TPE2")
                    {
                        richTextBox1.Text += frame_id + "\t\t" + frame_id_data + "\n";
                    }
                    else if (frame_id == "TPE1")
                    {
                        mp3InfoV2.Artist = frame_id_data;
                    }
                    else if (frame_id == "TALB")
                    {
                        mp3InfoV2.Album = frame_id_data;
                    }
                    else if (frame_id == "TYER")
                    {
                        mp3InfoV2.Year = frame_id_data;
                    }
                    else if (frame_id == "COMM")
                    {
                        if ((data[4] == 0xFF) && (data[5] == 0xFE))
                        {
                            //richTextBox1.Text += "Unicode解碼 " + frame_id + ", len = " + tag_size.ToString() + "\n";
                            j = 0;
                            for (i = currentIndex + 10; i < currentIndex + tag_size; i++)
                            {
                                data[j] = Info[i];
                                j++;
                            }
                            string str = Encoding.GetEncoding("utf-16").GetString(data);	//指名使用Unicode解碼解碼, 把拜列轉成字串
                            mp3InfoV2.Comment = str;
                            frame_id_data = str;
                            richTextBox1.Text += "COMM\t\t" + str + "\n";
                        }
                        else
                        {
                            mp3InfoV2.Comment = frame_id_data;
                        }

                        if (cb_raw_data.Checked == true)
                        {
                            richTextBox1.Text += "COMM data :\n";
                            int len = tag_size;
                            if (len > 100)
                                len = 100;
                            for (i = 0; i < len; i++)
                            {
                                richTextBox1.Text += data[i].ToString("X2");
                                if ((i % 32) == 31)
                                    richTextBox1.Text += "\n";
                                else
                                    richTextBox1.Text += " ";
                            }
                            richTextBox1.Text += "\ndata :\t\t" + frame_id_data + "\n";
                        }
                    }
                    else if (frame_id == "TRCK")
                    {
                        mp3InfoV2.Track = frame_id_data;
                    }
                    else if (frame_id == "TCON")
                    {
                        mp3InfoV2.Genre = frame_id_data;
                    }
                    else if (frame_id == "TLEN")
                    {
                        mp3InfoV2.Length = frame_id_data;
                    }
                    else
                    {
                        if (tag_size > 2)
                        {
                            if ((data[1] == 0xFF) && (data[2] == 0xFE))
                            {
                                //richTextBox1.Text += "Unicode解碼 " + frame_id + ", len = " + tag_size.ToString() + "\n";
                                data = new byte[tag_size - 3];
                                j = 0;
                                for (i = currentIndex + 3; i < currentIndex + tag_size; i++)
                                {
                                    data[j] = Info[i];
                                    j++;
                                }
                                string str = Encoding.GetEncoding("utf-16").GetString(data);	//指名使用Unicode解碼解碼, 把拜列轉成字串
                                frame_id_data = str;
                                richTextBox1.Text += "Unicode\t\t" + frame_id + "\t\t" + str + "\n";

                            }
                        }
                        else
                        {
                            richTextBox1.Text += "xxxxx 未定義:\t" + frame_id + "\t\t" + frame_id_data + "\n";
                            richTextBox1.Text += "xxxxx tag_size = " + tag_size.ToString() + "\n";
                        }

                        if (cb_raw_data.Checked == true)
                            richTextBox1.Text += "未定義:\t" + frame_id + "\t\t" + frame_id_data + "\n";
                    }

                    print_data_frame(frame_id, frame_id_data);

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
                frame_id = null;
                currentIndex += tag_size;
                //richTextBox1.Text += "\ncurrentIndex = " + currentIndex.ToString() + "\n";
                if (currentIndex >= Info.Length)
                    break;
            }
            return mp3InfoV2;
        }

        //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
        private byte[] getLast128(string filename)
        {
            //隨機binary讀取
            int len = 128;
            int seekPos = len;

            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            Stream stream = fs;
            stream.Seek(-seekPos, SeekOrigin.End);  //從最後開始往回算 128 拜
            int rl = 0;
            byte[] data = new byte[seekPos];
            rl = stream.Read(data, 0, seekPos);
            //釋放資源
            fs.Close();
            stream.Close();

            if (cb_raw_data.Checked == true)
            {
                richTextBox1.Text += "印出此檔案之末128拜資料\n";
                print_data(data);
            }
            return data;
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
            if (encoding != "utf-16")
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
            //openFileDialog1.InitialDirectory = "c:\\______test_files\\_id3";  //預設開啟的路徑
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
            this.Text = "讀取" + filename;
            this.BackColor = Color.Pink;
            richTextBox1.BackColor = Color.Pink;
            clear_textbox_id3_data();
            textBox_filename.Text = filename;
            richTextBox1.Text += "檔名:\t\t" + filename + "\n";
            if (cb_v1.Checked == true)
                get_ID3v1Tag(filename, encoding);
            if (cb_v2.Checked == true)
                get_ID3v2Tag(filename, encoding);
            this.Text = "ID3Tag";
            this.BackColor = Color.White;
            richTextBox1.BackColor = Color.White;
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

                if (encoding == "big5")
                {
                    textBox11.Text = mp3_information.identify;
                    textBox12.Text = mp3_information.Title;
                    textBox13.Text = mp3_information.Artist;
                    textBox14.Text = mp3_information.Album;
                    textBox15.Text = mp3_information.Year;
                    textBox16.Text = mp3_information.Comment;
                    if (mp3_information.Zero == 0)
                        textBox17.Text = mp3_information.Track.ToString();
                    else
                        textBox17.Text = "無資料";
                    textBox18.Text = mp3_information.Genre.ToString();
                    cb_id3v11.Checked = true;
                }
                else if (encoding == "gb2312")
                {
                    textBox21.Text = mp3_information.identify;
                    textBox22.Text = mp3_information.Title;
                    textBox23.Text = mp3_information.Artist;
                    textBox24.Text = mp3_information.Album;
                    textBox25.Text = mp3_information.Year;
                    textBox26.Text = mp3_information.Comment;
                    if (mp3_information.Zero == 0)
                        textBox27.Text = mp3_information.Track.ToString();
                    else
                        textBox27.Text = "無資料";
                    textBox28.Text = mp3_information.Genre.ToString();
                    cb_id3v21.Checked = true;
                }
                else if (encoding == "shift_jis")
                {
                    textBox31.Text = mp3_information.identify;
                    textBox32.Text = mp3_information.Title;
                    textBox33.Text = mp3_information.Artist;
                    textBox34.Text = mp3_information.Album;
                    textBox35.Text = mp3_information.Year;
                    textBox36.Text = mp3_information.Comment;
                    if (mp3_information.Zero == 0)
                        textBox37.Text = mp3_information.Track.ToString();
                    else
                        textBox37.Text = "無資料";
                    textBox38.Text = mp3_information.Genre.ToString();
                    cb_id3v31.Checked = true;
                }
                else
                {
                    textBox11.Text = mp3_information.identify;
                    textBox12.Text = mp3_information.Title;
                    textBox13.Text = mp3_information.Artist;
                    textBox14.Text = mp3_information.Album;
                    textBox15.Text = mp3_information.Year;
                    textBox16.Text = mp3_information.Comment;
                    if (mp3_information.Zero == 0)
                        textBox17.Text = mp3_information.Track.ToString();
                    else
                        textBox17.Text = "無資料";
                    textBox18.Text = mp3_information.Genre.ToString();
                    cb_id3v11.Checked = true;
                }

                print_genre(mp3_information.Genre);

                print_ID3TagV1(mp3_information);
            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\n";
                if (encoding == "big5")
                {
                    textBox11.Enabled = false;
                    textBox12.Enabled = false;
                    textBox13.Enabled = false;
                    textBox14.Enabled = false;
                    textBox15.Enabled = false;
                    textBox16.Enabled = false;
                    textBox17.Enabled = false;
                    textBox18.Enabled = false;
                    cb_id3v11.Checked = false;
                }
                else if (encoding == "gb2312")
                {
                    textBox21.Enabled = false;
                    textBox22.Enabled = false;
                    textBox23.Enabled = false;
                    textBox24.Enabled = false;
                    textBox25.Enabled = false;
                    textBox26.Enabled = false;
                    textBox27.Enabled = false;
                    textBox28.Enabled = false;
                    cb_id3v21.Checked = false;
                }
                else if (encoding == "shift_jis")
                {
                    textBox31.Enabled = false;
                    textBox32.Enabled = false;
                    textBox33.Enabled = false;
                    textBox34.Enabled = false;
                    textBox35.Enabled = false;
                    textBox36.Enabled = false;
                    textBox37.Enabled = false;
                    textBox38.Enabled = false;
                    cb_id3v31.Checked = false;
                }
                else
                {
                    textBox11.Enabled = false;
                    textBox12.Enabled = false;
                    textBox13.Enabled = false;
                    textBox14.Enabled = false;
                    textBox15.Enabled = false;
                    textBox16.Enabled = false;
                    textBox17.Enabled = false;
                    textBox18.Enabled = false;
                    cb_id3v11.Checked = false;
                }

            }
        }

        void get_ID3v2Tag(string filename, string encoding)
        {
            Mp3InfoV2 mp3_information;
            byte[] header = getID3v2Header(filename);
            if ((header[0] == 'I') && (header[1] == 'D') && (header[2] == '3'))
            {
                mp3_information.identify = "ID3";
                if (encoding == "big5")
                {
                    textBox11b.Text = "ID3";
                    cb_id3v11b.Checked = true;
                }
                else if (encoding == "gb2312")
                {
                    textBox21b.Text = "ID3";
                    cb_id3v21b.Checked = true;
                }
                else if (encoding == "shift_jis")
                {
                    textBox31b.Text = "ID3";
                    cb_id3v31b.Checked = true;
                }
                else
                {
                    textBox11b.Text = "ID3";
                    cb_id3v11b.Checked = true;
                }

                /*
                richTextBox1.Text += "印出此檔案之前10拜資料(ID3 header)\n";
                print_data(header);

                richTextBox1.Text += "有ID3 v2資料\n";
                richTextBox1.Text += "Major version : " + header[3].ToString() + "\n";
                richTextBox1.Text += "minor version : " + header[4].ToString() + "\n";
                richTextBox1.Text += "flags : " + header[5].ToString("X2") + "\n";
                */
                int tag_size = (((header[6] & 0x7f) << 21) + ((header[7] & 0x7f) << 14) + ((header[8] & 0x7f) << 7) + (header[9] & 0x7f));
                richTextBox1.Text += "ID3 tag_size = " + tag_size.ToString() + "\n";

                byte[] Info = getID3v2Data(filename, tag_size);
                mp3_information = getMp3InfoV2(Info);

                print_ID3TagV2(mp3_information);
            }
            else
            {
                richTextBox1.Text += "無ID3 v2資料\n";
                if (encoding == "big5")
                {
                    textBox11b.Enabled = false;
                    textBox12b.Enabled = false;
                    textBox13b.Enabled = false;
                    textBox14b.Enabled = false;
                    textBox15b.Enabled = false;
                    textBox16b.Enabled = false;
                    textBox17b.Enabled = false;
                    textBox18b.Enabled = false;
                    textBox19b.Enabled = false;
                    cb_id3v11b.Checked = false;
                }
                else if (encoding == "gb2312")
                {
                    textBox21b.Enabled = false;
                    textBox22b.Enabled = false;
                    textBox23b.Enabled = false;
                    textBox24b.Enabled = false;
                    textBox25b.Enabled = false;
                    textBox26b.Enabled = false;
                    textBox27b.Enabled = false;
                    textBox28b.Enabled = false;
                    textBox29b.Enabled = false;
                    cb_id3v21b.Checked = false;
                }
                else if (encoding == "shift_jis")
                {
                    textBox31b.Enabled = false;
                    textBox32b.Enabled = false;
                    textBox33b.Enabled = false;
                    textBox34b.Enabled = false;
                    textBox35b.Enabled = false;
                    textBox36b.Enabled = false;
                    textBox37b.Enabled = false;
                    textBox38b.Enabled = false;
                    textBox39b.Enabled = false;
                    cb_id3v31b.Checked = false;
                }
                else
                {
                    textBox11b.Enabled = false;
                    textBox12b.Enabled = false;
                    textBox13b.Enabled = false;
                    textBox14b.Enabled = false;
                    textBox15b.Enabled = false;
                    textBox16b.Enabled = false;
                    textBox17b.Enabled = false;
                    textBox18b.Enabled = false;
                    textBox19b.Enabled = false;
                    cb_id3v11b.Checked = false;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            encoding = "big5";
            get_ID3Tag(filename, encoding);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\uramachi.mp3";       //一定要有@
            encoding = "gb2312";
            get_ID3Tag(filename, encoding);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\harumi.mp3";       //一定要有@
            encoding = "shift_jis";
            get_ID3Tag(filename, encoding);
        }

        void clear_textbox_id3_data_big5()
        {
            textBox11.Clear();
            textBox12.Clear();
            textBox13.Clear();
            textBox14.Clear();
            textBox15.Clear();
            textBox16.Clear();
            textBox17.Clear();
            textBox18.Clear();
            textBox11b.Clear();
            textBox12b.Clear();
            textBox13b.Clear();
            textBox14b.Clear();
            textBox15b.Clear();
            textBox16b.Clear();
            textBox17b.Clear();
            textBox18b.Clear();
            textBox19b.Clear();

            textBox11.Enabled = true;
            textBox12.Enabled = true;
            textBox13.Enabled = true;
            textBox14.Enabled = true;
            textBox15.Enabled = true;
            textBox16.Enabled = true;
            textBox17.Enabled = true;
            textBox18.Enabled = true;

            textBox11b.Enabled = true;
            textBox12b.Enabled = true;
            textBox13b.Enabled = true;
            textBox14b.Enabled = true;
            textBox15b.Enabled = true;
            textBox16b.Enabled = true;
            textBox17b.Enabled = true;
            textBox18b.Enabled = true;
            textBox19b.Enabled = true;

            cb_id3v11.Checked = false;
            cb_id3v11b.Checked = false;
        }

        void clear_textbox_id3_data_gb2312()
        {
            textBox21.Clear();
            textBox22.Clear();
            textBox23.Clear();
            textBox24.Clear();
            textBox25.Clear();
            textBox26.Clear();
            textBox27.Clear();
            textBox28.Clear();
            textBox21b.Clear();
            textBox22b.Clear();
            textBox23b.Clear();
            textBox24b.Clear();
            textBox25b.Clear();
            textBox26b.Clear();
            textBox27b.Clear();
            textBox28b.Clear();
            textBox29b.Clear();

            textBox21.Enabled = true;
            textBox22.Enabled = true;
            textBox23.Enabled = true;
            textBox24.Enabled = true;
            textBox25.Enabled = true;
            textBox26.Enabled = true;
            textBox27.Enabled = true;
            textBox28.Enabled = true;

            textBox21b.Enabled = true;
            textBox22b.Enabled = true;
            textBox23b.Enabled = true;
            textBox24b.Enabled = true;
            textBox25b.Enabled = true;
            textBox26b.Enabled = true;
            textBox27b.Enabled = true;
            textBox28b.Enabled = true;
            textBox29b.Enabled = true;

            cb_id3v21.Checked = false;
            cb_id3v21b.Checked = false;
        }

        void clear_textbox_id3_data_shift_jis()
        {
            textBox31.Clear();
            textBox32.Clear();
            textBox33.Clear();
            textBox34.Clear();
            textBox35.Clear();
            textBox36.Clear();
            textBox37.Clear();
            textBox38.Clear();
            textBox31b.Clear();
            textBox32b.Clear();
            textBox33b.Clear();
            textBox34b.Clear();
            textBox35b.Clear();
            textBox36b.Clear();
            textBox37b.Clear();
            textBox38b.Clear();
            textBox39b.Clear();

            textBox31.Enabled = true;
            textBox32.Enabled = true;
            textBox33.Enabled = true;
            textBox34.Enabled = true;
            textBox35.Enabled = true;
            textBox36.Enabled = true;
            textBox37.Enabled = true;
            textBox38.Enabled = true;

            textBox31b.Enabled = true;
            textBox32b.Enabled = true;
            textBox33b.Enabled = true;
            textBox34b.Enabled = true;
            textBox35b.Enabled = true;
            textBox36b.Enabled = true;
            textBox37b.Enabled = true;
            textBox38b.Enabled = true;
            textBox39b.Enabled = true;

            cb_id3v31.Checked = false;
            cb_id3v31b.Checked = false;
        }

        void clear_textbox_id3_data()
        {
            textBox_filename.Clear();
            if (encoding == "big5")
            {
                clear_textbox_id3_data_big5();
            }
            else if (encoding == "gb2312")
            {
                clear_textbox_id3_data_gb2312();
            }
            else if (encoding == "shift_jis")
            {
                clear_textbox_id3_data_shift_jis();
            }
            else
            {
                clear_textbox_id3_data_big5();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            textBox_filename.Clear();
            clear_textbox_id3_data_big5();
            clear_textbox_id3_data_gb2312();
            clear_textbox_id3_data_shift_jis();
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
            //openFileDialog1.InitialDirectory = "c:\\______test_files\\_id3";  //預設開啟的路徑
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
                if (encoding == "big5")
                {
                    textBox18.Text = genre.ToString() + "  " + genre_data[genre, 1] + "  " + genre_data[genre, 2];
                }
                else if (encoding == "gb2312")
                {
                    textBox28.Text = genre.ToString() + "  " + genre_data[genre, 1] + "  " + genre_data[genre, 2];
                }
                else if (encoding == "shift_jis")
                {
                    textBox38.Text = genre.ToString() + "  " + genre_data[genre, 1] + "  " + genre_data[genre, 2];
                }
                else
                {
                    textBox18.Text = genre.ToString() + "  " + genre_data[genre, 1] + "  " + genre_data[genre, 2];
                }
            }
            else
            {
                if (encoding == "big5")
                {
                    textBox18.Text = genre.ToString() + "  無資料";
                }
                else if (encoding == "gb2312")
                {
                    textBox28.Text = genre.ToString() + "  無資料";
                }
                else if (encoding == "shift_jis")
                {
                    textBox38.Text = genre.ToString() + "  無資料";
                }
                else
                {
                    textBox18.Text = genre.ToString() + "  無資料";
                }
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
                    if (encoding == "big5")
                    {
                        textBox12b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox22b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox32b.Text = data;
                    }
                    else
                    {
                        textBox12b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TPE1")
                {
                    if (encoding == "big5")
                    {
                        textBox13b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox23b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox33b.Text = data;
                    }
                    else
                    {
                        textBox13b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TALB")
                {
                    if (encoding == "big5")
                    {
                        textBox14b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox24b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox34b.Text = data;
                    }
                    else
                    {
                        textBox14b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TYER")
                {
                    if (encoding == "big5")
                    {
                        textBox15b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox25b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox35b.Text = data;
                    }
                    else
                    {
                        textBox15b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "COMM")
                {
                    if (encoding == "big5")
                    {
                        textBox16b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox26b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox36b.Text = data;
                    }
                    else
                    {
                        textBox16b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TRCK")
                {
                    if (encoding == "big5")
                    {
                        textBox17b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox27b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox37b.Text = data;
                    }
                    else
                    {
                        textBox17b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TCON")
                {
                    if (encoding == "big5")
                    {
                        textBox18b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox28b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox38b.Text = data;
                    }
                    else
                    {
                        textBox18b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "TLEN")
                {
                    if (encoding == "big5")
                    {
                        textBox19b.Text = data;
                    }
                    else if (encoding == "gb2312")
                    {
                        textBox29b.Text = data;
                    }
                    else if (encoding == "shift_jis")
                    {
                        textBox39b.Text = data;
                    }
                    else
                    {
                        textBox19b.Text = data;
                    }
                    found_frame_id = true;
                }
                else if (id == "????")
                {
                    //skip data
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

        void print_ID3TagV1(Mp3InfoV1 mp3_information)
        {
            richTextBox1.Text += "\nID3TagV1 資料 :\n";
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
        }

        void print_ID3TagV2(Mp3InfoV2 mp3_information)
        {
            richTextBox1.Text += "\nID3TagV2 資料 :\n";
            richTextBox1.Text += "identify : " + mp3_information.identify + "\n";
            richTextBox1.Text += "Title : " + mp3_information.Title + "\n";
            richTextBox1.Text += "Artist : " + mp3_information.Artist + "\n";
            richTextBox1.Text += "Album : " + mp3_information.Album + "\n";
            richTextBox1.Text += "Year : " + mp3_information.Year + "\n";
            richTextBox1.Text += "Comment : " + mp3_information.Comment + "\n";
            richTextBox1.Text += "Genre : " + mp3_information.Genre + "\n";
            richTextBox1.Text += "Length : " + mp3_information.Length + "\n";
            richTextBox1.Text += "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            string filename2 = filename + ".no.id3v1." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";

            richTextBox1.Text += "移除 MP3 ID3 v1\n";
            richTextBox1.Text += "原檔名:\t" + filename + "\n";
            richTextBox1.Text += "新檔名:\t" + filename2 + "\n";
            remove_ID3TagV1(filename, filename2);
        }

        void remove_ID3TagV1(string filename, string filename2)
        {
            clear_textbox_id3_data();

            textBox_filename.Text = filename;

            byte[] Info = getLast128(filename);
            if ((Info[0] == 'T') && (Info[1] == 'A') && (Info[2] == 'G'))
            {
                richTextBox1.Text += "有ID3 v1資料\t移除之\n";

                //讀取資料
                byte[] data = File.ReadAllBytes(filename);
                int len = data.Length;
                //richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
                //richTextBox1.Text += "長度 : " + len.ToString() + "\n";

                int i;
                using (FileStream fileStream = new FileStream(filename2, FileMode.Create))
                {
                    // Write the data to the file, byte by byte.
                    for (i = 0; i < (len - 128); i++)
                    {
                        fileStream.WriteByte(data[i]);
                    }
                }
                //richTextBox1.Text += "\nWriteByte存檔完成, 檔名 : " + filename2 + "\n";
            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            string filename2 = filename + ".add.id3v1." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";

            richTextBox1.Text += "新增 MP3 ID3 v1\n";
            richTextBox1.Text += "原檔名:\t" + filename + "\n";
            richTextBox1.Text += "新檔名:\t" + filename2 + "\n";
            add_ID3TagV1(filename, filename2);
        }

        void add_ID3TagV1(string filename, string filename2)
        {
            clear_textbox_id3_data();

            textBox_filename.Text = filename;

            byte[] Info = getLast128(filename);
            if ((Info[0] == 'T') && (Info[1] == 'A') && (Info[2] == 'G'))
            {
                richTextBox1.Text += "有ID3 v1資料\t不可新增\n";
            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\t可新增\n";
                //TBD


            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            string filename2 = filename + ".modify.id3v1." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";

            richTextBox1.Text += "修改 MP3 ID3 v1\n";
            richTextBox1.Text += "原檔名:\t" + filename + "\n";
            richTextBox1.Text += "新檔名:\t" + filename2 + "\n";
            modify_ID3TagV1(filename, filename2);
        }

        void modify_ID3TagV1(string filename, string filename2)
        {
            clear_textbox_id3_data();

            textBox_filename.Text = filename;

            byte[] Info = getLast128(filename);
            if ((Info[0] == 'T') && (Info[1] == 'A') && (Info[2] == 'G'))
            {
                richTextBox1.Text += "有ID3 v1資料\t可修改\n";
                //TBD


            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\t不可修改\n";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup_item_location();
        }

        void setup_item_location()
        {
            int x_st;
            int y_st;
            int offset_x;
            int offset_y;
            int xx = 20;
            int yy = 5;

            x_st = 12;
            y_st = 80;
            offset_x = 0;
            offset_y = 25;
            cb_v1.Location = new Point(x_st, y_st + offset_y * 0);
            cb_v2.Location = new Point(x_st, y_st + offset_y * 1);
            cb_raw_data.Location = new Point(x_st, y_st + offset_y * 2);

            x_st = 85;
            y_st = 210;
            offset_x = 255;
            offset_y = 35;

            cb_id3v11.Location = new Point(x_st, y_st + offset_y * 0 + yy);
            textBox11.Size = new Size(textBox11.Size.Width - xx, textBox11.Size.Height);
            textBox11.Location = new Point(x_st + xx, y_st + offset_y * 0);
            textBox12.Location = new Point(x_st, y_st + offset_y * 1);
            textBox13.Location = new Point(x_st, y_st + offset_y * 2);
            textBox14.Location = new Point(x_st, y_st + offset_y * 3);
            textBox15.Location = new Point(x_st, y_st + offset_y * 4);
            textBox16.Location = new Point(x_st, y_st + offset_y * 5);
            textBox17.Location = new Point(x_st, y_st + offset_y * 6);
            textBox18.Location = new Point(x_st, y_st + offset_y * 7);

            cb_id3v11b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 0 + yy);
            textBox11b.Size = new Size(textBox11b.Size.Width - xx, textBox11b.Size.Height);
            textBox11b.Location = new Point(x_st + offset_x * 1 + xx, y_st + offset_y * 0);
            textBox12b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 1);
            textBox13b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 2);
            textBox14b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 3);
            textBox15b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 4);
            textBox16b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 5);
            textBox17b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 6);
            textBox18b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 7);
            textBox19b.Location = new Point(x_st + offset_x * 1, y_st + offset_y * 8);

            cb_id3v21.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 0 + yy);
            textBox21.Size = new Size(textBox21.Size.Width - xx, textBox21.Size.Height);
            textBox21.Location = new Point(x_st + offset_x * 2 + xx, y_st + offset_y * 0);
            textBox22.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 1);
            textBox23.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 2);
            textBox24.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 3);
            textBox25.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 4);
            textBox26.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 5);
            textBox27.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 6);
            textBox28.Location = new Point(x_st + offset_x * 2, y_st + offset_y * 7);

            cb_id3v21b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 0 + yy);
            textBox21b.Size = new Size(textBox21b.Size.Width - xx, textBox21b.Size.Height);
            textBox21b.Location = new Point(x_st + offset_x * 3 + xx, y_st + offset_y * 0);
            textBox22b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 1);
            textBox23b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 2);
            textBox24b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 3);
            textBox25b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 4);
            textBox26b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 5);
            textBox27b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 6);
            textBox28b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 7);
            textBox29b.Location = new Point(x_st + offset_x * 3, y_st + offset_y * 8);

            cb_id3v31.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 0 + yy);
            textBox31.Size = new Size(textBox31.Size.Width - xx, textBox31.Size.Height);
            textBox31.Location = new Point(x_st + offset_x * 4 + xx, y_st + offset_y * 0);
            textBox32.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 1);
            textBox33.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 2);
            textBox34.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 3);
            textBox35.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 4);
            textBox36.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 5);
            textBox37.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 6);
            textBox38.Location = new Point(x_st + offset_x * 4, y_st + offset_y * 7);

            cb_id3v31b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 0 + yy);
            textBox31b.Size = new Size(textBox31b.Size.Width - xx, textBox31b.Size.Height);
            textBox31b.Location = new Point(x_st + offset_x * 5 + xx, y_st + offset_y * 0);
            textBox32b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 1);
            textBox33b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 2);
            textBox34b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 3);
            textBox35b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 4);
            textBox36b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 5);
            textBox37b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 6);
            textBox38b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 7);
            textBox39b.Location = new Point(x_st + offset_x * 5, y_st + offset_y * 8);

            textBox_filename.Location = new Point(x_st + offset_x * 0, y_st - offset_y * 1);
            button4.Location = new Point(x_st + offset_x * 6-button4.Size.Width-5, y_st - offset_y * 1);

            label0.Text = "Filename";
            label1.Text = "Header";
            label2.Text = "Title";
            label3.Text = "Artist";
            label4.Text = "Album";
            label5.Text = "Year";
            label6.Text = "Comment";
            label7.Text = "Track";
            label8.Text = "Genre";
            label9.Text = "Length";

            int left = 70;
            label0.Location = new Point(x_st - left, y_st - offset_y * 1);
            label1.Location = new Point(x_st - left, y_st + offset_y * 0);
            label2.Location = new Point(x_st - left, y_st + offset_y * 1);
            label3.Location = new Point(x_st - left, y_st + offset_y * 2);
            label4.Location = new Point(x_st - left, y_st + offset_y * 3);
            label5.Location = new Point(x_st - left, y_st + offset_y * 4);
            label6.Location = new Point(x_st - left, y_st + offset_y * 5);
            label7.Location = new Point(x_st - left, y_st + offset_y * 6);
            label8.Location = new Point(x_st - left, y_st + offset_y * 7);
            label9.Location = new Point(x_st - left, y_st + offset_y * 8);

            richTextBox1.Location = new Point(x_st, y_st + offset_y * 10);

            richTextBox1.Size = new Size(250 * 6 + 5 * 5, 300);

            this.Size = new Size(1650, 920);


        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\unicode_ナレーション(岡本妙子).mp3";       //一定要有@
            encoding = "big5";
            get_ID3Tag(filename, encoding);
        }

        string check_frame_id_dataunicode(byte[] Info, int currentIndex, int tag_size)
        {
            string str = null;
            //richTextBox1.Text += "check_frame_id_dataunicode, currentIndex = " + currentIndex.ToString() + ", tag_size = " + tag_size.ToString() + "\n";
            if ((Info[currentIndex + 1] == 0xFF) && (Info[currentIndex+2] == 0xFE))
            {
                //獲取字串資料
                byte[] data = new byte[tag_size - 3];
                int i = 0;
                int j = 0;
                for (i = currentIndex + 3; i < currentIndex + tag_size; i++)
                {
                    data[j] = Info[i];
                    j++;
                }
                str = Encoding.GetEncoding("utf-16").GetString(data);	//指名使用Unicode解碼解碼, 把拜列轉成字串
                //richTextBox1.Text += "Unicode解碼的到\t" + str + "\n";
            }
            return str;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            string filename2 = filename + ".no.id3v2." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";

            richTextBox1.Text += "移除 MP3 ID3 v2\n";
            richTextBox1.Text += "原檔名:\t" + filename + "\n";
            richTextBox1.Text += "新檔名:\t" + filename2 + "\n";
            remove_ID3TagV2(filename, filename2);
        }

        void remove_ID3TagV2(string filename, string filename2)
        {
            clear_textbox_id3_data();

            textBox_filename.Text = filename;

            byte[] header = getID3v2Header(filename);
            if ((header[0] == 'I') && (header[1] == 'D') && (header[2] == '3'))
            {
                richTextBox1.Text += "有ID3 v2資料\t移除之\n";

                /*
                richTextBox1.Text += "印出此檔案之前10拜資料(ID3 header)\n";
                print_data(header);

                richTextBox1.Text += "有ID3 v2資料\n";
                richTextBox1.Text += "Major version : " + header[3].ToString() + "\n";
                richTextBox1.Text += "minor version : " + header[4].ToString() + "\n";
                richTextBox1.Text += "flags : " + header[5].ToString("X2") + "\n";
                */

                int tag_size = (((header[6] & 0x7f) << 21) + ((header[7] & 0x7f) << 14) + ((header[8] & 0x7f) << 7) + (header[9] & 0x7f));
                //richTextBox1.Text += "ID3 tag_size = " + tag_size.ToString() + "\n";

                //讀取資料
                byte[] data = File.ReadAllBytes(filename);
                int len = data.Length;
                //richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
                //richTextBox1.Text += "長度 : " + len.ToString() + "\n";

                int i;
                using (FileStream fileStream = new FileStream(filename2, FileMode.Create))
                {
                    // Write the data to the file, byte by byte.
                    for (i = (10 + tag_size); i < len; i++)
                    {
                        fileStream.WriteByte(data[i]);
                    }
                }
                //richTextBox1.Text += "\nWriteByte存檔完成, 檔名 : " + filename2 + "\n";
            }
            else
            {
                richTextBox1.Text += "無ID3 v2資料\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_id3\aaaa.mp3";       //一定要有@
            string filename2 = filename + ".no.id3v1v2." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";

            richTextBox1.Text += "移除 MP3 ID3 v1 v2\n";
            richTextBox1.Text += "原檔名:\t" + filename + "\n";
            richTextBox1.Text += "新檔名:\t" + filename2 + "\n";
            remove_ID3TagV1V2(filename, filename2);
        }

        void remove_ID3TagV1V2(string filename, string filename2)
        {
            bool flag_remove_tag_v1 = false;
            bool flag_remove_tag_v2 = false;
            int tag_size_v1 = 0;
            int tag_size_v2 = 0;

            clear_textbox_id3_data();

            textBox_filename.Text = filename;

            byte[] Info = getLast128(filename);
            if ((Info[0] == 'T') && (Info[1] == 'A') && (Info[2] == 'G'))
            {
                richTextBox1.Text += "有ID3 v1資料\t移除之\n";
                tag_size_v1 = 128;
                flag_remove_tag_v1 = true;
            }
            else
            {
                richTextBox1.Text += "無ID3 v1資料\n";
            }

            byte[] header = getID3v2Header(filename);
            if ((header[0] == 'I') && (header[1] == 'D') && (header[2] == '3'))
            {
                richTextBox1.Text += "有ID3 v2資料\t移除之\n";
                tag_size_v2 = (((header[6] & 0x7f) << 21) + ((header[7] & 0x7f) << 14) + ((header[8] & 0x7f) << 7) + (header[9] & 0x7f));
                //richTextBox1.Text += "ID3 tag_size_v2 = " + tag_size_v2.ToString() + "\n";
                flag_remove_tag_v2 = true;
            }
            else
            {
                richTextBox1.Text += "無ID3 v2資料\n";
            }

            if ((flag_remove_tag_v1 == true) && (flag_remove_tag_v2 == true))
            {
                richTextBox1.Text += "移除ID3 v1 和 v2資料\n";

                //讀取資料
                byte[] data = File.ReadAllBytes(filename);
                int len = data.Length;
                //richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
                //richTextBox1.Text += "長度 : " + len.ToString() + "\n";

                int i;
                using (FileStream fileStream = new FileStream(filename2, FileMode.Create))
                {
                    // Write the data to the file, byte by byte.
                    for (i = (10 + tag_size_v2); i < (len - tag_size_v1); i++)
                    {
                        fileStream.WriteByte(data[i]);
                    }
                }
                //richTextBox1.Text += "\nWriteByte存檔完成, 檔名 : " + filename2 + "\n";
            }
            else if (flag_remove_tag_v1 == true)
            {
                richTextBox1.Text += "僅移除ID3 v1資料\n";

                //讀取資料
                byte[] data = File.ReadAllBytes(filename);
                int len = data.Length;
                //richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
                //richTextBox1.Text += "長度 : " + len.ToString() + "\n";

                int i;
                using (FileStream fileStream = new FileStream(filename2, FileMode.Create))
                {
                    // Write the data to the file, byte by byte.
                    for (i = 0; i < (len - tag_size_v1); i++)
                    {
                        fileStream.WriteByte(data[i]);
                    }
                }
                //richTextBox1.Text += "\nWriteByte存檔完成, 檔名 : " + filename2 + "\n";
            }
            else if (flag_remove_tag_v2 == true)
            {
                richTextBox1.Text += "僅移除ID3 v2資料\n";

                //讀取資料
                byte[] data = File.ReadAllBytes(filename);
                int len = data.Length;
                //richTextBox1.Text += "全部binary讀取\t檔案" + filename + "\t";
                //richTextBox1.Text += "長度 : " + len.ToString() + "\n";

                int i;
                using (FileStream fileStream = new FileStream(filename2, FileMode.Create))
                {
                    // Write the data to the file, byte by byte.
                    //for (i = 0; i < (len - 128); i++)
                    for (i = (10 + tag_size_v2); i < len; i++)
                    {
                        fileStream.WriteByte(data[i]);
                    }
                }
                //richTextBox1.Text += "\nWriteByte存檔完成, 檔名 : " + filename2 + "\n";
            }
            else
            {
                richTextBox1.Text += "無ID3 v1 v2資料可移除\n";
            }
        }

        private void cb_id3v11_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void cb_id3v11b_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void cb_id3v21_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void cb_id3v21b_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void cb_id3v31_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void cb_id3v31b_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
