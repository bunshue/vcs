using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Reflection;    //for Assembly
using System.Diagnostics;   //for FileVersionInfo

namespace vcs_Assembly
{
    public partial class Form1 : Form
    {
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

            //button
            x_st = 10;
            y_st = 10;
            dx = 170 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //Get APP Info
            string result = appInfo();
            richTextBox1.Text += result + "\n";
        }

        public static string appInfo()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fvi = FileVersionInfo.GetVersionInfo(assembly.Location);
            string result = "File Version: " + fvi.FileVersion
                + Environment.NewLine + "Company Name: " + fvi.CompanyName
                + Environment.NewLine + "Comments: " + fvi.Comments
                + Environment.NewLine + "Product Name: " + fvi.ProductName
                + Environment.NewLine + "Copyright: " + fvi.LegalCopyright
                + Environment.NewLine + "File Name: " + fvi.FileName
                + Environment.NewLine + "Original File Name: " + fvi.OriginalFilename
                + Environment.NewLine + "Product Version: " + fvi.ProductVersion
                + Environment.NewLine + "Special build: " + fvi.SpecialBuild
                + Environment.NewLine + "" + fvi.CompanyName;
            return result;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取exe版本號
            //讀取exe版本號

            string filename = @"C:\______test_files\_material\_dll\AForge.Video.dll";

            Assembly currentAssembly = Assembly.LoadFile(filename);
            //Assembly updatedAssembly = Assembly.LoadFile(updatedAssemblyPath);

            AssemblyName currentAssemblyName = currentAssembly.GetName();
            //AssemblyName updatedAssemblyName = updatedAssembly.GetName();

            richTextBox1.Text += currentAssembly.GetName() + "\n";



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //通過exe文件獲得版本

            //通過exe文件獲得版本

            //string path = @"C:\Program Files (x86)\ArcGIS\Desktop10.8\bin\ArcMap.exe";
            string path = @"vcs_Assembly.exe";

