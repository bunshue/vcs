using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using com.google.zxing;
using com.google.zxing.common;

namespace Webcam_Test
{
    /*
     * http://www.planet-source-code.com/vb/scripts/ShowCode.asp?txtCodeId=1339&lngWId=10
     * */
    /// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
		private WebCam_Capture.WebCamCapture UserControl1;
		private WebCam_Capture.WebCamCapture WebCamCapture;
		private System.Windows.Forms.PictureBox pictureBox1;
		private System.Windows.Forms.Button cmdStart;
		private System.Windows.Forms.Button cmdStop;
		private System.Windows.Forms.Button cmdContinue;
		private System.Windows.Forms.NumericUpDown numCaptureTime;
		private System.Windows.Forms.Label label1;
        private TextBox textBox1;
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		public Form1()
		{
			//
			// Required for Windows Form Designer support
			//
			InitializeComponent();

			//
			// TODO: Add any constructor code after InitializeComponent call
			//
		}

		/// <summary>
		/// Clean up any resources being used.
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

		#region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
            this.WebCamCapture = new WebCam_Capture.WebCamCapture();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.cmdStart = new System.Windows.Forms.Button();
            this.cmdStop = new System.Windows.Forms.Button();
            this.cmdContinue = new System.Windows.Forms.Button();
            this.numCaptureTime = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numCaptureTime)).BeginInit();
            this.SuspendLayout();
            // 
            // WebCamCapture
            // 
            this.WebCamCapture.CaptureHeight = 240;
            this.WebCamCapture.CaptureWidth = 320;
            this.WebCamCapture.FrameNumber = ((ulong)(0ul));
            this.WebCamCapture.Location = new System.Drawing.Point(17, 17);
            this.WebCamCapture.Name = "WebCamCapture";
            this.WebCamCapture.Size = new System.Drawing.Size(342, 252);
            this.WebCamCapture.TabIndex = 0;
            this.WebCamCapture.TimeToCapture_milliseconds = 100;
            this.WebCamCapture.ImageCaptured += new WebCam_Capture.WebCamCapture.WebCamEventHandler(this.WebCamCapture_ImageCaptured);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(6, 7);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // cmdStart
            // 
            this.cmdStart.Location = new System.Drawing.Point(6, 502);
            this.cmdStart.Name = "cmdStart";
            this.cmdStart.Size = new System.Drawing.Size(78, 27);
            this.cmdStart.TabIndex = 1;
            this.cmdStart.Text = "Start";
            this.cmdStart.Click += new System.EventHandler(this.cmdStart_Click);
            // 
            // cmdStop
            // 
            this.cmdStop.Location = new System.Drawing.Point(102, 502);
            this.cmdStop.Name = "cmdStop";
            this.cmdStop.Size = new System.Drawing.Size(78, 27);
            this.cmdStop.TabIndex = 2;
            this.cmdStop.Text = "Stop";
            this.cmdStop.Click += new System.EventHandler(this.cmdStop_Click);
            // 
            // cmdContinue
            // 
            this.cmdContinue.Location = new System.Drawing.Point(198, 502);
            this.cmdContinue.Name = "cmdContinue";
            this.cmdContinue.Size = new System.Drawing.Size(78, 27);
            this.cmdContinue.TabIndex = 3;
            this.cmdContinue.Text = "Continue";
            this.cmdContinue.Click += new System.EventHandler(this.cmdContinue_Click);
            // 
            // numCaptureTime
            // 
            this.numCaptureTime.Location = new System.Drawing.Point(162, 550);
            this.numCaptureTime.Maximum = new decimal(new int[] {
            32000,
            0,
            0,
            0});
            this.numCaptureTime.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numCaptureTime.Name = "numCaptureTime";
            this.numCaptureTime.Size = new System.Drawing.Size(66, 22);
            this.numCaptureTime.TabIndex = 4;
            this.numCaptureTime.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(6, 557);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(150, 21);
            this.label1.TabIndex = 5;
            this.label1.Text = "Capture Time (Milliseconds)";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(8, 587);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(318, 22);
            this.textBox1.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(778, 629);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.numCaptureTime);
            this.Controls.Add(this.cmdContinue);
            this.Controls.Add(this.cmdStop);
            this.Controls.Add(this.cmdStart);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "WebCam Capture";
            this.Closing += new System.ComponentModel.CancelEventHandler(this.Form1_Closing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numCaptureTime)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

		}
		#endregion

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new Form1());
		}

		private void Form1_Load(object sender, System.EventArgs e)
		{
			// set the image capture size
			this.WebCamCapture.CaptureHeight = this.pictureBox1.Height;
			this.WebCamCapture.CaptureWidth = this.pictureBox1.Width;
		}

		private void Form1_Closing(object sender, System.ComponentModel.CancelEventArgs e)
		{
			// stop the video capture
			this.WebCamCapture.Stop();
		}
        private Boolean b = true;
		/// <summary>
		/// An image was capture
		/// </summary>
		/// <param name="source">control raising the event</param>
		/// <param name="e">WebCamEventArgs</param>
		private void WebCamCapture_ImageCaptured(object source, WebCam_Capture.WebcamEventArgs e)
		{
			// set the picturebox picture
			this.pictureBox1.Image = e.WebCamImage;

            if (b)
            {
                b = false;
                this.textBox1.Text = "checking";
                System.Drawing.Bitmap img = new System.Drawing.Bitmap(this.pictureBox1.Image, this.pictureBox1.Image.Size);
                thread1 obj = new thread1(img, this);
                System.Threading.Thread t = new System.Threading.Thread(obj.runMe);
               
                t.Start();
            }
		}
        public void setTextBox(String str,Boolean b)
        {
            this.textBox1.Text = str;
            this.b = b;
        }
        public delegate void decodeValue(string str,Boolean b);
		private void cmdStart_Click(object sender, System.EventArgs e)
		{
			// change the capture time frame
			this.WebCamCapture.TimeToCapture_milliseconds = (int) this.numCaptureTime.Value;

			// start the video capture. let the control handle the
			// frame numbers.
			this.WebCamCapture.Start(0);

		}

		private void cmdStop_Click(object sender, System.EventArgs e)
		{
			// stop the video capture
			this.WebCamCapture.Stop();
            

		}

		private void cmdContinue_Click(object sender, System.EventArgs e)
		{
			// change the capture time frame
			this.WebCamCapture.TimeToCapture_milliseconds = (int) this.numCaptureTime.Value;
            setTextBox("",true);
			// resume the video capture from the stop
			this.WebCamCapture.Start(this.WebCamCapture.FrameNumber);

		}
	}
    /*
     *
     * 
     */
    class thread1
    {
        private System.Drawing.Bitmap picDecode;

        private Form1 form;
        public thread1(System.Drawing.Bitmap picDecode, Form1 form)
        {
            this.picDecode = picDecode;
            this.form = form;
        }
        public void runMe()
        {
            //while (true)
            {
                QrDecode(picDecode);


                //System.Threading.Thread.Sleep(1000);
            }
        }
        public void QrDecode(System.Drawing.Bitmap picDecode)
        {

            try
            {
                Reader reader = new MultiFormatReader();
                //MonochromeBitmapSource image = new BufferedImageMonochromeBitmapSource(new Bitmap(Image.FromFile("barcode.jpg")), false);
                RGBLuminanceSource source = new RGBLuminanceSource(picDecode, picDecode.Width, picDecode.Height);
                // BinaryBitmap bitmap = 
                BinaryBitmap image = new BinaryBitmap(new HybridBinarizer(source));
                Result result = (Result)reader.decode(image);
                string text = result.Text;
                
               
                BarcodeFormat format = result.BarcodeFormat;
                ResultPoint[] points = result.ResultPoints;
                Console.WriteLine("barcode text: {0}", text);
                //Console.WriteLine("raw bytes: {0}", rawbytes);
                Console.WriteLine("format: {0}", format);
                Console.ReadLine();
                form.Invoke(new Form1.decodeValue(form.setTextBox), new object[] { System.Text.Encoding.UTF8.GetString(System.Text.Encoding.GetEncoding("SJIS").GetBytes(text)), false });
                

            }
            catch (com.google.zxing.ReaderException ex)
            {
                
                form.Invoke(new Form1.decodeValue(form.setTextBox), new object[] { "error",true });
                
                return;
                
            }
            
        }
    }

}
