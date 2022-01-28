using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;

namespace WindowsFormsApplication1227d
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

        private void button1_Click(object sender, EventArgs e)
        {
                         //reflecting reflect=new reflecting();//定義一個新的自身類
             //調用一個reflecting.exe程序集

            Assembly myAssembly = Assembly.LoadFrom("WindowsFormsApplication1227d.exe");
            getreflectioninfo(myAssembly);
             //reflect.getreflectioninfo(myAssembly);//獲取反射信息

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string fname = "WindowsFormsApplication1227d.exe";

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
    }
}
