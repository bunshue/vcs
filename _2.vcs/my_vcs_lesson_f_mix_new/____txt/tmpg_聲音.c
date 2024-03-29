微软 SAPI.SpVoice C# 使用方法 + 实例


using System;
using System.Collections.Generic;
using System.Text;

using DotNetSpeech;
using System.Threading;
using System.IO;

namespace SpVoiceDemo
{
    class SpVoiceUtil
    {
        SpVoice voice = new DotNetSpeech.SpVoiceClass();

        public delegate void CallBack(bool b,int InputWordPosition, int InputWordLength); 

        /// <summary>
        /// 朗读文本
        /// </summary>
        /// <param name="str">要朗读的文本</param>
        /// <param name="CallBack">回调地址</param>
        /// <returns>返回bool</returns>
        public bool Speak(string str, CallBack CallBack)
        {
            int n = voice.Speak(str, SpeechVoiceSpeakFlags.SVSFlagsAsync);
            Thread thread = new Thread(new ParameterizedThreadStart(Call));
            thread.IsBackground = true;
            thread.Start((Object)CallBack);
            return !(n!=1);
        }


        /// <summary>
        /// 回调函数线程子程序
        /// </summary>
        /// <param name="callBack"></param>
        private void Call(Object callBack)
        {
            int InputWordLength = 0;    //局部_朗读长度
            int InputWordPosition = 0; //局部_朗读位置

            CallBack CallBack = (CallBack)callBack;

            while ((int)voice.Status.RunningState != 1)
            {
                if (InputWordPosition != voice.Status.InputWordPosition || InputWordLength != voice.Status.InputWordLength)
                {
                    InputWordPosition = voice.Status.InputWordPosition;
                    InputWordLength = voice.Status.InputWordLength;

                    //回调                  
                    CallBack(false, InputWordPosition, InputWordLength);
                }
            }
            CallBack(true, InputWordPosition, InputWordLength);
        }

        /// <summary>
        /// 获取语音库
        /// </summary>
        /// <returns>List<string></returns>
        public List<string> getDescription()
        {
            List<string> list = new List<string>();
            DotNetSpeech.ISpeechObjectTokens obj = voice.GetVoices();
            int count = obj.Count;//获取语音库总数
            for (int i = 0; i < count; i++)
            {
               string desc = obj.Item(i).GetDescription(); //遍历语音库
               list.Add(desc);
            }
            return list;
        }

        /// <summary>
        /// 设置当前使用语音库
        /// </summary>
        /// <returns>bool</returns>
        public bool setDescription(string name)
        {
            List<string> list = new List<string>();
            DotNetSpeech.ISpeechObjectTokens obj = voice.GetVoices();
            int count = obj.Count;//获取语音库总数
            bool result = false;
            for (int i = 0; i < count; i++)
            {
                string desc = obj.Item(i).GetDescription(); //遍历语音库
                if (desc.Equals(name))
                {
                    voice.Voice = obj.Item(i);
                    result = true;
                }
            }
            return result;
        }

        /// <summary>
        /// 设置语速
        /// </summary>
        /// <param name="n"></param>
        public void setRate(int n)
        {
            voice.Rate = n;
        }

        /// <summary>
        /// 设置声音大小
        /// </summary>
        /// <param name="n"></param>
        public void setVolume(int n)
        {
            voice.Volume = n;
        }

        /// <summary>
        /// 暂停
        /// </summary>
        public void Pause()
        {
            voice.Pause();
        }

        /// <summary>
        /// 继续
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
        /// 输出WAV
        /// </summary>
        /// <param name="path">保存路径</param>
        /// <param name="str">要转换的文本内容</param>
        /// <returns></returns>
        public bool WreiteToWAV(string path,string str,SpeechAudioFormatType SpAudioType)
        {
            SpeechStreamFileMode SpFileMode = SpeechStreamFileMode.SSFMCreateForWrite;
            SpFileStream SpFileStream = new SpFileStream();
            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpAudioFormat SpAudio = new DotNetSpeech.SpAudioFormat();
            SpAudio.Type = SpAudioType;
            SpFileStream.Format = SpAudio;
            SpFileStream.Open(path, SpFileMode, false);
            voice.AudioOutputStream = SpFileStream;
            voice.Speak(str, SpFlags);
            voice.WaitUntilDone(Timeout.Infinite);
            SpFileStream.Close();
            return File.Exists(path);
        }
    }
}

 


