using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path
using System.Diagnostics;   //for Process
using System.Text.RegularExpressions;

//參考/加入參考 /COM/Microsoft Shell Controls and Automation
using Shell32;  //for Shell

using AxWMPLib;

namespace vcs_FFMPEG
{
    public partial class Form1 : Form
    {
        string ffmpeg = @"C:\______test_files\_exe\ffmpeg\ffmpeg.exe";
        AxWindowsMediaPlayer axWindowsMediaPlayer1;
        int flag_play_mode = 0;    //0: stop, 1: play, 2:  pause
        int mp3_position = 0;
        string mp3_filename = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            lb_total.Text = "全長 : ";
            lb_st.Text = "起始 : ";
            lb_sp.Text = "結束 : ";
            lb_cut.Text = "選取 : ";
            trackBar_st.Maximum = 100;
            trackBar_st.Minimum = 0;
            trackBar_st.Value = 0;

            trackBar_sp.Maximum = 100;
            trackBar_sp.Minimum = 0;
            trackBar_sp.Value = 100;

            this.axWindowsMediaPlayer1 = new AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            this.Controls.Add(this.axWindowsMediaPlayer1);
            axWindowsMediaPlayer1.Visible = false;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 30;
            dx = 160;
            dy = 70;

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //音頻轉換與音頻切割


            //音频转换
            //string fromMusic = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            string fromMusic = @"C:\______test_files\_wav\WindowsShutdown.wav";
            string toMusic = @"aaaaa.wav";

            int bitrate = 12 * 1000;//恒定码率
            int Hz = 3000;//采样频率  

