using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_MouseCursor1
{
    public partial class Form1 : Form
    {
        private const int Wid = 75;
        private const int Hgt = 70;
        private const int BmWid = 32;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            ShowCursor("AppStarting", Cursors.AppStarting);
            ShowCursor("Arrow", Cursors.Arrow);
            ShowCursor("Cross", Cursors.Cross);
            ShowCursor("Default", Cursors.Default);
            ShowCursor("Hand", Cursors.Hand);
            ShowCursor("Help", Cursors.Help);
            ShowCursor("HSplit", Cursors.HSplit);
            ShowCursor("IBeam", Cursors.IBeam);
            ShowCursor("No", Cursors.No);
            ShowCursor("NoMove2D", Cursors.NoMove2D);
            ShowCursor("NoMoveHoriz", Cursors.NoMoveHoriz);
            ShowCursor("NoMoveVert", Cursors.NoMoveVert);
            ShowCursor("PanEast", Cursors.PanEast);
            ShowCursor("PanNE", Cursors.PanNE);
            ShowCursor("PanNorth", Cursors.PanNorth);
            ShowCursor("PanNorth", Cursors.PanNW);
            ShowCursor("PanSE", Cursors.PanSE);
            ShowCursor("PanSouth", Cursors.PanSouth);
            ShowCursor("PanSW", Cursors.PanSW);
            ShowCursor("PanWest", Cursors.PanWest);
            ShowCursor("SizeAll", Cursors.SizeAll);
            ShowCursor("SizeNESW", Cursors.SizeNESW);
            ShowCursor("SizeNS", Cursors.SizeNS);
            ShowCursor("SizeNWSE", Cursors.SizeNWSE);
            ShowCursor("SizeWE", Cursors.SizeWE);
            ShowCursor("UpArrow", Cursors.UpArrow);
            ShowCursor("VSplit", Cursors.VSplit);
            ShowCursor("WaitCursor", Cursors.WaitCursor);
        }

        // Display a cursor.
        private void ShowCursor(string cursor_name, Cursor the_cursor)
        {
            // Make a Panel to hold the Label and PictureBox.
            Panel pan = new Panel();
            pan.Size = new Size(Wid, Hgt);
            pan.Cursor = the_cursor;
            flowLayoutPanel1.Controls.Add(pan);

            // Display the cursor's name in a Label.
            Label lbl = new Label();
            lbl.AutoSize = false;
            lbl.Text = cursor_name;
            lbl.Size = new Size(Wid, 13);
            lbl.TextAlign = ContentAlignment.MiddleCenter;
            lbl.Location = new Point(0, 0);
            pan.Controls.Add(lbl);

            // Draw the cursor onto a Bitmap.
            Bitmap bm = new Bitmap(BmWid, BmWid);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                the_cursor.Draw(gr, new Rectangle(0, 0, BmWid, BmWid));
            }

            // Display the Bitmap in a PictureBox.
            PictureBox pic = new PictureBox();
            pic.Location = new Point((Wid - BmWid) / 2, 15);
            pic.BorderStyle = BorderStyle.Fixed3D;
            pic.ClientSize = new Size(BmWid, BmWid);
            pic.Image = bm;
            pan.Controls.Add(pic);
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 390 - 30);
            flowLayoutPanel1.Size = new Size(620, 690 - 390);
            flowLayoutPanel1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 390);

            label1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            comboBox1.Size = new Size(400, 80);
            comboBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 40);

            numericUpDown1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 80);
            lb_cursor.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 80 + 40);

            richTextBox1.Size = new Size(400, 690 - 390);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 390);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1490, 750);
            this.Text = "vcs_MouseCursor1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
            {
                System.Threading.Thread.Sleep(1);
            }
        }

        //------------------------------------------------------------  # 60個

        //移動滑鼠鼠標
        [DllImport("user32")]
        static extern bool SetCursorPos(int X, int Y);

        int screenWidth = Screen.PrimaryScreen.Bounds.Width;
        int screenHeight = Screen.PrimaryScreen.Bounds.Height;

        private void button0_Click(object sender, EventArgs e)
        {
            //移動滑鼠鼠標
            //移動滑鼠鼠標
            int xx = screenWidth / 2;
            int yy = screenHeight / 2;
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //取得滑鼠資訊

            if (SystemInformation.MousePresent)  // 是否安裝滑鼠
            {
                richTextBox1.Text += "是否安裝滑鼠 : 是\n";
            }
            else
            {
                richTextBox1.Text += "是否安裝滑鼠 : 否\n";
            }

            // 滑鼠按鈕的數目
            richTextBox1.Text += "滑鼠按鈕的數目 : " + SystemInformation.MouseButtons.ToString() + "\n";

            if (SystemInformation.MouseWheelPresent) // 滑鼠是否有滾輪
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 是\n";
            }
            else
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 否\n";
            }
            // 滑鼠速度 (1 ~ 20)
            richTextBox1.Text += "滑鼠速度 (1 ~ 20) : " + SystemInformation.MouseSpeed.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        [DllImport("user32.dll")]
        public static extern IntPtr LoadCursorFromFile(string fileName);

        [DllImport("user32.dll")]
        public static extern IntPtr SetCursor(IntPtr cursorHandle);

        [DllImport("user32.dll")]
        public static extern uint DestroyCursor(IntPtr cursorHandle);

        private void button2_Click(object sender, EventArgs e)
        {
            //自定義游標
            Cursor myCursor = new Cursor(Cursor.Current.Handle);
            //dinosau2.ani為Windows自帶的光標：
            IntPtr colorCursorHandle = LoadCursorFromFile(@"C:\Windows\Cursors\aero_link_il.cur");
            myCursor.GetType().InvokeMember("handle", BindingFlags.Public |
            BindingFlags.NonPublic | BindingFlags.Instance |
            BindingFlags.SetField, null, myCursor, new object[] { colorCursorHandle });
            this.Cursor = myCursor;
        }

        //------------------------------------------------------------  # 60個

        //限制滑鼠只能在本表單上移動 ST
        bool flag_limit_mouse_activity_area = false;
        private void button3_Click(object sender, EventArgs e)
        {
            //限制滑鼠只能在本表單上移動

            if (flag_limit_mouse_activity_area == false)
            {
                flag_limit_mouse_activity_area = true;
                button3.Text = "解除";

                this.Cursor = new Cursor(Cursor.Current.Handle);//创建Cursor对象
                Cursor.Position = new Point(Cursor.Position.X, Cursor.Position.Y);//设置鼠标位置
                Cursor.Clip = new Rectangle(this.Location, this.Size);//设置鼠标的活动区域
            }
            else
            {
                flag_limit_mouse_activity_area = false;
                button3.Text = "限制滑鼠只能在本表單上移動";

                Screen[] screens = Screen.AllScreens;//获取显示的数组
                this.Cursor = new Cursor(Cursor.Current.Handle);//创建Cursor对象
                Cursor.Clip = screens[0].Bounds;//接触对鼠标活动区域的限制
            }
        }
        //限制滑鼠只能在本表單上移動 SP

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //移動滑鼠鼠標到螢幕正中央

            SetCursorPos(1920 / 2, 1080 / 2);
        }

        //------------------------------------------------------------  # 60個

        //隱藏滑鼠鼠標 ST
        //重寫API函數
        [DllImport("user32.dll", EntryPoint = "ShowCursor")]
        public extern static bool ShowCursor(bool bShow);

        private void button5_Click(object sender, EventArgs e)
        {
            //隱藏滑鼠鼠標
            button5.Text = "按Alt+F4離開程式";
            ShowCursor(false);  //隱藏滑鼠鼠標

            //ShowCursor(true);  //顯示滑鼠鼠標
        }

        //隱藏滑鼠鼠標 SP

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
            //改變本表單中的滑鼠游標
            richTextBox1.Text += "1111在窗體中改變鼠標樣式\n";

            Cursor myCursor = new Cursor(Cursor.Current.Handle);
            IntPtr colorCursorHandle = LoadCursorFromFile("..//..//image/special.ani");//鼠標圖標路徑
            myCursor.GetType().InvokeMember("handle", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.SetField, null, myCursor, new object[] { colorCursorHandle });
            this.Cursor = myCursor;
        }

        //------------------------------------------------------------  # 60個

        [DllImport("user32", EntryPoint = "LoadCursorFromFile")]
        public static extern int IntLoadCursorFromFile(string lpFileName);

        [DllImport("user32", EntryPoint = "SetSystemCursor")]
        public static extern void SetSystemCursor(int hcur, int i);

        const int OCR_NORAAC = 32512;   //標準
        const int OCR_HAND = 32649;     //手
        const int OCR_NO = 32648;       //斜的圓
        const int OCR_SIZEALL = 32646;  //移動

        private void button9_Click(object sender, EventArgs e)
        {
            //設定滑鼠游標

            //將要修改的標鼠圖片存入到系統的WINDOWS\Cursors目錄下

            //改變系統中的滑鼠游標
            richTextBox1.Text += "3333設定正常選擇滑鼠游標\n";
            //設定正常選擇滑鼠游標
            int cur = IntLoadCursorFromFile("..//..//image/01.cur");
            SetSystemCursor(cur, OCR_NORAAC);
            //設定移動
            cur = IntLoadCursorFromFile("..//..//image/03.cur");
            SetSystemCursor(cur, OCR_SIZEALL);
            //設定不可用
            cur = IntLoadCursorFromFile("..//..//image/04.cur");
            SetSystemCursor(cur, OCR_NO);
            //設定超鏈接
            cur = IntLoadCursorFromFile("..//..//image/06.cur");
            SetSystemCursor(cur, OCR_HAND);
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
            //恢復
            richTextBox1.Text += "2222在窗體中還原鼠標樣式\n";
            this.Cursor = Cursors.Default;
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
            //恢復滑鼠游標
            richTextBox1.Text += "4444恢復正常選擇滑鼠游標\n";
            //恢復正常選擇滑鼠游標
            int cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\arrow_m.cur");
            SetSystemCursor(cur, OCR_NORAAC);
            //恢復移動
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\move_r.cur");
            SetSystemCursor(cur, OCR_SIZEALL);
            //恢復不可用
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\no_r.cur");
            SetSystemCursor(cur, OCR_NO);
            //恢復超鏈接
            cur = IntLoadCursorFromFile(@"C:\WINDOWS\Cursors\hand.cur");
            SetSystemCursor(cur, OCR_HAND);
        }

        //------------------------------------------------------------  # 60個

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0: this.Cursor = Cursors.Default; break;
                case 1: this.Cursor = Cursors.Arrow; break;
                case 2: this.Cursor = Cursors.Cross; break;
                case 3: this.Cursor = Cursors.No; break;
                case 4: this.Cursor = Cursors.WaitCursor; break;
                case 5: this.Cursor = Cursors.Hand; break;
                case 6: this.Cursor = Cursors.Help; break;
                case 7: this.Cursor = Cursors.HSplit; break;
                case 8: this.Cursor = Cursors.AppStarting; break;
                case 9: this.Cursor = Cursors.IBeam; break;
                case 10: this.Cursor = Cursors.NoMove2D; break;
                case 11: this.Cursor = Cursors.NoMoveHoriz; break;
                case 12: this.Cursor = Cursors.NoMoveVert; break;
                case 13: this.Cursor = Cursors.PanEast; break;
                case 14: this.Cursor = Cursors.PanNE; break;
                case 15: this.Cursor = Cursors.PanNorth; break;
                case 16: this.Cursor = Cursors.PanNW; break;
                case 17: this.Cursor = Cursors.PanSE; break;
                case 18: this.Cursor = Cursors.PanSouth; break;
                case 19: this.Cursor = Cursors.PanSW; break;
                case 20: this.Cursor = Cursors.PanWest; break;
                case 21: this.Cursor = Cursors.SizeAll; break;
                case 22: this.Cursor = Cursors.SizeNESW; break;
                case 23: this.Cursor = Cursors.SizeNS; break;
                case 24: this.Cursor = Cursors.SizeNWSE; break;
                case 25: this.Cursor = Cursors.SizeWE; break;
                case 26: this.Cursor = Cursors.UpArrow; break;
                case 27: this.Cursor = Cursors.VSplit; break;
                default: break;
            }
        }

        //------------------------------------------------------------  # 60個

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            switch ((int)numericUpDown1.Value)
            {
                case 0: this.Cursor = Cursors.Default; lb_cursor.Text = "Default : 取得預設游標，通常為箭號游標。"; break;
                case 1: this.Cursor = Cursors.Arrow; lb_cursor.Text = "Arrow : 取得箭號游標。"; break;
                case 2: this.Cursor = Cursors.AppStarting; lb_cursor.Text = "AppStarting : 取得應用程式啟動時出現的游標。"; break;
                case 3: this.Cursor = Cursors.Cross; lb_cursor.Text = "Cross : 取得十字型游標。"; break;
                case 4: this.Cursor = Cursors.Hand; lb_cursor.Text = "Hand : 取得手狀游標，通常在游標停留在 Web 連結上方時使用。"; break;
                case 5: this.Cursor = Cursors.Help; lb_cursor.Text = "Help : 取得由箭號和問號組成的說明游標"; break;
                case 6: this.Cursor = Cursors.HSplit; lb_cursor.Text = "HSplit : 取得當滑鼠位在水平分割列上時出現的游標"; break;
                case 7: this.Cursor = Cursors.IBeam; lb_cursor.Text = "IBeam : 取得 I 型游標，這個游標用來顯示當按一下滑鼠時文字游標出現的位置。"; break;
                case 8: this.Cursor = Cursors.No; lb_cursor.Text = "No : 取得指示目前作業的特定區域無效的游標"; break;
                case 9: this.Cursor = Cursors.NoMove2D; lb_cursor.Text = "NoMove2D : 取得當滑鼠不移動，但視窗可以水平和垂直方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 10: this.Cursor = Cursors.NoMoveHoriz; lb_cursor.Text = "NoMoveHoriz : 取得當滑鼠不移動，但視窗可以水平方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 11: this.Cursor = Cursors.NoMoveVert; lb_cursor.Text = "NoMoveVert : 取得當滑鼠不移動，但視窗可以垂直方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 12: this.Cursor = Cursors.PanEast; lb_cursor.Text = "PanEast : 取得當滑鼠移動，而且視窗可水平捲動至右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 13: this.Cursor = Cursors.PanNE; lb_cursor.Text = "PanNE : 取得當滑鼠移動，而且視窗可水平和垂直捲動至上方和右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 14: this.Cursor = Cursors.PanNorth; lb_cursor.Text = "PanNorth : 取得當滑鼠移動，而且視窗可垂直捲動至上方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 15: this.Cursor = Cursors.PanNW; lb_cursor.Text = "PanNW : 取得當滑鼠移動，而且視窗可水平和垂直捲動至上方和左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 16: this.Cursor = Cursors.PanSE; lb_cursor.Text = "PanSE : 取得當滑鼠移動，而且視窗可水平和垂直捲動至下方和右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 17: this.Cursor = Cursors.PanSouth; lb_cursor.Text = "PanSouth : 取得當滑鼠移動，而且視窗可垂直捲動至下方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 18: this.Cursor = Cursors.PanSW; lb_cursor.Text = "PanSW : 取得當滑鼠移動，而且視窗可水平和垂直捲動至下方和左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 19: this.Cursor = Cursors.PanWest; lb_cursor.Text = "PanWest : 取得當滑鼠移動而且視窗可水平捲動至左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 20: this.Cursor = Cursors.SizeAll; lb_cursor.Text = "SizeAll : 取得四頭調整大小游標，它是由四個連結的箭號 (分別指向北、南、東和西) 所組成。"; break;
                case 21: this.Cursor = Cursors.SizeNESW; lb_cursor.Text = "SizeNESW : 取得雙頭斜線 (東北/西南) 調整大小游標。"; break;
                case 22: this.Cursor = Cursors.SizeNS; lb_cursor.Text = "SizeNS : 取得雙頭垂直 (北/南) 調整大小游標。"; break;
                case 23: this.Cursor = Cursors.SizeNWSE; lb_cursor.Text = "SizeNWSE : 取得雙頭斜線 (西北/東南) 調整大小游標。"; break;
                case 24: this.Cursor = Cursors.SizeWE; lb_cursor.Text = "SizeWE : 取得雙頭水平 (西/東) 調整大小游標。"; break;
                case 25: this.Cursor = Cursors.UpArrow; lb_cursor.Text = "UpArrow : 取得向上箭號游標，通常用來辨認插入點。"; break;
                case 26: this.Cursor = Cursors.VSplit; lb_cursor.Text = "VSplit : 取得當滑鼠位在垂直分割列上方時出現的游標。"; break;
                case 27: this.Cursor = Cursors.WaitCursor; lb_cursor.Text = "WaitCursor : 取得等待游標，其形狀通常為沙漏形狀。"; break;
                default: this.Cursor = Cursors.Default; lb_cursor.Text = "XXXXXXXXXXX"; break;
            }
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



//測試滑鼠移動
//mouse_event(MOUSEEVENTF_MOVE,-10,-10,0,0);
/*
            if (e.Button == MouseButtons.Right)
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            else
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);

*/


