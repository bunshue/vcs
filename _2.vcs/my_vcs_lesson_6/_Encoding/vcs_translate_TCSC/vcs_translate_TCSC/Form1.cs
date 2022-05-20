using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.IO;                        //for FileAccess, File


namespace vcs_translate_TCSC
{
    public partial class Form1 : Form
    {
        private string Big5toGB2312(string strBig5)
        {
            StringBuilder sb = new StringBuilder();
            byte[] tmp = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
            return Encoding.GetEncoding("gb2312").GetString(tmp); // 簡體中文 (GB2312) 
        }

        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        /// <summary>
        /// 將簡體中文字元轉換成繁體中文
        /// </summary>
        /// <param name="strGB2312"></param>
        /// <returns></returns>
        private string GB2312translateBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

        /// <summary>
        /// 將繁體中文字元轉換成簡體中文
        /// </summary>
        /// <param name="strBig5"></param>
        /// <returns></returns>
        private string Big5translateGB2312(string strBig5)
        {
            String tTarget = new String(' ', strBig5.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_SIMPLIFIED_CHINESE, strBig5, strBig5.Length, tTarget, strBig5.Length);
            return tTarget;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int border = 10;

            int W = 600;
            int H = 800;

            richTextBox_tc.Size = new Size(W, H);
            richTextBox_sc.Size = new Size(W, H);

            x_st = border;
            y_st = border;
            dx = border + 80 + border;   // border + 80 + border

            richTextBox_tc.Location = new Point(x_st, y_st);
            richTextBox_sc.Location = new Point(x_st + W + dx, y_st);

            bt_tc_sc.Location = new Point(x_st + W + 10, y_st + H * 1 / 3 - bt_tc_sc.Height);
            bt_sc_tc.Location = new Point(x_st + W + 10, y_st + H * 2 / 3 - bt_sc_tc.Height);

            lb_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - lb_tc.Size.Width, y_st);
            lb_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - lb_sc.Size.Width, y_st);

            bt_clear_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - bt_clear_tc.Size.Width, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_clear_tc.Size.Height);
            bt_copy_tc.Location = new Point(richTextBox_tc.Location.X + richTextBox_tc.Size.Width - bt_clear_tc.Size.Width - bt_copy_tc.Size.Width, richTextBox_tc.Location.Y + richTextBox_tc.Size.Height - bt_copy_tc.Size.Height);

            bt_clear_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - bt_clear_sc.Size.Width, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_clear_sc.Size.Height);
            bt_copy_sc.Location = new Point(richTextBox_sc.Location.X + richTextBox_sc.Size.Width - bt_clear_sc.Size.Width - bt_copy_sc.Size.Width, richTextBox_sc.Location.Y + richTextBox_sc.Size.Height - bt_copy_sc.Size.Height);

            this.ClientSize = new Size(border + W + dx + W + border, border + H + border);
        }

        private void bt_tc_sc_Click(object sender, EventArgs e)
        {
            //正中轉簡中
            richTextBox_sc.Text = Big5translateGB2312(this.richTextBox_tc.Text);
        }

        private void bt_sc_tc_Click(object sender, EventArgs e)
        {
            //簡中轉正中
            richTextBox_tc.Text = GB2312translateBig5(this.richTextBox_sc.Text);
        }

        private void bt_copy_tc_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox_tc.Text + "\n");      //建議用此
            richTextBox_tc.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_copy_sc_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox_sc.Text + "\n");      //建議用此
            richTextBox_sc.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_clear_tc_Click(object sender, EventArgs e)
        {
            richTextBox_tc.Clear();
        }

        private void bt_clear_sc_Click(object sender, EventArgs e)
        {
            richTextBox_sc.Clear();
        }
    }
}