            try
            {
                ExcuteProcess(ffmpeg, "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + fromMusic + "\" \"" + toMusic + "\"");

                richTextBox1.Text += "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + fromMusic + "\" \"" + toMusic + "\"";
                richTextBox1.Text += "轉換完成\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }

            //音頻切割
            string mp3_filename = @"C:\______test_files\_wav\harumi99.wav";
            string mp3_cut_filename = Application.StartupPath + "\\cut_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

            string startTime = "0:0:30";
            string cutTime = "0:0:30";

            try
            {
                //-y : 強制覆蓋檔案
                //-i : 要擷取的原始檔案
                //-ss : 起始時間
                //-t : 擷取長度, -t sec 或 -t hh:mm:ss
                //-acodec copy : 音訊編碼格式和來源檔案相同
                //-vcodec copy : 影像編碼格式和來源檔案相同
                string command_arg = "-y -i \"" + mp3_filename + "\" -ss " + startTime + " -t " + cutTime + " -acodec copy \"" + mp3_cut_filename + "\"";

                ExcuteProcess(ffmpeg, command_arg);

                richTextBox1.Text += "命令 : " + ffmpeg + "\n";
                richTextBox1.Text += "參數 : " + command_arg + "\n";
                richTextBox1.Text += "已切割完成\t檔案 : " + mp3_cut_filename + "\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        /// <summary>
        /// 转换函数
        /// </summary>
        /// <param name="exe">ffmpeg程序</param>
        /// <param name="arg">执行参数</param>
        public static void ExcuteProcess(string exe, string arg)
        {
            using (var p = new Process())
            {
                p.StartInfo.FileName = exe;
                p.StartInfo.Arguments = arg;
                p.StartInfo.UseShellExecute = false;    //输出信息重定向  
                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.RedirectStandardOutput = true;
                p.Start();                    //启动线程  
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();
                p.WaitForExit();//等待进程结束                                        
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得mp3音樂長度

            richTextBox1.Text += "取得音樂檔案長度 :\n";

            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "音樂長度 : ";
            string[] result = GetMP3Time(filename);
            foreach (string str in result)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
        }


        /// <summary>  
        /// 获得音乐长度  
        /// </summary>  
        /// <param name="filePath">文件的完整路径</param>
        public static string[] GetMP3Time(string filePath)
        {
            string dirName = Path.GetDirectoryName(filePath);
            string SongName = Path.GetFileName(filePath);//获得歌曲名称             
            Shell sh = new Shell();
            //ShellClass sh = new ShellClass();  or
            Folder dir = sh.NameSpace(dirName);
            FolderItem item = dir.ParseName(SongName);
            string SongTime = dir.GetDetailsOf(item, 27);//27为获得歌曲持续时间 ，28为获得音乐速率，1为获得音乐文件大小      
            string[] time = Regex.Split(SongTime, ":");
            return time;

        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            //取得mp3音樂長度

            richTextBox1.Text += "取得音樂檔案長度 :\n";

            string filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_日本演歌\__石川さゆり\Ishikawa Sayuri 【アルバム】[演歌] 石川さゆり ‐ 全曲集 Super Best.mp3";
            //string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "音樂長度 : ";
            string[] result = GetMP3Time(filename);
            foreach (string str in result)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
            int total_length = 0;

            total_length = int.Parse(result[0]) * 60 * 60 + int.Parse(result[1]) * 60 + int.Parse(result[2]);
            lb_total.Text = "全長 : " + (total_length / 3600).ToString("D2") + " : " + ((total_length / 60) % 60).ToString("D2") + " : " + (total_length % 60).ToString("D2") + "    " + total_length.ToString();
            richTextBox1.Text += "total_length = " + total_length.ToString() + "\n";

            trackBar_st.Maximum = total_length;
            trackBar_st.Minimum = 0;
            trackBar_st.Value = 0;

            trackBar_sp.Maximum = total_length;
            trackBar_sp.Minimum = 0;
            trackBar_sp.Value = total_length;

            axWindowsMediaPlayer1.URL = filename;

            axWindowsMediaPlayer1.Ctlcontrols.stop();
            mp3_position = 0;
            mp3_filename = filename;

            lb_st.Text = "起始 : " + (mp3_position / 3600).ToString("D2") + " : " + ((mp3_position / 60) % 60).ToString("D2") + " : " + (mp3_position % 60).ToString("D2") + "    " + mp3_position.ToString();
            lb_sp.Text = "結束 : " + (total_length / 3600).ToString("D2") + " : " + ((total_length / 60) % 60).ToString("D2") + " : " + (total_length % 60).ToString("D2") + "    " + total_length.ToString();

            int cut = trackBar_sp.Value - trackBar_st.Value;
            lb_cut.Text = "選取 : " + (cut / 3600).ToString("D2") + " : " + ((cut / 60) % 60).ToString("D2") + " : " + (cut % 60).ToString("D2") + "    " + cut.ToString();
        }

        private void bt_save_file_Click(object sender, EventArgs e)
        {
            if (File.Exists(mp3_filename) == false)
            {
                richTextBox1.Text += "未開啟檔案, 離開\n";
                return;
            }

            int cut1 = trackBar_st.Value;
            int cut2 = trackBar_sp.Value;
            int cut_time = 0;

            if (cut1 >= cut2)
            {
                richTextBox1.Text += "擷取範圍不合理, 離開\n";
                return;
            }

            cut_time = cut2 - cut1;
            richTextBox1.Text += "擷取範圍 : " + cut1.ToString() + " 到 " + cut2.ToString() + "\t共 " + cut_time.ToString() + " 秒\n";

            //音頻切割
            string mp3_cut_filename = Application.StartupPath + "\\cut_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".mp3";
            string startTime = (cut1 / 3600).ToString("D2") + ":" + ((cut1 / 60) % 60).ToString("D2") + ":" + (cut1 % 60).ToString("D2");
            string cutTime = (cut_time / 3600).ToString("D2") + ":" + ((cut_time / 60) % 60).ToString("D2") + ":" + (cut_time % 60).ToString("D2");

            try
            {
                //-y : 強制覆蓋檔案
                //-i : 要擷取的原始檔案
                //-ss : 起始時間
                //-t : 擷取長度, -t sec 或 -t hh:mm:ss
                //-acodec copy : 音訊編碼格式和來源檔案相同
                //-vcodec copy : 影像編碼格式和來源檔案相同
                string command_arg = "-y -i \"" + mp3_filename + "\" -ss " + startTime + " -t " + cutTime + " -acodec copy \"" + mp3_cut_filename + "\"";

                ExcuteProcess(ffmpeg, command_arg);

                richTextBox1.Text += "命令 : " + ffmpeg + "\n";
                richTextBox1.Text += "參數 : " + command_arg + "\n";
                richTextBox1.Text += "已切割完成\t檔案 : " + mp3_cut_filename + "\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }



        }


        private void bt_play_pause_Click(object sender, EventArgs e)
        {
            //flag_play_mode = 0;    //0: stop, 1: play, 2:  pause
            if ((flag_play_mode == 0) || (flag_play_mode == 2))
            {
                flag_play_mode = 1;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
            else if (flag_play_mode == 1)
            {
                flag_play_mode = 2;
                axWindowsMediaPlayer1.Ctlcontrols.pause();

            }

        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            flag_play_mode = 0;
            axWindowsMediaPlayer1.Ctlcontrols.stop();
            mp3_position = 0;
            trackBar_st.Value = mp3_position;
        }

        private void trackBar_st_Scroll(object sender, EventArgs e)
        {
            mp3_position = trackBar_st.Value;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            lb_st.Text = "起始 : " + (mp3_position / 3600).ToString("D2") + " : " + ((mp3_position / 60) % 60).ToString("D2") + " : " + (mp3_position % 60).ToString("D2") + "    " + mp3_position.ToString();

            if (trackBar_st.Value < trackBar_sp.Value)
            {
                int cut = trackBar_sp.Value - trackBar_st.Value;
                lb_cut.Text = "選取 : " + (cut / 3600).ToString("D2") + " : " + ((cut / 60) % 60).ToString("D2") + " : " + (cut % 60).ToString("D2") + "    " + cut.ToString();
            }
        }

        private void trackBar_sp_Scroll(object sender, EventArgs e)
        {
            mp3_position = trackBar_sp.Value;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            lb_sp.Text = "結束 : " + (mp3_position / 3600).ToString("D2") + " : " + ((mp3_position / 60) % 60).ToString("D2") + " : " + (mp3_position % 60).ToString("D2") + "    " + mp3_position.ToString();

            if (trackBar_st.Value < trackBar_sp.Value)
            {
                int cut = trackBar_sp.Value - trackBar_st.Value;
                lb_cut.Text = "選取 : " + (cut / 3600).ToString("D2") + " : " + ((cut / 60) % 60).ToString("D2") + " : " + (cut % 60).ToString("D2") + "    " + cut.ToString();
            }
        }
    }
}
