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
using System.Threading;

namespace IMGAddDate
{
    public partial class Frm_Main : Form
    {
        public string flag = null;
        PropertyItem[] pi;
        string TakePicDateTime;
        int SpaceLocation;
        string pdt;
        string ptm;
        Bitmap bitmap1;
        Graphics g;
        Thread td;

        //字串陣列的寫法(一維)：
        string[] pic_array = { 
            @"C:\______test_files1\p3.jpg", 
            @"C:\______test_files1\p3.jpg", 
            @"C:\______test_files1\p3.jpg", 
                             };

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            CheckForIllegalCrossThreadCalls = false;
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (td != null)
            {
                td.Abort();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //string[] IMG;
            listBox1.Items.Clear();
            //if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //IMG = openFileDialog1.FileNames;
                //if (IMG.Length > 0)
                {
                    for (int i = 0; i < pic_array.Length; i++)
                    {
                        listBox1.Items.Add(pic_array[i]);
                    }
                }
                flag = pic_array.Length.ToString();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            flag = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag == null)
            {
                richTextBox1.Text += "尚未添加圖片\n";
                return;
            }
            else
            {
                td = new Thread(new ThreadStart(AddDate));
                td.Start();
            }
        }

        private void AddDate()
        {
            Font normalContentFont = new Font("宋体", 36, FontStyle.Bold);
            Color normalContentColor = Color.Red;
            int kk = 1;
            richTextBox1.Text += "开始添加数码相片拍摄日期\n";

            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                pi = GetExif(listBox1.Items[i].ToString());
                //获取元数据中的拍照日期时间，以字符串形式保存
                TakePicDateTime = GetDateTime(pi);
                richTextBox1.Text += "1取得相片的拍攝時間 : " + TakePicDateTime + "\n";
                //分析字符串分别保存拍照日期和时间的标准格式
                SpaceLocation = TakePicDateTime.IndexOf(" ");
                pdt = TakePicDateTime.Substring(0, SpaceLocation);
                pdt = pdt.Replace(":", "-");
                ptm = TakePicDateTime.Substring(SpaceLocation + 1, TakePicDateTime.Length - SpaceLocation - 2);
                TakePicDateTime = pdt + " " + ptm;
                //由列表中的文件创建内存位图对象
                bitmap1 = new Bitmap(listBox1.Items[i].ToString());
                //由位图对象创建Graphics对象的实例
                g = Graphics.FromImage(bitmap1);

                //绘制数码照片的日期/时间
                richTextBox1.Text += "\n2取得相片的拍攝時間 : " + TakePicDateTime + "\n";

                g.DrawString(TakePicDateTime, normalContentFont, new SolidBrush(normalContentColor), 10, bitmap1.Height - 40);
                g.DrawString("西江月製作", normalContentFont, new SolidBrush(normalContentColor), 10, bitmap1.Height - 80);

                //将添加日期/时间戳后的图像进行保存

                bitmap1.Save(Application.StartupPath + "\\" + Path.GetFileName(listBox1.Items[i].ToString()));

                //释放内存位图对象
                bitmap1.Dispose();
                if (kk == listBox1.Items.Count)
                {
                    richTextBox1.Text += "全部数码相片拍摄日期添加成功\n";
                    flag = null;
                    listBox1.Items.Clear();
                }
                kk++;

                //System.Threading.Thread.Sleep(3500);
                //Application.DoEvents();
            }
        }

        #region 获取数码相片的拍摄日期
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
        #endregion
    }
}
