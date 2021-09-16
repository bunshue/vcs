using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;

using System.Text;
using System.Windows.Forms;

using System.Linq;  // 欲使用LINQ查詢必須引用System.Linq命名空間
using System.IO;   // 欲使用檔案處理必須引用System.IO命名空間

namespace Linq_to_Object2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //按 [搜尋] 鈕執行此事件處理函式 
        private void btnSearch_Click(object sender, EventArgs e)
        {
            try
            {
                txtFileName.Text = "";
                DirectoryInfo dir = new DirectoryInfo(txtInput.Text);
                FileInfo[] f = dir.GetFiles();
                var myFile = from s in f select s.FullName;
                foreach (var s in myFile)
                {
                    txtFileName.Text +=s + Environment .NewLine ;
                }
            }
            catch (Exception ex)
            {
                txtFileName.Text ="路徑有錯";
            }
        }
    }
}
