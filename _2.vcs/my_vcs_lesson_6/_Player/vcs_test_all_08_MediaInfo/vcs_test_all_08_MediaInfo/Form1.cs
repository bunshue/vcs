using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using MediaInfoNET;

using System.Globalization; //for CultureInfo

namespace vcs_test_all_08_MediaInfo
{
    public partial class Form1 : Form
    {
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
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            richTextBox1.Size = new Size(800, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1050, 750);
            this.Text = "vcs_test_all_08_MediaInfo";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void get_MediaInfo(string filename)
        {
            MediaFile f = new MediaFile(filename);

            if (f.InfoAvailable == true)
            {
                richTextBox1.Text += "有MediaInfo資料, 全部資料:\n" + f.Info_Text + "\n\n";

                richTextBox1.Text += "有MediaInfo資料, 分項資料:\n";
                richTextBox1.Text += "File : " + f.File + "\n";
                richTextBox1.Text += "Name : " + f.Name + "\n";
                richTextBox1.Text += "Title : " + f.Title + "\n";
                richTextBox1.Text += "FileSize : " + f.FileSize.ToString() + " Bytes\n";
                richTextBox1.Text += "FrameCount : " + f.FrameCount.ToString() + "\n";
                richTextBox1.Text += "StreamCount : " + f.StreamCount.ToString() + "\n";
                richTextBox1.Text += "ParentFolder : " + f.ParentFolder + "\n";
                richTextBox1.Text += "Extension : " + f.Extension + "\n";
                richTextBox1.Text += "Description : \n" + f.Description + "\n";
                richTextBox1.Text += "Capacity : " + f.Text.Capacity.ToString() + "\n";

                //General
                richTextBox1.Text += "Format : " + f.General.Format + "\n";
                richTextBox1.Text += "Bitrate : " + f.General.Bitrate.ToString() + "\n";
                richTextBox1.Text += "CodecID : " + f.General.CodecID + "\n";
                richTextBox1.Text += "Description : " + f.General.Description + "\n";
                richTextBox1.Text += "DurationMillis : " + f.General.DurationMillis.ToString() + "\n";
                richTextBox1.Text += "DurationString : " + f.General.DurationString + "\n";
                richTextBox1.Text += "DurationStringAccurate : " + f.General.DurationStringAccurate + "\n";
                richTextBox1.Text += "Extension : " + f.General.Extension + "\n";
                richTextBox1.Text += "Format : " + f.General.Format + "\n";
                richTextBox1.Text += "FormatID : " + f.General.FormatID + "\n";
                richTextBox1.Text += "ID : " + f.General.ID.ToString() + "\n";
                richTextBox1.Text += "StreamSize : " + f.General.StreamSize.ToString() + "\n";
                richTextBox1.Text += "StreamType : " + f.General.StreamType + "\n";

                richTextBox1.Text += "\n";
                richTextBox1.Text += "Audio Count: " + f.Audio.Count.ToString() + "\n";
                richTextBox1.Text += "Video Count: " + f.Video.Count.ToString() + "\n";
                richTextBox1.Text += "\n";

                if (f.Audio.Count > 0)
                {
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Audio ---------------------------------" + "\n";
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Format : " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "Bitrate : " + f.Audio[0].Bitrate.ToString() + "\n";
                    richTextBox1.Text += "Channels : " + f.Audio[0].Channels.ToString() + "\n";
                    richTextBox1.Text += "Sampling : " + f.Audio[0].SamplingRate.ToString() + "\n";

                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "[音訊資訊]\n";
                    richTextBox1.Text += "  音訊編碼: " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "  取樣率: " + f.Audio[0].SamplingRate.ToString() + "\n";
                    richTextBox1.Text += "  聲道數: " + f.Audio[0].Channels.ToString() + "\n";
                    richTextBox1.Text += "  Bitrate: " + f.Audio[0].Bitrate.ToString() + " kbps\n";

                    /*
                    richTextBox1.Text += "CodecID : " + f.Audio[0].CodecID + "\n";
                    richTextBox1.Text += "Description : " + f.Audio[0].Description + "\n";
                    richTextBox1.Text += "DurationString : " + f.Audio[0].DurationString + "\n";
                    richTextBox1.Text += "Format : " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "FormatID : " + f.Audio[0].FormatID + "\n";
                    richTextBox1.Text += "ID : " + f.Audio[0].ID + "\n";
                    richTextBox1.Text += "MPlayerID : " + f.Audio[0].MPlayerID + "\n";
                    richTextBox1.Text += "StreamSize : " + f.Audio[0].StreamSize + "\n";
                    richTextBox1.Text += "StreamType : " + f.Audio[0].StreamType + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "\n無MediaInfo Audio資料\n";
                }

                if (f.Video.Count > 0)
                {
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Video ---------------------------------" + "\n";
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Format : " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "Bit rate : " + f.Video[0].Bitrate.ToString() + "\n";
                    richTextBox1.Text += "Frame rate : " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "Frame size : " + f.Video[0].FrameSize.ToString() + "\n";

                    richTextBox1.Text += "\n";
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;

                    richTextBox1.Text += "[視訊資訊]\n";
                    richTextBox1.Text += "  視訊編碼: " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "  輸入格式: " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "  Bitrate: " + f.Video[0].Bitrate.ToString() + " kbps\n";

                    /*
                    richTextBox1.Text += "Format : " + f.General.Format.ToString() + "\n";
                    richTextBox1.Text += "W : " + f.Video[0].Width.ToString() + "\n";
                    richTextBox1.Text += "H : " + f.Video[0].Height.ToString() + "\n";
                    richTextBox1.Text += "時間 : " + f.Video[0].DurationString + "\n";

                    richTextBox1.Text += "Description : " + f.Video[0].Description + "\n";
                    richTextBox1.Text += "Format : " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "FrameRate : " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "FrameSize : " + f.Video[0].FrameSize.ToString() + "\n";
                    richTextBox1.Text += "MPlayerID : " + f.Video[0].MPlayerID.ToString() + "\n";
                    richTextBox1.Text += "PixelFormat : " + f.Video[0].PixelFormat + "\n";
                    richTextBox1.Text += "Resolution : " + f.Video[0].Resolution.ToString() + "\n";
                    richTextBox1.Text += "StreamSize : " + f.Video[0].StreamSize.ToString() + "\n";
                    richTextBox1.Text += "StreamType : " + f.Video[0].StreamType + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "\n無MediaInfo Video資料\n";
                }
            }
            else
            {
                richTextBox1.Text += "無MediaInfo資料\n";
            }

            //Info
            if (f.MediaInfo_Available == true)
            {
                richTextBox1.Text += "有MediaInfo資料, 全部資料:\n" + f.MediaInfo_Text + "\n";
            }
            else
            {
                richTextBox1.Text += "無MediaInfo資料\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //MediaFile

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_video\鹿港.mp4";

            MediaFile f = new MediaFile(filename);
            richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
            richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
            richTextBox1.Text += "  Extension: " + f.Extension + "\n";

            FileInfo fi = new FileInfo(filename);

            richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
            richTextBox1.Text += fi.Directory + "\n";
            richTextBox1.Text += fi.DirectoryName + "\n";

            if ((f.InfoAvailable == true) && (f.Video.Count > 0))
            {
                int w = f.Video[0].Width;
                int h = f.Video[0].Height;
                richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                string items = string.Empty;
                string item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                if (h >= 1080)
                    items = "大";
                else if (h <= 480)
                    items = "小";
                else
                    items = "中";
            }
            else
            {
                richTextBox1.Text += "非影片\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            richTextBox1.Text += "檔案名稱: " + filename + "\n";
            get_MediaInfo(filename);
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\_mp3";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n\n";
                foreach (var filename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "檔名:\t" + filename + "\n";
                    get_MediaInfo(filename);
                }
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //MediaFile new

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_video\鹿港.mp4";

            MediaFile f = new MediaFile(filename);
            FileInfo fi = new FileInfo(filename);

            if ((f.InfoAvailable == true) && (f.Video.Count > 0))
            {
                int w = f.Video[0].Width;
                int h = f.Video[0].Height;

                richTextBox1.Text += "影片檔案\t" + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\t";
                richTextBox1.Text += f.Video[0].FrameRate.ToString() + "\t";
                richTextBox1.Text += f.General.DurationString + "\n";

                richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                richTextBox1.Text += "影片\t";
                richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            }
            else
            {
                richTextBox1.Text += "非 影片檔案\n";
                richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            }

            //MediaFile f = new MediaFile(filename);
            richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
            richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
            richTextBox1.Text += "  Extension: " + f.Extension + "\n";
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個



        //以下的沒用到

        void show_file_info()  //轉出一層
        {
            richTextBox1.Text += "show_file_info show_file_info show_file_info\n";
            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            int i;
            for (i = 0; i < 10; i++)
            {
                //richTextBox1.Text += fileinfos[i].filename + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                string filename = @"D:\_git\vcs\_1.data\______test_files1\_video\鹿港.mp4";
                MediaFile f = new MediaFile(filename);

                //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    //richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    //richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                    /*
                    if (((cb_video_l.Checked == true) && (h >= 1080)) || ((cb_video_m.Checked == true) && (h < 1080) && (h > 480)) || ((cb_video_s.Checked == true) && (h <= 480)))
                    {
                        item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        if (h >= 1080)
                            items = "大";
                        else if (h <= 480)
                            items = "小";
                        else
                            items = "中";
                        itema = fileinfos[i].filename;
                        itemb = fileinfos[i].filepath;
                        itemc = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                        //i1 = new ListViewItem(fileinfos[i].filename);
                        i1 = new ListViewItem(item);
                        i1.UseItemStyleForSubItems = false;

                        //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                        sub_i1s.Text = items;
                        i1.SubItems.Add(sub_i1s);

                        sub_i1a.Text = itema;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fileinfos[i].filepath;
                        //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        sub_i1b.Text = itemb;
                        i1.SubItems.Add(sub_i1b);

                        //sub_i1a.Text = fi.Length.ToString();
                        //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        sub_i1c.Text = itemc;
                        i1.SubItems.Add(sub_i1c);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;
                        sub_i1c.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1c.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    }
                    else
                        continue;
                    */
                }
                else
                {
                    /*
                    if (cb_video_only.Checked == true)
                        continue;

                    if (cb_generate_text.Checked == false)
                        continue;

                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                    //richTextBox1.Text += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    */
                }
            }
        }

