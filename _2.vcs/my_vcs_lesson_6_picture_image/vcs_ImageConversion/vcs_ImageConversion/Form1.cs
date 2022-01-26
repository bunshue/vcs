using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_ImageConversion
{
    public partial class Form1 : Form
    {
        List<String> selected_files = new List<String>();

        private Bitmap bitmap1;
        private int m_width0;
        private int m_height0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = null;
            m_width0 = pictureBox1.Size.Width;
            m_height0 = pictureBox1.Size.Height;


            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();

            int len = selected_files.Count;
            richTextBox2.Text = "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + selected_files[i] + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            selected_files.Clear();

            //選取檔案
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
            openFileDialog1.Filter = "bmp文件(*.bmp)|*.bmp|gif文件(*.gif)|*.gif|Jpeg文件	(*.jpg)|*.jpg";	//設置當前選定篩選器字符串以決定對話框中“文檔類型”選項
            openFileDialog1.FilterIndex = 3;            //設置對話框中當前選定篩選器的索引, 預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = false;   //關閉對話框，還原當前的目錄
            openFileDialog1.Multiselect = true;     //允許多選檔案
            openFileDialog1.Title = "選擇圖片";     //設置對話框的標題
            openFileDialog1.FileName = "";          //預設開啟的檔名
            //openFileDialog1.ShowHelp = true;
            //openFileDialog1.DefaultExt = "*.jpg";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                int len = openFileDialog1.FileNames.Length;
                richTextBox1.Text += "已選取檔案個數: " + len.ToString() + "\n";
                richTextBox1.Text += "已選取檔案: \n";
                foreach (string strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += strFilename + "\n";

                    int index = strFilename.LastIndexOf("\\");          		//路徑中最後一個反斜槓位置
                    richTextBox1.Text += "文件名：" + openFileDialog1.FileName.Substring(index + 1) + "\n";						//顯示文件名

                    selected_files.Add(strFilename);

                }

                /*
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;	//圖像充滿相框且維持比例
                string strpath = openFileDialog1.FileName;		//獲取文件路徑      
                pictureBox1.Image = Image.FromFile(strpath);	//加載圖片
                int index = strpath.LastIndexOf("\\");          		//路徑中最後一個反斜槓位置
                richTextBox1.Text = "文件名：" + openFileDialog1.FileName.Substring
                (index + 1);						//顯示文件名
                */

                //openFileDialog1.FileName

                //如果是OK，則建立一個圖象對象

                bitmap1 = new Bitmap(openFileDialog1.FileName);//調整pictureBox1的大小以適合圖象大小

                if (bitmap1.Width > bitmap1.Height)
                {

                    //保持寬度

                    pictureBox1.Width = m_width0;

                    pictureBox1.Height = (int)((double)bitmap1.Height * m_width0 / bitmap1.Width);

                }

                else
                {

                    //保持高度
                    pictureBox1.Height = m_height0;
                    pictureBox1.Width = (int)((double)bitmap1.Width * m_height0 / bitmap1.Height);
                }
                pictureBox1.Image = bitmap1;



            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟檔案\n";
                return;
            }

            //轉換

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";


            string save_type = "*.bmp";

            //根據不同的選項保存為相應格式的文件
            switch (save_type)
            {
                case "*.bmp":
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    break;
                case "*.jpg":
                    bitmap1.Save(filename, ImageFormat.Jpeg);
                    break;
                case "*.gif":
                    bitmap1.Save(filename, ImageFormat.Gif);
                    break;
                case "*.tif":
                    bitmap1.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    richTextBox1.Text += "未知檔案格式 : " + save_type + "\n";
                    break;

            }

            richTextBox1.Text += "已存檔 : " + filename + "\n";



        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}


/*

轉成ico


            if (bitmap1 == null)
            {
                richTextBox1.Text += "無圖片資料\n";
                return;
            }

            //圖示中包含的圖片常見尺寸有16×16（小圖示）、32×32、48×48，另外24×24、64×64、128×128也比較常見。
            Size size = new Size(128, 128);
            //獲得原始圖片文件
            //using (Bitmap bm = new Bitmap(FileName))
            {
                //從現有的圖像縮小, 為了得到合適的icon文件
                using (Bitmap iconBm = new Bitmap(bitmap1, size))
                {
                    using (Icon icon = Icon.FromHandle(iconBm.GetHicon()))
                    {
                        string icon_filename = Application.StartupPath + "\\ICO_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".ico";
                        using (Stream stream = new System.IO.FileStream(icon_filename, System.IO.FileMode.Create))
                        {
                            icon.Save(stream);
                            richTextBox1.Text += "轉換成功, 路徑是 : " + icon_filename + "\n";
                        }
                    }
                }
            }




*/





