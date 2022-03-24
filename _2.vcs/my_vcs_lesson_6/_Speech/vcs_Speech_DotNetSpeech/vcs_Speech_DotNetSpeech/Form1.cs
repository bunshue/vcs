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

using DotNetSpeech; //for SpVoice

//使用DotNetSpeech 做 文字轉語音
//微軟 SAPI.SpVoice C# 使用方法

//參考/加入參考, 選DotNetSpeech.dll
//DotNetSpeech屬性/內嵌Interop型別 改false

namespace vcs_Speech_DotNetSpeech
{
    public partial class Form1 : Form
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
            int InputWordLength = 0;	//局部_朗讀長度
            int InputWordPosition = 0;	//局部_朗讀位置
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
        /// <param name="path">保存路徑</param>
        /// <param name="str">要轉換的文本內容</param>
        /// <returns></returns>
        public bool WreiteToWAV(string path, string str, SpeechAudioFormatType SpAudioType)
        {
            SpeechStreamFileMode SpFileMode = SpeechStreamFileMode.SSFMCreateForWrite;
            SpFileStream SpFileStream = new SpFileStream();
            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpAudioFormat SpAudio = new SpAudioFormat();
            SpAudio.Type = SpAudioType;
            SpFileStream.Format = SpAudio;
            SpFileStream.Open(path, SpFileMode, false);
            voice.AudioOutputStream = SpFileStream;
            voice.Speak(str, SpFlags);
            voice.WaitUntilDone(Timeout.Infinite);

            SpFileStream.Close();
            return File.Exists(path);
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var text = "In compupting, a system call is the mechanism used by an application program to request service from the operating system.";
            //var path = Path.Combine(@"C:\ZZ_VoiceFile", $"1.wav");
            text = AddKongGeToPlateNo(text).Trim();
            setRate(0);
            setVolume(100);
            WreiteToWAV("aaa.wav", text, SpeechAudioFormatType.SAFTCCITT_uLaw_11kHzMono); //SAFT11kHz16BitMono 生成wav文件
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
    }
}