代码下载地址：http://download.csdn.net/detail/rootsuper/5039830
发布此文章仅为传递网友分享，不代表本站观点，若侵权请联系我们删除，本站将不对此承担任何责任。

    不懂技术不要对懂技术的人说这很容易实现
不懂技术不要对懂技术的人说这很容易实现

    我的丈夫是个程序员
我的丈夫是个程序员

    如何成为一名黑客
如何成为一名黑客

    聊聊HTTPS和SSL/TLS协议
聊聊HTTPS和SSL/TLS协议

    写给自己也写给你 自己到底该何去何从
写给自己也写给你 自己到底该何去何从

    漫画:程序员的工作
漫画:程序员的工作

    旅行，写作，编程
旅行，写作，编程

    为啥Android手机总会越用越慢？
为啥Android手机总会越用越慢？

C#-热门
C#-最新
C#-其它

    1请教逻辑层的类方法为什么要写成静态的啊
    2ThreadStart跟ParameterizedThreadStart区别
    3C# 中 byte[]转换成string 型 打印输出乱码,该如何解决
    4winform以管理员身份运行 dragdrop事件没有触发，请教怎么解决
    5请教各位大师怎么在对话框放大缩小时，实现字体随按钮缩放？
    6picturebox画图， 已经实现，求怎么保存图片
    7[小结]文件传输模型之文件中转
    8C#怎么调用MPI
    9npoi 生成Excel文档的一个有关问题
    10请教各位大师，怎么在c#工程中不使用第三方插件或组件实现多图层的处理

    上一篇：面向对象3大特性 之 多态(C#)
    下一篇：全排列跟组合算法的C#语言实现

文章评论
相关解决方案

    1FirstKeyOnlyFilter的使用方法及范例
    2范例解说 fdisk 使用方法
    3转（Jquery AutoComplete的使用方法范例）
    4KeyOnlyFilter使用方法及范例
    5关于C# WinForm FastReport Studio的使用方法
    6C#调用SAPI兑现语音合成的两种方法
    7C#调用SAPI兑现语音识别的两种方法
    8SpVoice的使用解决思路
    9Jquery AutoComplete的使用方法范例(网上找的留着备用)
    10Jquery AutoComplete自动完成 的使用方法范例

    做程序猿的老婆应该注意的一些事情
做程序猿的老婆应该注意的一些事情

    我跳槽是因为他们的显示器更大
我跳槽是因为他们的显示器更大

    10个调试和排错的小建议
10个调试和排错的小建议

    程序员的样子
程序员的样子

    每天工作4小时的程序员
每天工作4小时的程序员

    程序员应该关注的一些事儿
程序员应该关注的一些事儿

    程序员眼里IE浏览器是什么样的
程序员眼里IE浏览器是什么样的

    程序员都该阅读的书
程序员都该阅读的书

    10个帮程序员减压放松的网站
10个帮程序员减压放松的网站

    要嫁就嫁程序猿—钱多话少死的早
要嫁就嫁程序猿—钱多话少死的早

    老美怎么看待阿里赴美上市
老美怎么看待阿里赴美上市

    什么才是优秀的用户界面设计
什么才是优秀的用户界面设计

    程序员的鄙视链
程序员的鄙视链

    “肮脏的”IT工作排行榜
“肮脏的”IT工作排行榜

    十大编程算法助程序员走上高手之路
十大编程算法助程序员走上高手之路

    程序员周末都喜欢做什么？
程序员周末都喜欢做什么？

    5款最佳正则表达式编辑调试器
5款最佳正则表达式编辑调试器

    “懒”出效率是程序员的美德
“懒”出效率是程序员的美德

    如何区分一个程序员是“老手“还是“新手“？
如何区分一个程序员是“老手“还是“新手“？

    鲜为人知的编程真相
鲜为人知的编程真相

    科技史上最臭名昭著的13大罪犯
科技史上最臭名昭著的13大罪犯

    团队中“技术大拿”并非越多越好
团队中“技术大拿”并非越多越好

    编程语言是女人
编程语言是女人

    为什么程序员都是夜猫子
为什么程序员都是夜猫子

    程序员和编码员之间的区别
程序员和编码员之间的区别

    代码女神横空出世
代码女神横空出世

    中美印日四国程序员比较
中美印日四国程序员比较

    老程序员的下场
老程序员的下场

    总结2014中国互联网十大段子
总结2014中国互联网十大段子

软件开发程序错误异常ExceptionCopyright © 2009-2015 MyException 版权所有


