using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

//窗體的縮放效果 AnimateWindow

namespace vcs_Form5_OnLoad
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", EntryPoint = "AnimateWindow")]
        private static extern bool AnimateWindow(IntPtr handle, int ms, int flags);

        /*
        //flags的取值如下
        public const Int32 AW_HOR_POSITIVE = 0x00000001; //從左到右顯示
        public const Int32 AW_HOR_NEGATIVE = 0x00000002; //從右到左顯示
        public const Int32 AW_VER_POSITIVE = 0x00000004; //從上到下顯示
        public const Int32 AW_VER_NEGATIVE = 0x00000008; //從下到上顯示
        public const Int32 AW_CENTER = 0x00000010; //若使用了AW_HIDE標誌，則使窗口向內重疊，即收縮窗口；否則使窗口向外擴展，即展開窗口
        public const Int32 AW_HIDE = 0x00010000; //隱藏窗口，缺省則顯示窗口
        public const Int32 AW_ACTIVATE = 0x00020000; //激活窗口。 在使用了AW_HIDE標誌後不能使用這個標誌
        public const Int32 AW_SLIDE = 0x00040000; //使用滑動類型。 缺省則為滾動動畫類型。 當使用AW_CENTER標誌時，這個標誌就被忽略
        public const Int32 AW_BLEND = 0x00080000; //透明度從高到低
        */
        /*
        API函數值:
        0:無動畫
        2:從右到左
        1,3:從左到右
        4,12從上到下
        5,7,13左上到右下
        6,14右上到左下
        8下到上
        9,11左下到右上
        10右下到左上
        16中間到四周

        用法:   設定三千毫秒

        AnimateWindow(this.Handle, 3000, AW_VER_POSITIVE | AW_HIDE);//關
        AnimateWindow(this.Handle, 3000, AW_VER_POSITIVE | AW_ACTIVATE);//開

        */

        public Form1()
        {
            InitializeComponent();
            this.StartPosition = FormStartPosition.CenterScreen;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        protected override void OnLoad(EventArgs e)
        {
            base.OnLoad(e);
            AnimateWindow(this.Handle, 1000, 0x20010);   // 居中逐漸顯示。
            //AnimateWindow(this.Handle, 1000, 0xA0000); // 淡入淡出效果。
            //AnimateWindow(this.Handle, 1000, 0x60004); // 自上向下。
            //AnimateWindow(this.Handle, 1000, 0x20004); // 自上向下。
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            base.OnFormClosing(e);
            AnimateWindow(this.Handle, 1000, 0x10010);    // 居中逐漸隱藏。
            //AnimateWindow(this.Handle, 1000, 0x90000); // 淡入淡出效果。
            //AnimateWindow(this.Handle, 1000, 0x50008); // 自下而上。
            //AnimateWindow(this.Handle, 1000, 0x10008); // 自下而上。
        }
    }
}

