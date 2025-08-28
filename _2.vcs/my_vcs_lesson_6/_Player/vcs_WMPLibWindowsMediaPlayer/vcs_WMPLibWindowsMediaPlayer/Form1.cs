using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList
using System.IO;    //for FileStream, path

using WMPLib;   //for WindowsMediaPlayer

//參考/加入參考/dll內的兩個dll
//Interop.WMPLib的內嵌Interop型別改成False

namespace vcs_WMPLibWindowsMediaPlayer
{
    public partial class Form1 : Form
    {
        private WindowsMediaPlayer wmp;// = new WindowsMediaPlayer();
        string mp3_filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\09    都はるみ--裏町人生(後街人生).mp3";

        ArrayList musicPath = new ArrayList();    //用於保存歌曲目錄

        string playlist_filename = "my_playlist.txt";
        int playlist_index = 0;
        public Form1()
        {
            InitializeComponent();
            wmp = new WindowsMediaPlayer();
            //wmp.URL = @"D:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";   //指名單一檔案
            wmp.URL = mp3_filename;
            wmp.settings.setMode("loop", true);

            wmp.settings.autoStart = true;          //自动播放
            wmp.settings.setMode("shuffle", false);  //顺序播放
            wmp.settings.enableErrorDialogs = true;
            wmp.settings.balance = 0;
            wmp.settings.mute = false;
            wmp.settings.volume = 50;  //設定音量大小

            wmp.controls.stop();
            trackBar1.Value = wmp.settings.volume;
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }


        void Get_Mp3_Information(string filename)
        {
            Mp3Info mp3_information;
            byte[] Info = getLast128(filename);
            mp3_information = getMp3Info(Info);

            richTextBox1.Text += "Title : " + mp3_information.Title + "\t";
            richTextBox1.Text += "Artist : " + mp3_information.Artist + "\n";
            richTextBox1.Text += "Album : " + mp3_information.Album + "\n";
            richTextBox1.Text += "Year : " + mp3_information.Year + "\t";
            richTextBox1.Text += "identify : " + mp3_information.identify + "\t";
            richTextBox1.Text += "Comment : " + mp3_information.Comment + "\n";
            richTextBox1.Text += "reserved1 : " + mp3_information.reserved1 + "\t";
            richTextBox1.Text += "reserved2 : " + mp3_information.reserved2 + "\t";
            richTextBox1.Text += "reserved3 : " + mp3_information.reserved3 + "\n";
        }

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
            Encoding enc = Encoding.GetEncoding("BIG5");
            string str = enc.GetString(b);
            str = str.Substring(0, str.IndexOf('\0') >= 0 ? str.IndexOf('\0') : str.Length);//去掉無用字元
            return str;
        }

        //參考/加入參考/COM 選Windows Media Player (wmp.dll)
        //using WMPLib;
        private void button5_Click(object sender, EventArgs e)
        {
            //wmp.URL = @"D:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";   //指名單一檔案
            //wmp.settings.setMode("loop", true);
            wmp.URL = mp3_filename;

            wmp.controls.play();
            timer1.Enabled = true;
            richTextBox1.Text += "Title: " + wmp.currentMedia.getItemInfo("Title") + "\t";
            richTextBox1.Text += "Author: " + wmp.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright: " + wmp.currentMedia.getItemInfo("Copyright") + "\t";
            richTextBox1.Text += "Description: " + wmp.currentMedia.getItemInfo("Description") + "\t";
            richTextBox1.Text += "Duration: " + wmp.currentMedia.getItemInfo("Duration").ToString() + " Sec\t";
            richTextBox1.Text += "FileSize: " + wmp.currentMedia.getItemInfo("FileSize").ToString() + "\t";
            richTextBox1.Text += "FileType: " + wmp.currentMedia.getItemInfo("FileType").ToString() + "\n";
            richTextBox1.Text += "sourceURL: " + wmp.currentMedia.getItemInfo("sourceURL").ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            wmp.controls.stop();
            timer1.Enabled = false;
            progressBar1.Value = 0;
            trackBar2.Value = 0;
        }

