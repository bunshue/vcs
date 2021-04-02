using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace SnatchPlayTime
{
    public partial class SnatchPlayTime : Form
    {
        public SnatchPlayTime()
        {
            InitializeComponent();
        }

        private void unfold_Click(object sender,EventArgs e)
        {
            OpenFileDialog MP3Dialog = new OpenFileDialog();//声明一个提示用户打开文件的对象
            MP3Dialog.Filter = "MP3文件(*.MP3)|*.MP3"; //获取或设置当前文件名筛选器字符串，该字符串决定对话框的“另存为文件类型”或“文件类型”框中出现的选择内容。 （继承自 FileDialog。）
            if(MP3Dialog.ShowDialog() == DialogResult.OK) //当选定文件之后单击“打开”按钮时
            {
                filePath.Text = MP3Dialog.FileName;//在文本框中显示打开文件的文件路径
            }
        }

        private void snatch_Click(object sender,EventArgs e)
        {
            string fileName = System.IO.Path.GetFileName (filePath.Text);//获取指定路径下的文件名
            playTime.Text = GetFileTime(LongTime(fileName));//在文本框中显示歌曲的播放时间
        }

        #region  获取文件的播放时间，并在列表中进行显示
        /// <summary>
        /// 获取文件的播放时间，并在列表中进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        //添加using System.Runtime.InteropServices;API函数的命名空间
        [DllImport("kernel32.dll",CharSet = CharSet.Auto)]
        public static extern int GetShortPathName(string lpszLongPath,string shortFile,int cchBuffer);//获取指定文件的短路径名

        [DllImport("winmm.dll",EntryPoint = "mciSendString",CharSet = CharSet.Auto)]
        public static extern int mciSendString(string lpstrCommand,string lpstrReturnString,int uReturnLength,int hwndCallback);//播放多媒体文件

        public int LongTime(string Spath)
        {
            string Pname = "";//用来保存多媒体文件的命令       
            string TemStr = "";//用来保存处理后的字符串
            int ilong = 0;//用来保存短路径文件名
            string tem_str = "";//用来保存最终的文件名
            int t = 0;//声明一个用来保存时间的变量
            TemStr = TemStr.PadLeft(128,Convert.ToChar(" "));//右对齐此实例中的字符，在左边用空格或指定的 Unicode 字符填充以达到指定的总长度
            ilong = GetShortPathName(Spath,TemStr,TemStr.Length);//获取指定路径下的短路径文件名
            Pname = "open " + Convert.ToChar(34) + Spath + Convert.ToChar(34) + " alias media";//为变量Pname赋值
            t = mciSendString(Pname,TemStr,TemStr.Length,0);//打开指定的多媒体文件
            t = mciSendString("status " + Spath + " length",TemStr,128,0);//获取当前多媒体文件的状态
            tem_str = TemStr.Substring(0,TemStr.IndexOf("\0"));//为变量tem_str赋值
            if(tem_str.Trim() == "")//当变量tem_str的值为空时
                t = 0;//设定变量t的值为0
            else//当变量tem_str的值为非空时
                t = Convert.ToInt32(tem_str);//重新设定变量t的值
            return t;//返回变量t的值
        }
        #endregion

        #region  获取文件的播放时间，并按指定格式进行显示
        /// <summary>
        /// 获取文件的播放时间，并按指定格式进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        public string GetFileTime(int Millisecond)
        {
            string Tem_Time = ""; //用来保存歌曲的播放时间
            double Tem_min = 0;  //用来保存歌曲播放的分钟部分
            double Tem_sec = 0;  //用来保存歌曲播放时间的秒
            double Tem_millisec = 0; //用来保存歌曲播放时间的毫秒

            Tem_min = Millisecond / 1000;//将当前时间转化为以秒为单位的数据类型
            Tem_min = Tem_min / 60.0; //将当前时间转化为以分为单位的数据类型

            Tem_sec = Tem_min - (int)Tem_min; //保存歌曲播放时间的小数部分（当以分为单位时）
            Tem_min = (int)Tem_min; //将double型变量Tem_min转化为int型变量
            Tem_sec = (60 * Tem_sec) / 100.0; //将获得的小数转化为以秒为单位的数据
            Tem_sec = (int)(Tem_sec * 100);//将数据类型转化为int型
            Tem_millisec = (int)((Millisecond - Tem_min * 60 * 1000 - Tem_sec * 1000) / 1000 * 100);//将歌曲播放的时间转换为以秒为单位存储
            if(Tem_min >= 100)//当Tem_min的值大于等于100时
            {
                Tem_Time = Tem_min.ToString("000") + ":" + Tem_sec.ToString("00");//设置时间的显示格式
            }
            else//当Tem_min的值小于100时
                Tem_Time = Tem_min.ToString("00") + ":" + Tem_sec.ToString("00"); //设置事件的显示格式
            return Tem_Time;//返回变量Tem_Time
        }
        #endregion

        private void filePath_TextChanged(object sender,EventArgs e)
        {
            if(filePath.Text != "" && filePath.Text != null)//当文本框中内容不为空且存在时
            {
                snatch.Enabled = true;//设置“获取”按钮为可用状态
            }
            else//当文本框中内容为空或这不存在时
            {
                snatch.Enabled = false;//设置“获取”按钮为不可用状态
            }
        }
    }
}
