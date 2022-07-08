using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}
