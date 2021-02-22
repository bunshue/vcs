using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Forms;
using System.Drawing;
using System.Collections;
using MyFunc;

namespace vcs_MidiKeyboard
{
	/// <summary>
	/// MIDI琴键类
	/// </summary>
	public class MidiKey
	{
		public MidiKey()
		{
			HotKey = new List<Keys>();
			Rect = new Rectangle();
		}

		/// <summary>
		/// 名称
		/// </summary>
		public string Name;

		/// <summary>
		/// 值（内部发音音阶代码）
		/// </summary>
		public byte Value;

		/// <summary>
		/// 是否被按下
		/// </summary>
		public Boolean isDown;

		/// <summary>
		/// 热键（为支持多热键对应同一音）
		/// </summary>
		public List<Keys> HotKey;

		/// <summary>
		/// 画布上的区域
		/// </summary>
		public RectangleF Rect;

		/// <summary>
		/// 是否为黑键（偏音）
		/// </summary>
		public bool isBlack;
	}

	/// <summary>
	/// 琴键面板类
	/// </summary>
	public class MidiBoard
	{
		private int[] bl = { 1, 3, 6, 8, 10 };  //黑键列表
		private int[] wl = { 0, 2, 4, 5, 7, 9, 11 };  //白键列表

		/// <summary>
		/// 按键标识字体
		/// </summary>
		private Font fontTitle;

		/// <summary>
		/// 琴键边框画笔
		/// </summary>
		private Pen penBorder;

		/// <summary>
		/// 白键填充色
		/// </summary>
		SolidBrush brushWhite;

		/// <summary>
		/// 按下的白键填充色
		/// </summary>
		SolidBrush brushLightWhite;

		/// <summary>
		/// 黑键填充色
		/// </summary>
		SolidBrush brushBlack;

		/// <summary>
		/// 按下的黑键填充色
		/// </summary>
		SolidBrush brushLightBlack;

		/// <summary>
		/// 字体写入格式
		/// </summary>
		private StringFormat sfBottomCenter;

		/// <summary>
		/// 外联画板控件（用于画键盘、接收鼠标事件）
		/// </summary>
		private Control PaintCtrl;

		/// <summary>
		/// 外联热键控件（用于接收键盘发音）
		/// </summary>
		private Control HotKeyCtrl;

		/// <summary>
		/// 键盘琴键列表
		/// </summary>
		private List<MidiKey> MidiKeys;

		/// <summary>
		/// 画板是否可用
		/// </summary>
		private bool canPaint;

		/// <summary>
		/// 画板是否过窄
		/// </summary>
		private bool isLowWidth;

		/// <summary>
		/// 外联WinMM基类
		/// </summary>
		private MidiBase Mid;

		/// <summary>
		/// 鼠标是否被按下
		/// </summary>
		private bool isMouseDown;

		/// <summary>
		/// 发标发音的ID（同时只能指向一个键）
		/// </summary>
		private int MousePosID;

		/// <summary>
		/// 键盘中哪些键被按下
		/// </summary>
		private List<bool> listKeyDown;

		/// <summary>
		/// 键盘发音列表（同时可使多键发音）
		/// </summary>
		private List<int> listKeyBeep;

		/// <summary>
		/// 构造函数（初始化）
		/// </summary>
		public MidiBoard()
		{
			init();
		}

		/// <summary>
		/// 构造函数（初始化外联控件）
		/// </summary>
		/// <param name="hotkeyCtrl"></param>
		/// <param name="paintCtrl"></param>
		public MidiBoard(Control hotkeyCtrl, Control paintCtrl)
		{
			init();
			if (hotkeyCtrl != null)
			{
				//如果热键控件可用则接收按键事件
				initHotKey();
				HotKeyCtrl = hotkeyCtrl;
				hotkeyCtrl.KeyDown += this.IO_KeyDown;
				hotkeyCtrl.KeyUp += this.IO_KeyUp;
			}

			if (paintCtrl != null)
			{
				//如果画板控件可用则初始化画板及鼠标事件
				PaintCtrl = paintCtrl;
				canPaint = true;
				paintCtrl.MouseDown += this.IO_MouseDown;
				paintCtrl.MouseUp += this.IO_MouseUp;
				paintCtrl.MouseMove += this.IO_MouseMove;
				paintCtrl.Paint += this.IO_Paint;
				paintCtrl.Resize += this.IO_Resize;
				this.initRect();
				paintCtrl.Refresh();
			}
		}

