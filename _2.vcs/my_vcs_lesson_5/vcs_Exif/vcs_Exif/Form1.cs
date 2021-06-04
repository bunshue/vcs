using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PropertyItem

using System.IO;    //for FileStream
//方案總管/加入/現有項目/選取ExifStuff.cs, 把 namespace 改成 vcs_Exif

namespace vcs_Exif
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\vcs_reference2\\_icon\\IMG_20180228_215525.jpg";

            richTextBox1.Text += "讀取檔案:\t" + filename + "\n";

            using (Bitmap bm = new Bitmap(filename))
            {
                richTextBox1.Text += "Property\t\t\tID\t\t\tData Type\t\t\tDataLength\t\t\tValue\n";
                // Get EXIF property data.
                List<ExifStuff.ExifPropertyData> property_data = ExifStuff.GetExifProperties(bm);

                // Display the property information.
                List<string> results = new List<string>();
                foreach (ExifStuff.ExifPropertyData data in property_data)
                {
                    ListViewItem item = listView1.Items.Add(data.PropertyType.ToString());
                    item.SubItems.Add(data.Id.ToString());
                    item.SubItems.Add(data.DataType.ToString());
                    item.SubItems.Add(data.DataLength.ToString());
                    item.SubItems.Add(data.DataString);

                    richTextBox1.Text += data.PropertyType.ToString() + "\t\t\t";
                    richTextBox1.Text += data.Id.ToString() + "\t\t\t";
                    richTextBox1.Text += data.DataType.ToString() + "\t\t\t";
                    richTextBox1.Text += data.DataLength.ToString() + "\t\t\t";
                    if (data.DataLength < 32)
                    {
                        richTextBox1.Text += data.DataString + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "\n";
                    }
                }
            }
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\vcs_reference2\\_icon\\IMG_20180228_215525.jpg";

            richTextBox1.Text += "相片檔案:\t" + filename + "\n";

            PropertyItem[] pi;
            pi = GetExif(filename);
            string TakePicDateTime = GetDateTime(pi);

            richTextBox1.Text += "取得相片拍攝時間:\t" + TakePicDateTime + "\n";
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
        private string GetDateTime(System.Drawing.Imaging.PropertyItem[] parr)
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
