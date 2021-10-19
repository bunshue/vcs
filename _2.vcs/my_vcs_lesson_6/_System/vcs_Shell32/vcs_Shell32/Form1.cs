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

    }
}

