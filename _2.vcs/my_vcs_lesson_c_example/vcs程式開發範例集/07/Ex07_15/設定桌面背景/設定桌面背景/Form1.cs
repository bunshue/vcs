using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;
using System.Drawing.Imaging;

namespace 設定桌面背景
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        #region 呼叫API
        [DllImport("user32.dll", EntryPoint = "SystemParametersInfoA")]
        static extern Int32 SystemParametersInfo(Int32 uAction, Int32 uParam, string lpvparam, Int32 fuwinIni);
        private const int SPI_SETDESKWALLPAPER = 20;
        #endregion
        private void 新增ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                listView1.Items.Clear();
                string[] files = openFileDialog1.FileNames;
                string[] fileinfo = new string[3];
                for (int i = 0; i < files.Length; i++)
                {
                    string path = files[i].ToString();
                    string fileName = path.Substring(path.LastIndexOf("\\") + 1, path.Length - 1 - path.LastIndexOf("\\"));
                    string filetype = fileName.Substring(fileName.LastIndexOf(".") + 1, fileName.Length - 1 - fileName.LastIndexOf("."));
                    fileinfo[0] = fileName;
                    fileinfo[1] = path;
                    fileinfo[2] = filetype;
                    ListViewItem lvi = new ListViewItem(fileinfo);
                    listView1.Items.Add(lvi);
                }
            }
        }

        private void 刪除ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count > 0)
            {
                listView1.Items.RemoveAt(listView1.SelectedItems[0].Index);
            }
        }

        private void 清空ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
        }

        private void 設為桌面背景ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count > 0)
            {
                string FPath = listView1.SelectedItems[0].SubItems[1].Text;
                //取得指定圖片的擴充名
                string SFileType = FPath.Substring(FPath.LastIndexOf(".") + 1, (FPath.Length - FPath.LastIndexOf(".") - 1));
                //將擴充名轉換成小寫
                SFileType = SFileType.ToLower();
                //取得文件名
                string SFileName = FPath.Substring(FPath.LastIndexOf("\\") + 1, (FPath.LastIndexOf(".") - FPath.LastIndexOf("\\") - 1));
                //如果圖片的類型是bmp則呼叫API中的方法將其設定為桌面背景
                if (SFileType == "bmp")
                {
                    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, FPath, 1);
                }
                else
                {
                    string SystemPath = Environment.SystemDirectory;//取得系統路徑
                    string path = SystemPath + "\\" + SFileName + ".bmp";
                    FileInfo fi = new FileInfo(path);
                    if (fi.Exists)
                    {
                        fi.Delete();
                        PictureBox pb = new PictureBox();
                        pb.Image = Image.FromFile(FPath);
                        pb.Image.Save(SystemPath + "\\" + SFileName + ".bmp", ImageFormat.Bmp);
                    }
                    else
                    {
                        PictureBox pb = new PictureBox();
                        pb.Image = Image.FromFile(FPath);
                        pb.Image.Save(SystemPath + "\\" + SFileName + ".bmp", ImageFormat.Bmp);
                    }
                    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, path, 1);
                }
            }
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count > 0)
            {
                string path = listView1.SelectedItems[0].SubItems[1].Text;
                pictureBox1.Image = Image.FromFile(path);
            }
        }
    }
}
