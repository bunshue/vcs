using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_Exif2
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
            string filename = @"C:\______test_files\p3.jpg";

            PropertyItem[] pi;
            pi = GetExif(filename);
            //获取元数据中的拍照日期时间，以字符串形式保存
            string TakePicDateTime = GetDateTime(pi);
            richTextBox1.Text += "1取得相片的拍攝時間 : " + TakePicDateTime + "\n";



            GetInfo(pi);
        }

        //获取图像文件的所有元数据属性，保存倒PropertyItem数组
        public static PropertyItem[] GetExif(string fileName)
        {
            FileStream Mystream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
            //通过指定的数据流来创建Image
            Image image = Image.FromStream(Mystream, true, false);
            return image.PropertyItems;
        }

        //遍历所有元数据，获取拍照日期/时间
        private string GetDateTime(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            //遍历图像文件元数据，检索所有属性
            foreach (PropertyItem pp in parr)
            {
                //如果是PropertyTagDateTime，则返回该属性所对应的值
                if (pp.Id == 0x0132)
                {
                    return ascii.GetString(pp.Value);
                }
            }
            //若没有相关的EXIF信息则返回N/A
            return "N/A";
        }

        private void GetInfo(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            foreach (PropertyItem pp in parr)
            {
                richTextBox1.Text += "\nID = " + pp.Id.ToString() + "\t" + ascii.GetString(pp.Value) + "\n";
            }
            return;
        }



    }
}