        public int MediaGetPosition()
        {
            int ret = 0;
            if (WMPPlayState.wmppsPlaying != wmp.playState)
            {
                return ret;
            }
            double curPos = wmp.controls.currentPosition;
            double totalLen = wmp.currentMedia.duration;
            ret = (int)((curPos / totalLen) * 1000);
            //richTextBox1.Text += "curPos = " + curPos.ToString() + "\n";
            //richTextBox1.Text += "totalLen = " + totalLen.ToString() + "\n";
            //richTextBox1.Text += "ret = " + ret.ToString() + "\n";
            return ret;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (WMPPlayState.wmppsPlaying != wmp.playState)
            {
                return;
            }
            int position = MediaGetPosition();
            progressBar1.Value = position;
            trackBar2.Value = position;
            if (WMPPlayState.wmppsPlaying == wmp.playState)
            {
                label1.Text = wmp.controls.currentPositionString + " / " + wmp.currentMedia.durationString;
            }
            else
            {
                label1.Text = "00:00" + " / " + wmp.currentMedia.durationString;
                timer1.Enabled = false;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            wmp.controls.pause();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            wmp.controls.play();
            timer1.Enabled = true;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            wmp.settings.volume = trackBar1.Value;
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            if (WMPPlayState.wmppsPlaying != wmp.playState)
            {
                trackBar2.Value = 0;
                return;
            }
            int position = (int)(trackBar2.Value * wmp.currentMedia.duration / 1000);
            wmp.settings.mute = true;
            wmp.controls.currentPosition = position;
            wmp.settings.mute = false;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\_mp3";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                /*
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                */
                mp3_filename = openFileDialog1.FileName;
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //無效
            //richTextBox1.Text += "playCount = 0\n";
            //wmp.settings.playCount = 0;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //無效
            //richTextBox1.Text += "playCount = 1\n";
            //wmp.settings.playCount = 1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "mute\n";
            wmp.settings.mute = true;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "unmute\n";
            wmp.settings.mute = false;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            Get_Mp3_Information(mp3_filename);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //改成附加至播放清單，以下4行為清空播放清單
            //listView1.Clear();
            //listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            //listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
            //wmp.currentPlaylist.clear();

            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\_mp3";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n";
                richTextBox1.Text += "已選取檔案: \n";
                foreach (var strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "\t" + strFilename + "\n";
                    musicPath.Add(strFilename);
                    wmp.currentPlaylist.insertItem(wmp.currentPlaylist.count, wmp.newMedia(strFilename));

                    ListViewItem i1 = new ListViewItem(strFilename);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    //sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                    sub_i1a.Text = string.Empty;
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();

                richTextBox1.Text += "\n";

            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            wmp.controls.play();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            wmp.controls.next();
            playlist_index++;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            wmp.controls.previous();
            if (playlist_index < 1)
            {
                playlist_index = wmp.currentPlaylist.count + playlist_index - 1;
            }
            else
                playlist_index--;
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.listView1.SelectedIndices.Count <= 0)
                return;

            /* 一樣
            if (listView1.SelectedItems.Count <= 0)
                return;
            */

            /* 一樣
            //ListView.SelectedListViewItemCollection selected = listView1.SelectedItems;
            //mp3_filename = selected[0].SubItems[0].Text;
            */
            /*
            int selNdx = listView1.SelectedIndices[0];
            mp3_filename = listView1.Items[selNdx].Text;

            wmp.controls.stop();
            //wmp.settings.setMode("loop", true);
            wmp.URL = mp3_filename;

            wmp.controls.play();
            timer1.Enabled = true;

            richTextBox1.Text += "Title: " + wmp.currentMedia.getItemInfo("Title") + "\t";
            richTextBox1.Text += "Author: " + wmp.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright: " + wmp.currentMedia.getItemInfo("Copyright") + "\t";
            richTextBox1.Text += "Description: " + wmp.currentMedia.getItemInfo("Description") + "\t";
            richTextBox1.Text += "Duration: " + wmp.currentMedia.getItemInfo("Duration").ToString() + " Sec\t";
            richTextBox1.Text += "FileSize: " + wmp.currentMedia.getItemInfo("FileSize").ToString() + "\t";
            richTextBox1.Text += "FileType: " + wmp.currentMedia.getItemInfo("FileType").ToString() + "\n";
            richTextBox1.Text += "sourceURL: " + wmp.currentMedia.getItemInfo("sourceURL").ToString() + "\n";
            */
        }

        private void button6_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
            wmp.currentPlaylist.clear();
            playlist_index = 0;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (System.IO.File.Exists(playlist_filename) == false)
            {
                richTextBox1.Text += "檔案 " + playlist_filename + " 不存在，離開。\n";
            }
            else
            {
                int i = 0;
                richTextBox1.Text += "檔案 " + playlist_filename + " 存在, 開啟，並讀入播放清單。\n";

                listView1.Clear();
                listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
                listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
                wmp.currentPlaylist.clear();
                playlist_index = 0;

                String line;
                StreamReader sr = new StreamReader(playlist_filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\tlength:" + line.Length.ToString() + "\n";
                    if (line.Length > 0)
                    {
                        wmp.currentPlaylist.insertItem(wmp.currentPlaylist.count, wmp.newMedia(line));
                        ListViewItem i1 = new ListViewItem(line);
                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        //sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                        sub_i1a.Text = string.Empty;
                        i1.SubItems.Add(sub_i1a);
                        listView1.Items.Add(i1);
                    }
                }
                sr.Close();
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();

                playlist_index = 0;
                richTextBox1.Text += "wmp.currentPlaylist.count = " + wmp.currentPlaylist.count.ToString() + "\n";

                label2.Text = ((playlist_index % wmp.currentPlaylist.count) + 1).ToString() + " / " + wmp.currentPlaylist.count.ToString();

            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            int i = 0;
            int numberMusic = listView1.Items.Count;

            if (numberMusic <= 0)
            {
                richTextBox1.Text += "0首歌，不用存檔\n";
            }
            else
            {
                richTextBox1.Text += "共有 " + numberMusic.ToString() + " 首歌, 依序是：\n";
                StreamWriter sw = File.CreateText(playlist_filename);
                string content = "";

                //mp3_filename = listView1.Items[selNdx].Text;
                for (i = 0; i < numberMusic; i++)
                {
                    richTextBox1.Text += listView1.Items[i].Text + "\n";
                    content += listView1.Items[i].Text + "\n";
                }
                sw.WriteLine(content);
                sw.Close();
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (wmp.currentPlaylist.count > 0)
                label2.Text = ((playlist_index % wmp.currentPlaylist.count) + 1).ToString() + " / " + wmp.currentPlaylist.count.ToString();
            else
                label2.Text = "0 / 0";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = @"D:\_git\vcs\_1.data\______test_files1\_mp3";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                //C# 取得資料夾下的所有檔案(包括子目錄)
                string[] files = System.IO.Directory.GetFiles(folderBrowserDialog1.SelectedPath, "*.mp3", System.IO.SearchOption.AllDirectories);
                foreach (string strFilename in files)
                {
                    richTextBox1.Text += strFilename + "\n";
                    musicPath.Add(strFilename);
                    wmp.currentPlaylist.insertItem(wmp.currentPlaylist.count, wmp.newMedia(strFilename));

                    ListViewItem i1 = new ListViewItem(strFilename);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    //sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                    sub_i1a.Text = string.Empty;
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();

                richTextBox1.Text += "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }

        }

        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            //int selNdx = listView1.SelectedIndices[0];
            //richTextBox1.Text += "you clicked " + listView1.Items[selNdx].Text + "\n";

            int selNdx = listView1.SelectedIndices[0];
            mp3_filename = listView1.Items[selNdx].Text;

            wmp.controls.stop();
            //wmp.settings.setMode("loop", true);
            wmp.URL = mp3_filename;

            wmp.controls.play();
            timer1.Enabled = true;

            richTextBox1.Text += "Title: " + wmp.currentMedia.getItemInfo("Title") + "\t";
            richTextBox1.Text += "Author: " + wmp.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright: " + wmp.currentMedia.getItemInfo("Copyright") + "\t";
            richTextBox1.Text += "Description: " + wmp.currentMedia.getItemInfo("Description") + "\t";
            richTextBox1.Text += "Duration: " + wmp.currentMedia.getItemInfo("Duration").ToString() + " Sec\t";
            richTextBox1.Text += "FileSize: " + wmp.currentMedia.getItemInfo("FileSize").ToString() + "\t";
            richTextBox1.Text += "FileType: " + wmp.currentMedia.getItemInfo("FileType").ToString() + "\n";
            richTextBox1.Text += "sourceURL: " + wmp.currentMedia.getItemInfo("sourceURL").ToString() + "\n";
        }

    }
}
