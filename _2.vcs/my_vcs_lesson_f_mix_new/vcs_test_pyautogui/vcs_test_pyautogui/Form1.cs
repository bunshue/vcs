using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_pyautogui
{
    public partial class Form1 : Form
    {
        //Pen p = new Pen(Color.Red, 3);
        SolidBrush sb = new SolidBrush(Color.Black);
        Font f = new Font("標楷體", 18);

        Graphics g;
        Graphics ig;        //繪製bitmap的Graphics實例
        Pen PenStyle;
        Pen p;
        Bitmap bitmap1;

        Color foreColor = Color.Red;
        Color backColor = Color.White;

        private Point startPoint, oldPoint; //繪圖時紀錄滑鼠位置
        //枚举类型，各种绘图工具
        private enum drawTools
        {
            Pen = 0, Line, Circle, Rectangle, String, Erase, None
        };
        //当前使用的工具
        //private drawTools drawTool = drawTools.Pen;
        private drawTools drawTool = drawTools.Line;
        private bool isDrawing = false;     //是否正在繪圖

        //做RichTextBox的右鍵選單
        private ContextMenuStrip menu;

        private ToolStripMenuItem miUndo;
        private ToolStripMenuItem miRedo;
        private ToolStripMenuItem miCut;
        private ToolStripMenuItem miCopy;
        private ToolStripMenuItem miPaste;
        private ToolStripMenuItem miSelectAll;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //創建一個bitmap
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            p = new Pen(Color.Red, 3);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            ig = Graphics.FromImage(bitmap1);
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            PenStyle = new Pen(foreColor);
            PenStyle.Width = 8;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

            g.Clear(backColor);
            ig.Clear(backColor);

            pictureBox1.Image = bitmap1;

            //------------------------------------------------------------  # 60個

            //做RichTextBox的右鍵選單
            CreateContextMenu();

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "百战无残垒\n巍然独此存\n古藤犹铁色\n旧碣尚苔痕\n" +
                "有相能逃劫\n无为道益尊\n台城落日里\n多少未归人\n";
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            pictureBox1.Size = new Size(410, 500);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_reset.Size.Height);

            button0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            richTextBox1.Size = new Size(410, 500);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox1.Right + 10, richTextBox1.Bottom + 10);

            this.Text = "vcs_test_pyautogui";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox1.Image = bitmap1;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個
        //做RichTextBox的右鍵選單 ST
        private void CreateContextMenu()
        {
            menu = new ContextMenuStrip();

            miUndo = new ToolStripMenuItem("復原");
            miRedo = new ToolStripMenuItem("重做");

            miCut = new ToolStripMenuItem("剪下");
            miCopy = new ToolStripMenuItem("複製");
            miPaste = new ToolStripMenuItem("貼上");

            miSelectAll = new ToolStripMenuItem("全選");

            menu.Items.Add(miUndo);
            menu.Items.Add(miRedo);

            menu.Items.Add(new ToolStripSeparator());

            menu.Items.Add(miCut);
            menu.Items.Add(miCopy);
            menu.Items.Add(miPaste);

            menu.Items.Add(new ToolStripSeparator());

            menu.Items.Add(miSelectAll);

            richTextBox1.ContextMenuStrip = menu;

            menu.Opening += Menu_Opening;

            miUndo.Click += MiUndo_Click;
            miRedo.Click += MiRedo_Click;

            miCut.Click += MiCut_Click;
            miCopy.Click += MiCopy_Click;
            miPaste.Click += MiPaste_Click;

            miSelectAll.Click += MiSelectAll_Click;
        }

        private void Menu_Opening(object sender, CancelEventArgs e)
        {
            miUndo.Enabled = richTextBox1.CanUndo;
            miRedo.Enabled = richTextBox1.CanRedo;

            bool hasSelection = richTextBox1.SelectionLength > 0;

            miCut.Enabled = hasSelection;
            miCopy.Enabled = hasSelection;

            miPaste.Enabled = Clipboard.ContainsText();
        }

        private void MiUndo_Click(object sender, EventArgs e)
        {
            if (richTextBox1.CanUndo)
                richTextBox1.Undo();
        }

        private void MiRedo_Click(object sender, EventArgs e)
        {
            if (richTextBox1.CanRedo)
                richTextBox1.Redo();
        }

        private void MiCut_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void MiCopy_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void MiPaste_Click(object sender, EventArgs e)
        {
            //richTextBox1.Paste();
            richTextBox1.SelectedText = Clipboard.GetText();
        }

        private void MiSelectAll_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }
        //做RichTextBox的右鍵選單 SP

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (bitmap1 == null)
                return;

            if (e.Button == MouseButtons.Left)
            {
                g.FillEllipse(new SolidBrush(Color.Red), e.X - 10, e.Y - 10, 20, 20);
                pictureBox1.Image = bitmap1;

                //如果开始绘制，则开始记录鼠标位置
                if ((isDrawing = !isDrawing) == true)
                {
                    //isDrawing = true;
                    startPoint = new Point(e.X, e.Y);
                    oldPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //this.Text = e.X.ToString() + ", " + e.Y.ToString();   //same
            this.Text = "(" + System.Windows.Forms.Cursor.Position.X.ToString() + ", " + System.Windows.Forms.Cursor.Position.Y.ToString() + ")";

            if (bitmap1 == null)
                return;

            if (isDrawing == true)
            {
                if (drawTool == drawTools.Pen)
                {
                    g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    oldPoint.X = e.X;
                    oldPoint.Y = e.Y;
                    pictureBox1.Image = bitmap1;
                }
                else if (drawTool == drawTools.Line)
                {
                    g.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    ig.DrawLine(PenStyle, oldPoint, new Point(e.X, e.Y));
                    oldPoint.X = e.X;
                    oldPoint.Y = e.Y;
                    pictureBox1.Image = bitmap1;
                }
                else if (drawTool == drawTools.Rectangle)
                {
                    //首先恢复此次操作之前的图像，然后再添加Rectangle
                    //this.Form1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));
                    //this.pictureBox1_Paint(this, new PaintEventArgs(this.CreateGraphics(), this.ClientRectangle));

                    //g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                    //ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                    pictureBox1.Image = bitmap1;
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (bitmap1 == null)
                return;

            isDrawing = false;
            if (drawTool == drawTools.Rectangle)
            {
                g.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                ig.DrawRectangle(new Pen(foreColor, 1), startPoint.X, startPoint.Y, e.X - startPoint.X, e.Y - startPoint.Y);
                pictureBox1.Image = bitmap1;
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            /*
            //将Image中保存的图像，绘制出来
            Graphics g = this.CreateGraphics();
            if (bitmap1 != null)
            {
                g.Clear(Color.White);
                g.DrawImage(bitmap1, this.ClientRectangle);
            }
            */
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

