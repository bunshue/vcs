using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileStream, path
using System.Media;         //SystemSounds類別、SoundPlayer類別
using System.Runtime.InteropServices;   //for DllImport
using System.Text.RegularExpressions;

using WMPLib;   //for mp3

namespace vcs_AudioVideoTest1
{
    public partial class Form1 : Form
    {
        private WMPLib.WindowsMediaPlayer wplayer;// = new WMPLib.WindowsMediaPlayer();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            wplayer = new WMPLib.WindowsMediaPlayer();
            trackBar1.Value = wplayer.settings.volume;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 220 + 10;
            dy = 50 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            button7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            button14.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button15.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7 + 20);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_wav\chimes.wav";

            //法一
            //直接使用 SoundPlayer 類別 播放.wav檔
            //SoundPlayer sp = new SoundPlayer(@"C:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav");

            //法二, 直接使用 SoundPlayer 類別
            //SoundPlayer sp = new SoundPlayer();
            //sp.SoundLocation = @"F:\_______mp3_ALL_all1\_mp3_0_中英日語文\《遥远的绝响--配乐朗诵余秋雨作品(共4篇)》.赵忠祥.[wav]\02.都江堰.wav";

            //法三
            //using System.Media;
            //SoundPlayer sp = new SoundPlayer(@"C:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav");
            //sp.Play(); // 撥放

            //法四
            //SoundPlayer sp = new SoundPlayer();   // 新增一個SoundPlayer物件
            //sp.SoundLocation = filename;          // 設定聲音檔案的路徑和名稱
            //sp.Play();    // 播放

            //法五    播放外部的聲音檔
            //SoundPlayer sp = new SoundPlayer(filename);
            //sp.Play();  // 播放
            //sp.PlayLooping(); // 重複循環播放
            //sp.PlaySync(); // 播放 -- 等候播放完成後，再繼續執行程式碼
            //sp.Stop(); // 停止播放

            //法六    設定檔案的串流 從專案的資源來的
            SoundPlayer sp = new SoundPlayer();// 新增一個SoundPlayer物件
            sp.Stream = Properties.Resources.WindowsShutdown; // 設定檔案的串流 從專案的資源來的
            sp.Play(); // 播放

            /*
            SoundPlayer sp = new SoundPlayer();
            sp.SoundLocation = filename;
            sp.Load(); //同步加載聲音
            sp.Play(); //啟用新線程播放
            //sp.PlayLooping(); //循環播放模式
            //sp.PlaySync(); //UI線程播放
            */

