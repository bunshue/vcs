using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ShowPicture2
{
    public partial class Frm_Main : Form
    {
        string strInfo = "";
        string[] strName = null;
        int Num = 0;
        int Count = 0;

        string foldername = @"C:\______test_files\__pic\_peony1";

        public Frm_Main()
        {
            InitializeComponent();
        }

        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);  //實例化一個DirectoryInfo類對象
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos(); 	//初始化一個FileSystemInfo類型的數組
            foreach (FileSystemInfo fi in fileinfo) 					//循環遍歷fileinfo中的每一個記錄
            {
                if (fi is DirectoryInfo) 						//當i在類DirectoryInfo中存在時
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);   //獲取i下的所有文件
                }
                else										//當不存在該i時
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    //if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")

                    string str = fi.FullName; 				//記錄變量i的全名
                    int b = str.LastIndexOf("\\");				//在此示例中獲取最后一個匹配項的索引
                    string strType = str.Substring(b + 1); 	//保存文件的后綴

                    //當文件格式為“jpg”或者“bmp”時
                    if (strType.Substring(strType.Length - 3) == "jpg" || strType.Substring(strType.Length - 3) == "bmp")
                    {
                        strInfo += strType + "#";			//為變量strInfo賦值
                    }
                }
            }
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            GetAllFiles(foldername);                           //獲取dir下的所有文件

            if (strInfo != "")								//當字符串不為空時
            {
                strName = strInfo.Split('#'); 					//獲取文件名
                Num = 0; 								//初始化Num的值
                showPic(Num); 							//顯示圖片
                Count = strName.Length - 1; 					//記錄Array中的元素數
            }
            else										//當字符串為空時
            {
                MessageBox.Show("影集里沒有照片");			//彈出信息提示
            }
        }

        private void showPic(int X)
        {
            this.pictureBox1.ImageLocation = foldername + "\\" + strName[X];
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Num += 1;
            if (Count > Num)
            {
                showPic(Num);
            }
            else
            {
                Num = 0;
                showPic(Num);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Num -= 1;
            if (Num >= 0)
            {
                showPic(Num);
            }
            else
            {
                Num = Count - 1;
                showPic(Num);
            }
        }
    }
}


