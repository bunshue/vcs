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
        string ffmpeg_filename = @"C:\______test_files\_exe\ffmpeg\ffmpeg.exe";
        string mp3_filename = string.Empty;

        AxWindowsMediaPlayer axWindowsMediaPlayer1;
        int flag_play_mode = 0;    //0: stop, 1: play, 2:  pause
        int mp3_position = 0;
        int mp3_length = 0;
        int mp3_volume = 50;
        PictureBox pbx = new PictureBox();

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
            tb_filename.Text = "";
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

            //pbx.Parent = this;  //相當於 this.Controls.Add(pbx)
            //pbx.SizeMode = PictureBoxSizeMode.Zoom;
            //pbx.Image = bitmap1;
            pbx.BackColor = Color.Pink;
            pbx.Size = new Size(693, 60);
            pbx.Location = new Point(12, 12);

            pbx.MouseHover += new EventHandler(pbx_MouseHover);
            pbx.MouseDown += new MouseEventHandler(pbx_MouseDown);
            pbx.MouseMove += new MouseEventHandler(pbx_MouseMove);
            pbx.MouseUp += new MouseEventHandler(pbx_MouseUp);
            pbx.Paint += new PaintEventHandler(pbx_Paint);

            this.Controls.Add(pbx);

            bt_open_file_Click(sender, e);
        }

        ToolTip toolTip1 = new ToolTip();

        // The current value.
        int PbxStartValue = 234;
        int PbxStopValue = 567;

        int move_value = 0; //1:PbxStartValue, 2: PbxStopValue

        // The minimum and maximum allowed values.
        int PbxMinimumValue = 0;
        int PbxMaximumValue = 1000;

        private void pbx_MouseHover(object sender, EventArgs e)
        {
            //TBD
            //int value = XtoValue(sender, e.X);


        }

        // Move the needle to this position.
        private bool flag_pbx_mouse_down = false;
        private void pbx_MouseDown(object sender, MouseEventArgs e)
        {
            int value = XtoValue(sender, e.X);

            int abs1 = Math.Abs(value - PbxStartValue);
            int abs2 = Math.Abs(value - PbxStopValue);

            if ((abs1 < abs2) && (abs1 < 30))
            {
                //選中 PbxStartValue
                flag_pbx_mouse_down = true;
                SetValue(sender, XtoValue(sender, e.X));
                move_value = 1;
            }

            if ((abs1 > abs2) && (abs2 < 30))
            {
                //選中 PbxStopValue
                flag_pbx_mouse_down = true;
                SetValue(sender, XtoValue(sender, e.X));
                move_value = 2;
            }

            richTextBox1.Text += "value = " + value.ToString() + "\tabs1 = " + abs1.ToString() + "\tabs2 = " + abs2.ToString() + "\n";

            return;
        }

        private void pbx_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pbx_mouse_down == false)
            {
                return;
            }
            SetValue(sender, XtoValue(sender, e.X));
        }

        private void pbx_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pbx_mouse_down = false;
            toolTip1.Hide(this);
            move_value = 0;
        }

        // Draw the needle.
        private void pbx_Paint(object sender, PaintEventArgs e)
        {
            // Calculate the needle's X coordinate.
            int x1 = ValueToX(sender, PbxStartValue);
            int x2 = ValueToX(sender, PbxStopValue);

            //case 1
            using (Pen pen = new Pen(Color.Lime, 2))
            {
                e.Graphics.DrawLine(pen, x1, 0, x1, ((PictureBox)sender).ClientSize.Height);
            }

            using (Pen pen = new Pen(Color.Red, 2))
            {
                e.Graphics.DrawLine(pen, x2, 0, x2, ((PictureBox)sender).ClientSize.Height);
            }


            /*
            //case 2
            int y = (int)(pbx.ClientSize.Height * 0.25);
            int hgt = pbx.ClientSize.Height - 2 * y;

            // Draw it.
            e.Graphics.FillRectangle(Brushes.Blue, 0, y, x, hgt);
            using (Pen pen = new Pen(Color.Blue, 3))
            {
                e.Graphics.DrawLine(pen, x, 0, x, pbx.ClientSize.Height);
            }
            */
        }

        // Convert an X coordinate to a value.
        private int XtoValue(object sender, int x)
        {
            return PbxMinimumValue + (PbxMaximumValue - PbxMinimumValue) * x / (int)(((PictureBox)sender).ClientSize.Width - 1);
        }

        // Convert value to an X coordinate.
        private int ValueToX(object sender, int value)
        {
            return (((PictureBox)sender).ClientSize.Width - 1) * (value - PbxMinimumValue) / (int)(PbxMaximumValue - PbxMinimumValue);
        }

        // Set the slider's value. If the value has changed,
        // display the value tooltip.
        private void SetValue(object sender, int value)
        {
            // Make sure the new value is within bounds.
            if (value < PbxMinimumValue)
            {
                value = PbxMinimumValue;
            }
            if (value > PbxMaximumValue)
            {
                value = PbxMaximumValue;
            }

            // See if the value has changed.
            if (move_value == 1)
            {
                if (PbxStartValue == value)
                {
                    return;
                }
            }
            else if (move_value == 2)
            {
                if (PbxStopValue == value)
                {
                    return;
                }
            }

            // Save the new value.
            if (move_value == 1)
                PbxStartValue = value;
            else if (move_value == 2)
                PbxStopValue = value;

            // Redraw to show the new value.
            ((PictureBox)sender).Refresh();

            // Display the value tooltip.
            int tip_x = 0;
            int tip_y = 0;
            if (move_value == 1)
            {
                tip_x = ((PictureBox)sender).Left + (int)ValueToX(sender, PbxStartValue);
                tip_y = ((PictureBox)sender).Top;
                toolTip1.Show(PbxStartValue.ToString(), this, tip_x, tip_y, 3000);
            }
            else if (move_value == 2)
            {
                tip_x = ((PictureBox)sender).Left + (int)ValueToX(sender, PbxStopValue);
                tip_y = ((PictureBox)sender).Top;
                toolTip1.Show(PbxStopValue.ToString(), this, tip_x, tip_y, 3000);
            }
        }

        void show_item_location()
        {
            /*
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 30;
            dx = 160;
            dy = 70;
            */

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
            mp3_length = total_length;

            trackBar_st.Maximum = total_length;
            trackBar_st.Minimum = 0;
            trackBar_st.Value = 0;

            trackBar_sp.Maximum = total_length;
            trackBar_sp.Minimum = 0;
            trackBar_sp.Value = total_length;

            PbxMinimumValue = 0;
            PbxMaximumValue = total_length;
            PbxStartValue = 0;
            PbxStopValue = total_length;

            axWindowsMediaPlayer1.URL = filename;

            axWindowsMediaPlayer1.Ctlcontrols.stop();
            mp3_position = 0;
            mp3_filename = filename;
            tb_filename.Text = filename;
            lb_time.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString;

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

                ExcuteProcess(ffmpeg_filename, command_arg);

                richTextBox1.Text += "命令 : " + ffmpeg_filename + "\n";
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
                //richTextBox1.Text += "start at : " + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
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
            lb_time.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString;
            mp3_position = 0;
            trackBar_st.Value = mp3_position;
            trackBar_sp.Value = mp3_length;
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            do_plus();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            do_minus();
        }

        void do_plus()	//+
        {
            int amount = 5;
            axWindowsMediaPlayer1_setup_volume(true, amount);
        }

        void do_minus()	//-
        {
            int amount = 5;
            axWindowsMediaPlayer1_setup_volume(false, amount);
        }

        void axWindowsMediaPlayer1_setup_volume(bool dir, int amount)
        {
            if (dir == true)   //volume up
            {
                if (mp3_volume <= 95)
                {
                    mp3_volume += 5;
                    axWindowsMediaPlayer1.settings.volume = mp3_volume;
                }
            }
            else   //volume down
            {
                if (mp3_volume >= 5)
                {
                    mp3_volume -= 5;
                    axWindowsMediaPlayer1.settings.volume = mp3_volume;
                }
            }
            //show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);
        }

        private void trackBar_st_Scroll(object sender, EventArgs e)
        {
            mp3_position = trackBar_st.Value;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            lb_time.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString;
            lb_st.Text = "起始 : " + (mp3_position / 3600).ToString("D2") + " : " + ((mp3_position / 60) % 60).ToString("D2") + " : " + (mp3_position % 60).ToString("D2") + "    " + mp3_position.ToString();

            if (trackBar_st.Value < trackBar_sp.Value)
            {
                int cut = trackBar_sp.Value - trackBar_st.Value;
                lb_cut.Text = "選取 : " + (cut / 3600).ToString("D2") + " : " + ((cut / 60) % 60).ToString("D2") + " : " + (cut % 60).ToString("D2") + "    " + cut.ToString();
            }
        }

        private void trackBar_sp_Scroll(object sender, EventArgs e)
        {
            lb_sp.Text = "結束 : " + (mp3_position / 3600).ToString("D2") + " : " + ((mp3_position / 60) % 60).ToString("D2") + " : " + (mp3_position % 60).ToString("D2") + "    " + mp3_position.ToString();

            if (trackBar_st.Value < trackBar_sp.Value)
            {
                int cut = trackBar_sp.Value - trackBar_st.Value;
                lb_cut.Text = "選取 : " + (cut / 3600).ToString("D2") + " : " + ((cut / 60) % 60).ToString("D2") + " : " + (cut % 60).ToString("D2") + "    " + cut.ToString();
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //test 1


            string atPositioin = "10";
            string filename = "";
            string tmpFileName = "";

            string cmdParams = String.Format("-hide_banner -ss {0} -i {1} -r 1 -t 1 -f image2 {2}", atPositioin, filename, tmpFileName);


            // Execute command to let FFMPEG extract the frame
            Execute(ffmpeg_filename, cmdParams);
        }

        private static string Execute(string exePath, string parameters)
        {
            string result = String.Empty;

            using (Process p = new Process())
            {
                p.StartInfo.UseShellExecute = false;
                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.RedirectStandardOutput = true;
                p.StartInfo.FileName = exePath;
                p.StartInfo.Arguments = parameters;
                p.Start();
                p.WaitForExit();

                result = p.StandardOutput.ReadToEnd();
            }
            return result;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //test 2
            //影片轉mp3

            //影片轉mp3
            //ffmpeg -i test.mp4 -f mp3 -vn test.mp3
            /*
            參數解釋：
            -i 表示input，即輸入文件
            -f 表示format，即輸出格式
            -vn表示vedio not，即輸出不包含視頻
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //test 3
            //

            string filename1 = @"D:\vcs\_烏龍派出所\_烏龍派出所151~200\烏龍派出所181(日語).mp4";
            string filename2 = @"D:\vcs\_烏龍派出所\_烏龍派出所151~200\烏龍派出所181(日語)aaaaaaaaaaaa.mp4";

            //要將視頻升級到1080p，請輸入：

            string cmdParams = String.Format("-i {0} -vf scale = 1920x1080:flags = lanczos {1}", filename1, filename2);

            //ffmpeg -i {0} -vf scale = 1920x1080：flags = lanczos {1}


            //要升級到4K視頻，請輸入：
            //ffmpeg -i input.mp4 -vf scale = 3840x2560：flags = lanczos -c：v libx264 -preset slow -crf 21 output_compress_4k.mp4

            // Execute command to let FFMPEG extract the frame
            Execute(ffmpeg_filename, cmdParams);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //test 4

            //視頻截圖
            string filename = @"D:\vcs\_烏龍派出所\_烏龍派出所151~200\烏龍派出所181(日語).mp4";
            CatchImg(filename);
        }

        /// <summary>
        /// @從視頻文件截圖,生成在視頻文件所在文件夾
        /// 在Web.Config 中需要兩個前置配置項:
        /// 1.ffmpeg.exe文件的路徑
        /// <add key="ffmpeg" value="E:\ffmpeg\ffmpeg.exe" />
        /// 2.截圖的尺寸大小
        /// <add key="CatchFlvImgSize" value="240x180" />
        /// 3.視頻處理程序ffmpeg.exe
        /// </summary>
        /// <param name="vFileName">視頻文件地址,如:/Web/FlvFile/User1/00001.Flv</param>
        /// <returns>成功:返回圖片虛擬地址; 失敗:返回空字符串</returns>

        public string CatchImg(string vFileName)
        {
            if ((File.Exists(ffmpeg_filename) == false) || (File.Exists(vFileName) == false))
            {
                return "";
            }

            //獲得圖片相對路徑/最後存儲到數據庫的路徑,如:/Web/FlvFile/User1/00001.jpg
            string flv_img = Path.ChangeExtension(vFileName, ".jpg");

            //圖片絕對路徑,如:D:\Video\Web\FlvFile\User1\0001.jpg
            //string flv_img_p = HttpContext.Current.Server.MapPath(flv_img);
            string flv_img_p = "aaaaaa.jpg";

            //截圖的尺寸大小,配置在Web.Config中,如:<add key="CatchFlvImgSize" value="240x180" />
            //string FlvImgSize = System.Configuration.ConfigurationSettings.APPSettings["CatchFlvImgSize"];

            ProcessStartInfo startInfo = new ProcessStartInfo(ffmpeg_filename);
            startInfo.WindowStyle = ProcessWindowStyle.Hidden;

            //此處組合成ffmpeg.exe文件需要的參數即可,此處命令在ffmpeg 0.4.9調試通過
            //startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + FlvImgSize + " " + flv_img_p ;
            //startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + "960x540" + " " + flv_img_p;
            startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + "960x480" + " " + flv_img_p;

            try
            {
                Process.Start(startInfo);
            }
            catch
            {
                return "";
            }

            ///注意:圖片截取成功後,數據由內存緩存寫到磁盤需要時間較長,大概在3,4秒甚至更長;
            ///這兒需要延時後再檢測,我服務器延時8秒,即如果超過8秒圖片仍不存在,認為截圖失敗;
            ///此處略去延時代碼.如有那位知道如何捕捉ffmpeg.exe截圖失敗消息,請告知,先謝過!
            if (File.Exists(flv_img_p) == true)
            {
                return flv_img;
            }

            return "";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //取得mp3音樂長度

            richTextBox1.Text += "取得音樂檔案長度 :\n";

            //string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            string filename = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_日本演歌\__石川さゆり\Ishikawa Sayuri 【アルバム】[演歌] 石川さゆり ‐ 全曲集 Super Best.mp3";

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
        /// 獲得音樂長度  
        /// </summary>  
        /// <param name="filePath">文件的完整路徑</param>
        public static string[] GetMP3Time(string filePath)
        {
            string dirName = Path.GetDirectoryName(filePath);
            string SongName = Path.GetFileName(filePath);//獲得歌曲名稱             
            Shell sh = new Shell();
            //ShellClass sh = new ShellClass();  or
            Folder dir = sh.NameSpace(dirName);
            FolderItem item = dir.ParseName(SongName);
            string SongTime = dir.GetDetailsOf(item, 27);//27為獲得歌曲持續時間 ，28為獲得音樂速率，1為獲得音樂文件大小      
            string[] time = Regex.Split(SongTime, ":");
            return time;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //音頻轉換與音頻切割

            //音頻轉換
            //string filename1 = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            string filename1 = @"C:\______test_files\_wav\WindowsShutdown.wav";
            string filename2 = @"aaaaa.wav";

            int bitrate = 12 * 1000;//恒定碼率
            int Hz = 3000;//采樣頻率  

            try
            {
                ExcuteProcess(ffmpeg_filename, "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + filename1 + "\" \"" + filename2 + "\"");

                richTextBox1.Text += "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + filename1 + "\" \"" + filename2 + "\"";
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

                ExcuteProcess(ffmpeg_filename, command_arg);

                richTextBox1.Text += "命令 : " + ffmpeg_filename + "\n";
                richTextBox1.Text += "參數 : " + command_arg + "\n";
                richTextBox1.Text += "已切割完成\t檔案 : " + mp3_cut_filename + "\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        /// <summary>
        /// 轉換函數
        /// </summary>
        /// <param name="exe">ffmpeg程序</param>
        /// <param name="arg">執行參數</param>
        public static void ExcuteProcess(string exe, string arg)
        {
            using (var p = new Process())
            {
                p.StartInfo.FileName = exe;
                p.StartInfo.Arguments = arg;
                p.StartInfo.UseShellExecute = false;    //輸出信息重定向  
                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.RedirectStandardOutput = true;
                p.Start();                    //啟動線程  
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();
                p.WaitForExit();//等待進程結束                                        
            }

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        //FFMPEG的使用 ST
        private void bt_ffmpeg0_Click(object sender, EventArgs e)
        {
            //取得影片的寬高

            //CMD 命令  通過ffmpeg執行一條CMD命令可以讀取出視頻的幀高度和幀寬度信息。
            //C:\______test_files\_exe>ffmpeg.exe -i "C:\______test_files\_video\i2c.avi"

            //string ffmpeg_filename = @"C:\______test_files\_exe\ffmpeg.exe";

            string video_filename1 = @"C:\______test_files\_video\i2c.avi";
            string video_filename2 = @"D:\內視鏡影片\190902-0827.mp4";

            //System.Diagnostics.Process.Start(ffmpeg_filename, video_filename);

            int? width, height;

            GetVideoFormatSize(video_filename1, out width, out height);
            richTextBox1.Text += "影片 : " + video_filename1 + "\tW = " + width.ToString() + ", H = " + height.ToString() + "\n";

            GetVideoFormatSize(video_filename2, out width, out height);
            richTextBox1.Text += "影片 : " + video_filename2 + "\tW = " + width.ToString() + ", H = " + height.ToString() + "\n";
        }

        private void bt_ffmpeg1_Click(object sender, EventArgs e)
        {
            //獲取視頻時長
            string video_filename1 = @"C:\______test_files\_video\i2c.avi";
            string video_filename2 = @"D:\內視鏡影片\190902-0827.mp4";

            string length;

            length = Fromffmpeg(video_filename1);
            richTextBox1.Text += "影片 : " + video_filename1 + "\t len = " + length + "\n";

            length = Fromffmpeg(video_filename2);
            richTextBox1.Text += "影片 : " + video_filename2 + "\t len = " + length + "\n";
        }

        private void bt_ffmpeg2_Click(object sender, EventArgs e)
        {
            //獲取視頻第一秒圖片

            string video_filename1 = @"C:\______test_files\_video\i2c.avi";
            //string video_filename2 = @"D:\內視鏡影片\190902-0827.mp4";

            string path = @"C:\dddddddddd3\";
            CatchImg(video_filename1, path);
        }

        /// <summary>
        /// 獲取視頻的幀寬度和幀高度
        /// </summary>
        /// <param name="video_filename">mov文件的路徑</param>
        /// <returns>null表示獲取寬度或高度失敗</returns>
        public void GetVideoFormatSize(string video_filename, out int? width, out int? height)
        {
            try
            {
                //判斷文件是否存在
                if (File.Exists(video_filename) == false)
                {
                    width = null;
                    height = null;
                }

                //執行命令獲取該文件的一些信息 
                string output;
                string error;
                ExecuteCommand("\"" + ffmpeg_filename + "\"" + " -i " + "\"" + video_filename + "\"", out output, out error);
                if (string.IsNullOrEmpty(error))
                {
                    width = null;
                    height = null;
                }

                //string result = process.StandardError.ReadToEnd(); // 注意，是：StandardError。                
                //通過正則表達式獲取信息裏面的寬度信息
                Regex regex = new Regex("(\\d{2,4})x(\\d{2,4})", RegexOptions.Compiled);
                Match m = regex.Match(error);
                if (m.Success)
                {
                    width = int.Parse(m.Groups[1].Value);
                    height = int.Parse(m.Groups[2].Value);
                }
                else
                {
                    width = null;
                    height = null;
                }
            }
            catch (Exception)
            {
                width = null;
                height = null;
            }
        }


        /// <summary>
        /// 執行一條command命令
        /// </summary>
        /// <param name="command">需要執行的Command</param>
        /// <param name="output">輸出</param>
        /// <param name="error">錯誤</param>
        public static void ExecuteCommand(string command, out string output, out string error)
        {
            try
            {
                //創建一個進程
                Process p = new Process();
                p.StartInfo.FileName = command;
                p.StartInfo.UseShellExecute = false;
                p.StartInfo.RedirectStandardOutput = true;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.CreateNoWindow = true;

                //啓動進程
                p.Start();

                //準備讀出輸出流和錯誤流
                string outputData = string.Empty;
                string errorData = string.Empty;
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();

                p.OutputDataReceived += (ss, ee) =>
                {
                    outputData += ee.Data;
                };

                p.ErrorDataReceived += (ss, ee) =>
                {
                    errorData += ee.Data;
                };

                //等待退出
                p.WaitForExit();

                //關閉進程
                p.Close();

                //返回流結果
                output = outputData;
                error = errorData;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                output = null;
                error = null;
            }
        }

        //獲取視頻第一秒圖片
        public string CatchImg(string FileName, string oldimg)
        {
            string imgpath = @"C:\dddddddddd3\";
            //string trueimgpath = "";
            //trueimgpath = "InfoReleaseResources/Image/" + GroupId + "/";
            if (Directory.Exists(imgpath)==false)
            {
                Directory.CreateDirectory(imgpath);
            }

            string vFileName = FileName;
            if ((System.IO.File.Exists(ffmpeg_filename) == false) || (System.IO.File.Exists(vFileName) == false))
            {
                return "";
            }
            
            //獲得圖片相對路徑/最後存儲到數據庫的路徑,如:/InfoReleaseResources/Image/分組/圖片.jpg

            richTextBox1.Text += "3333333\n";

            string flv_img = oldimg;
            //圖片絕對路徑,如:D:\Video\Web\FlvFile\User1\0001.jpg
            string flv_img_p = flv_img;
            //截圖的尺寸大小
            int? width, height;
            GetVideoFormatSize(vFileName, out width, out height);
            string FlvImgSize = width + "x" + height;
            ProcessStartInfo startInfo = new ProcessStartInfo(ffmpeg_filename);
            startInfo.UseShellExecute = false; // 要獲取輸出，此值必須爲 false。
            startInfo.CreateNoWindow = true;
            //startInfo.RedirectStandardResult = true;
            startInfo.RedirectStandardError = true;
            startInfo.WindowStyle = ProcessWindowStyle.Hidden;
            //此處組合成ffmpeg.exe文件需要的參數即可,此處命令在ffmpeg 0.4.9調試通過
            //startInfo.Arguments = " -i " + vFileName + " -y -f image2 -ss 1 -t 0.001 -s " + FlvImgSize + " " + flv_img_p;
            //string command = string.Format("\"{0}\" -i \"{1}\" -ss {2} -vframes 1 -r 1 -ac 1 -ab 2 -s {3}*{4} -f image2 \"{5}\"", ffmpeg, vFileName, 1, width, height, flv_img_p);
            startInfo.Arguments = string.Format("-i \"{0}\" -ss {1} -vframes 1 -r 1 -ac 1 -ab 2 -s {2}*{3} -f image2 \"{4}\"", vFileName, 1, width, height, flv_img_p);
            try
            {
                //Process.Start(startInfo);
                //string result= process.StandardError.ReadToEnd();
                Process process = Process.Start(startInfo);
                string result = process.StandardError.ReadToEnd();
                process.WaitForExit();
                process.Close();
                richTextBox1.Text += "OKOK\n";
            }
            catch
            {
                richTextBox1.Text += "FAIL\n";
                return "";
            }

            ///注意:圖片截取成功後,數據由內存緩存寫到磁盤需要時間較長,大概在3,4秒甚至更長;
            ///這兒需要延時後再檢測,我服務器延時8秒,即如果超過8秒圖片仍不存在,認爲截圖失敗;
            ///此處略去延時代碼.如有那位知道如何捕捉ffmpeg.exe截圖失敗消息,請告知,先謝過!
            //if (System.IO.File.Exists(flv_img_p))
            //{
            //    return flv_img;
            //}

            richTextBox1.Text += "flv_img_p = " + flv_img_p + "\n";
            richTextBox1.Text += "flv_img = " + flv_img + "\n";

            return flv_img;
        }

        //獲取視頻時長
        public string Fromffmpeg(string fileName)
        {
            string duration = "";
            using (Process pro = new Process())
            {
                pro.StartInfo.UseShellExecute = false;
                pro.StartInfo.ErrorDialog = false;
                pro.StartInfo.RedirectStandardError = true;

                pro.StartInfo.FileName = ffmpeg_filename;   //FFMPEG程式所在地

                pro.StartInfo.Arguments = " -i " + fileName;

                pro.Start();
                System.IO.StreamReader errorreader = pro.StandardError;
                pro.WaitForExit(1000);

                string result = errorreader.ReadToEnd();
                if (string.IsNullOrEmpty(result) == false)
                {
                    result = result.Substring(result.IndexOf("Duration: ") + ("Duration: ").Length, ("00:00:00").Length);
                    duration = result;
                }
                return duration;
            }
        }
        //FFMPEG的使用 SP

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_play_mode == 1)
            {
                lb_time.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString;
            }
            else
            {
                return;
            }
        }

    }
}