		/// <summary>
		/// 直接发声
		/// </summary>
		/// <param name="m">音号0-48</param>
		public void Down(int m)
		{
			//如果音号可用则发声、更改标志、刷新
			if (m < 0) return;
			Mid.Down(MidiKeys[m].Value);
			MidiKeys[m].isDown = true;
			if (canPaint) PaintCtrl.Refresh();
		}

		/// <summary>
		/// 停止发声
		/// </summary>
		/// <param name="m">音号0-48</param>
		public void Up(int m)
		{
			//如果音号可用则停止、更改标志、刷新
			if (m < 0) return;
			Mid.Up(MidiKeys[m].Value);
			MidiKeys[m].isDown = false;
			if (canPaint) PaintCtrl.Refresh();
		}

		/// <summary>
		/// 按键按下
		/// </summary>
		/// <param name="k">键值(字母与数字)</param>
		public void KeyDown(Keys k)
		{
			//如果该键未被接下（一直按着会blllllll不停的叫唤）
			if (!listKeyDown[(int)k])
			{
				//将该键加入列表
				listKeyDown[(int)k] = true;
				int n = GetIDByKey(k);
				if (n >= 0)
				{
					//该键有对应音则调用加一，重新发声
					listKeyBeep[n]++;
					Down(n);
				}
				//刷新
				if (canPaint) PaintCtrl.Refresh();
			}
		}

		/// <summary>
		/// 按键松开
		/// </summary>
		/// <param name="k">键值(字母与数字)</param>
		public void KeyUp(Keys k)
		{
			//如果该键已被按下
			if (listKeyDown[(int)k])
			{
				//将该键从列表移除
				listKeyDown[(int)k] = false;
				int n = GetIDByKey(k);
				if (n >= 0)
				{
					//该键有对应，调用减一，为零则停止发声
					listKeyBeep[n]--;
					if (listKeyBeep[n] <= 0 && MousePosID != n) Up(n);
				}
				//刷新
				if (canPaint) PaintCtrl.Refresh();
			}
		}

		/// <summary>
		/// 鼠标按下
		/// </summary>
		/// <param name="p">鼠标位置</param>
		public void MouseDown(Point p)
		{
			//更改标志，取得鼠标位置键
			isMouseDown = true;
			int n = GetIDByPoint(p);
			//如果鼠标指向非当前键
			if (n >= 0 && MousePosID != n)
			{
				//如果当前键存在并且非键盘控制，则停止当前键
				if (MousePosID >= 0 && listKeyBeep[MousePosID] <= 0) Up(MousePosID);
				//发声并重置当前键
				Down(n);
				MousePosID = n;
			}
		}

		/// <summary>
		/// 鼠标松开
		/// </summary>
		/// <param name="p">鼠标位置</param>
		public void MouseUp()
		{
			//更改标制，如果当前键非键盘控制则停止当前键发声
			isMouseDown = false;
			if (MousePosID >= 0)
			{
				if (listKeyBeep[MousePosID] <= 0) Up(MousePosID);
				MousePosID = -1;
			}
		}

		/// <summary>
		/// 根据鼠标当前位置取得音阶编号
		/// </summary>
		/// <param name="p">鼠标位置</param>
		/// <returns></returns>
		private int GetIDByPoint(Point p)
		{
			if (!canPaint || isLowWidth) return -1;
			for (int i1 = 0; i1 < 4; i1++)
			{
				foreach (int i in bl)
				{
					if (MidiKeys[i1 * 12 + i].Rect.Contains(p)) return (i1 * 12 + i);
				}

				foreach (int i in wl)
				{
					if (MidiKeys[i1 * 12 + i].Rect.Contains(p)) return (i1 * 12 + i);
				}
			}
			return -1;
		}

		/// <summary>
		/// 根据按键取得对应音阶编号
		/// </summary>
		/// <param name="k">热键</param>
		/// <returns></returns>
		private int GetIDByKey(Keys k)
		{
			int i = -1;
			foreach (MidiKey x in MidiKeys)
			{
				i++;
				if (x.HotKey.IndexOf(k) >= 0) return i;
			}
			return -1;
		}

		/// <summary>
		/// 设定乐器
		/// </summary>
		/// <param name="tone"></param>
		public void Set(MidiToneType tone)
		{
			Mid.SetTimbre((byte)tone);
		}

		/// <summary>
		/// 改变音量
		/// </summary>
		/// <param name="Vol"></param>
		public void Vol(int Vol)
		{
			Mid.Volume = (byte)Vol;
		}