            /*
            //播放wav檔
            SoundPlayer sp = new SoundPlayer(); //声明一个控制WAV文件的声音播放文件对象
            sp.SoundLocation = filename; //指定声音文件的路径
            sp.LoadAsync();  //设置播放的方法
            sp.Play(); //播放声音文件
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //法一
            //直接使用 SoundPlayer 類別
            SoundPlayer sp = new SoundPlayer(@"C:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav");

            //法二
            //SoundPlayer sp = new SoundPlayer();
            //sp.SoundLocation = @"F:\_______mp3_ALL_all1\_mp3_0_中英日語文\《遥远的绝响--配乐朗诵余秋雨作品(共4篇)》.赵忠祥.[wav]\02.都江堰.wav";

            sp.Stop(); // 停止
        }

        int number = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            //播放系統預設的音效
            switch (number)
            {
                case 0:
                    SystemSounds.Beep.Play();
                    richTextBox1.Text += "Beep\n";
                    break;
                case 1:
                    SystemSounds.Asterisk.Play();
                    richTextBox1.Text += "Asterisk\n";
                    break;
                case 2:
                    SystemSounds.Exclamation.Play();
                    richTextBox1.Text += "Exclamation\n";
                    break;
                case 3:
                    SystemSounds.Hand.Play();
                    richTextBox1.Text += "Hand\n";
                    break;
                case 4:
                    SystemSounds.Question.Play();
                    richTextBox1.Text += "Question\n";
                    break;
                default:
                    SystemSounds.Beep.Play();
                    richTextBox1.Text += "Beep\n";
                    break;
            }
            number++;
            if (number > 4)
                number = 0;

        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            PlayWav(@"C:\_git\vcs\_1.data\______test_files1\_wav\Frog.wav", false);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            PlayWav(@"C:\_git\vcs\_1.data\______test_files1\_wav\Frog.wav", true);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            PlayWav(null, false);
        }

        // The player making the current sound.
        private SoundPlayer Player = null;

        // Dispose of the current player and
        // play the indicated WAV file.
        private void PlayWav(string filename, bool play_looping)
        {
            // Stop the player if it is running.
            if (Player != null)
            {
                Player.Stop();
                Player.Dispose();
                Player = null;
            }

            // If we have no file name, we're done.
            if (filename == null) return;
            if (filename.Length == 0) return;

            // Make the new player for the WAV file.
            Player = new SoundPlayer(filename);

            // Play.
            if (play_looping)
                Player.PlayLooping();
            else
                Player.Play();
        }

        public int MediaGetPosition()
        {
            int ret = 0;
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                return ret;
            }
            double curPos = wplayer.controls.currentPosition;
            double totalLen = wplayer.currentMedia.duration;
            ret = (int)((curPos / totalLen) * 1000);
            //richTextBox1.Text += "curPos = " + curPos.ToString() + "\n";
            //richTextBox1.Text += "totalLen = " + totalLen.ToString() + "\n";
            //richTextBox1.Text += "ret = " + ret.ToString() + "\n";
            return ret;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                return;
            }
            int position = MediaGetPosition();
            progressBar1.Value = position;
            trackBar2.Value = position;
            if (WMPLib.WMPPlayState.wmppsPlaying == wplayer.playState)
            {
                label1.Text = wplayer.controls.currentPositionString + " / " + wplayer.currentMedia.durationString;
            }
            else
            {
                label1.Text = "00:00" + " / " + wplayer.currentMedia.durationString;
                timer1.Enabled = false;
            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            wplayer.settings.volume = trackBar1.Value;
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            if (WMPLib.WMPPlayState.wmppsPlaying != wplayer.playState)
            {
                trackBar2.Value = 0;
                return;
            }
            int position = (int)(trackBar2.Value * wplayer.currentMedia.duration / 1000);
            wplayer.controls.pause();
            wplayer.controls.currentPosition = position;
            wplayer.controls.play();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //參考/加入參考/COM 選W indows Media Player (wmp.dll)
        //using WMPLib;
        private void mp3_player_play_Click(object sender, EventArgs e)
        {
            wplayer.URL = @"C:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";
            wplayer.settings.setMode("loop", true);
            wplayer.controls.play();
            timer1.Enabled = true;
            richTextBox1.Text += wplayer.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Title: " + wplayer.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Author: " + wplayer.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright: " + wplayer.currentMedia.getItemInfo("Copyright") + "\n";
            richTextBox1.Text += "Description: " + wplayer.currentMedia.getItemInfo("Description") + "\n";
            richTextBox1.Text += "Duration: " + wplayer.currentMedia.getItemInfo("Duration").ToString() + " Sec\n";
            richTextBox1.Text += "FileSize: " + wplayer.currentMedia.getItemInfo("FileSize").ToString() + "\n";
            richTextBox1.Text += "FileType: " + wplayer.currentMedia.getItemInfo("FileType").ToString() + "\n";
            richTextBox1.Text += "sourceURL: " + wplayer.currentMedia.getItemInfo("sourceURL").ToString() + "\n";
        }

        private void mp3_player_pause_Click(object sender, EventArgs e)
        {
            wplayer.controls.pause();
        }

        private void mp3_player_resume_Click(object sender, EventArgs e)
        {
            wplayer.controls.play();
            timer1.Enabled = true;

        }

        private void mp3_player_stop_Click(object sender, EventArgs e)
        {
            wplayer.controls.stop();
            timer1.Enabled = false;
            progressBar1.Value = 0;
            trackBar2.Value = 0;
        }

        //使用 winmm.DLL 的 PlaySound() 播放.wav檔 ST
        [System.Runtime.InteropServices.DllImport("winmm.DLL", EntryPoint = "PlaySound", SetLastError = true)]
        private static extern bool PlaySound(string szSound, System.IntPtr hMod, PlaySoundFlags flags);

        [System.Flags]
        public enum PlaySoundFlags : int
        {
            SND_SYNC = 0x0000,
            SND_ASYNC = 0x0001,
            SND_NODEFAULT = 0x0002,
            SND_LOOP = 0x0008,
            SND_NOSTOP = 0x0010,
            SND_NOWAIT = 0x00002000,
            SND_FILENAME = 0x00020000,
            SND_RESOURCE = 0x00040004
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //使用 winmm.DLL 的 PlaySound() 播放.wav檔
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_wav\chimes.wav";

            PlaySound(filename, new System.IntPtr(), PlaySoundFlags.SND_SYNC);
        }
        //使用 winmm.DLL 的 PlaySound() 播放.wav檔 SP


        private void button8_Click(object sender, EventArgs e)
        {
            /// 利用C#來解讀MP3文件的TAG區信息。
            //string mp3_filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";

            // TBD

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //從mp3中提取信息1

            //從mp3中提取信息 1
            //從mp3中提取信息

            string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";

            byte[] b = new byte[128];
            string sTitle;
            string sSinger;
            string sAlbum;
            string sYear;
            string sComm;

            FileStream fs = new FileStream(filename, FileMode.Open);

            fs.Seek(-128, SeekOrigin.End);
            fs.Read(b, 0, 128);

            bool isSet = false;
            String sFlag = System.Text.Encoding.Default.GetString(b, 0, 3);
            if (sFlag.CompareTo("TAG") == 0)
            {
                System.Console.WriteLine("Tag is setted!Replica Watches");
                richTextBox1.Text += "Tag is setted!Replica Watches\n";
                isSet = true;
            }

            if (isSet)
            {
                //http://study.pctoday.net.cn/3_Visual+Studio.aspx

                sTitle = System.Text.Encoding.Default.GetString(b, 3, 30);

                System.Console.WriteLine("标题:" + sTitle);
                richTextBox1.Text += "標題:" + sTitle + "\n";

                //Exclusive Replica Rolex Watches;

                sSinger = System.Text.Encoding.Default.GetString(b, 33, 30);

                System.Console.WriteLine("艺术家:" + sSinger);
                richTextBox1.Text += "藝術家:" + sSinger + "\n";

                //get album;

                sAlbum = System.Text.Encoding.Default.GetString(b, 63, 30);

                System.Console.WriteLine("唱片标题:" + sAlbum);
                richTextBox1.Text += "唱片標題:" + sAlbum + "\n";

                //egacn.com/Watches/Tag-Heuer;

                sYear = System.Text.Encoding.Default.GetString(b, 93, 4);

                System.Console.WriteLine("发行年:" + sYear);
                richTextBox1.Text += "發行年:" + sYear + "\n";

                //watchstylish.com;

                sComm = System.Text.Encoding.Default.GetString(b, 97, 30);

                System.Console.WriteLine("备注:" + sComm);
                richTextBox1.Text += "備註:" + sComm + "\n";

            }
            fs.Close();

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //從mp3中提取信息2

            //從mp3中提取信息 2
            //get mp3 info

            //string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\aaaa.mp3";

            byte[] b = new byte[128];
            string sTitle;
            string sSinger;
            string sAlbum;
            string sYear;
            string sComm;

            FileStream fs = new FileStream(filename, FileMode.Open);

            fs.Seek(-128, SeekOrigin.End);

            fs.Read(b, 0, 128);

            bool isSet = false;

            String sFlag = System.Text.Encoding.Default.GetString(b, 0, 3);

            if (sFlag.CompareTo("TAG") == 0)
            {
                System.Console.WriteLine("Tag is setted!Replica Watches");
                richTextBox1.Text += "Tag is setted!Replica Watches" + "\n";
                isSet = true;
            }

            if (isSet)
            {
                //http://study.pctoday.net.cn/3_Visual+Studio.aspx

                sTitle = System.Text.Encoding.Default.GetString(b, 3, 30);

                System.Console.WriteLine("标题:" + sTitle);
                richTextBox1.Text += "标题:" + sTitle + "\n";

                //Exclusive Replica Rolex Watches;

                sSinger = System.Text.Encoding.Default.GetString(b, 33, 30);

                System.Console.WriteLine("艺术家:" + sSinger);
                richTextBox1.Text += "艺术家:" + sSinger + "\n";

                //get album;

                sAlbum = System.Text.Encoding.Default.GetString(b, 63, 30);

                System.Console.WriteLine("唱片标题:" + sAlbum);
                richTextBox1.Text += "唱片标题:" + sAlbum + "\n";

                //egacn.com/Watches/Tag-Heuer;

                sYear = System.Text.Encoding.Default.GetString(b, 93, 4);

                System.Console.WriteLine("发行年:" + sYear);
                richTextBox1.Text += "发行年:" + sYear + "\n";

                //watchstylish.com;

                sComm = System.Text.Encoding.Default.GetString(b, 97, 30);

                System.Console.WriteLine("备注:" + sComm);
                richTextBox1.Text += "备注:" + sComm + "\n";
            }
            fs.Close();


        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //mp3 info

            string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            Mp3Info mp3 = new Mp3Info(filename);
            string artist = mp3.Artist;
            string album = mp3.Album;
            string title = mp3.Title;

            richTextBox1.Text += "artist : " + artist + "\n";
            richTextBox1.Text += "album : " + album + "\n";
            richTextBox1.Text += "title : " + title + "\n";

        }

        List<string> al = new List<string>(); //當前歌詞時間表
        private void button13_Click(object sender, EventArgs e)
        {
            //從mp3檔名找lrc
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\04-三月雪(&黃妃).mp3";

            string filename_lyrics = Path.Combine(Path.GetDirectoryName(filename), Path.GetFileNameWithoutExtension(filename) + ".lrc");

            richTextBox1.Text += "f1 = " + filename + "\n";
            richTextBox1.Text += "f2 = " + filename_lyrics + "\n";

            if (!File.Exists(filename_lyrics))
            {
                richTextBox1.Text = "無 歌詞檔案\n";
                return;
            }

            using (StreamReader sr = new StreamReader(new FileStream(filename_lyrics, FileMode.Open), Encoding.Default))
            {
                string tempLrc = "";
                while (!sr.EndOfStream)
                {
                    tempLrc = sr.ReadToEnd();
                }

                if (tempLrc.Trim() == "")
                {
                    this.richTextBox1.Text = "歌詞檔案內容為空";
                    return;
                }

                tempLrc = tempLrc.Trim();
                Regex rg = new Regex("\r*\n*\\[ver:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[al:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[by:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[offset:(.*)\\]\r*\n*");
                tempLrc = rg.Replace(tempLrc, "");
                rg = new Regex("\r*\n*\\[ar:(.*)\\]\r*\n*");
                Match mtch;
                mtch = rg.Match(tempLrc);
                tempLrc = rg.Replace(tempLrc, "\n歌手:" + mtch.Groups[1].Value + "\n");
                rg = new Regex("\r*\n*\\[ti:(.+?)\\]\r*\n*");   //這裡注意貪婪匹配問題.+?
                mtch = rg.Match(tempLrc);
                tempLrc = rg.Replace(tempLrc, "\n歌名:" + mtch.Groups[1].Value + "\n");
                rg = new Regex("\r*\n*\\[[0-9][0-9]:[0-9][0-9].[0-9][0-9]\\]");
                MatchCollection mc = rg.Matches(tempLrc);
                al.Clear();

                foreach (Match m in mc)
                {
                    string temp = m.Groups[0].Value;
                    //this.Text += temp + "+";                        
                    string mi = temp.Substring(temp.IndexOf('[') + 1, 2);
                    string se = temp.Substring(temp.IndexOf(':') + 1, 2);
                    string ms = temp.Substring(temp.IndexOf('.') + 1, 2);   //這是毫秒，其實我只精確到秒，毫秒後面並沒有用
                    //this.Text += mi + ":" + se + "+";
                    string time = Convert.ToInt32(mi) * 60 + Convert.ToInt32(se) + "";  //這裡並沒有新增毫秒
                    al.Add(time);
                }

                tempLrc = rg.Replace(tempLrc, "\n");
                char[] remove = { '\r', '\n', ' ' };
                this.richTextBox1.Text = tempLrc.TrimStart(remove);
                this.timer1.Interval = 1000;
                this.timer1.Tick += ShowLineLrc;
                this.timer1.Start();
            }

            int len = al.Count;
            richTextBox1.Text = "len = " + len.ToString() + "\n";
        }

        int position = 0;
        /// <summary>
        /// 定時器執行的方法，每隔1秒執行一次  歌詞逐行顯示
        private void ShowLineLrc(object sender, EventArgs e)
        {
            //int pos = al.IndexOf(trackBarValue.ToString());
            position++;
            int pos = position;
            bool isAr = this.richTextBox1.Text.Contains("歌手:");
            bool isTi = this.richTextBox1.Text.Contains("歌名:");


            if ((pos >= 0) && (pos < 25))
            {
                int n = isAr ? 1 : 0;
                int m = isTi ? 1 : 0;

                int height = 28 * (this.al.Count + m + n);
                int max = height - this.richTextBox1.Height;


                this.richTextBox1.SelectAll();
                this.richTextBox1.SelectionColor = Color.Black;
                this.richTextBox1.SelectionLength = 0;/**/