        void show_file_info1()  //轉出一層
        {
            /*
            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }
            */

            for (int i = 0; i < 5; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                ListViewItem.ListViewSubItem sub_i1s = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                string item = string.Empty;
                string items = string.Empty;
                string itema = string.Empty;
                string itemb = string.Empty;
                string itemc = string.Empty;

                ListViewItem i1;

                //debug mesg
                //richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                string filename = @"D:\_git\vcs\_1.data\______test_files1\_video\鹿港.mp4";
                MediaFile f = new MediaFile(filename);

                //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    //richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    //richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                    //if (((cb_video_l.Checked == true) && (h >= 1080)))
                    {
                        item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        if (h >= 1080)
                            items = "大";
                        else if (h <= 480)
                            items = "小";
                        else
                            items = "中";

                        //itemc = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                        //i1 = new ListViewItem(fileinfos[i].filename);
                        i1 = new ListViewItem(item);
                        i1.UseItemStyleForSubItems = false;

                        //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                        sub_i1s.Text = items;
                        i1.SubItems.Add(sub_i1s);

                        sub_i1a.Text = itema;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fileinfos[i].filepath;
                        //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        sub_i1b.Text = itemb;
                        i1.SubItems.Add(sub_i1b);

                        //sub_i1a.Text = fi.Length.ToString();
                        //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        sub_i1c.Text = itemc;
                        i1.SubItems.Add(sub_i1c);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;
                        sub_i1c.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1c.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                    }
                }
                else
                {

                    //richTextBox1.Text += ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                    //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                }
                /*
                else
                {
                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                }
                */
            }
        }

        /*
        richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
        richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
        */

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

