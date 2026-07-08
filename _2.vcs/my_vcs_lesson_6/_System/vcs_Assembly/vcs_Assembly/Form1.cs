using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Reflection;  // for Assembly

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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(600, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1060, 750);
            this.Text = "vcs_Assembly";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取exe版本號 決定要不要更新(複製檔案)

            //原檔
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\_material\_dll\AForge.Video.dll";
            //新檔
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\_material\_dll\AForge.Video.dll";

            Assembly asm1 = Assembly.LoadFile(filename1);
            Assembly asm2 = Assembly.LoadFile(filename2);

            AssemblyName asm_Name1 = asm1.GetName();
            AssemblyName asm_Name2 = asm2.GetName();

            richTextBox1.Text += asm1.GetName() + "\n";

        // 比較版本號
            if (asm_Name2.Version.CompareTo(asm_Name1.Version) <= 0)
            {
                // 不需要更新
                return;
            }

            //AssemblyName asm_Name1 = AssemblyName.GetAssemblyName(filename1);
            //AssemblyName asm_Name2 = AssemblyName.GetAssemblyName(filename2);

            // 比較版本
            if (asm_Name2.Version.CompareTo(asm_Name1.Version) <= 0)
            {
                // 不需要更新
                return;
            }
            else
            {
                // 更新
                // File.Copy(filename2, filename1, true);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //獲取反射信息1

            //reflecting reflect=new reflecting();//定義一個新的自身類
            //調用一個reflecting.exe程序集

            Assembly asm = Assembly.LoadFrom("vcs_Assembly.exe");
            getreflectioninfo(asm);
            //reflect.getreflectioninfo(asm);//獲取反射信息
        }

        //定義一個獲取反射內容的方法
        void getreflectioninfo(Assembly asm)
        {
            Type[] typearr = asm.GetTypes();//獲取類型

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

            Assembly asm = null;
            try
            {
                asm = Assembly.LoadFrom(fname);

                Type[] types = asm.GetTypes();

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

            Assembly asm = this.GetType().Assembly;
            richTextBox1.Text += "取得專案名稱 : " + asm.GetName().Name + "\n";

            //取得目前執行程式的名字 與所在的資料夾
            string sPath = System.Reflection.Assembly.GetExecutingAssembly().Location;
            string installDirectory = Path.GetDirectoryName(sPath) + @"\";
            richTextBox1.Text += "取得目前執行程式的名字 = " + sPath + "\n";
            richTextBox1.Text += "取得目前執行程式所在的資料夾 = " + installDirectory + "\n";
        }

        //#region 組件屬性存取子
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
        //#endregion

        private void button8_Click(object sender, EventArgs e)
        {
            //取得專案內所有表單名稱

            Assembly asm = Assembly.GetExecutingAssembly();       //取得目前組件

            richTextBox1.Text += "目前組件 : " + asm.ToString() + "\n";
            richTextBox1.Text += "CodeBase : " + asm.CodeBase.ToString() + "\n";
            richTextBox1.Text += "FullName : " + asm.FullName.ToString() + "\n";
            richTextBox1.Text += "Location : " + asm.Location.ToString() + "\n";
            richTextBox1.Text += "GetType : " + asm.GetType().ToString() + "\n";
            richTextBox1.Text += "GetName : " + asm.GetName() + "\n";
            richTextBox1.Text += "ImageRuntimeVersion : " + asm.ImageRuntimeVersion + "\n";

            foreach (Type t in asm.GetTypes())                    //找尋組件內所有類別型態
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
            //Assembly 大全集

            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            richTextBox1.Text += "location : " + location + "\n";
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";

            string namespaceName = Assembly.GetExecutingAssembly().GetName().Name.ToString();   //獲取前文檔命名空間的名稱
            richTextBox1.Text += namespaceName + "\n";

            Assembly asm = Assembly.GetExecutingAssembly();
            string name = asm.GetName().Name;
            richTextBox1.Text += "name : " + name + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //取得 AssemblyInfo
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title : " + info.Title + "\n";
            richTextBox1.Text += "Description : " + info.Description + "\n";
            richTextBox1.Text += "Company : " + info.Company + "\n";
            richTextBox1.Text += "Product : " + info.Product + "\n";
            richTextBox1.Text += "Copyright : " + info.Copyright + "\n";
            richTextBox1.Text += "Trademark : " + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version : " + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version : " + info.FileVersion + "\n";
            richTextBox1.Text += "GUID : " + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language : " + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible : " + info.IsComVisible.ToString() + "\n";

        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //組件資訊  Assembly Info

            //方案總管/專案屬性/應用程式/組件資訊 內 修改組件資訊

            //方案總管/加入/現有項目/選取AssemblyInfo.cs, 把 namespace 改成 vcs_System1
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title\t" + info.Title + "\n";
            richTextBox1.Text += "Description\t" + info.Description + "\n";
            richTextBox1.Text += "Company\t" + info.Company + "\n";
            richTextBox1.Text += "Product\t" + info.Product + "\n";
            richTextBox1.Text += "Copyright\t" + info.Copyright + "\n";
            richTextBox1.Text += "Trademark\t" + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version\t" + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version\t" + info.FileVersion + "\n";
            richTextBox1.Text += "GUID\t" + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language\t" + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible\t" + info.IsComVisible.ToString() + "\n";

        }

        //------------------------------------------------------------  # 60個

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

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


/*
private void AboutBox_Load(object sender, EventArgs e)
{
	AssemblyInfoClass asmi = new AssemblyInfoClass();
	labelProductName.Text = "產品名稱：" + asmi.Product;
	labelVersion.Text = "版本：" + asmi.Version;
	labelCopyright.Text = "版權宣告：" + asmi.Copyright;
	labelCompanyName.Text = "公司名稱：" + asmi.Company;
	textBoxDescription.Text = "細部描述：" + asmi.Description;
}

                string location = Assembly.GetExecutingAssembly().Location;
                string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";

一、獲取程序集版本
label版本.Text = Assembly.GetExecutingAssembly().GetName().Version.ToString();

            //獲取本代碼所在的文件作為臨時文件，用於獲取屬性列表
            string tempFile = Assembly.GetExecutingAssembly().FullName;


            //取得 namespaceName
            string namespaceName = Assembly.GetExecutingAssembly().GetName().Name.ToString();
            richTextBox1.Text += namespaceName + "\n";
            richTextBox1.Text += Assembly.GetExecutingAssembly().Location + "\n";

一、獲取程序集版本
label版本.Text = Assembly.GetExecutingAssembly().GetName().Version.ToString();

使用資源檔的圖片

屬性/資源/加入資源/加入現有檔案/ 選取檔案 picture1.jpg
此時, Resources 會出現 picture1.jpg
點選picture1.jpg, 屬性
建置動作 改成 內嵌資源

            Assembly asm = this.GetType().Assembly;
            Stream stream = asm.GetManifestResourceStream("vcs_test.Resources.picture1.jpg");
            this.BackgroundImage = new Bitmap(stream);
*/
/*
            var RootDirectory = AppDomain.CurrentDomain.BaseDirectory ?? System.Reflection.Assembly.GetExecutingAssembly().Location;
            richTextBox1.Text += "RootDirectory = " + RootDirectory + "\n";
*/

