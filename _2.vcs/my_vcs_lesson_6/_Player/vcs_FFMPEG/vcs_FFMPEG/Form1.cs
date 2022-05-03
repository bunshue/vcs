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

        private void button5_Click(object sender, EventArgs e)
        {
            //test 1


            string atPositioin = "10";
            string filename = "";
            string tmpFileName = "";

            string cmdParams = String.Format("-hide_banner -ss {0} -i {1} -r 1 -t 1 -f image2 {2}", atPositioin, filename, tmpFileName);


            // Execute command to let FFMPEG extract the frame
            Execute(ffmpeg, cmdParams);






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
            参数解释：
            -i 表示input，即输入文件
            -f 表示format，即输出格式
            -vn表示vedio not，即输出不包含视频
            */



        }

        private void button7_Click(object sender, EventArgs e)
        {
            //test 3

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
            if ((!File.Exists(ffmpeg)) || (!File.Exists(vFileName)))
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

            ProcessStartInfo startInfo = new ProcessStartInfo(ffmpeg);
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
            if (File.Exists(flv_img_p))
            {
                return flv_img;
            }

            return "";
        }


        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

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
            //C:\______test_files\_exe>ffmpeg.exe -i "C:\______test_files\__RW\_avi\i2c.avi"

            //string ffmpeg_filename = @"C:\______test_files\_exe\ffmpeg.exe";

            string video_filename1 = @"C:\______test_files\__RW\_avi\i2c.avi";
            string video_filename2 = @"D:\內視鏡影片\190902-0827.mp4";

            //System.Diagnostics.Process.Start(ffmpeg_filename, video_filename);

            int? width, height;

            GetMovWidthAndHeight(video_filename1, out width, out height);
            richTextBox1.Text += "影片 : " + video_filename1 + "\tW = " + width.ToString() + ", H = " + height.ToString() + "\n";


            GetMovWidthAndHeight(video_filename2, out width, out height);
            richTextBox1.Text += "影片 : " + video_filename2 + "\tW = " + width.ToString() + ", H = " + height.ToString() + "\n";
        }

        private void bt_ffmpeg1_Click(object sender, EventArgs e)
        {
            //獲取視頻時長
            string video_filename1 = @"C:\______test_files\__RW\_avi\i2c.avi";
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

            string video_filename1 = @"C:\______test_files\__RW\_avi\i2c.avi";
            //string video_filename2 = @"D:\內視鏡影片\190902-0827.mp4";

            string path = @"D:\dddddddddd3\";
            CatchImg(video_filename1, path);
        }

        /// <summary>
        /// 獲取視頻的幀寬度和幀高度
        /// </summary>
        /// <param name="videoFilePath">mov文件的路徑</param>
        /// <returns>null表示獲取寬度或高度失敗</returns>
        public static void GetMovWidthAndHeight(string videoFilePath, out int? width, out int? height)
        {
            try
            {
                //判斷文件是否存在
                if (!File.Exists(videoFilePath))
                {
                    width = null;
                    height = null;
                }

                //執行命令獲取該文件的一些信息 
                //string ffmpegPath = new FileInfo(Process.GetCurrentProcess().MainModule.FileName).DirectoryName + @"\ffmpeg.exe";
                string ffmpegPath = @"C:\______test_files\_exe\ffmpeg.exe";

                string output;
                string error;
                ExecuteCommand("\"" + ffmpegPath + "\"" + " -i " + "\"" + videoFilePath + "\"", out output, out error);
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
                Process pc = new Process();
                pc.StartInfo.FileName = command;
                pc.StartInfo.UseShellExecute = false;
                pc.StartInfo.RedirectStandardOutput = true;
                pc.StartInfo.RedirectStandardError = true;
                pc.StartInfo.CreateNoWindow = true;

                //啓動進程
                pc.Start();

                //準備讀出輸出流和錯誤流
                string outputData = string.Empty;
                string errorData = string.Empty;
                pc.BeginOutputReadLine();
                pc.BeginErrorReadLine();

                pc.OutputDataReceived += (ss, ee) =>
                {
                    outputData += ee.Data;
                };

                pc.ErrorDataReceived += (ss, ee) =>
                {
                    errorData += ee.Data;
                };

                //等待退出
                pc.WaitForExit();

                //關閉進程
                pc.Close();

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
            string imgpath = @"C:\dddddddddd\";
            //string trueimgpath = "";
            //trueimgpath = "InfoReleaseResources/Image/" + GroupId + "/";
            if (!Directory.Exists(imgpath))
            {
                Directory.CreateDirectory(imgpath);
            }
            //取得ffmpeg.exe的路徑
            string ffmpeg = @"C:\______test_files\_exe\ffmpeg.exe";
            string vFileName = FileName;
            if ((!System.IO.File.Exists(ffmpeg)) || (!System.IO.File.Exists(vFileName)))
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
            GetMovWidthAndHeight(vFileName, out width, out height);
            string FlvImgSize = width + "x" + height;
            ProcessStartInfo startInfo = new ProcessStartInfo(ffmpeg);
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

                string ffmpeg_filename = @"C:\______test_files\_exe\ffmpeg.exe";

                pro.StartInfo.FileName = ffmpeg_filename;
                pro.StartInfo.Arguments = " -i " + fileName;

                pro.Start();
                System.IO.StreamReader errorreader = pro.StandardError;
                pro.WaitForExit(1000);

                string result = errorreader.ReadToEnd();
                if (!string.IsNullOrEmpty(result))
                {
                    result = result.Substring(result.IndexOf("Duration: ") + ("Duration: ").Length, ("00:00:00").Length);
                    duration = result;
                }
                return duration;

            }
        }
        //FFMPEG的使用 SP

    
    }
}

