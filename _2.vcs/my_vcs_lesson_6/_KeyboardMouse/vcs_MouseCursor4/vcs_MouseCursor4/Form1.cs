using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Reflection;

namespace vcs_MouseCursor4
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll")]
        public static extern IntPtr LoadCursorFromFile(string fileName);

        [DllImport("user32", EntryPoint = "LoadCursorFromFile")]
        public static extern int IntLoadCursorFromFile(string lpFileName);

        [DllImport("user32", EntryPoint = "SetSystemCursor")]
        public static extern void SetSystemCursor(int hcur, int i);

        const int OCR_NORAAC = 32512;   //標準
        const int OCR_HAND = 32649;     //手
        const int OCR_NO = 32648;       //斜的圓
        const int OCR_SIZEALL = 32646;  //移動


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //改變本表單中的滑鼠游標
            richTextBox1.Text += "1111在窗体中改变鼠标样式\n";

            Cursor myCursor = new Cursor(Cursor.Current.Handle);
            IntPtr colorCursorHandle = LoadCursorFromFile("..//..//image/special.ani");//鼠标图标路径
            myCursor.GetType().InvokeMember("handle", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.SetField, null, myCursor, new object[] { colorCursorHandle });
            this.Cursor = myCursor;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //恢復
            richTextBox1.Text += "2222在窗体中还原鼠标样式\n";
            this.Cursor = Cursors.Default;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //設定滑鼠游標

            //將要修改的標鼠圖片存入到系統的WINDOWS\Cursors目錄下

            //改變系統中的滑鼠游標
            richTextBox1.Text += "3333設定正常選擇滑鼠游標\n";
            //設定正常選擇滑鼠游標
            int cur = IntLoadCursorFromFile("..//..//image/01.cur");
            SetSystemCursor(cur, OCR_NORAAC);
            //設定移動
            cur = IntLoadCursorFromFile("..//..//image/03.cur");
            SetSystemCursor(cur, OCR_SIZEALL);
            //設定不可用
            cur = IntLoadCursorFromFile("..//..//image/04.cur");
            SetSystemCursor(cur, OCR_NO);
            //設定超鏈接
            cur = IntLoadCursorFromFile("..//..//image/06.cur");
            SetSystemCursor(cur, OCR_HAND);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //恢復滑鼠游標
            richTextBox1.Text += "4444恢復正常選擇滑鼠游標\n";
            //恢復正常選擇滑鼠游標
            int cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\arrow_m.cur");
            SetSystemCursor(cur, OCR_NORAAC);
            //恢復移動
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\move_r.cur");
            SetSystemCursor(cur, OCR_SIZEALL);
            //恢復不可用
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\no_r.cur");
            SetSystemCursor(cur, OCR_NO);
            //恢復超鏈接
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\hand.cur");
            SetSystemCursor(cur, OCR_HAND);
        }
    }
}

