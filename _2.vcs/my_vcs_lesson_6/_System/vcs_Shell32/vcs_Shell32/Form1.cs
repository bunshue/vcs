using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//參考/加入參考/shell32.dll
//(備注:該引用是系統dll文件 在C:\Windows\System32\shell32.dll 目錄下 可以自行拷貝到項目中)
using Shell32;

namespace vcs_Shell32
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得所有檔案屬性1
            string filename = @"C:\______test_files\picture1.jpg";

            string filePath = filename;

            //實例化一個shell 對象

            //Shell32.Shell shell = new Shell32.ShellClass();

            Shell shell = new Shell();
            //獲取文件所在父目錄對象 
            Folder folder = shell.NameSpace(filePath.Substring(0, filePath.LastIndexOf('\\')));
            //獲取文件對應的FolderItem對象 
            FolderItem item = folder.ParseName(filePath.Substring(filePath.LastIndexOf('\\') + 1));
            //字典存放屬性名和屬性值的鍵值關系對 
            //Dictionary<string, string> Properties = new Dictionary<string, string>();
            int i = 0;
            while (true)
            {
                //獲取屬性名稱 
                string key = folder.GetDetailsOf(null, i);
                if (string.IsNullOrEmpty(key))
                {
                    //當無屬性可取時，推出循環 
                    break;
                }
                //獲取屬性值 
                string value = folder.GetDetailsOf(item, i);
                //保存屬性 
                //Properties.Add(key, value);

                richTextBox1.Text += "第 " + i.ToString() + " 項:\t" + key + " :\t" + value + '\n';  // 窗體界面上創建的richTextBox 控件上顯示所有的屬性值

                i++;
            }
        }

        /// <summary>
        /// 獲取指定文件指定下標的屬性值
        /// </summary>
        /// <param name="filePath">文件路徑</param>
        /// <param name="index">屬性下標</param>
        /// <returns>屬性值</returns>
        public static string GetPropertyByIndex(string filePath, int index)
        {
            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException("指定的文件不存在。", filePath);
            }

            //初始化Shell接口 
            //Shell32.Shell shell = new Shell32.ShellClass();
            Shell shell = new Shell();
            //獲取文件所在父目錄對象 
            Folder folder = shell.NameSpace(Path.GetDirectoryName(filePath));
            //獲取文件對應的FolderItem對象 
            FolderItem item = folder.ParseName(Path.GetFileName(filePath));
            string value = null;

            //獲取屬性名稱 
            string key = folder.GetDetailsOf(null, index);
            if (false == string.IsNullOrEmpty(key))
            {
                //獲取屬性值 
                value = folder.GetDetailsOf(item, index);
            }
            return value;
        }

        /// <summary>
        /// 獲取指定文件指定屬性名的值
        /// </summary>
        /// <param name="filePath">文件路徑</param>
        /// <param name="propertyName">屬性名</param>
        /// <returns>屬性值</returns>
        public static string GetProperty(string filePath, string propertyName)
        {
            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException("指定的文件不存在。", filePath);

            }

            //初始化Shell接口 
            //Shell32.Shell shell = new Shell32.ShellClass();
            Shell shell = new Shell();

            //獲取文件所在父目錄對象 
            Folder folder = shell.NameSpace(Path.GetDirectoryName(filePath));
            //獲取文件對應的FolderItem對象 
            FolderItem item = folder.ParseName(Path.GetFileName(filePath));
            string value = null;
            int i = 0;
            while (true)
            {
                //獲取屬性名稱 
                string key = folder.GetDetailsOf(null, i);
                if (string.IsNullOrEmpty(key))
                {
                    //當無屬性可取時，退出循環 
                    break;
                }
                if (true == string.Equals(key, propertyName, StringComparison.CurrentCultureIgnoreCase))
                {
                    //獲取屬性值 
                    value = folder.GetDetailsOf(item, i);
                    break;
                }
                i++;
            }
            return value;
        }

        /// <summary>
        /// 存儲屬性名與其下標（key值均為小寫）
        /// </summary>

        private static Dictionary<string, int> _propertyIndex = null;

        /// <summary>
        /// 獲取指定文件指定屬性名的值
        /// </summary>
        /// <param name="filePath">文件路徑</param>
        /// <param name="propertyName">屬性名</param>
        /// <returns>屬性值</returns>

        public static string GetPropertyEx(string filePath, string propertyName)
        {
            if (_propertyIndex == null)
            {
                InitPropertyIndex();
            }

            //轉換為小寫
            string propertyNameLow = propertyName.ToLower();
            if (_propertyIndex.ContainsKey(propertyNameLow))
            {
                int index = _propertyIndex[propertyNameLow];
                return GetPropertyByIndex(filePath, index);
            }
            return null;
        }

        /// <summary>
        /// 初始化屬性名的下標
        /// </summary>
        private static void InitPropertyIndex()
        {
            /*
            Dictionary<string, int> propertyIndex = new Dictionary<string, int>();
            //獲取本代碼所在的文件作為臨時文件，用於獲取屬性列表
            string tempFile = System.Reflection.Assembly.GetExecutingAssembly().FullName;
            Dictionary<string, string> allProperty = GetProperties(tempFile);
            if (allProperty != null)
            {
                int index = 0;
                foreach (var item in allProperty.Keys)
                {
                    //屬性名統一轉換為小寫，用於忽略大小寫
                    _propertyIndex.Add(item.ToLower(), index);
                    index++;
                }
            }

            _propertyIndex = propertyIndex;
            */
        }

        /// <summary> /// 獲取檔案屬性字典 /// </summary> 
        /// <param name="filePath">檔案路徑</param> 
        /// <returns>屬性字典</returns> 
        public Dictionary<string, string> GetProperties(string filePath)
        {
            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException("指定的檔案不存在。", filePath);
            }
            //初始化Shell介面 
            //Shell32.Shell shell = new Shell32.ShellClass();
            Shell shell = new Shell();
            //ShellClass shell = new ShellClass();

            //獲取檔案所在父目錄物件
            Folder folder = shell.NameSpace(Path.GetDirectoryName(filePath));
            //獲取檔案對應的FolderItem物件
            FolderItem item = folder.ParseName(Path.GetFileName(filePath));
            //字典存放屬性名和屬性值的鍵值關係對
            Dictionary<string, string> Properties = new Dictionary<string, string>();
            int i = 0;
            while (true)
            {
                //獲取屬性名稱
                string key = folder.GetDetailsOf(null, i);
                if (string.IsNullOrEmpty(key))
                {
                    //當無屬性可取時,退出迴圈
                    break;
                }
                //獲取屬性值
                string value = folder.GetDetailsOf(item, i);
                //儲存屬性
                if (i != 36)
                    Properties.Add(key, value);
                richTextBox1.Text += "第 " + i.ToString() + " 項:\t" + key + " :\t" + value + '\n';  // 窗體界面上創建的richTextBox 控件上顯示所有的屬性值
                i++;
            }
            return Properties;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            //取得所有檔案屬性2

            string filename = @"C:\______test_files\picture1.jpg";

            Dictionary<string, int> _propertyIndex2 = new Dictionary<string, int>();

            Dictionary<string, int> propertyIndex = new Dictionary<string, int>();

            richTextBox1.Text += "filename = " + filename + "\n";

            Dictionary<string, string> allProperty = GetProperties(filename);
            if (allProperty != null)
            {
                int index = 0;
                foreach (var item in allProperty.Keys)
                {
                    //屬性名統一轉換為小寫，用於忽略大小寫
                    _propertyIndex2.Add(item.ToLower(), index);
                    index++;
                }
            }

            _propertyIndex2 = propertyIndex;




        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得一項檔案屬性1
            string filename = @"C:\______test_files\picture1.jpg";

            string result = GetPropertyByIndex(filename, 31);
            richTextBox1.Text += "尺寸 : " + result + "\n";


            result = GetProperty(filename, "尺寸");
            richTextBox1.Text += "尺寸 : " + result + "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得一項檔案屬性2
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得檔案內容中的詳細資料\n";

            string filename = @"C:\______test_files\picture1.jpg";

            int i;
            for (i = 0; i < 30; i++)
            {
                string result = GetDetailValue(filename, i);
                richTextBox1.Text += i.ToString() + "\t" + result + "\n";
            }
        }

        static string GetDetailValue(string file, int column)
        {
            Shell shell = new Shell();
            Folder dir = shell.NameSpace(Path.GetDirectoryName(file));
            FolderItem item = dir.ParseName(Path.GetFileName(file));
            return dir.GetDetailsOf(item, column);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得媒體資訊
            //使用Shell32讀取影音文件屬性
            /*
            由於需要用到實時讀取影音文件(mp3、wma、wmv …)播放時間長度的功能，搜索到的結果有：
            （1）硬編碼分析影音文件，需要分析各種媒體格式，代價最大；
            （2）使用WMLib SDK，需要熟悉SDK各個接口，且不同版本的WM接口有別，代價次之；
            （3）使用系統Shell32的COM接口，直接訪問媒體文體屬性，取其特定內容，代價最小。
            顯然第3種方案見效最快，立即操刀：
            ①引用Shell32底層接口c:\windows\system32\shell32.dll，VS自動轉換成Interop.Shell32.dll（注：64位系統和32位系統生成的Interop.Shell32.dll不一樣）
            ②編碼讀取播放時間長度：
            */

            //取得媒體資訊
            //string filename = @"C:\______test_files\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\______test_files\_mp3\aaaa.mp3";
            int i;
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + GetMediaInfo(filename, i) + "\n";
            }
        }

        public string GetMediaInfo(string path, int item)
        {
            //參考/Shell32/右鍵/屬性/內嵌Interop型別改成False
            try
            {
                string result = string.Empty;
                Shell shell = new ShellClass();
                Folder folder = shell.NameSpace(path.Substring(0, path.LastIndexOf("\\")));
                FolderItem folderItem = folder.ParseName(path.Substring(path.LastIndexOf("\\") + 1));
                return folder.GetDetailsOf(folderItem, item);

                /* another
                ShellClass sh = new ShellClass();
                Folder dir = sh.NameSpace(Path.GetDirectoryName(sFile));
                FolderItem item = dir.ParseName(Path.GetFileName(sFile));
                string det = dir.GetDetailsOf(item, iCol);
                */
            }
            catch (Exception ex)
            {
                return null;
            }
        }

    }
}

