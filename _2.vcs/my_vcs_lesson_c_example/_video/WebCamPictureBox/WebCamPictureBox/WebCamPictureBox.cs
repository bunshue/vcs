using System;
using System.ComponentModel;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace WebCamPictureBox
{
	[Browsable(true), Description("WebCam PictureBox"), ToolboxBitmap(typeof(WebCamPictureBox), "WebPictureBox.jpg")]
	public class WebCamPictureBox : PictureBox
	{
		#region PInvoke
		[DllImport("user32", EntryPoint = "SendMessage")]
		private static extern int SendMessage(IntPtr hWnd, uint Msg, int wParam, int lParam);

		[DllImport("avicap32.dll", EntryPoint = "capCreateCaptureWindowA")]
		private static extern IntPtr capCreateCaptureWindowA(string lpszWindowName, int dwStyle, int X, int Y, int nWidth, int nHeight, int hwndParent, int nID);

		[DllImport("user32.dll")]
		[return: MarshalAs(UnmanagedType.Bool)]
		private static extern bool SetWindowPos(IntPtr hWnd, int hWndInsertAfter, int X, int Y, int cx, int cy, int uFlags);

		[DllImport("user32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
		[return: MarshalAs(UnmanagedType.Bool)]
		private static extern bool DestroyWindow(IntPtr hwnd);
		#endregion


		#region Const
		const int WS_CHILD = 1073741824;
		const int WS_VISIBLE = 268435456;
		const int WM_CAP_START = 1024;
		const int WM_CAP_CONNECT = 1034;
		const int WM_CAP_DISCONNECT = 1035;
		const int WM_CAP_GET_FRAME = 1084;
		const int WM_CAP_EDIT_COPY = 1054;
		const int WM_CAP_SET_SCALE = WM_CAP_START + 53;
		const int WM_CAP_SET_PREVIEWRATE = WM_CAP_START + 52;
		const int WM_CAP_SET_PREVIEW = WM_CAP_START + 50;
		const int SWP_NOMOVE = 2;
		const int SWP_NOZORDER = 4;
		const int HWND_BOTTOM = 1;
		#endregion


		#region Var
		private IntPtr? _capHwnd;
		private bool _bIsStart;
		#endregion



		#region Private Property
		private IntPtr? m_CapHwnd
		{
			get
			{
				return _capHwnd ?? (_capHwnd = capCreateCaptureWindowA("WebCap", WS_CHILD | WS_VISIBLE, 0, 0, this.Width, this.Height, this.Handle.ToInt32(), 0));
			}
			set
			{
				_capHwnd = value;
			}
		}
		#endregion




		#region Public Property
		public new Image Image 
		{
			get
			{
				return (IsStarted) ? GetSnapshot() : base.Image;
			}
			set
			{
				base.Image = value;
			}
		}

		public bool IsStarted
		{
			get { return _bIsStart; }
			private set
			{
				if (_bIsStart != value)
				{
					OnConnectStateChanging(new EventArgs());
					_bIsStart = value;
					OnConnectStateChanged(new EventArgs());
				}
			}
		}
		#endregion



		#region Event
		public event EventHandler ConnectStateChanging;
		public event EventHandler ConnectStateChanged;
		#endregion



		#region Protected Method
		/// <summary>
		/// Raises the <see cref="E:ConnectStateChanging" /> event.
		/// </summary>
		/// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
		protected void OnConnectStateChanging(EventArgs e)
		{
			if (ConnectStateChanging != null)
				ConnectStateChanging(this, e);
		}

		/// <summary>
		/// Raises the <see cref="E:ConnectStateChanged" /> event.
		/// </summary>
		/// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
		protected void OnConnectStateChanged(EventArgs e)
		{
			if (ConnectStateChanged != null)
				ConnectStateChanged(this, e);
		}
		#endregion



		#region Public Method
		/// <summary>
		/// Tests the connect.
		/// </summary>
		/// <returns></returns>
		public bool TestConnect()
		{
			try
			{
				SendMessage(m_CapHwnd.Value, WM_CAP_CONNECT, 0, 0);
				SendMessage(m_CapHwnd.Value, WM_CAP_DISCONNECT, 0, 0);
				return true;
			}
			catch (Exception e)
			{
				return false;
			}
		}


		/// <summary>
		/// Starts the video capture
		/// </summary    
		public void Start()
		{
			try
			{
				// for safety, call stop, just in case we are already running
				this.Stop();

				IsStarted = true;

				// connect to the capture device               
				SendMessage(m_CapHwnd.Value, WM_CAP_CONNECT, 0, 0);
				SendMessage(m_CapHwnd.Value, WM_CAP_SET_SCALE, 1, 0);
				SendMessage(m_CapHwnd.Value, WM_CAP_SET_PREVIEWRATE, 30, 0);
				SendMessage(m_CapHwnd.Value, WM_CAP_SET_PREVIEW, 1, 0);

				SetWindowPos(m_CapHwnd.Value, HWND_BOTTOM, 0, 0, this.Width, this.Height, SWP_NOMOVE | SWP_NOZORDER);
			}

			catch (Exception e)
			{
				MessageBox.Show("An error ocurred while starting the video capture. Check that your webcamera is connected properly and turned on.\r\n\n" + e.Message);
				this.Stop();
			}
		}


		/// <summary>
		/// Stops the video capture
		/// </summary>
		public void Stop()
		{
			if (!IsStarted)
				return;

			// stop the timer
			IsStarted = false;

			// disconnect from the video source              
			SendMessage(m_CapHwnd.Value, WM_CAP_DISCONNECT, 0, 0);

			DestroyWindow(m_CapHwnd.Value);

			m_CapHwnd = null;
		}

		/// <summary>
		/// Gets the snapshot.
		/// </summary>
		/// <returns></returns>
		public Image GetSnapshot()
		{
			if (!IsStarted)
				return null;

			SendMessage(m_CapHwnd.Value, WM_CAP_EDIT_COPY, 0, 0);
			var data = Clipboard.GetDataObject();

			if (!data.GetDataPresent(typeof(Bitmap)))
				return null;

			return data.GetData(typeof(Bitmap)) as Image;
		}
		#endregion
	}
}
