//參考 點擊滑鼠 : http://www.dotblogs.com.tw/sam319/archive/2009/12/24/12643.aspx
//     滑鼠位置 : http://www.dotblogs.com.tw/optimist9266/archive/2011/06/06/27194.aspx
//     鍵盤hook : http://www.dotblogs.com.tw/optimist9266/archive/2011/06/08/27315.aspx
//     HotKey   : http://www.dotblogs.com.tw/sam319/archive/2010/01/10/12945.aspx
//     列舉取得1 : http://www.dotblogs.com.tw/dc690216/archive/2009/09/16/10666.aspx
//     列舉取得2 :http://www.dotblogs.com.tw/ouch1978/archive/2011/01/27/enumtolist.aspx

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MouseControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.hScrollBar1.Value = 200;

            this.listBox1.Items.Add("None");
            this.listBox1.Items.Add("Alt");
            this.listBox1.Items.Add("Ctrl");
            this.listBox1.Items.Add("Shift");

            //取得key的列舉
            foreach (var item in Enum.GetNames(typeof(System.Windows.Forms.Keys)))
            {
                if ((item.Length == 1) || (item.Length == 2 && item.StartsWith("F")))
                {
                    this.comboBox1.Items.Add(item);
                }
            }
            //-------------------------------

            this.comboBox1.SelectedIndex = this.comboBox1.Items.IndexOf(System.Windows.Forms.Keys.F1.ToString());
            this.listBox1.SelectedIndex = 0;

            //新增一組hotkey
            this.HotKey = new GlobalHotKey(this.Handle, (System.Windows.Forms.Keys)Enum.Parse(typeof(System.Windows.Forms.Keys), this.comboBox1.Text), Keys.None);

            this.HotKey.OnHotkey += new GlobalHotKey.HotkeyEventHandler(HotKey_OnHotkey);
            //-------------------------------

            //開始監聽按鍵資料
            WindwosHook.KeyboardHook.Enabled = true;

            WindwosHook.KeyboardHook.GlobalKeyDown += new EventHandler<WindwosHook.KeyboardHook.KeyEventArgs>(KeyboardHook_GlobalKeyDown);
            //WindwosHook.KeyboardHook.GlobalKeyUp += new EventHandler<WindwosHook.KeyboardHook.KeyEventArgs>(KeyboardHook_GlobalKeyUp);
            //-------------------------------

            //開始監聽滑鼠位置
            System.Threading.ThreadPool.QueueUserWorkItem(new System.Threading.WaitCallback(AutoGetCursorPosition), null);
            //-------------------------------

            System.Reflection.Assembly asm = System.Reflection.Assembly.GetExecutingAssembly();

            nicon = new NotifyIcon();
            nicon.Icon = new Icon(asm.GetManifestResourceStream(asm.GetName().Name + ".1207680.ico"));
            nicon.Text = "Clicker";
            this.Icon = nicon.Icon;
            nicon.Click += new EventHandler(nicon_Click);
            this.pictureBox1.Image = GenerateBitmap(System.Drawing.Color.Green, new Size(20, 20));
        }

        void nicon_Click(object sender, EventArgs e)
        {
            nicon.Visible = false;
            this.Show();
            Win32Native.Methods.SetForegroundWindow(this.Handle);
        }

        NotifyIcon nicon;

        Bitmap GenerateBitmap(Color c, Size s)
        {
            Bitmap bmp = new Bitmap(s.Width, s.Height, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(c);
            g.Dispose();
            return bmp;
        }

        void KeyboardHook_GlobalKeyDown(object sender, WindwosHook.KeyboardHook.KeyEventArgs e)
        {
            if (e.Keys == Keys.A || e.Keys == Keys.X || e.Keys == Keys.W || e.Keys == Keys.D)
            {
                switch (e.Keys)
                {
                    case Keys.A:
                        MouseLogicControl.SetCursorLocation(MouseLogicControl.MoveDirection.Left, 10);
                        break;
                    case Keys.D:
                        MouseLogicControl.SetCursorLocation(MouseLogicControl.MoveDirection.Right, 10);
                        break;
                    case Keys.X:
                        MouseLogicControl.SetCursorLocation(MouseLogicControl.MoveDirection.Down, 10);
                        break;
                    case Keys.W:
                        MouseLogicControl.SetCursorLocation(MouseLogicControl.MoveDirection.Up, 10);
                        break;
                }
            }
            else
            {
                Console.WriteLine(e.Keys.ToString());
                Console.WriteLine(e.VirtualKeyCode.ToString());
            }
        }

        void AutoGetCursorPosition(object obj)
        {
            Point pt = new Point();

            while (true)
            {
                Win32Native.Methods.GetCursorPos(out pt);
                try
                {
                    SetText(this.label1, "滑鼠位置 : ( " + pt.X + " , " + pt.Y + " )");
                    //this.Text = "滑鼠位置 : ( " + pt.X + " , " + pt.Y + " )"; fail
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace.ToString());
                    break;
                }

                System.Threading.Thread.Sleep(50);
            }
        }

        delegate void SetTextDelegate(Control c, String str);
        void SetText(Control c, String str)
        {
            if (c.InvokeRequired)
            {
                c.Invoke(new SetTextDelegate(SetText), c, str);
            }
            else
            {
                c.Text = str;
            }
        }

        private void hScrollBar1_ValueChanged(object sender, EventArgs e)
        {
            SetText(this.label2, "滑鼠連點間隔時間 : " + this.hScrollBar1.Value + "毫秒");
        }

        private GlobalHotKey HotKey;

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.comboBox1.SelectedIndex != -1)
            {
                ChangeHotkey();
            }
        }

        /// <summary>
        /// 改變目前熱鍵
        /// </summary>
        void ChangeHotkey()
        {
            if (this.HotKey != null)
            {
                this.HotKey.Dispose();
            }
            //取得設定的key值
            System.Windows.Forms.Keys k = (System.Windows.Forms.Keys)Enum.Parse(typeof(System.Windows.Forms.Keys), this.comboBox1.Text);

            if (this.listBox1.Text != "None")
            {
                System.Windows.Forms.Keys com = Keys.None;
                switch (this.listBox1.Text)
                {
                    case "Alt":
                        com = Keys.Alt;
                        break;
                    case "Ctrl":
                        com = Keys.Control;
                        break;
                    case "Shift":
                        com = Keys.Shift;
                        break;
                }
                this.HotKey = new GlobalHotKey(this.Handle, k, com);
            }
            else
            {
                this.HotKey = new GlobalHotKey(this.Handle, k, Keys.None);
            }
            this.HotKey.OnHotkey += new GlobalHotKey.HotkeyEventHandler(HotKey_OnHotkey);
        }

        bool isWorking = false;

        MouseLogicControl.EventType CT = MouseLogicControl.EventType.LeftClick;

        private void AutoClicking(object obj)
        {
            int ClickTime = (int)obj;
            while (isWorking)
            {
                MouseLogicControl.ControlMouse(CT, new MouseLogicControl.Config());
                System.Threading.Thread.Sleep(ClickTime);
            }
        }

        /// <summary>
        /// 當熱鍵被使用者按下處理的事情
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        void HotKey_OnHotkey(object sender, HotKeyEventArgs e)
        {
            this.isWorking = this.groupBox1.Enabled;
            this.groupBox1.Enabled = !this.groupBox1.Enabled;
            this.hScrollBar1.Enabled = this.groupBox1.Enabled;
            this.groupBox2.Enabled = this.groupBox1.Enabled;

            if (isWorking)
            {
                ChangeStateView(System.Drawing.Color.Red);
                MessageBox.Show("開始自動連點!\r\n本程式自動縮小。", "提醒", MessageBoxButtons.OK, MessageBoxIcon.Information);
                System.Threading.ThreadPool.QueueUserWorkItem(new System.Threading.WaitCallback(AutoClicking), this.hScrollBar1.Value);
                this.Hide();
                this.nicon.Visible = true;
            }
            else
            {
                nicon_Click(this.nicon, new EventArgs());
                ChangeStateView(System.Drawing.Color.Green);
            }
        }

        void ChangeStateView(Color c)
        {
            this.pictureBox1.Image.Dispose();
            this.pictureBox1.Image = GenerateBitmap(c, new Size(20, 20));
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.listBox1.SelectedIndex != -1)
            {
                ChangeHotkey();
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            RadioButton r = (RadioButton)sender;
            if (r.Checked)
            {
                switch (r.Text)
                {
                    case "左":
                        this.CT = MouseLogicControl.EventType.LeftClick;
                        richTextBox1.Text += "你按了 左\n";
                        break;
                    case "中":
                        this.CT = MouseLogicControl.EventType.MidClick;
                        richTextBox1.Text += "你按了 中\n";
                        break;
                    case "右":
                        this.CT = MouseLogicControl.EventType.RightClick;
                        richTextBox1.Text += "你按了 右\n";
                        break;
                    default:
                        break;
                }
            }
        }
    }
}

