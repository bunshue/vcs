using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1301
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        float StrFontSize; //表字串大小
        String StrFont; //表字串樣式
        FontStyle StrFontStyle; //表字串字型    

        private void Form1_Load(object sender, EventArgs e)
        {
            //預設字型為微軟正黑體，字型大小為20
            StrFont = "微軟正黑體";
            StrFontSize = 20;
            //預設字型樣式為標準體
            StrFontStyle = FontStyle.Regular;
            //依設定值，文字方塊的文字會以新字型來載入
            rtxtShow.Font = new Font(StrFont, StrFontSize,
               StrFontStyle);
        }
        //將字變成大寫
        private void Upper_menuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.Text = rtxtShow.Text.ToUpper();
        }

        //將字變成小寫
        private void Lower_menuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.Text = rtxtShow.Text.ToLower();
        }

        private void Std_menuItem_Click(object sender, EventArgs e)
        {
            //設標楷體為預設字體，新細明體的預設字型取消
            StrFont = "標楷體";
            Std_menuItem.Checked = true;
            rtxtShow.Font = new Font(StrFont,
               StrFontSize, StrFontStyle);
        }

        private void Font8MenuItem_Click(object sender, EventArgs e)
        {
            StrFontSize = 8; //將字型大小設定為8
                             //將其他字型的屬性Checked設false
            Font8MenuItem.Checked = true;
            Font10MenuItem.Checked = false;
            Font12MenuItem.Checked = false;
            Font14MenuItem.Checked = false;
            Font16MenuItem.Checked = false;
            rtxtShow.Font = new Font(
               StrFont, StrFontSize, StrFontStyle);
        }

        private void Font10MenuItem_Click(object sender, EventArgs e)
        {
            StrFontSize = 10; //字型大小設定10
                              //將其他字型的屬性Checked設false
            Font8MenuItem.Checked = false;
            Font10MenuItem.Checked = true;
            Font12MenuItem.Checked = false;
            Font14MenuItem.Checked = false;
            Font16MenuItem.Checked = false;
            rtxtShow.Font = new Font(
               StrFont, StrFontSize, StrFontStyle);
        }

        private void Font12MenuItem_Click(object sender, EventArgs e)
        {
            StrFontSize = 12; //字型大小設定12
                              //將其他字型的屬性Checked設false
            Font8MenuItem.Checked = false;
            Font10MenuItem.Checked = false;
            Font12MenuItem.Checked = true;
            Font14MenuItem.Checked = false;
            Font16MenuItem.Checked = false;
            rtxtShow.Font = new Font(
               StrFont, StrFontSize, StrFontStyle);
        }

        private void Font14MenuItem_Click(object sender, EventArgs e)
        {
            StrFontSize = 14; //字型大小設定14
                              //將其他字型的屬性Checked設false
            Font8MenuItem.Checked = false;
            Font10MenuItem.Checked = false;
            Font12MenuItem.Checked = false;
            Font14MenuItem.Checked = true;
            Font16MenuItem.Checked = false;
            rtxtShow.Font = new Font(
               StrFont, StrFontSize, StrFontStyle);
        }

        private void Font16MenuItem_Click(object sender, EventArgs e)
        {
            StrFontSize = 16; //字型大小設定16
                              //將其他字型的屬性Checked設false
            Font8MenuItem.Checked = false;
            Font10MenuItem.Checked = false;
            Font12MenuItem.Checked = false;
            Font14MenuItem.Checked = false;
            Font16MenuItem.Checked = true;
            rtxtShow.Font = new Font(
               StrFont, StrFontSize, StrFontStyle);
        }

        private void StyleBold_menuItem_Click(object sender, EventArgs e)
        {
            //設定字型樣式為粗體，取消字體的斜體和標準
            StrFontStyle = FontStyle.Bold;
            StyleBold_menuItem.Checked = true;
            StyleItalic_menuItem.Checked = false;
            StyleStd_menuItem.Checked = false;
            rtxtShow.Font = new Font(StrFont, StrFontSize,
               StrFontStyle);
        }

        private void StyleItalic_menuItem_Click(object sender, EventArgs e)
        {
            //設定字型樣式為斜體，取消字體的粗體和標準
            StrFontStyle = FontStyle.Italic;
            StyleBold_menuItem.Checked = false;
            StyleItalic_menuItem.Checked = true;
            StyleStd_menuItem.Checked = false;
            rtxtShow.Font = new Font(StrFont, StrFontSize,
               StrFontStyle);
        }

        private void StyleStd_menuItem_Click(object sender, EventArgs e)
        {
            //設定字型樣式為標準，取消字體的斜體和粗體
            StrFontStyle = FontStyle.Regular;
            StyleBold_menuItem.Checked = false;
            StyleItalic_menuItem.Checked = false;
            StyleStd_menuItem.Checked = true;
            rtxtShow.Font = new Font(StrFont, StrFontSize,
               StrFontStyle);
        }

        private void NewFile_menuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.Clear();
            Form1_Load(sender, e);  //呼叫表單載入事件
        }

        private void OpenFile_menuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.LoadFile("D:\\C#Lab\\CH12\\Demo01.rtf");
        }

        private void SaveFile_menuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.SaveFile("D:\\C#Lab\\CH12\\Demo02.rtf");
        }

        private void EndFile_menuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //快顯功能表
        private void 綠色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //綠色ToolStripMenuItem.Checked = !綠色ToolStripMenuItem.Checked;         
            rtxtShow.ForeColor = Color.Green;
        }

        private void 黑色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //黑色ToolStripMenuItem.Checked = !黑色ToolStripMenuItem.Checked;         
            rtxtShow.ForeColor = Color.Black;
        }

        private void 黃色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.ForeColor = Color.Yellow;
        }

        private void 紅色ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            rtxtShow.ForeColor = Color.Red;
        }
    }
}
