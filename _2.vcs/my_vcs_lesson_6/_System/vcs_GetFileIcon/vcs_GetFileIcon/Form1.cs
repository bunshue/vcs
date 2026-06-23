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
            show_item_location();

            //------------------------------------------------------------  # 60個

            label1.Text = "";
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

            listView1.Size = new Size(620, 690);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_test_all_00_Usually";

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
            //取得文件夾中的圖標資源


        }

        //------------------------------------------------------------  # 60個

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

    //6060

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

