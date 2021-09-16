using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_4_11
{
    public partial class Form1 : Form
    {
        ToolStripStatusLabel leftSideToolStripStatusLabel;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            statusStrip1.ShowItemToolTips = true;

            // 加入ToolStripStatusLabel
            leftSideToolStripStatusLabel = new ToolStripStatusLabel();
            leftSideToolStripStatusLabel.BorderStyle = Border3DStyle.Raised;
            leftSideToolStripStatusLabel.IsLink = true;
            leftSideToolStripStatusLabel.Name = "toolStripStatusLabel1";
            leftSideToolStripStatusLabel.Size = new Size(246, 20);
            leftSideToolStripStatusLabel.Spring = true;
            leftSideToolStripStatusLabel.Text = "有彈性的Label";
            leftSideToolStripStatusLabel.Alignment = ToolStripItemAlignment.Left;
            leftSideToolStripStatusLabel.Tag = "http://msdn.microsoft.com/zh-TW/";
            leftSideToolStripStatusLabel.Click += 
                new EventHandler(leftSideToolStripStatusLabel_Click);

            statusStrip1.Items.Add(leftSideToolStripStatusLabel);

            // 加入ToolStripButton與ToolStripSeparator
            ToolStripButton newToolStripButton = new ToolStripButton("開新檔案");
            ToolStripButton helpToolStripButton = new ToolStripButton("輔助說明");

            newToolStripButton.ToolTipText = "這是ToolStripButton物件";
            helpToolStripButton.ToolTipText = "這是ToolStripButton物件";

            ToolStripSeparator s1 = new ToolStripSeparator();

            statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] 
                        {
                            newToolStripButton,
                            helpToolStripButton,
                            s1
                        }
            );

            // 建構ToolStripMenuItem
            Bitmap image2 = new Bitmap(@"C:\frai32x32.png", true);
            ToolStripMenuItem m1 = new ToolStripMenuItem("MenuItem-I");
            ToolStripMenuItem m2 = new ToolStripMenuItem("MenuItem-II");
            ToolStripMenuItem m3 = new ToolStripMenuItem("MenuItem-III");

            ToolStripMenuItem m = new ToolStripMenuItem("MenuItem",
                image2,
                new ToolStripItem[] { m1, m2, m3 });

            m.ToolTipText = "這是ToolStripMenuItem物件";

            m.DropDownClosed += new
                EventHandler(toolStripDropDownItem_DropDownClosed);
            m.DropDownItemClicked += new
                ToolStripItemClickedEventHandler(toolStripDropDownItem_DropDownItemClicked);
            m.DropDownOpened += new
                EventHandler(toolStripDropDownItem_DropDownOpened);

            // 建構ToolStripSplitButton
            Bitmap image1 = new Bitmap(@"C:\user32x32.png", true);
            ToolStripButton buttonRed = new ToolStripButton();
            buttonRed.ForeColor = Color.Red;
            buttonRed.Text = "紅色-文字色彩";

            ToolStripButton buttonBlue = new ToolStripButton();
            buttonBlue.ForeColor = Color.Blue;
            buttonBlue.Text = "藍色-文字色彩";

            ToolStripButton buttonGreen = new ToolStripButton();
            buttonGreen.ForeColor = Color.Green;
            buttonGreen.Text = "綠色-文字色彩";

            buttonBlue.Click += new EventHandler(colorButtonsClick);
            buttonRed.Click += new EventHandler(colorButtonsClick);
            buttonGreen.Click += new EventHandler(colorButtonsClick);

            ToolStripSplitButton sb = new ToolStripSplitButton("SplitButton",
                image1,
                new ToolStripItem[] { buttonRed, buttonBlue, buttonGreen });

            sb.ToolTipText = "這是ToolStripSplitButton物件";

            sb.DropDownClosed += 
                new EventHandler(toolStripDropDownItem_DropDownClosed);
            sb.DropDownItemClicked += 
                new ToolStripItemClickedEventHandler(toolStripDropDownItem_DropDownItemClicked);
            sb.DropDownOpened += 
                new EventHandler(toolStripDropDownItem_DropDownOpened);

            // 加入ToolStripButton與ToolStripSplitButton
            statusStrip1.Items.AddRange(new ToolStripItem[] { m, sb });
        }

        // leftSideToolStripStatusLabel控制項的Click事件處理程序
        void leftSideToolStripStatusLabel_Click(object sender, EventArgs e)
        {
            // 切換Spring屬性
            leftSideToolStripStatusLabel.Spring ^= true;

            leftSideToolStripStatusLabel.Text =
                leftSideToolStripStatusLabel.Spring ? "有彈性的Label-True" : "有彈性的Label-False";

            // 如果還具有LinkLabel功能，點選後後開啟IE瀏覽URL的網址
            if (leftSideToolStripStatusLabel.IsLink)
            {
                string URL = leftSideToolStripStatusLabel.Tag.ToString();
                System.Diagnostics.Process.Start("IEXPLORE.EXE", URL);
                leftSideToolStripStatusLabel.LinkVisited = true;
            }
        }

        // 選項被開啟時的事件處理程序 
        void toolStripDropDownItem_DropDownOpened(object sender, EventArgs e)
        {
            ToolStripDropDownItem item = sender as ToolStripDropDownItem;

            string msg = String.Format("選項已開啟：{0}", item.Text);
            leftSideToolStripStatusLabel.Text = "使用者的操作：" + msg;
        }

        // 選項被點選時的事件處理程序 
        void toolStripDropDownItem_DropDownItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {
            string msg = String.Format("選項已點選： {0}", e.ClickedItem.Text);
            leftSideToolStripStatusLabel.Text = "使用者的操作：" + msg;
        }

        // 選項被關閉時的事件處理程序 
        void toolStripDropDownItem_DropDownClosed(object sender, EventArgs e)
        {
            ToolStripDropDownItem item = sender as ToolStripDropDownItem;

            string msg = String.Format("選項已關閉：{0}", item.Text);
            leftSideToolStripStatusLabel.Text = "使用者的操作：" + msg;
        }

        // 位於SplitButton中各ToolStripButton的事件處理程序
        void colorButtonsClick(object sender, EventArgs e)
        {
            ToolStripButton x = (ToolStripButton)sender;
            leftSideToolStripStatusLabel.IsLink = false;
            leftSideToolStripStatusLabel.ForeColor = Color.Yellow;
            switch (x.Text)
            {
                case "紅色-文字色彩": leftSideToolStripStatusLabel.BackColor = Color.Red; break;
                case "藍色-文字色彩": leftSideToolStripStatusLabel.BackColor = Color.Blue; break;
                case "綠色-文字色彩": leftSideToolStripStatusLabel.BackColor = Color.Green; break;
            }
        }
    }
}
