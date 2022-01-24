using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;

using System.IO;
using System.Net;
using System.Web;

using System.Data.OleDb;    //for OleDbConnection


using System.Runtime.InteropServices;
using System.Resources;

using System.Diagnostics;   //for FileVersionInfo

using System.Text.RegularExpressions;

using System.Threading;

namespace test4_romeo
{
    public partial class Form1 : Form
    {
        //定義OleDb======================================================
        //1.檔案位置    注意絕對路徑 -> 非 \  是 \\
        //private const string FileName = "C:\\Users\\user\\documents\\visual studio 2010\\Projects\\WindowsFormsApplication1\\WindowsFormsApplication1\\Data\\Book1.xlsx";
        private const string FileName = @"C:\______test_files\__RW\_excel\excel_20210602_131921.xls";
        //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
        //private const string ProviderName = "Microsoft.ACE.OLEDB.12.0;";
        private const string ProviderName = "Microsoft.Jet.OLEDB.4.0;";
        //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
        private const string ExtendedString = "'Excel 8.0;";
        //4.第一行是否為標題
        private const string Hdr = "Yes;";
        //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取
        private const string IMEX = "0';";
        //=============================================================

        //連線字串
        string cs =
                "Data Source=" + FileName + ";" +
                "Provider=" + ProviderName +
                "Extended Properties=" + ExtendedString +
                "HDR=" + Hdr +
                "IMEX=" + IMEX;
        //Excel 的工作表名稱 (Excel左下角有的分頁名稱)
        string SheetName = "Sheet1";

        public delegate void mydelegate();
        public mydelegate eventMethod;
        private static Form1 pLoading = new Form1();
        delegate void SetTextCallback(string title, string caption, string description);
        delegate void CloseFormCallback();
        
        public Form1()
        {
            InitializeComponent();

            initLoadintForm();
            Thread t = new Thread(new ThreadStart(delegateEventMethod));
            t.IsBackground = true;
            t.Start();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (!this.IsDisposed)
            {
                this.Dispose(true);
            }

        }

        private void initLoadintForm()
        {
            this.ControlBox = false;   // 設置不出現關閉按鈕
            this.StartPosition = FormStartPosition.CenterParent;
        }

        private void delegateEventMethod()
        {
            eventMethod();
        }

        public static Form1 getLoading()
        {
            if (pLoading.IsDisposed)
            {
                pLoading = new Form1();
                return pLoading;
            }
            else
            {
                return pLoading;
            }
        }

        //這種方法演示如何在線程安全的模式下調用Windows窗體上的控件。  
        /// <summary>
        /// 設置Loading 窗體的 標題title,標簽 caption 和描述 description
        /// </summary>
        /// <param name="title">窗口的標題[為空時，取默認值]</param>
        /// <param name="caption">標簽（例如:please wait）[為空時，取默認值]</param>
        /// <param name="description">描述(例如：正在加載資源...)[為空時，取默認值]</param>
        public void SetCaptionAndDescription(string title, string caption, string description)
        {
            if (this.InvokeRequired && lbl_caption.InvokeRequired && lbl_description.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(SetCaptionAndDescription);
                this.Invoke(d, new object[] { title, caption, description });
            }
            else
            {
                if (!title.Equals(""))
                {
                    this.Text = title;
                }
                if (!caption.Equals(""))
                {
                    Form1.lbl_caption.Text = caption;
                }
                if (!description.Equals(""))
                {
                    Form1.lbl_description.Text = description;
                }
            }
        }

        public void CloseLoadingForm()
        {
            if (this.InvokeRequired)
            {
                CloseFormCallback d = new CloseFormCallback(CloseLoadingForm);
                this.Invoke(d, new object[] { });
            }
            else
            {
                if (!this.IsDisposed)
                {
                    this.Dispose(true);
                }
            }
        }

        public void SetExecuteMethod(mydelegate method)
        {
            this.eventMethod += method;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            using (OleDbConnection cn = new OleDbConnection(cs))
            {
                cn.Open();
                string qs = "select * from[" + SheetName + "$]";
                try
                {
                    using (OleDbDataAdapter dr = new OleDbDataAdapter(qs, cn))
                    {
                        DataTable dt = new DataTable();
                        dr.Fill(dt);
                        this.dataGridView1.DataSource = dt;
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //C#獲取網頁源碼，自動判斷網頁字符集編碼

        }

        private string getHtml(string url, string charSet)//url是要訪問的網站地址，charSet是目標網頁的編碼，如果傳入的是null或者""，那就自動分析網頁的編碼
        {
            WebClient myWebClient = new WebClient(); //創建WebClient實例myWebClient

            // 需要注意的：
            //有的網頁可能下不下來，有種種原因比如需要cookie,編碼問題等等
            //這是就要具體問題具體分析比如在頭部加入cookie 
            // webclient.Headers.Add("Cookie", cookie); 
            //這樣可能需要一些重載方法。根據需要寫就可以了
            //獲取或設置用於對向 Internet 資源的請求進行身份驗證的網絡憑據。

            myWebClient.Credentials = CredentialCache.DefaultCredentials;
            //如果服務器要驗證用戶名,密碼
            //NetworkCredential mycred = new NetworkCredential(struser, strpassword);
            //myWebClient.Credentials = mycred;
            //從資源下載數據並返回字節數組。（加@是因為網址中間有"/"符號）
            byte[] myDataBuffer = myWebClient.DownloadData(url);
            string strWebData = Encoding.Default.GetString(myDataBuffer);

            //獲取網頁字符編碼描述信息
            Match charSetMatch = Regex.Match(strWebData, "<meta([^<]*)charset=([^<]*)\"", RegexOptions.IgnoreCase | RegexOptions.Multiline);
            string webCharSet = charSetMatch.Groups[2].Value;
            if (charSet == null || charSet == "")
                charSet = webCharSet;

            if (charSet != null && charSet != "" && Encoding.GetEncoding(charSet) != Encoding.Default)
                strWebData = Encoding.GetEncoding(charSet).GetString(myDataBuffer);
            return strWebData;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取屏幕的分辨率，也就是顯示器屏幕的大小。
            int W = SystemInformation.PrimaryMonitorSize.Width;
            int H = SystemInformation.PrimaryMonitorSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

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

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }
}

