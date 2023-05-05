using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using MediaInfoNET;

using System.Globalization; //for CultureInfo

namespace vcs_test_all_08_MediaInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

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

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            richTextBox1.Text += "檔案名稱: " + filename + "\n";
            get_MediaInfo(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
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
            //openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\_mp3";  //預設開啟的路徑
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
    }
}

