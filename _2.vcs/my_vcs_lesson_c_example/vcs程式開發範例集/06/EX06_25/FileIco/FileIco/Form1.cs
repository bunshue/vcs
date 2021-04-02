using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;


namespace FileIco
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length > 0)
                GetListViewItem(textBox1.Text, imageList1, listView1);
        }

        [DllImport("shell32.dll", EntryPoint = "SHGetFileInfo")]
        public static extern IntPtr SHGetFileInfo(string pszPath, uint dwFileAttribute, ref SHFILEINFO psfi, uint cbSizeFileInfo, uint Flags);
        [DllImport("User32.dll", EntryPoint = "DestroyIcon")]
        public static extern int DestroyIcon(IntPtr hIcon);
        [DllImport("shell32.dll")]
        public static extern uint ExtractIconEx(string lpszFile, int nIconIndex, int[] phiconLarge, int[] phiconSmall, uint nIcons);
        [StructLayout(LayoutKind.Sequential)]
        public struct SHFILEINFO
        {
            public IntPtr hIcon;
            public IntPtr iIcon;
            public uint dwAttributes;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 260)]
            public string szDisplayName;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 80)]
            public string szTypeName;
        }

        public void GetListViewItem(string path, ImageList imglist, ListView lv)//取得指定路徑下所有文件及其圖標
        {
            lv.Items.Clear();
            SHFILEINFO shfi = new SHFILEINFO();//實例化SHFILEINFO類
            try
            {
                string[] dirs = Directory.GetDirectories(path);//取得指定目錄中子目錄的名稱
                string[] files = Directory.GetFiles(path);//取得目錄中文件的名稱
                for (int i = 0; i < dirs.Length; i++)//搜尋子文件夾
                {
                    string[] info = new string[4];//定義一個數組
                    DirectoryInfo dir = new DirectoryInfo(dirs[i]);//根據文件夾的路徑實例化DirectoryInfo類
                    if (!(dir.Name == "RECYCLER" || dir.Name == "RECYCLED" || dir.Name == "Recycled" || dir.Name == "System Volume Information"))
                    {
                        SHGetFileInfo(dirs[i], (uint)0x80, ref shfi, (uint)System.Runtime.InteropServices.Marshal.SizeOf(shfi), (uint)(0x100 | 0x400)); //取得文件夾的圖標及類型
                        imglist.Images.Add(dir.Name, (Icon)Icon.FromHandle(shfi.hIcon).Clone());//新增圖標
                        info[0] = dir.Name;//取得文件夾的名稱
                        info[1] = "";//取得文件夾的大小
                        info[2] = "文件夾";//取得類型
                        info[3] = dir.LastWriteTime.ToString();//取得修改時間
                        ListViewItem item = new ListViewItem(info, dir.Name);//實例化ListViewItem類
                        lv.Items.Add(item);//新增目前文件夾的基本訊息
                        DestroyIcon(shfi.hIcon);//銷毀圖標
                    }
                }
                for (int i = 0; i < files.Length; i++)//搜尋文件
                {
                    string[] info = new string[4];//定義一個數組
                    FileInfo fi = new FileInfo(files[i]);//根據文件的路徑實例化FileInfo類
                    string Filetype = fi.Name.Substring(fi.Name.LastIndexOf(".") + 1, fi.Name.Length - fi.Name.LastIndexOf(".") - 1);//取得文件的類型
                    string newtype = Filetype.ToLower();//將文件類型轉換為小寫
                    if (!(newtype == "sys" || newtype == "ini" || newtype == "bin" || newtype == "log" || newtype == "com" || newtype == "bat" || newtype == "db"))
                    {
                        SHGetFileInfo(files[i], (uint)0x80, ref shfi, (uint)System.Runtime.InteropServices.Marshal.SizeOf(shfi), (uint)(0x100 | 0x400)); //取得文件的圖標及類型
                        imglist.Images.Add(fi.Name, (Icon)Icon.FromHandle(shfi.hIcon).Clone());//新增圖標
                        info[0] = fi.Name;//取得文件的名稱
                        info[1] = fi.Length.ToString();//取得文件的大小
                        info[2] = fi.Extension.ToString();//取得文件的類型
                        info[3] = fi.LastWriteTime.ToString();//取得文件的修改時間
                        ListViewItem item = new ListViewItem(info, fi.Name);//實例化ListViewItem類
                        lv.Items.Add(item);//新增目前文件的基本訊息
                        DestroyIcon(shfi.hIcon);//銷毀圖標
                    }
                }
            }
            catch { }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
                textBox1.Text = folderBrowserDialog1.SelectedPath;
        }
    }
}
