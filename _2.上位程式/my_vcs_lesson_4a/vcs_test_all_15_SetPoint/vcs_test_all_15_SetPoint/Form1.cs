using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_15_SetPoint
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "文字檔(*.txt)|*.txt | Word檔|*.doc | 所有檔(*.*)|*.*";       //要在對話方塊中顯示的檔篩選器
            //saveFileDialog1.Filter = "JPeg Image|*.jpg|Bitmap Image|*.bmp|Gif Image|*.gif";
            saveFileDialog1.InitialDirectory = "c:\\";  //對話方塊的初始目錄
            saveFileDialog1.RestoreDirectory = true;    //控制對話方塊在關閉之前是否恢復目前的目錄
            //saveFileDialog1.AddExtension = 

            saveFileDialog1.Title = "另存新檔";                 //將顯示在對話方塊標題列中的字元
            saveFileDialog1.FileName = "SetPoint Report.txt";   //預設檔名

            if(saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //MessageBox.Show("Got filename : " + saveFileDialog1.FileName);
                string strFilePath = "";
                string FilePath = "";
                string fileNameExt = "";
                //獲得路徑檔名
                strFilePath = saveFileDialog1.FileName.ToString();
                //獲取檔路徑，不帶檔案名
                FilePath = strFilePath.Substring(0, strFilePath.LastIndexOf("\\"));
                //獲取檔案名，不帶路徑
                fileNameExt = strFilePath.Substring(strFilePath.LastIndexOf("\\") + 1);
                MessageBox.Show("路徑檔名: " + strFilePath + "\n" + "路徑: " + FilePath + "\n" + "檔名: " + fileNameExt + "\n");
            }
        }
    }
}

