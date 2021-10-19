using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PropertyItem

using System.IO;

namespace vcs_Exif3
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
            string filename = @"C:\______test_files\orient1.jpg";
            string TakePicDateTime = GetTakePicDateTime(GetExifPropertIEs(filename));
            richTextBox1.Text += TakePicDateTime + "\n\n\n";

            //分析字符串分別保存拍照日期和時間的標准格式
            int SpaceLocation = TakePicDateTime.IndexOf(" ");
            string dt = TakePicDateTime.Substring(0, SpaceLocation);
            dt = dt.Replace(":", "-");
            string tm = TakePicDateTime.Substring(SpaceLocation + 1, TakePicDateTime.Length - SpaceLocation - 2);
            TakePicDateTime = dt + " " + tm;

            richTextBox1.Text += "\n\n\nTakePicDateTime = " + TakePicDateTime + "\n";

            //ex: 2019:11:16 20:07:23 => 2019-11-16 20:07:23




        }

        //獲取圖像文件的所有元數據屬性，以PropertyItem數組的格式保存
        public static PropertyItem[] GetExifPropertIEs(string fileName)
        {
            FileStream stream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
            //通過指定的數據流來創建Image
            System.Drawing.Image image = System.Drawing.Image.FromStream(stream, true, false);
            return image.PropertyItems;
        }

        //遍歷所有元數據，獲取拍照日期/時間
        private string GetTakePicDateTime(System.Drawing.Imaging.PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            //遍歷圖像文件元數據，檢索所有屬性
            foreach (System.Drawing.Imaging.PropertyItem p in parr)
            {
                //如果是PropertyTagDateTime，則返回該屬性所對應的值
                if (p.Id == 0x0132)
                {
                    return ascii.GetString(p.Value);
                }
            }
            //若沒有相關的EXIF信息則返回N/A
            return "N/A";
        }

    }
}
