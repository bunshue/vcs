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
using System.Drawing.Drawing2D; //for MatrixOrder

namespace vcs_MouseCursor1
{
    public partial class Form1 : Form
    {
        private const int Wid = 75;
        private const int Hgt = 70;
        private const int BmWid = 32;

        //------------------------------------------------------------  # 60個

        // 取得滑鼠座標 ST
        [DllImport("user32.dll")]
        public static extern bool GetCursorPos(out POINT lpPoint);

        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int X;
            public int Y;
            public POINT(int x, int y)
            {
                this.X = x;
                this.Y = y;
            }
        }
        // 取得滑鼠座標 SP

        //原子鼠標 ST

        // Cursors.
        private Cursor[] Cursors_atom;
        private const int NumCursors_atom = 18;

        //原子鼠標 SP

        //定義變量
        const int diff = 30;

        //將枚舉作為位域處理
        [Flags]
        enum MouseEventFlag : uint //設置鼠標動作的鍵值
        {
            Move = 0x0001,               //發生移動
            LeftDown = 0x0002,           //鼠標按下左鍵
            LeftUp = 0x0004,             //鼠標松開左鍵
            RightDown = 0x0008,          //鼠標按下右鍵
            RightUp = 0x0010,            //鼠標松開右鍵
            MiddleDown = 0x0020,         //鼠標按下中鍵
            MiddleUp = 0x0040,           //鼠標松開中鍵
            XDown = 0x0080,
            XUp = 0x0100,
            Wheel = 0x0800,              //鼠標輪被移動
            VirtualDesk = 0x4000,        //虛擬桌面
            Absolute = 0x8000
        }

        //設置鼠標按鍵和動作
        [DllImport("user32.dll")]
        static extern void mouse_event(MouseEventFlag flags, int dx, int dy,
            uint data, UIntPtr extraInfo); //UIntPtr指針多句柄類型

        //------------------------------------------------------------  # 60個

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


        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();         //執行某一事件，以達到延遲效果。
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

