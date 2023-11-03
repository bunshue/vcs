using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;   //滙入IO名稱空間

namespace CH1402
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            rtxtShow.Lines = new string[] {
            "Irish poets learn your trade ",
            "Sing whatever is well made ",
            "Scorn the sort now growing up"};
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            //設定預設目錄, 預設欲儲存的檔案類型
            dlgSaveFile.InitialDirectory = "D:\\C#Lab";
            dlgSaveFile.Filter =
               "文字檔(*.txt)|*.txt|RTF格式|*.rtf";
            //設定對話方塊的標題
            dlgSaveFile.Title = "儲存檔案";
            //設定是否在關閉之前要還原至目前的目錄
            dlgSaveFile.RestoreDirectory = true;
            dlgSaveFile.CreatePrompt = true;
            dlgSaveFile.OverwritePrompt = true;
            //假如按下儲存按鈕時
            DialogResult result = dlgSaveFile.ShowDialog();
            if (result == DialogResult.OK)
            {
                StreamWriter writer;
                //設定檔案名稱
                string filename = dlgSaveFile.FileName;
                writer = new StreamWriter(
                   filename, false, Encoding.Default);
                //將文字方塊內容寫入指定的檔案中
                writer.Write(rtxtShow.Text);
                writer.Close(); //關閉檔案
            }
        }
    }
}
