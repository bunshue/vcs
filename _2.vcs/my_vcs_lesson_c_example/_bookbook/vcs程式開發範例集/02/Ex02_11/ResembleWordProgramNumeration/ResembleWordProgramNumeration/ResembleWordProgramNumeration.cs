using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;//引用與輸入輸出流有關的命名空間

namespace ResembleWordProgramNumeration
{
    public partial class ResembleWordProgramNumeration : Form
    {
        public ResembleWordProgramNumeration()
        {
            InitializeComponent();
        }

        private static string temp = "tomorrow.RTF";//用來保存RTF文件的路徑
        private RichTextBoxEx richTextBox1 = new RichTextBoxEx();//聲明一個自定義類的實例
        private void ResembleWordProgramNumeration_Load(object sender, EventArgs e)
        {
            this.richTextBox1.Parent = this.groupBox1;//設置自定義類的父容器
            this.groupBox1.Controls.Add(this.richTextBox1);//向指定的父容器中添加控件
            if (File.Exists(temp))//當存在該RTF文件時
            {
                this.richTextBox1.LoadFile(temp, RichTextBoxStreamType.RichText);//將該文件顯示在RichTextBox控件中
                unfold.Enabled = false;//設置打開按鈕為不可用狀態
                hold.Enabled = false;//設置保存按鈕為不可用狀態                                         
            }
            richTextBox1.SelectionBullet = true;//設置RichTextBox控件標識項目符號的值為true
        }

        private void programNumeration_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionBullet)//當RichTextBox控件標識項目符號的值為true時
            {
                richTextBox1.SelectionBullet = false;//設置RichTextBox控件標識項目符號的值為false
            }
            else //當RichTextBox控件標識項目符號的值為false時
            {
                richTextBox1.SelectionBullet = true;//設置RichTextBox控件標識項目符號的值為true
            }
        }

        private void unfold_Click(object sender, EventArgs e)
        {
            OpenFileDialog TxTOpenDialog = new OpenFileDialog();//聲明一個打開文件對話框的對象
            TxTOpenDialog.Filter = "RTF文件(*.RTF)|*.RTF";//設置打開文件的格式
            if (TxTOpenDialog.ShowDialog() == DialogResult.OK)//當單擊「打開」按鈕時
            {
                temp = TxTOpenDialog.FileName;//保存打開文件的路徑
                this.richTextBox1.LoadFile(TxTOpenDialog.FileName, RichTextBoxStreamType.RichText);//在RichTextBox控件中打開文件
                MessageBox.Show("讀取成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出讀取成功的信息提示
            }
        }

        private void hold_Click(object sender, EventArgs e)
        {
            SaveFileDialog TxTSaveDialog = new SaveFileDialog();//聲明一個保存文件對話框對像
            TxTSaveDialog.Filter = "RTF文件（*.RTF)|*.RTF";//設置保存文件的格式
            if (File.Exists(temp))//當在指定路徑下存在該文件時
            {
                this.richTextBox1.SaveFile(temp, RichTextBoxStreamType.RichText);//在指定路徑下保存該文件
                MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的信息提示
                this.richTextBox1.Clear();//清空RichTextBox控件中的原有內容
            }
            else//當在指定路徑下不存在該文件時
            {
                if (TxTSaveDialog.ShowDialog() == DialogResult.OK)//當單擊「保存」按鈕時
                {
                    this.richTextBox1.SaveFile(TxTSaveDialog.FileName, RichTextBoxStreamType.RichText);//以指定的格式保存該文件
                    MessageBox.Show("保存成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出保存成功的信息提示
                    this.richTextBox1.Clear();//清空RichTextBox控件中的原有內容
                }
            }
        }

        private void figuresNumeration_Click(object sender, EventArgs e)
        {
            richTextBox1.BulletType = RichTextBoxEx.AdvRichTextBulletType.Number;//設置文件的項目編號屬性
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }
    }
}
