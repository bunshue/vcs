using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_ReadWritePrivateProfileString
{
    public partial class Form1 : Form
    {
        string filename = @"../../vcs_ReadWrite_INI5.ini";
        public string ini_filename = @"../../vcs_ReadWritePrivateProfileString.ini";
        public string path;
        //[DllImport("kernel32")]
        [DllImport("kernel32", CharSet = CharSet.Unicode)]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        //[DllImport("kernel32")]
        [DllImport("kernel32", CharSet = CharSet.Unicode)]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);
        public void IniWriteValue(string section, string key, string value, string path)
        {
            WritePrivateProfileString(section, key, value, path);
        }
        public string IniReadValue(string section, string key, string path)
        {
            StringBuilder temp = new StringBuilder(255);
            int i = GetPrivateProfileString(section, key, "", temp, 255, path);
            return temp.ToString();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            path = Application.StartupPath.ToString();
            path = path.Substring(0, path.LastIndexOf("\\"));
            path = path.Substring(0, path.LastIndexOf("\\"));
            path += @"\Setup.ini";

            richTextBox1.Text += path + "\n";

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            richTextBox1.Size = new Size(400, 600);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(660, 670);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        string MyCursor;
        string MyPicPath;

        private void button0_Click(object sender, EventArgs e)
        {
            //Read

            MyCursor = IniReadValue("Setup", "CapMouse", path);
            MyPicPath = IniReadValue("Setup", "Dir", path);

            richTextBox1.Text += "MyCursor : " + MyCursor + "\n";
            richTextBox1.Text += "MyPicPath : " + MyPicPath + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\dddddddddd";
            //Write        主欄位   次欄位      內容
            IniWriteValue("Setup", "CapMouse", "1111", path);
            IniWriteValue("Setup", "Dir", foldername, path);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Read ini data from " + ini_filename + "\n";
            try
            {
                if (File.Exists(ini_filename))
                {
                    richTextBox1.Text += IniReadValue("Language", "lang1", ini_filename) + "\n";
                    richTextBox1.Text += IniReadValue("Language", "lang2", ini_filename) + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            IniWriteValue("Language", "lang1", "AAAAA", ini_filename);
            IniWriteValue("Language", "lang2", "BBBBB", ini_filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用 StreamReader 讀取
            try
            {
                using (StreamReader oStreamReader = new StreamReader(filename, Encoding.Default))
                {
                    int iResult = -1;

                    //listBox1.Items.Clear();

                    do
                    {
                        richTextBox1.Text += oStreamReader.ReadLine() + "\n";
                        iResult = oStreamReader.Peek();

                    } while (iResult != -1);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            using (TINI oTINI = new TINI(filename))
            {
                string sResult = oTINI.getKeyValue("Test5", "1");　//Test5： Section；1：Key
                richTextBox1.Text += sResult + "\n";
            }
        }
    }

    public class TINI : IDisposable
    {
        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

        private bool bDisposed = false;
        private string _FilePath = string.Empty;
        public string FilePath
        {
            get
            {
                if (_FilePath == null)
                    return string.Empty;
                else
                    return _FilePath;
            }
            set
            {
                if (_FilePath != value)
                    _FilePath = value;
            }
        }

        /// <summary>
        /// 建構子。
        /// </summary>
        /// <param name="path">檔案路徑。</param>      
        public TINI(string path)
        {
            _FilePath = path;
        }

        /// <summary>
        /// 解構子。
        /// </summary>
        ~TINI()
        {
            Dispose(false);
        }

        /// <summary>
        /// 釋放資源(程式設計師呼叫)。
        /// </summary>
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this); //要求系統不要呼叫指定物件的完成項。
        }

        /// <summary>
        /// 釋放資源(給系統呼叫的)。
        /// </summary>        
        protected virtual void Dispose(bool IsDisposing)
        {
            if (bDisposed)
            {
                return;
            }
            if (IsDisposing)
            {
                //補充：

                //這裡釋放具有實做 IDisposable 的物件(資源關閉或是 Dispose 等..)
                //ex: DataSet DS = new DataSet();
                //可在這邊 使用 DS.Dispose();
                //或是 DS = null;
                //或是釋放 自訂的物件。
                //因為我沒有這類的物件，故意留下這段 code ;若繼承這個類別，
                //可覆寫這個函式。
            }

            bDisposed = true;
        }


        /// <summary>
        /// 設定 KeyValue 值。
        /// </summary>
        /// <param name="IN_Section">Section。</param>
        /// <param name="IN_Key">Key。</param>
        /// <param name="IN_Value">Value。</param>
        public void setKeyValue(string IN_Section, string IN_Key, string IN_Value)
        {
            WritePrivateProfileString(IN_Section, IN_Key, IN_Value, this._FilePath);
        }

        /// <summary>
        /// 取得 Key 相對的 Value 值。
        /// </summary>
        /// <param name="IN_Section">Section。</param>
        /// <param name="IN_Key">Key。</param>        
        public string getKeyValue(string IN_Section, string IN_Key)
        {
            StringBuilder temp = new StringBuilder(255);
            int i = GetPrivateProfileString(IN_Section, IN_Key, "", temp, 255, this._FilePath);
            return temp.ToString();
        }

        /// <summary>
        /// 取得 Key 相對的 Value 值，若沒有則使用預設值(DefaultValue)。
        /// </summary>
        /// <param name="Section">Section。</param>
        /// <param name="Key">Key。</param>
        /// <param name="DefaultValue">DefaultValue。</param>        
        public string getKeyValue(string Section, string Key, string DefaultValue)
        {
            StringBuilder sbResult = null;
            try
            {
                sbResult = new StringBuilder(255);
                GetPrivateProfileString(Section, Key, "", sbResult, 255, this._FilePath);
                return (sbResult.Length > 0) ? sbResult.ToString() : DefaultValue;
            }
            catch
            {
                return string.Empty;
            }
        }
    }
}

