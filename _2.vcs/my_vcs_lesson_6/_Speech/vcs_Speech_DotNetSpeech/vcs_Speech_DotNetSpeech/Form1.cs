using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;

using DotNetSpeech;  // for SpVoice

// 使用DotNetSpeech 做 文字轉語音
// 微軟 SAPI.SpVoice C# 使用方法
// 參考/加入參考, 選DotNetSpeech.dll
// DotNetSpeech屬性/內嵌Interop型別 改false
/*
DotNetSpeech----文本轉wave語音文件wav操作
引入dll(DotNetSpeech.dll)，引入以后需要選中項目中引入的dll，鼠標右鍵，選擇屬性，把“嵌入互操作類型”設置為False。
不然會提示無法嵌入互操作類型"SpeechLib.SpVoiceClass".請改用適用的接口.
DotNetSpeech.SpeechAudioFormatType.SAFTCCITT_uLaw_11kHzMono表示音頻編碼格式為G711U
*/

namespace vcs_Speech_DotNetSpeech
{
    public partial class Form1 : Form
    {
        string speech_text = "影像邊緣檢測(edge detection) 函數 Canny() Sobel()";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += speech_text + "\n";
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
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            richTextBox1.Size = new Size(640, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(890, 750);
            this.Text = "vcs_Speech_DotNetSpeech";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            // 使用 DotNetSpeech 的 SpVoiceClass

            DotNetSpeech.SpVoice vo = new SpVoiceClass();

            ISpeechObjectTokens obj = vo.GetVoices();
            int count = obj.Count;//获取语音库总数
            for (int i = 0; i < count; i++)
            {
                string desc = obj.Item(i).GetDescription(); //遍历语音库
                richTextBox1.Text += "取得語音庫 : " + desc + "\n";
            }

            //------------------------------  # 30個

            //朗讀

            DotNetSpeech.SpeechVoiceSpeakFlags SSF = DotNetSpeech.SpeechVoiceSpeakFlags.SVSFlagsAsync;
            //DotNetSpeech.SpVoice vo = new SpVoiceClass();
            vo.Speak(speech_text, SSF);

            //------------------------------  # 30個

            /*
            //錄音
            DotNetSpeech.SpeechVoiceSpeakFlags SSF = DotNetSpeech.SpeechVoiceSpeakFlags.SVSFlagsAsync;
            DotNetSpeech.SpVoice vo = new SpVoiceClass();
            DotNetSpeech.SpeechStreamFileMode SSFM = DotNetSpeech.SpeechStreamFileMode.SSFMCreateForWrite;
            DotNetSpeech.SpFileStream SFS = new DotNetSpeech.SpFileStreamClass();
            string filename = "tmp_spvoice2.wav";
            SFS.Open(filename, SSFM, false);
            vo.AudioOutputStream = SFS;
            vo.Speak(speech_text, SSF);
            vo.WaitUntilDone(System.Threading.Timeout.Infinite);
            SFS.Close();

            richTextBox1.Text += "done\n";
            */
        }

        //------------------------------------------------------------  # 60個