		/// <summary>
		/// 初始化内部变量
		/// </summary>
		private void init()
		{
			string keynamestr = "1,C#,2,D#,3,4,F#,5,G#,6,A#,7,";
			string[] keyname = keynamestr.Split(',');
			MidiKeys = new List<MidiKey>(48);
			for (byte i = 0; i < 48; i++)
			{
				string l = ".,,,".Split(',')[i / 12];
				string r = ",,',\"".Split(',')[i / 12];
				MidiKey key = new MidiKey();
				key.Name = l + keyname[i % 12] + r;
				key.Value = (byte)(i + 48);
				key.isDown = false;
				//key.isBlack = (i % 12 == 1 || i % 12 == 3 || i % 12 == 6 || i % 12 == 8 || i % 12 == 10);
				key.isBlack = Array.Exists<int>(bl, (x) => { return x == (i % 12); });
				MidiKeys.Add(key);
			}
			isLowWidth = false;
			canPaint = false;
			Mid = new MidiBase();

			isMouseDown = false;
			MousePosID = -1;
			listKeyDown = new List<bool>(256);
			for (int i = 0; i < 256; i++) listKeyDown.Add(false);
			listKeyBeep = new List<int>(48);
			for (int i = 0; i < 48; i++) listKeyBeep.Add(0);
		}

		/// <summary>
		/// 初始化热键对应音
		/// </summary>
		private void initHotKey()
		{
			this.MidiKeys[0].HotKey.Add(Keys.Z);
			this.MidiKeys[2].HotKey.Add(Keys.X);
			this.MidiKeys[4].HotKey.Add(Keys.C);
			this.MidiKeys[5].HotKey.Add(Keys.V);
			this.MidiKeys[7].HotKey.Add(Keys.B);
			this.MidiKeys[9].HotKey.Add(Keys.N);
			this.MidiKeys[11].HotKey.Add(Keys.M);

			this.MidiKeys[12].HotKey.Add(Keys.A);
			this.MidiKeys[14].HotKey.Add(Keys.S);
			this.MidiKeys[16].HotKey.Add(Keys.D);
			this.MidiKeys[17].HotKey.Add(Keys.F);
			this.MidiKeys[19].HotKey.Add(Keys.G);
			this.MidiKeys[21].HotKey.Add(Keys.H);
			this.MidiKeys[23].HotKey.Add(Keys.J);
			this.MidiKeys[24].HotKey.Add(Keys.K);
			this.MidiKeys[26].HotKey.Add(Keys.L);

			this.MidiKeys[24].HotKey.Add(Keys.Q);
			this.MidiKeys[26].HotKey.Add(Keys.W);
			this.MidiKeys[28].HotKey.Add(Keys.E);
			this.MidiKeys[29].HotKey.Add(Keys.R);
			this.MidiKeys[31].HotKey.Add(Keys.T);
			this.MidiKeys[33].HotKey.Add(Keys.Y);
			this.MidiKeys[35].HotKey.Add(Keys.U);
			this.MidiKeys[36].HotKey.Add(Keys.I);
			this.MidiKeys[38].HotKey.Add(Keys.O);
			this.MidiKeys[40].HotKey.Add(Keys.P);

			this.MidiKeys[36].HotKey.Add(Keys.D1);
			this.MidiKeys[38].HotKey.Add(Keys.D2);
			this.MidiKeys[40].HotKey.Add(Keys.D3);
			this.MidiKeys[41].HotKey.Add(Keys.D4);
			this.MidiKeys[43].HotKey.Add(Keys.D5);
			this.MidiKeys[45].HotKey.Add(Keys.D6);
			this.MidiKeys[47].HotKey.Add(Keys.D7);
		}