            richTextBox1.Text += "版本 : " + GetVersion(path) + "\n";
        }

        public string GetVersion(string path)
        {
            string version = string.Empty;
            FileVersionInfo file = FileVersionInfo.GetVersionInfo(path);
            //版本号显示为“主版本号.次版本号.内部版本号.专用部件号”。
            //version = String.Format("{0}.{1}.{2}.{3}", file.FileMajorPart, file.FileMinorPart, file.FileBuildPart, file.FilePrivatePart);
            //使用文件版本信息
            version = file.FileVersion;
            return version;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得目前應用程式版本
            richTextBox1.Text += "本程式版本資訊 : " + "Ver：" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得NOTEPAD版本資訊
            richTextBox1.Text += "取得NOTEPAD版本資訊 : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //獲取反射信息1

            //reflecting reflect=new reflecting();//定義一個新的自身類
            //調用一個reflecting.exe程序集

            Assembly myAssembly = Assembly.LoadFrom("vcs_Assembly.exe");
            getreflectioninfo(myAssembly);
            //reflect.getreflectioninfo(myAssembly);//獲取反射信息
        }

        //定義一個獲取反射內容的方法
        void getreflectioninfo(Assembly myassembly)
        {
            Type[] typearr = myassembly.GetTypes();//獲取類型

            foreach (Type type in typearr)//針對每個類型獲取詳細信息
            {
                //獲取類型的結構信息
                ConstructorInfo[] myconstructors = type.GetConstructors();
                Console.WriteLine(myconstructors.ToString());

                //獲取類型的字段信息
                FieldInfo[] myfields = type.GetFields();
                Console.WriteLine(myfields.ToString());

                //獲取方法信息
                MethodInfo[] myMethodInfo = type.GetMethods();
                Console.WriteLine(myMethodInfo.ToString());

                //獲取屬性信息
                PropertyInfo[] myproperties = type.GetProperties();
                Console.WriteLine(myproperties.ToString());

                //獲取事件信息
                EventInfo[] Myevents = type.GetEvents();
                Console.WriteLine(Myevents.ToString());
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //獲取反射信息2
            string fname = "vcs_Assembly.exe";

            Assembly assembly = null;
            try
            {
                // try to load assembly
                assembly = Assembly.LoadFrom(fname);

                // get types of the assembly
                Type[] types = assembly.GetTypes();

                // check all types
                foreach (Type type in types)
                {
                    // get interfaces ot the type
                    Type[] interfaces = type.GetInterfaces();
                }
            }
            catch (Exception)
            {
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //取得Assembly資料
            richTextBox1.Text += "取得Assembly資料\n";

            richTextBox1.Text += "Title\t" + String.Format("關於 {0}", AssemblyTitle) + "\n";
            richTextBox1.Text += "Product\t" + AssemblyProduct + "\n";
            richTextBox1.Text += "Version\t" + String.Format("版本 {0}", AssemblyVersion) + "\n";
            richTextBox1.Text += "Copyright\t" + AssemblyCopyright + "\n";
            richTextBox1.Text += "Company\t" + AssemblyCompany + "\n";
            richTextBox1.Text += "Description\t" + AssemblyDescription + "\n";

            Assembly assembly = this.GetType().Assembly;
            richTextBox1.Text += "取得專案名稱 : " + assembly.GetName().Name + "\n";

            //取得目前執行程式的名字 與所在的資料夾
            string sPath = System.Reflection.Assembly.GetExecutingAssembly().Location;
            string installDirectory = Path.GetDirectoryName(sPath) + @"\";
            richTextBox1.Text += "取得目前執行程式的名字 = " + sPath + "\n";
            richTextBox1.Text += "取得目前執行程式所在的資料夾 = " + installDirectory + "\n";

        }

        #region 組件屬性存取子
        public string AssemblyTitle
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyTitleAttribute), false);
                if (attributes.Length > 0)
                {
                    AssemblyTitleAttribute titleAttribute = (AssemblyTitleAttribute)attributes[0];
                    if (titleAttribute.Title != "")
                    {
                        return titleAttribute.Title;
                    }
                }
                return System.IO.Path.GetFileNameWithoutExtension(Assembly.GetExecutingAssembly().CodeBase);
            }
        }

        public string AssemblyVersion
        {
            get
            {
                return Assembly.GetExecutingAssembly().GetName().Version.ToString();
            }
        }

        public string AssemblyDescription
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyDescriptionAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyDescriptionAttribute)attributes[0]).Description;
            }
        }

        public string AssemblyProduct
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyProductAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyProductAttribute)attributes[0]).Product;
            }
        }

        public string AssemblyCopyright
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCopyrightAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyCopyrightAttribute)attributes[0]).Copyright;
            }
        }

        public string AssemblyCompany
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCompanyAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyCompanyAttribute)attributes[0]).Company;
            }
        }
        #endregion

        private void button8_Click(object sender, EventArgs e)
        {
            //取得專案內所有表單名稱

            //取得專案內所有表單名稱

            Assembly a = Assembly.GetExecutingAssembly();       //取得目前組件

            richTextBox1.Text += "目前組件 : " + a.ToString() + "\n";
            richTextBox1.Text += "CodeBase : " + a.CodeBase.ToString() + "\n";
            richTextBox1.Text += "FullName : " + a.FullName.ToString() + "\n";
            richTextBox1.Text += "Location : " + a.Location.ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetType().ToString() + "\n";
            richTextBox1.Text += "GetName : " + a.GetName() + "\n";
            richTextBox1.Text += "ImageRuntimeVersion : " + a.ImageRuntimeVersion + "\n";

            foreach (Type t in a.GetTypes())                    //找尋組件內所有類別型態
            {
                richTextBox1.Text += t.ToString() + "\n";

                if (t.IsSubclassOf(typeof(Form)))           //如果父類別是繼承自Form的話
                {
                    //richTextBox1.Text += t.ToString() + "\n"; //列出該類別資訊
                }
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}
