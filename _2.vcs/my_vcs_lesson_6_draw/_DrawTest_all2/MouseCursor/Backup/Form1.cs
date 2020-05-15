using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

namespace 模拟鼠标
{
	/// <summary>
	/// Form1 的摘要说明。
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
		/// <summary>
		/// 必需的设计器变量。
		/// </summary>
		private System.ComponentModel.Container components = null;

		public Form1()
		{
			//
			// Windows 窗体设计器支持所必需的
			//
			InitializeComponent();

			//
			// TODO: 在 InitializeComponent 调用后添加任何构造函数代码
			//
		}

		/// <summary>
		/// 清理所有正在使用的资源。
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows 窗体设计器生成的代码
		/// <summary>
		/// 设计器支持所需的方法 - 不要使用代码编辑器修改
		/// 此方法的内容。
		/// </summary>
		private void InitializeComponent()
		{
			System.Resources.ResourceManager resources = new System.Resources.ResourceManager(typeof(Form1));
			this.pictureBox1 = new System.Windows.Forms.PictureBox();
			this.SuspendLayout();
			// 
			// pictureBox1
			// 
			this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
			this.pictureBox1.Location = new System.Drawing.Point(0, 0);
			this.pictureBox1.Name = "pictureBox1";
			this.pictureBox1.Size = new System.Drawing.Size(344, 344);
			this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
			this.pictureBox1.TabIndex = 0;
			this.pictureBox1.TabStop = false;
			// 
			// Form1
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(6, 14);
			this.ClientSize = new System.Drawing.Size(344, 342);
			this.Controls.Add(this.pictureBox1);
			this.Name = "Form1";
			this.Text = "Form1";
			this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
			this.Load += new System.EventHandler(this.Form1_Load);
			this.KeyUp += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyUp);
			this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseMove);
			this.ResumeLayout(false);

		}
		#endregion

		/// <summary>
		/// 应用程序的主入口点。
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new Form1());
		}
		[System.Runtime.InteropServices.DllImport("user32")]
	    private static extern int mouse_event(int dwFlags,int dx,int dy,int cButtons,int dwExtraInfo);
		const int MOUSEEVENTF_MOVE=0x0001;
		const int MOUSEEVENTF_LEFTDOWN=0X0002;
		const int MOUSEEVENTF_LEFTUP=0X0004;
		const int MOUSEEVENTF_RIGHTDOWN=0X0008;
		const int MOUSEEVENTF_RIGHTUP=0X0010;
		const int MOUSEEVENTF_MIDDLEDOWN=0X0020;
		const int MOUSEEVENTF_MIDDLEUP=0X0040;
		private System.Windows.Forms.PictureBox pictureBox1;
		const int MOUSEEVENTF_ABSOLUTE=0X8000;

		private void Form1_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			//mouse_event(MOUSEEVENTF_MOVE,-10,-10,0,0);
		}

		private void Form1_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
		{
			if(e.KeyCode==Keys.Down)
				mouse_event(MOUSEEVENTF_MOVE,0,20,0,0);
			if(e.KeyCode==Keys.Up)
				mouse_event(MOUSEEVENTF_MOVE,0,-20,0,0);
			if(e.KeyCode==Keys.Left)
				mouse_event(MOUSEEVENTF_MOVE,-20,0,0,0);
			if(e.KeyCode==Keys.Right)
				mouse_event(MOUSEEVENTF_MOVE,20,0,0,0);
		}

		public void pictureBox1_KeyDown(object sender, System.Windows.Forms.KeyEventArgs e)
		{
			/*if(e.KeyCode==Keys.Down)
				mouse_event(MOUSEEVENTF_MOVE,0,20,0,0);
			if(e.KeyCode==Keys.Up)
				mouse_event(MOUSEEVENTF_MOVE,0,-20,0,0);
			if(e.KeyCode==Keys.Left)
				mouse_event(MOUSEEVENTF_MOVE,-20,0,0,0);
			if(e.KeyCode==Keys.Right)
				mouse_event(MOUSEEVENTF_MOVE,20,0,0,0);
				*/
		}
		private void Form1_KeyUp(object sender, System.Windows.Forms.KeyEventArgs e)
		{
		
		}

		

		private void pictureBox1_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			if(e.Button==MouseButtons.Right)
				mouse_event(MOUSEEVENTF_MOVE,0,20,0,0);
			else
				mouse_event(MOUSEEVENTF_MOVE,0,-20,0,0);
		}

		private void Form1_Load(object sender, System.EventArgs e)
		{
			
		}


		
	
	}
}