        bool flag_atom_cursor = false;
        private void button6_Click(object sender, EventArgs e)
        {
            if (flag_atom_cursor == false)
            {
                // Geometry.
                const int cursor_wid = 32;
                const int cursor_hgt = 32;
                float cx = cursor_wid / 2f;
                float cy = cursor_hgt / 2f;
                float rx = cx * 0.9f;
                float ry = cx * 0.4f;
                RectangleF rect = new RectangleF(-rx, -ry, 2 * rx, 2 * ry);
                float radius = cx * 0.15f;

                // Make the transformations we will use.
                Matrix transform1 = new Matrix();
                transform1.Rotate(60f, MatrixOrder.Append);
                transform1.Translate(cx, cy, MatrixOrder.Append);
                Matrix transform2 = new Matrix();
                transform2.Rotate(-60f, MatrixOrder.Append);
                transform2.Translate(cx, cy, MatrixOrder.Append);
                Matrix transform3 = new Matrix();
                transform3.Translate(cx, cy, MatrixOrder.Append);

                // Make an orbital image.
                Bitmap orbital_bm = new Bitmap(cursor_wid, cursor_hgt);
                using (Graphics gr = Graphics.FromImage(orbital_bm))
                {
                    // Use a transparent background.
                    gr.SmoothingMode = SmoothingMode.AntiAlias;
                    gr.Clear(Color.Transparent);

                    // Draw the orbitals.
                    gr.Transform = transform1;
                    gr.DrawEllipse(Pens.Red, rect);

                    gr.Transform = transform2;
                    gr.DrawEllipse(Pens.Red, rect);

                    gr.Transform = transform3;
                    gr.DrawEllipse(Pens.Red, rect);

                    // Draw the nucleus.
                    gr.FillEllipse(Brushes.Black,
                        -radius, -radius, 2 * radius, 2 * radius);
                }

                // Make the cursors.
                Cursors_atom = new Cursor[NumCursors_atom];
                double theta1 = 0;
                double dtheta1 = 2 * Math.PI / NumCursors_atom;
                double theta2 = 0;
                double dtheta2 = 2 * Math.PI / NumCursors_atom * 2;
                double theta3 = 0;
                double dtheta3 = 2 * Math.PI / NumCursors_atom * 3;
                for (int i = 0; i < NumCursors_atom; i++)
                {
                    Bitmap cursor_bm = new Bitmap(cursor_wid, cursor_hgt);
                    using (Graphics gr = Graphics.FromImage(cursor_bm))
                    {
                        // Copy the background orbitals.
                        gr.SmoothingMode = SmoothingMode.AntiAlias;
                        gr.DrawImage(orbital_bm, 0, 0);

                        // Draw the electrons.
                        gr.Transform = transform1;
                        double x1 = rx * Math.Cos(theta1);
                        double y1 = ry * Math.Sin(theta1);
                        gr.FillEllipse(Brushes.Red,
                            (int)(x1 - radius), (int)(y1 - radius),
                            2 * radius, 2 * radius);
                        theta1 += dtheta1;

                        gr.Transform = transform2;
                        double x2 = rx * Math.Cos(theta2);
                        double y2 = ry * Math.Sin(theta2);
                        gr.FillEllipse(Brushes.Green,
                            (int)(x2 - radius), (int)(y2 - radius),
                            2 * radius, 2 * radius);
                        theta2 += dtheta2;

                        gr.Transform = transform3;
                        double x3 = rx * Math.Cos(theta3);
                        double y3 = ry * Math.Sin(theta3);
                        gr.FillEllipse(Brushes.Blue,
                            (int)(x3 - radius), (int)(y3 - radius),
                            2 * radius, 2 * radius);
                        theta3 += dtheta3;
                    }

                    // Turn the bitmap into a cursor.
                    Cursors_atom[i] = new Cursor(cursor_bm.GetHicon());

                    // Increment theta.
                    theta1 += dtheta1;
                }

                flag_atom_cursor = true;
                button6.Text = "取消原子鼠標";
                timer_atom.Enabled = true;
            }
            else
            {
                flag_atom_cursor = false;
                button6.Text = "原子鼠標";
                timer_atom.Enabled = false;
                this.Cursor = Cursors.Default;
            }
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

        int cnt = 0;
        private void button10_Click(object sender, EventArgs e)
        {
            //從中心起任意移動
            SetCursorPos(1920 / 2, 1080 / 2);
            cnt = 0;
            timer_set_cursor_pos.Enabled = true;
        }

        private void timer_set_cursor_pos_Tick(object sender, EventArgs e)
        {
            cnt++;
            if (cnt > 50)
            {
                timer_set_cursor_pos.Enabled = false;
            }
            Random r = new Random();
            int dx = r.Next(-diff, diff);
            int dy = r.Next(-diff, diff);
            //richTextBox1.Text += "(" + dx.ToString() + ", " + dy.ToString() + ") ";

            mouse_event(MouseEventFlag.Move, dx, dy, 0, UIntPtr.Zero);

            //mouse_event(MouseEventFlag.LeftDown, dx, dy, 0, UIntPtr.Zero);
            //mouse_event(MouseEventFlag.LeftUp, dx, dy, 0, UIntPtr.Zero);
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //設定鼠標位置
            int cx = 1920 / 2;
            int cy = 1080 / 2;
            int dx = 0;
            int dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 0;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = 100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = -100;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 0;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = -100;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 100;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

            dx = 00;
            dy = 0;
            richTextBox1.Text += "正中心 + dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            SetCursorPos(cx + dx, cy + dy);
            delay(200);

        }

        //------------------------------------------------------------  # 60個

        int x_st = 0;
        int y_st = 0;
        int angle = 0;
        private void button12_Click(object sender, EventArgs e)
        {
            //強制移動鼠標至特定位置
            //強制移動鼠標至特定位置
            //richTextBox1.Text += MousePosition.X.ToString() + ", " + MousePosition.Y.ToString() + "\n";

            x_st = MousePosition.X;
            y_st = MousePosition.Y;
            angle = 0;
            timer_set_mouse_pos.Enabled = true;
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void timer_set_mouse_pos_Tick(object sender, EventArgs e)
        {
            int r = 50;
            int dx = (int)(r * cosd(angle));
            int dy = (int)(r * sind(angle));
            int x_st2 = x_st + dx;
            int y_st2 = y_st + dy;

            SetCursorPos(x_st2, y_st2);

            angle += 10;

            if (angle > 360)
            {
                timer_set_mouse_pos.Enabled = false;
            }
        }

        //------------------------------------------------------------  # 60個

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

        private void timer1_Tick(object sender, EventArgs e)
        {
            //用GetCursorPos取得滑鼠座標
            POINT pt = new POINT();
            GetCursorPos(out pt);
            //this.Text = "滑鼠位置 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")";    same
            this.Text = "滑鼠位置 : (" + string.Format("X:{0}, Y:{1}", pt.X, pt.Y) + ")";
        }

        //------------------------------------------------------------  # 60個

        //原子鼠標
        // Display the next cursor.
        private int CursorNumber = 0;
        private void timer_atom_Tick(object sender, EventArgs e)
        {
            CursorNumber = (CursorNumber + 1) % NumCursors_atom;
            this.Cursor = Cursors_atom[CursorNumber];
        }

        //------------------------------------------------------------  # 60個

        private void timer_mouse_position_Tick(object sender, EventArgs e)
        {
            this.Text = "相較於視窗原點的鼠標位置 : " + String.Format("{0},{1}", MousePosition.X, MousePosition.Y);
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



/*

using System.Runtime.InteropServices;  //StructLayout

        //結構體布局 本機位置
        [StructLayout(LayoutKind.Sequential)]
        struct NativeRECT
        {
            public int left;
            public int top;
            public int right;
            public int bottom;
        }


        //設置鼠標位置
        [DllImport("user32.dll")]
        static extern bool SetCursorPos(int X, int Y);


        [DllImport("user32.dll")]
        static extern IntPtr FindWindow(string strClass, string strWindow);

        //該函數獲取一個窗口句柄,該窗口雷鳴和窗口名與給定字符串匹配 hwnParent=Null從桌面窗口查找
        [DllImport("user32.dll")]
        static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter,
            string strClass, string strWindow);

        [DllImport("user32.dll")]
        static extern bool GetWindowRect(HandleRef hwnd, out NativeRECT rect);


        //private Point pt_st;
        //private Point pt_sp;
        //private int count;

*/