		/// <summary>
		/// 初始化画板控件区域
		/// </summary>
		private void initRect()
		{
			if (canPaint)
			{
				float w = PaintCtrl.Width;
				float h = PaintCtrl.Height;
				float x = w / 28;
				if (x < 10)
				{
					isLowWidth = true;
					PaintCtrl.Refresh();
					return;
				}
				isLowWidth = false;
				for (int i = 0; i < 4; i++)
				{
					int l = i * 7;
					MidiKeys[i * 12 + 0].Rect = new RectangleF(l * x, 0, x, h);
					MidiKeys[i * 12 + 2].Rect = new RectangleF((l + 1) * x, 0, x, h);
					MidiKeys[i * 12 + 4].Rect = new RectangleF((l + 2) * x, 0, x, h);
					MidiKeys[i * 12 + 5].Rect = new RectangleF((l + 3) * x, 0, x, h);
					MidiKeys[i * 12 + 7].Rect = new RectangleF((l + 4) * x, 0, x, h);
					MidiKeys[i * 12 + 9].Rect = new RectangleF((l + 5) * x, 0, x, h);
					MidiKeys[i * 12 + 11].Rect = new RectangleF((l + 6) * x, 0, x, h);

					MidiKeys[i * 12 + 1].Rect = new RectangleF((l + 0.5F) * x, 0, x, h * 0.75F);
					MidiKeys[i * 12 + 3].Rect = new RectangleF((l + 1.5F) * x, 0, x, h * 0.75F);
					MidiKeys[i * 12 + 6].Rect = new RectangleF((l + 3.5F) * x, 0, x, h * 0.75F);
					MidiKeys[i * 12 + 8].Rect = new RectangleF((l + 4.5F) * x, 0, x, h * 0.75F);
					MidiKeys[i * 12 + 10].Rect = new RectangleF((l + 5.5F) * x, 0, x, h * 0.75F);
				}
				fontTitle = new Font("Tohoma", x * 0.4F);
				penBorder = new Pen(SystemColors.ControlDarkDark, x * 0.1F);
				sfBottomCenter = new StringFormat();
				sfBottomCenter.Alignment = StringAlignment.Center;
				sfBottomCenter.LineAlignment = StringAlignment.Center;
				brushWhite = new SolidBrush(Color.White);
				brushLightWhite = new SolidBrush(Color.FromArgb(255, 159, 159));
				brushBlack = new SolidBrush(Color.Black);
				brushLightBlack = new SolidBrush(Color.FromArgb(95, 0, 0));
				PaintCtrl.Refresh();
			}
		}

		/// <summary>
		/// 绘制画板
		/// </summary>
		/// <param name="g">画板接口</param>
		private void Draw(Graphics g)
		{
			//清空内容，检查宽度
			g.Clear(SystemColors.ControlDark);
			if (isLowWidth)
			{
				g.DrawString("宽度不够，请使用热键。", SystemFonts.DefaultFont, SystemBrushes.WindowText, 5,5);
				return;
			}

			//按四声阶画琴键及标识
			for (int i = 0; i < 4; i++)
			{
				//先画白键
				foreach (int i1 in wl)
				{
					MidiKey k = MidiKeys[i * 12 + i1];
					g.FillRectangle(k.isDown ? brushLightWhite : brushWhite, k.Rect);
					g.DrawRectangle(penBorder, k.Rect.X, k.Rect.Y, k.Rect.Width, k.Rect.Height);
					g.DrawString(k.Name, fontTitle, brushBlack, k.Rect.X + k.Rect.Width * 0.5F, k.Rect.Y + k.Rect.Height * 0.9F, sfBottomCenter);
				}

				//再画黑键（黑键无标识）
				foreach (int i1 in bl)
				{
					MidiKey k = MidiKeys[i * 12 + i1];
					g.FillRectangle(k.isDown ? brushLightBlack : brushBlack, k.Rect);
					g.DrawRectangle(penBorder, k.Rect.X, k.Rect.Y, k.Rect.Width, k.Rect.Height);
					//g.DrawString(k.Name, fontTitle, brushWhite, k.Rect.X + k.Rect.Width * 0.5F, k.Rect.Y + k.Rect.Height * 0.9F, sfBottomCenter);
				}
			}
		}

		/// <summary>
		/// 响应IO鼠标左键按下
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Button == MouseButtons.Left)
			{
				this.MouseDown(e.Location);
			}
		}

		/// <summary>
		/// 响应IO鼠标左键松开事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_MouseUp(object sender, MouseEventArgs e)
		{
			if (e.Button == MouseButtons.Left)
			{
				this.MouseUp();
			}
		}

		/// <summary>
		/// 响应IO鼠标移动事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_MouseMove(object sender, MouseEventArgs e)
		{
			if (isMouseDown)
			{
				this.MouseDown(e.Location);
			}
		}

		/// <summary>
		/// 响应IO改变大小事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_Resize(object sender, EventArgs e)
		{
			initRect();
		}

		/// <summary>
		/// 响应IO按下按键事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_KeyDown(object sender, KeyEventArgs e)
		{
			this.KeyDown(e.KeyCode);
			e.Handled = true;
		}

		/// <summary>
		/// 响应IO松开按键事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_KeyUp(object sender, KeyEventArgs e)
		{
			this.KeyUp(e.KeyCode);
		}

		/// <summary>
		/// 响应IO重画事件
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void IO_Paint(object sender, PaintEventArgs e)
		{
			this.Draw(e.Graphics);
		}
	}
}
