using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory
using WMPLib;       //for IWMPPlaylist IWMPMedia

namespace vcs_axWindowsMediaPlayer2_new
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

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
            dx = 165;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }


        private void bt_clear_Click(object sender, EventArgs e)
        {

        }




        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }


        public class MyFileInfo
        {
            public string filename;
            public string filepath;
            public string fileextension;
            public long filesize;
            public DateTime filecreationtime;

            public MyFileInfo(string n, string p, string e, long s, DateTime c)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;
            }
        }

        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

        string FolederName;
        Int64 total_size = 0;
        Int64 total_files = 0;

        Int64 folder_size = 0;
        Int64 folder_files = 0;


        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            try
            {
                string[] fileEntries = Directory.GetFiles(targetDirectory);
                Array.Sort(fileEntries);
                folder_size = 0;
                folder_files = 0;
                foreach (string fileName in fileEntries)
                {
                    ProcessFile(fileName);
                }
                //richTextBox1.Text += "folder_name = " + targetDirectory + "\n";
                //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
                //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
                if (folder_files == 0)
                {
                    //richTextBox1.Text += "空資料夾 folder_name = " + targetDirectory + "\n";
                }


                // Recurse into subdirectories of this directory.
                string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                Array.Sort(subdirectoryEntries);
                foreach (string subdirectory in subdirectoryEntries)
                {
                    DirectoryInfo di = new DirectoryInfo(subdirectory);
                    FolederName = subdirectory;
                    ProcessDirectory(subdirectory);
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
            }

            /*
            richTextBox1.Text += "資料夾 " + targetDirectory + "\t檔案個數 : " + folder_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(folder_size)) + "\n";
            richTextBox1.Text += "\n";
            */
        }

        // Insert logic for processing found files here.
        public void ProcessFile(string path)
        {
            //richTextBox1.Text += path + "\n";

            FileInfo fi;

            try
            {   //可能會產生錯誤的程式區段
                fi = new FileInfo(path);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "錯誤訊息1 : " + ex.Message + "\n";
                return;
            }
            finally
            {
                //一定會被執行的程式區段
            }

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

            fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
        }



        private void button0_Click(object sender, EventArgs e)
        {
            fileinfos.Clear();

            string path = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\";

            richTextBox1.Text += "\n搜尋路徑" + path + "\n";

            if (File.Exists(path))
            {
                //給定的路徑是一個檔案
                ProcessFile(path);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(path))
            {
                //給定的路徑是一個資料夾
                FolederName = path;
                ProcessDirectory(path);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案\n";
            }


            richTextBox1.Text += "\n\n\n";


            richTextBox1.Text += "fileinfos len = " + fileinfos.Count.ToString() + "\n";

            richTextBox1.Text += "total_size = " + total_size.ToString() + "\n";
            richTextBox1.Text += "total_files = " + total_files.ToString() + "\n";
            //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
            //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";

            int i;
            int len = fileinfos.Count;


            richTextBox1.Text += "照檔名排序:\n";
            for (i = 0; i < 20; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";

            }

            /*
            richTextBox1.Text += "照大小排序(由大到小):\n";

            //排序 由大到小  在return的地方多個負號
            fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            for (i = 0; i < 20; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";
            }

            richTextBox1.Text += "照大小排序(由小到大):\n";

            //排序 由小到大
            fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            for (i = 0; i < 20; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";
            }
            */

            //fileinfos[i].filename + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";

            //播放單一檔案
            //axWindowsMediaPlayer1.URL = fileinfos[0].filepath + "\\" + fileinfos[0].filename;   //開啟檔案

            //一次加入到播放清單
            axWindowsMediaPlayer1.currentPlaylist = axWindowsMediaPlayer1.newPlaylist("播放列表", "");

            for (i = 0; i < 20; i++)
            {
                axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(fileinfos[i].filepath + "\\" + fileinfos[i].filename));
                richTextBox1.Text += "加入播放清單: " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";
            }
            //foreach (string fn in ofd.FileNames)
            {
                //axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(fn));
                //richTextBox1.Text += "加入播放清單: " + fn + "\n";
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.settings.setMode("loop", true);   //循環播放
            axWindowsMediaPlayer1.Ctlcontrols.play();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int len;
            len = axWindowsMediaPlayer1.currentPlaylist.count;
            richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }

            //清除播放清單內所有資料
            //axWindowsMediaPlayer1.currentPlaylist.clear();
            //richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";

            richTextBox1.Text += "改變檔案位置\n";
            axWindowsMediaPlayer1.currentPlaylist.moveItem(3, 5);

            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].name + "\t";
                richTextBox1.Text += axWindowsMediaPlayer1.currentPlaylist.Item[i].sourceURL + "\n";
            }

            //移除檔案
            //axWindowsMediaPlayer1.currentPlaylist.removeItem(fileinfos[4].filepath + "\\" + fileinfos[4].filename);


            //state if (axWindowsMediaPlayer1.playState == WMPPlayState.wmppsMediaEnded)
            richTextBox1.Text += "state = " + axWindowsMediaPlayer1.playState.ToString() + "\n";

        }

        IWMPPlaylist playlist;
        IWMPMedia media;

        private void button3_Click(object sender, EventArgs e)
        {
            //建立播放清單

            playlist = axWindowsMediaPlayer1.playlistCollection.newPlaylist("myplaylist");

            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\06.紅燈青燈.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\04.行船人的純情曲.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\07.為錢賭生命.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\08.看破愛別人.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\09.戀歌.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\10.悲戀的酒杯.mp3");
            playlist.appendItem(media);
            media = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\11.一卡手指.mp3");
            playlist.appendItem(media);

            axWindowsMediaPlayer1.currentPlaylist = playlist;
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;

            richTextBox1.Text += "移除播放清單\n";
            axWindowsMediaPlayer1.playlistCollection.remove(playlist);
            playlist = null;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;
            int len = playlist.count;
            richTextBox1.Text += "目前播放清單內有 : " + len.ToString() + " 首歌\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += playlist.Item[i].sourceURL + "\n";
            }

            richTextBox1.Text += "改變檔案位置\n";
            playlist.moveItem(3, 5);


        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (playlist == null)
                return;

            /*      無法直接從播放清單內移除某項
            IWMPMedia to_remove;
            to_remove = axWindowsMediaPlayer1.newMedia(@"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\_陳一郎_台語精選集6CD\disc1\07.為錢賭生命.mp3");

            playlist.removeItem(to_remove);
            */

        }

        private void button7_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

    }
}
