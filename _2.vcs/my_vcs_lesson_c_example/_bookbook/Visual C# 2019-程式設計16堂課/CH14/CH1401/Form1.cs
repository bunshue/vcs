using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;   //滙人處理檔案的資料流

namespace CH1401
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            //建立處理資料流的物件note
            Stream note = null;
            //設定OpenFileDialog的屬性-InitialDirectory設預設路徑
            dlgOpenFile.InitialDirectory = "D:\\C#Lab\\";
            //篩選檔案，只顯示文字檔
            dlgOpenFile.Filter =
               "文字檔(*.txt)|*.txt|所有檔案(*.*)|*.*";
            //檔案類型會顯示-所有檔案
            dlgOpenFile.FilterIndex = 2;
            //對話方塊關閉前還原目前取得的路徑
            dlgOpenFile.RestoreDirectory = true;
            //以一般的訊息方塊來確認使用者按OK鈕 
            if (dlgOpenFile.ShowDialog() == DialogResult.OK)
            {
                //攔截例外狀況
                try
                {
                    //
                    if ((note = dlgOpenFile.OpenFile()) != null)
                    {
                        using (note)
                        {
                            //PlainText-代表OLE物件的純文字資料流，文字中允許有空格
                            rtxtShow.LoadFile(dlgOpenFile.FileName,
                               RichTextBoxStreamType.PlainText);
                        }
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"檔案有誤：{ex.Message}");
                }
            }
        }
    }
}
