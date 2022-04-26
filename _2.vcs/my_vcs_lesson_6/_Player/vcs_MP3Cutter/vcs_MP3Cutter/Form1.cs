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


namespace vcs_MP3Cutter
{
    public partial class Form1 : Form
    {
        string ffmpeg = @"C:\______test_files\_exe\ffmpeg\ffmpeg.exe";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

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

            //音频切割
            string fromPath = @"C:\______test_files\_wav\harumi99.wav";
            string savePath = @"bbbbb.wav";


            /*
                        int BeginM = 0;
                        int BeginS = 0;
                        int EndM = 0;
                        int EndS = 10;

                        string startTime = string.Format("0:{0}:{1}", BeginM.ToString(), BeginS.ToString()).Trim();//歌曲起始时间
                        //int duration = (Convert.ToInt32(this.txtEndM.Text) * 60 + Convert.ToInt32(this.txtEndS.Text)) - (Convert.ToInt32(this.txtBeginM.Text) * 60 + Convert.ToInt32(this.txtBeginS.Text));
                        int duration = (EndM * 60 + EndS) - (BeginM * 60 + BeginS);
                        string endTime = string.Format("0:{0}:{1}", duration / 60, duration % 60);//endTime是持续的时间，不是歌曲结束的时间
                        string savePath = @"aaaaaa.wav";//切割后音乐保存的物理路径
            */

            /*
            string startTime = string.Format("0:{0}:{1}", txtBeginM.Text, txtBeginS.Text).Trim();//歌曲起始时间  
            int duration = (Convert.ToInt32(this.txtEndM.Text) * 60 + Convert.ToInt32(this.txtEndS.Text)) - (Convert.ToInt32(this.txtBeginM.Text) * 60 + Convert.ToInt32(this.txtBeginS.Text));
            string endTime = string.Format("0:{0}:{1}", duration / 60, duration % 60);//endTime是持续的时间，不是歌曲结束的时间  
            */

            string startTime = "0:0:30";
            string endTime = "0:1:30";

            try
            {
                ExcuteProcess(ffmpeg, "-y -i \"" + fromPath + "\" -ss " + startTime + " -t " + endTime + " -acodec copy \"" + savePath + "\"");//-acodec copy表示歌曲的码率和采样频率均与前者相同

                richTextBox1.Text += "已切割完成\n";
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

    }
}
