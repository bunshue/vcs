using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

using System.IO;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;

namespace vcs_GetFileIcon
{
    public partial class Form1 : Form
    {
        ImageList imageList1 = new ImageList();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

            int cnt = 0;
            cnt = imageList1.Images.Count;
            richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";
            GetListViewItem(foldername, imageList1);

            cnt = imageList1.Images.Count;
            richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";

            if (cnt > 0)
            {
                pictureBox1.Image = imageList1.Images[0];
                label1.Text = aa.ToString() + ",  " + imageList1.Images[0].Width.ToString() + " X " + imageList1.Images[0].Height.ToString();
            }
        }

        int aa = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            aa++;

            int cnt = 0;
            cnt = imageList1.Images.Count;
            if (aa >= cnt)
                aa = 0;

            if (cnt > 0)
            {
                pictureBox1.Image = imageList1.Images[aa];

                label1.Text = aa.ToString() + ",  " + imageList1.Images[aa].Width.ToString() + " X " + imageList1.Images[aa].Height.ToString();

            }
        }

        /// <summary>
        /// 獲得指定路徑下面的所有文件及文件夾
        /// </summary>
        /// <param name="path">路徑</param>
        /// <returns></returns>
        public ArrayList GetListViewItem(string path, ImageList imglist)
        {
            Win32.SHFILEINFO shfi = new Win32.SHFILEINFO();
            try
            {
                string[] dirs = Directory.GetDirectories(path);
                string[] files = Directory.GetFiles(path);
                ArrayList itemarr = new ArrayList();

                for (int i = 0; i < dirs.Length; i++)
                {
                    string[] info = new string[4];
                    DirectoryInfo dir = new DirectoryInfo(dirs[i]);
                    //獲得圖標
                    Win32.SHGetFileInfo(dirs[i],
                                        (uint)0x80,
                                        ref shfi,
                                        (uint)System.Runtime.InteropServices.Marshal.SizeOf(shfi),
                                        (uint)(0x100 | 0x400)); //取得Icon和TypeName

                    richTextBox1.Text += "dir name = " + dir.Name + "\n";
                    //添加圖標
                    imglist.Images.Add(dir.Name, (Icon)Icon.FromHandle(shfi.hIcon).Clone());
                    info[0] = dir.Name;
                    info[1] = "";
                    info[2] = "文件夾";
                    info[3] = dir.LastWriteTime.ToString();
                    ListViewItem item = new ListViewItem(info, dir.Name);
                    itemarr.Add(item);
                    //銷毀圖標
                    Win32.DestroyIcon(shfi.hIcon);
                }
                for (int i = 0; i < files.Length; i++)
                {
                    string[] info = new string[4];
                    FileInfo fi = new FileInfo(files[i]);
                    //獲得圖標
                    Win32.SHGetFileInfo(files[i],
                                        (uint)0x80,
                                        ref shfi,
                                        (uint)System.Runtime.InteropServices.Marshal.SizeOf(shfi),
                                        (uint)(0x100 | 0x400)); //取得Icon和TypeName
                    //添加圖標
                    richTextBox1.Text += "file name = " + fi.Name + "\n";
                    imglist.Images.Add(fi.Name, (Icon)Icon.FromHandle(shfi.hIcon).Clone());
                    info[0] = fi.Name;
                    info[1] = fi.Length.ToString();
                    info[2] = fi.Extension.ToString();
                    info[3] = fi.LastWriteTime.ToString();
                    ListViewItem item = new ListViewItem(info, fi.Name);
                    itemarr.Add(item);
                    //銷毀圖標
                    Win32.DestroyIcon(shfi.hIcon);
                }
                return itemarr;

            }
            catch
            {
                return null;
            }
        }
    }

    public class Win32
    {
        [DllImport("shell32.dll", EntryPoint = "ExtractIcon")]
        public static extern int ExtractIcon(IntPtr hInst, string lpFileName, int nIndex);

        [DllImport("shell32.dll", EntryPoint = "SHGetFileInfo")]
        public static extern IntPtr SHGetFileInfo(string pszPath, uint dwFileAttribute, ref SHFILEINFO psfi, uint cbSizeFileInfo, uint Flags);

        [DllImport("User32.dll", EntryPoint = "DestroyIcon")]
        public static extern int DestroyIcon(IntPtr hIcon);

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
        };
    }
}

/*
SHGetFileInfo 的最後一個參數 Flags
uFlags常數：
  SHGFI_ICON                                   =   0x100   
  SHGFI_DISPLAYNAME                   =   0x200,            
  SHGFI_TYPENAME                        =   0x400,          
  SHGFI_ATTRIBUTES                     =   0x800,        
  SHGFI_ICONLOCATION                 =   0x1000,            
  SHGFI_EXETYPE                           =   0x2000,            
  SHGFI_SYSICONINDEX                 =   0x4000,          
  SHGFI_LINKOVERLAY                  =   0x8000,            
  SHGFI_SELECTED                        =   0x10000,            
  SHGFI_ATTR_SPECIFIED             =   0x20000,            
  SHGFI_LARGEICON                      =   0x0,            
  SHGFI_SMALLICON                     =   0x1,            
  SHGFI_OPENICON                        =   0x2,            
  SHGFI_SHELLICONSIZE              =   0x4,            
  SHGFI_PIDL                                 =   0x8,            
  SHGFI_USEFILEATTRIBUTES      =   0x10
*/

