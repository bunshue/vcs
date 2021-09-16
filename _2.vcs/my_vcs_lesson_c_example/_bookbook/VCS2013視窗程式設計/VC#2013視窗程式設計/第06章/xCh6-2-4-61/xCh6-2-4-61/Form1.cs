using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_61
{
    public partial class Form1 : Form
    {
        ToolStripDropDownButton toolStripDropDownButton1;
        ToolStripTextBox toolStripTextBox1;
        ToolStripDropDown dropDown;
        ToolStripButton buttonRed;
        ToolStripButton buttonBlue;
        ToolStripButton buttonGreen;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripDropDownButton1 = new ToolStripDropDownButton();

            // 根據預設的DisplayStyle為Image，因此Text的並不會顯示出來
            // 因此，調整其DisplayStyle，並調整文字與圖片的前後關係
            toolStripDropDownButton1.Text = "顏色設定";
            toolStripDropDownButton1.Image = 
                Image.FromFile(@"c:\user_red32x32.png");
            toolStripDropDownButton1.DisplayStyle = 
                ToolStripItemDisplayStyle.ImageAndText;
            toolStripDropDownButton1.TextImageRelation = 
                TextImageRelation.TextBeforeImage;

            // 設定下拉式清單出現的方向在左方
            toolStripDropDownButton1.DropDownDirection = 
                ToolStripDropDownDirection.Left;

            // 不顯示drop-down的下拉式箭頭
            toolStripDropDownButton1.ShowDropDownArrow = false;

            // 設定提示文字
            toolStripDropDownButton1.ToolTipText = "文字顏色設定";
 
            // 動態建構三個ToolStripButton物件，
            // 並設定為DropDown物件的內容，即「選項」
            buttonRed = new ToolStripButton();
            buttonRed.ForeColor = Color.Red;
            buttonRed.Text = "紅色";

            buttonBlue = new ToolStripButton();
            buttonBlue.ForeColor = Color.Blue;
            buttonBlue.Text = "藍色";

            buttonGreen = new ToolStripButton();
            buttonGreen.ForeColor = Color.Green;
            buttonGreen.Text = "綠色";

            // 委派三個ToolStripButton的事件處理程序
            buttonBlue.Click += new EventHandler(colorButtonsClick);
            buttonRed.Click += new EventHandler(colorButtonsClick);
            buttonGreen.Click += new EventHandler(colorButtonsClick);

            dropDown = new ToolStripDropDown();
            dropDown.Items.AddRange(new ToolStripItem[] 
             {
                buttonRed, 
                buttonBlue, 
                buttonGreen
             }
            );

            // 將dropdown設定給ToolStripDropDownButton.
            toolStripDropDownButton1.DropDown = dropDown;
            toolStrip1.Items.Add(toolStripDropDownButton1);

            toolStripTextBox1 = new ToolStripTextBox();
            toolStrip1.Items.Add(toolStripTextBox1);
        }

        private void colorButtonsClick(object sender, EventArgs e)
        {
            ToolStripButton senderButton = (ToolStripButton)sender;

            if (toolStripTextBox1.Text == "")
                toolStripTextBox1.Text = "顏色設定";
            toolStripTextBox1.ForeColor = senderButton.ForeColor;
        }
    }
}