                int l = this.richTextBox1.Lines[pos + m + n].Length;
                this.richTextBox1.Select(this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n), l);
                this.richTextBox1.SelectionColor = Color.OrangeRed;
                this.richTextBox1.SelectionLength = 0;
                //this.Text = GetScrollPos(this.richTextBox1.Handle, SB_VERT).ToString() + "-" + al.Count + "-" + this.richTextBox1.Height;

                if ((pos + m + n) * 28 <= max)
                {
                    int start = this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n);
                    this.richTextBox1.SelectionStart = start;
                    this.richTextBox1.ScrollToCaret();

                }
                else
                {
                    /*
                    //this.richTextBox1.Focus();
                    SendMessage(this.richTextBox1.Handle, WM_VSCROLL, SB_BOTTOM, 0);
                    UpdateWindow(this.richTextBox1.Handle);
                    //this.richTextBox1.SelectionStart = this.richTextBox1.Text.Length;
                    //this.richTextBox1.ScrollToCaret();
                    */
                }

                /*
                if (this.lrcForm != null)
                {
                    string l1 = this.richTextBox1.Lines[pos + m + n];
                    string l2;
                    if ((pos + m + n) < this.richTextBox1.Lines.Length - 1)
                    {
                        l2 = this.richTextBox1.Lines[pos + m + n + 1];
                    }
                    else
                    {
                        l2 = "。。。。。";
                    }

                    this.lrcForm.setLrc(l1, l2, pos);
                    //this.lrcForm.setLrc(ArrayList al,);

                }
                */
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //月亮代表我的心1

            //racket 定义节拍
            const int one = 600;//一拍
            const int half = 300;//半拍
            const int four_one = 150;//1/4拍
            const int onedot = 450;//附点音符
            ////note   定义音符
            //const int mnote1 = 440;//do
            //const int mnote2 = 495;//re
            //const int mnote3 = 550;//mi
            //const int mnote4 = 587;//fa
            //const int mnote5 = 660;//so
            //const int mnote6 = 733;//la
            //const int mnote7 = 825;//si

            //const int lnote5 = 325;

            #region
            //low note   低音区
            const int lnote1 = 262;
            const int lnote2 = 294;
            const int lnote3 = 330;
            const int lnote4 = 349;
            const int lnote5 = 392;
            const int lnote6 = 440;
            const int lnote7 = 494;
            //mid note   中音区
            const int mnote1 = 523;
            const int mnote2 = 578;
            const int mnote3 = 659;
            const int mnote4 = 698;
            const int mnote5 = 784;
            const int mnote6 = 880;
            const int mnote7 = 988;
            //hight note   高音区
            const int hnote1 = 1046;
            const int hnote2 = 1175;
            const int hnote3 = 1318;
            const int hnote4 = 1397;
            const int hnote5 = 1568;
            const int hnote6 = 1760;
            const int hnote7 = 1976;
            #endregion

            //月亮代表我的心
            Console.Beep(lnote5, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote3, half);
            Console.Beep(mnote5, onedot);
            Console.Beep(mnote1, half);

            Console.Beep(lnote7, onedot);
            Console.Beep(mnote3, half);
            Console.Beep(mnote5, onedot);
            Console.Beep(mnote5, half);


            Console.Beep(mnote6, onedot);
            Console.Beep(mnote7, half);
            Console.Beep(hnote1, onedot);
            Console.Beep(mnote6, half);

            Console.Beep(mnote5, one);
            System.Threading.Thread.Sleep(one);
            System.Threading.Thread.Sleep(one);
            Console.Beep(mnote3, half);
            Console.Beep(mnote2, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, one);
            Console.Beep(mnote3, half);
            Console.Beep(mnote2, half);

            Console.Beep(mnote1, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, half);
            Console.Beep(mnote1, one);
            Console.Beep(mnote2, half);
            Console.Beep(mnote3, half);


            Console.Beep(mnote2, onedot);
            Console.Beep(mnote1, half);
            Console.Beep(lnote6, one);
            Console.Beep(mnote2, half);
            Console.Beep(mnote3, half);

            Console.Beep(mnote2, one);
            
            


        }

        private void button15_Click(object sender, EventArgs e)
        {
            //月亮代表我的心2

        }

        private void button16_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_wav\chimes.wav";

            SoundPlayer sp = new SoundPlayer();
            sp.SoundLocation = filename;
            //sp.PlayLooping();   //沒效~~~
            sp.Play(); // 撥放

            //sp.Stop(); // 停止

            /*  ok
            //簡易播放wav的方法，僅可播放wav，不可播放mp3
            filename = @"C:\_git\vcs\_1.data\______test_files1\_wav\WindowsShutdown.wav";
            SoundPlayer sp = new SoundPlayer(filename);
            sp.Play();
            */
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

        private void button20_Click(object sender, EventArgs e)
        {

        }
    }

    public class clsMP3TAG
    {
        private byte[] TAGBody = new byte[128];

        private byte[] sTag = new byte[3];
        private byte[] sTitle = new byte[30];
        private byte[] sArtist = new byte[30];
        private byte[] sAlbum = new byte[30];
        private byte[] sYear = new byte[4];
        private byte[] sComment = new byte[30];
        private byte[] sGenre = new byte[1];

        System.Exception myException;

        public clsMP3TAG(byte[] TAG)
        {
            if (TAG.Length != 128)
            {
                myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG長度應該是 128 Byte。");
                throw (myException);
            }
            else
            {
                Array.Copy(TAG, 0, sTag, 0, 3);
                if (!Encoding.Default.GetString(sTag).Equals("TAG"))
                {
                    myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG位校驗出錯。");
                    throw (myException);
                }

                Array.Copy(TAG, 3, sTitle, 0, 30);
                Array.Copy(TAG, 33, sArtist, 0, 30);
                Array.Copy(TAG, 63, sAlbum, 0, 30);
                Array.Copy(TAG, 93, sYear, 0, 4);
                Array.Copy(TAG, 97, sComment, 0, 30);
                Array.Copy(TAG, 127, sGenre, 0, 1);


            }
        }

        /**/
        //////////////////////////////////////////////////////
        /// 以下是屬性，只讀
        //////////////////////////////////////////////////////
        public string Title
        {
            get
            {
                return Encoding.Default.GetString(sTitle);
            }
        }

        public string Artist
        {
            get
            {
                return Encoding.Default.GetString(sArtist);
            }
        }

        public string Album
        {
            get
            {
                return Encoding.Default.GetString(sAlbum);
            }
        }

        public string Year
        {
            get
            {
                return Encoding.Default.GetString(sYear);
            }
        }

        public string Comment
        {
            get
            {
                return Encoding.Default.GetString(sComment);
            }
        }

        public string Genre
        {
            get
            {
                switch (Convert.ToInt16(sGenre[0]))
                {
                    case 0: return "Blues";
                    case 20: return "Alternative";
                    case 40: return "AlternRock";
                    case 60: return "Top 40";
                    case 1: return "Classic Rock";
                    case 21: return "Ska";
                    case 41: return "Bass";
                    case 61: return "Christian Rap";
                    case 2: return "Country";
                    case 22: return "Death Metal";
                    case 42: return "Soul";
                    case 62: return "Pop/Funk";
                    case 3: return "Dance";
                    case 23: return "Pranks";
                    case 43: return "Punk";
                    case 63: return "Jungle";
                    case 4: return "Disco";
                    case 24: return "Soundtrack";
                    case 44: return "Space";
                    case 64: return "Native American";
                    case 5: return "Funk";
                    case 25: return "Euro-Techno";
                    case 45: return "Meditative";
                    case 65: return "Cabaret";
                    case 6: return "Grunge";
                    case 26: return "AmbIEnt";
                    case 46: return "Instrumental Pop";
                    case 66: return "New Wave";
                    case 7: return "Hip-Hop";
                    case 27: return "Trip-Hop";
                    case 47: return "Instrumental Rock";
                    case 67: return "Psychadelic";
                    case 8: return "Jazz";
                    case 28: return "Vocal";
                    case 48: return "Ethnic";
                    case 68: return "Rave";
                    case 9: return "Metal";
                    case 29: return "Jazz+Funk";
                    case 49: return "Gothic";
                    case 69: return "Showtunes";
                    case 10: return "New Age";
                    case 30: return "Fusion";
                    case 50: return "Darkwave";
                    case 70: return "Trailer";
                    case 11: return "OldIEs";
                    case 31: return "Trance";
                    case 51: return "Techno-Industrial";
                    case 71: return "Lo-Fi";
                    case 12: return "Other";
                    case 32: return "Classical";
                    case 52: return "Electronic";
                    case 72: return "Tribal";
                    case 13: return "Pop";
                    case 33: return "Instrumental";
                    case 53: return "Pop-Folk";
                    case 73: return "Acid Punk";
                    case 14: return "R&B";
                    case 34: return "Acid";
                    case 54: return "Eurodance";
                    case 74: return "Acid Jazz";
                    case 15: return "Rap";
                    case 35: return "House";
                    case 55: return "Dream";
                    case 75: return "Polka";
                    case 16: return "Reggae";
                    case 36: return "Game";
                    case 56: return "Southern Rock";
                    case 76: return "Retro";
                    case 17: return "Rock";
                    case 37: return "Sound Clip";
                    case 57: return "Comedy";
                    case 77: return "Musical";
                    case 18: return "Techno";
                    case 38: return "Gospel";
                    case 58: return "Cult";
                    case 78: return "Rock & Roll";
                    case 19: return "Industrial";
                    case 39: return "Noise";
                    case 59: return "Gangsta";
                    case 79: return "Hard Rock";


                    default:
                        return "未知類型";
                }
            }
        }
    }

    struct Mp3Info
    {
        public string Title;  //歌曲名,30个字节     3-62 
        public string Artist; //歌手名,30个字节     33-62
        public string Album;  //专辑名,30个字节     63-92
        //public string Year;//年,4个字符     
        //public string Comment;//注释,28个字节      
        //public char reserved1;//保留位，一个字节        
        //public char reserved2;//保留位，一个字节        
        //public char reserved3;//保留位，一个字节  

        public Mp3Info(string fileName)
        {
            FileStream fs = new FileStream(fileName, FileMode.Open, FileAccess.Read);
            fs.Seek(-128, SeekOrigin.End);
            byte[] Info = new byte[128];
            int length = fs.Read(Info, 0, 128);
            fs.Close();

            Title = Encoding.Default.GetString(Info, 3, 30).Replace("\0", string.Empty);
            Artist = Encoding.Default.GetString(Info, 33, 30).Replace("\0", string.Empty);
            Album = Encoding.Default.GetString(Info, 63, 30).Replace("\0", string.Empty);
        }
    }
}