        // 定義符合 CallBack 委派的方法
        private void MyCallBack(bool finished, int InputWordPosition, int InputWordLength)
        {
            if (this.InvokeRequired)
            {
                // 注意這裡要用 SpVoiceUtil.CallBack，而不是單純 CallBack
                this.Invoke(new SpVoiceUtil.CallBack(MyCallBack), finished, InputWordPosition, InputWordLength);
                return;
            }

            if (!finished)
            {
                label1.Text = string.Format("朗讀中... 位置={0}, 長度={1}", InputWordPosition, InputWordLength);

                progressBar1.Maximum = speech_text.Length;
                int pos = InputWordPosition + InputWordLength;
                if (pos > progressBar1.Maximum)
                {
                    pos = progressBar1.Maximum;
                }
                progressBar1.Value = pos;
            }
            else
            {
                label1.Text = "朗讀完成！";
                progressBar1.Value = progressBar1.Maximum;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // SpVoiceUtil 類別內用的是 SpVoiceClass()

            SpVoiceUtil svu = new SpVoiceUtil();

            //取得語音庫
            List<string> sss = svu.getDescription();
            foreach (string s in sss)
            {
                richTextBox1.Text += "取得語音庫 : " + s + "\n";
            }

            //取得語音庫 : Microsoft Hanhan Desktop - Chinese (Taiwan)
            //取得語音庫 : Microsoft Zira Desktop - English (United States)

            //------------------------------  # 30個

            //設置語音庫
            string language = "Microsoft Hanhan Desktop - Chinese (Taiwan)";  // 可以說中文
            //language = "Microsoft Zira Desktop - English (United States)";  // 不能說中文
            svu.setDescription(language);  // 設置語音庫

            //------------------------------  # 30個

            // 呼叫 Speak，並傳入 callback
            bool result = svu.Speak(speech_text, MyCallBack);
            label1.Text = result ? "朗讀開始..." : "朗讀失敗";
            progressBar1.Value = 0;

            richTextBox1.Text += "Speak 啟動結果: " + result + "\n";

            //------------------------------  # 30個

            //語音轉wav
            //speech_text = "我来测试一下！AB连续字母加空格";
            speech_text = "In compupting, a system call is the mechanism used by an application program to request service from the operating system.";
            speech_text = AddKongGeToPlateNo(speech_text).Trim();

            svu.setRate(0);  // 設置語速
            svu.setVolume(100);  // 設置聲音大小
            string filename = "tmp_wave_file.wav";
            svu.WriteToWAV(filename, speech_text, SpeechAudioFormatType.SAFTCCITT_uLaw_11kHzMono);  // SAFT11kHz16BitMono 生成wav文件

            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        // 连续字母中加空格
        private static string AddKongGeToPlateNo(string s)
        {
            int length = s.Length;
            string[] letters = new string[] { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
            for (int i = 0; i < length - 1; i++)
            {
                string str = s.Substring(i, 1);
                string str1 = s.Substring(i + 1, 1);
                if (letters.Contains(str) && letters.Contains(str1))
                {
                    s = s.Substring(0, i + 1) + " " + s.Substring(i + 1);
                    length = length + 1;
                }
            }
            return s;
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個


    }

    //------------------------------------------------------------  # 60個

    class SpVoiceUtil
    {
        SpVoice voice = new SpVoiceClass();

        public delegate void CallBack(bool b, int InputWordPosition, int InputWordLength);

        /// <summary>
        /// 朗讀文本
        /// </summary>
        /// <param name="str">要朗讀的文本</param>
        /// <param name="CallBack">回調地址</param>
        /// <returns>返回bool</returns>
        public bool Speak(string str, CallBack CallBack)
        {
            int n = voice.Speak(str, SpeechVoiceSpeakFlags.SVSFlagsAsync);

            Thread thread = new Thread(new ParameterizedThreadStart(Call));
            thread.IsBackground = true;
            thread.Start((Object)CallBack);
            return !(n != 1);
        }

        /// <summary>
        /// 回調函數線程子程序
        /// </summary>
        /// <param name="callBack"></param>
        private void Call(Object callBack)
        {
            int InputWordLength = 0;    //局部_朗讀長度
            int InputWordPosition = 0; //局部_朗讀位置

            CallBack CallBack = (CallBack)callBack;

            while ((int)voice.Status.RunningState != 1)
            {
                if (InputWordPosition != voice.Status.InputWordPosition || InputWordLength != voice.Status.InputWordLength)
                {
                    InputWordPosition = voice.Status.InputWordPosition;
                    InputWordLength = voice.Status.InputWordLength;

                    //回調                  
                    CallBack(false, InputWordPosition, InputWordLength);
                }
            }
            CallBack(true, InputWordPosition, InputWordLength);
        }

        /// <summary>
        /// 獲取語音庫
        /// </summary>
        /// <returns>List<string></returns>
        public List<string> getDescription()
        {
            List<string> list = new List<string>();
            ISpeechObjectTokens obj = voice.GetVoices();
            int count = obj.Count;//獲取語音庫總數
            for (int i = 0; i < count; i++)
            {
                string desc = obj.Item(i).GetDescription(); //遍歷語音庫
                list.Add(desc);
            }
            return list;
        }

        /// <summary>
        /// 設置當前使用語音庫
        /// </summary>
        /// <returns>bool</returns>
        public bool setDescription(string name)
        {
            List<string> list = new List<string>();
            ISpeechObjectTokens obj = voice.GetVoices();
            int count = obj.Count;//獲取語音庫總數
            bool result = false;
            for (int i = 0; i < count; i++)
            {
                string desc = obj.Item(i).GetDescription(); //遍歷語音庫
                if (desc.Equals(name))
                {
                    voice.Voice = obj.Item(i);
                    result = true;
                }
            }
            return result;
        }

        /// <summary>
        /// 設置語速
        /// </summary>
        /// <param name="n"></param>
        public void setRate(int n)
        {
            voice.Rate = n;
        }

        /// <summary>
        /// 設置聲音大小
        /// </summary>
        /// <param name="n"></param>
        public void setVolume(int n)
        {
            voice.Volume = n;
        }

        /// <summary>
        /// 暫停
        /// </summary>
        public void Pause()
        {
            voice.Pause();
        }

        /// <summary>
        /// 繼續
        /// </summary>
        public void Resume()
        {
            voice.Resume();
        }

        /// <summary>
        /// 停止
        /// </summary>
        public void Stop()
        {
            voice.Speak(string.Empty, SpeechVoiceSpeakFlags.SVSFPurgeBeforeSpeak);
        }

        /// <summary>
        /// 輸出WAV
        /// </summary>
        /// <param name="filename">保存路徑</param>
        /// <param name="str">要轉換的文本內容</param>
        /// <returns></returns>
        public bool WriteToWAV(string filename, string str, SpeechAudioFormatType SpAudioType)
        {
            SpeechStreamFileMode SpFileMode = SpeechStreamFileMode.SSFMCreateForWrite;
            SpFileStream SpFileStream = new SpFileStream();
            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpAudioFormat SpAudio = new SpAudioFormat();
            SpAudio.Type = SpAudioType;
            SpFileStream.Format = SpAudio;
            SpFileStream.Open(filename, SpFileMode, false);
            voice.AudioOutputStream = SpFileStream;
            voice.Speak(str, SpFlags);
            voice.WaitUntilDone(Timeout.Infinite);
            SpFileStream.Close();
            return File.Exists(filename);
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

