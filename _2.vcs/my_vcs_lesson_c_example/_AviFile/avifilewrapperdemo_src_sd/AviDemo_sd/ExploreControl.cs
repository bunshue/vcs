using System;
using System.Drawing;
using System.ComponentModel;
using System.Windows.Forms;
using AviFile;

namespace AviDemo
{
	/// <summary>
	/// Description of ExploreControl.	
	/// </summary>
	public class ExploreControl : System.Windows.Forms.UserControl
	{
		/// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnSelectFile;
        private System.Windows.Forms.TextBox txtAviFileName;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown numInsertWavePosition;
        private System.Windows.Forms.Button btnExtractWave;
        private System.Windows.Forms.Button btnAddSound;
        private System.Windows.Forms.TextBox txtReportSound;
        private System.Windows.Forms.GroupBox grpShow;
        private System.Windows.Forms.NumericUpDown numPosition;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox picFrame;
        private System.Windows.Forms.GroupBox grpRead;
        private System.Windows.Forms.Button btnRead;
        private System.Windows.Forms.TextBox txtReportRead;
        private System.Windows.Forms.GroupBox grpExtract;
        private System.Windows.Forms.Button btnExtractPart;
        private System.Windows.Forms.Button btnExtract;
        private System.Windows.Forms.TextBox txtReportCopy;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button btnDecompress;
        private System.Windows.Forms.Button btnCompress;
        private System.Windows.Forms.Button btnExtractVideo;
        private System.Windows.Forms.GroupBox grpWrite;
        private System.Windows.Forms.Button btnWrite;
        private System.Windows.Forms.TextBox txtFileNames;
        private System.Windows.Forms.Button btnWriteCompress;
        private System.Windows.Forms.Button btnAppend;
		
		public ExploreControl() {
            InitializeComponent();
        }

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnSelectFile = new System.Windows.Forms.Button();
            this.txtAviFileName = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.numInsertWavePosition = new System.Windows.Forms.NumericUpDown();
            this.btnExtractWave = new System.Windows.Forms.Button();
            this.btnAddSound = new System.Windows.Forms.Button();
            this.txtReportSound = new System.Windows.Forms.TextBox();
            this.grpShow = new System.Windows.Forms.GroupBox();
            this.numPosition = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.picFrame = new System.Windows.Forms.PictureBox();
            this.grpRead = new System.Windows.Forms.GroupBox();
            this.btnRead = new System.Windows.Forms.Button();
            this.txtReportRead = new System.Windows.Forms.TextBox();
            this.grpExtract = new System.Windows.Forms.GroupBox();
            this.btnExtractPart = new System.Windows.Forms.Button();
            this.btnExtract = new System.Windows.Forms.Button();
            this.txtReportCopy = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.btnDecompress = new System.Windows.Forms.Button();
            this.btnCompress = new System.Windows.Forms.Button();
            this.btnExtractVideo = new System.Windows.Forms.Button();
            this.grpWrite = new System.Windows.Forms.GroupBox();
            this.btnWrite = new System.Windows.Forms.Button();
            this.txtFileNames = new System.Windows.Forms.TextBox();
            this.btnWriteCompress = new System.Windows.Forms.Button();
            this.btnAppend = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.grpShow.SuspendLayout();
            this.grpRead.SuspendLayout();
            this.grpExtract.SuspendLayout();
            this.grpWrite.SuspendLayout();
            this.SuspendLayout();
// 
// panel1
// 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.btnSelectFile);
            this.panel1.Controls.Add(this.txtAviFileName);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Location = new System.Drawing.Point(4, 4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(740, 42);
            this.panel1.TabIndex = 14;
// 
// btnSelectFile
// 
            this.btnSelectFile.Location = new System.Drawing.Point(659, 10);
            this.btnSelectFile.Name = "btnSelectFile";
            this.btnSelectFile.Size = new System.Drawing.Size(62, 20);
            this.btnSelectFile.TabIndex = 7;
            this.btnSelectFile.Text = "Browse...";
            this.btnSelectFile.Click += new System.EventHandler(this.btnSelectFile_Click);
// 
// txtAviFileName
// 
            this.txtAviFileName.Location = new System.Drawing.Point(227, 10);
            this.txtAviFileName.Name = "txtAviFileName";
            this.txtAviFileName.Size = new System.Drawing.Size(425, 20);
            this.txtAviFileName.TabIndex = 5;
            this.txtAviFileName.Text = "..\\..\\testdata\\test.avi";
// 
// label2
// 
            this.label2.Location = new System.Drawing.Point(127, 10);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Explore AVI File";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
// 
// groupBox1
// 
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.numInsertWavePosition);
            this.groupBox1.Controls.Add(this.btnExtractWave);
            this.groupBox1.Controls.Add(this.btnAddSound);
            this.groupBox1.Controls.Add(this.txtReportSound);
            this.groupBox1.Location = new System.Drawing.Point(271, 274);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(267, 146);
            this.groupBox1.TabIndex = 15;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Read/Write Wave Stream";
// 
// label3
// 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(119, 60);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(87, 14);
            this.label3.TabIndex = 4;
            this.label3.Text = "at frame number";
// 
// numInsertWavePosition
// 
            this.numInsertWavePosition.Location = new System.Drawing.Point(213, 55);
            this.numInsertWavePosition.Name = "numInsertWavePosition";
            this.numInsertWavePosition.Size = new System.Drawing.Size(47, 20);
            this.numInsertWavePosition.TabIndex = 3;
            this.numInsertWavePosition.ValueChanged += new System.EventHandler(this.numPosition_ValueChanged);
// 
// btnExtractWave
// 
            this.btnExtractWave.Location = new System.Drawing.Point(7, 28);
            this.btnExtractWave.Name = "btnExtractWave";
            this.btnExtractWave.Size = new System.Drawing.Size(253, 20);
            this.btnExtractWave.TabIndex = 2;
            this.btnExtractWave.Text = "Extract Sound to \"..\\..\\testdata\\sound.wav\"";
            this.btnExtractWave.Click += new System.EventHandler(this.btnExtractWave_Click);
// 
// btnAddSound
// 
            this.btnAddSound.Location = new System.Drawing.Point(7, 55);
            this.btnAddSound.Name = "btnAddSound";
            this.btnAddSound.Size = new System.Drawing.Size(105, 20);
            this.btnAddSound.TabIndex = 2;
            this.btnAddSound.Text = "Add Sound";
            this.btnAddSound.Click += new System.EventHandler(this.btnAddSound_Click);
// 
// txtReportSound
// 
            this.txtReportSound.Location = new System.Drawing.Point(7, 90);
            this.txtReportSound.Multiline = true;
            this.txtReportSound.Name = "txtReportSound";
            this.txtReportSound.ReadOnly = true;
            this.txtReportSound.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtReportSound.Size = new System.Drawing.Size(253, 49);
            this.txtReportSound.TabIndex = 0;
// 
// grpShow
// 
            this.grpShow.Controls.Add(this.numPosition);
            this.grpShow.Controls.Add(this.label1);
            this.grpShow.Controls.Add(this.picFrame);
            this.grpShow.Location = new System.Drawing.Point(4, 198);
            this.grpShow.Name = "grpShow";
            this.grpShow.Size = new System.Drawing.Size(260, 222);
            this.grpShow.TabIndex = 13;
            this.grpShow.TabStop = false;
            this.grpShow.Text = "Show Frames";
// 
// numPosition
// 
            this.numPosition.Location = new System.Drawing.Point(120, 194);
            this.numPosition.Name = "numPosition";
            this.numPosition.Size = new System.Drawing.Size(47, 20);
            this.numPosition.TabIndex = 2;
            this.numPosition.ValueChanged += new System.EventHandler(this.numPosition_ValueChanged);
// 
// label1
// 
            this.label1.Location = new System.Drawing.Point(13, 194);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(107, 20);
            this.label1.TabIndex = 1;
            this.label1.Text = "Extract Frame No.";
// 
// picFrame
// 
            this.picFrame.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.picFrame.Location = new System.Drawing.Point(13, 28);
            this.picFrame.Name = "picFrame";
            this.picFrame.Size = new System.Drawing.Size(234, 145);
            this.picFrame.TabIndex = 0;
            this.picFrame.TabStop = false;
// 
// grpRead
// 
            this.grpRead.Controls.Add(this.btnRead);
            this.grpRead.Controls.Add(this.txtReportRead);
            this.grpRead.Location = new System.Drawing.Point(4, 66);
            this.grpRead.Name = "grpRead";
            this.grpRead.Size = new System.Drawing.Size(260, 125);
            this.grpRead.TabIndex = 10;
            this.grpRead.TabStop = false;
            this.grpRead.Text = "Statistics";
// 
// btnRead
// 
            this.btnRead.Location = new System.Drawing.Point(13, 28);
            this.btnRead.Name = "btnRead";
            this.btnRead.Size = new System.Drawing.Size(234, 20);
            this.btnRead.TabIndex = 2;
            this.btnRead.Text = "Read General Information";
            this.btnRead.Click += new System.EventHandler(this.btnRead_Click);
// 
// txtReportRead
// 
            this.txtReportRead.Location = new System.Drawing.Point(13, 62);
            this.txtReportRead.Multiline = true;
            this.txtReportRead.Name = "txtReportRead";
            this.txtReportRead.ReadOnly = true;
            this.txtReportRead.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtReportRead.Size = new System.Drawing.Size(234, 49);
            this.txtReportRead.TabIndex = 0;
// 
// grpExtract
// 
            this.grpExtract.Controls.Add(this.btnExtractPart);
            this.grpExtract.Controls.Add(this.btnExtract);
            this.grpExtract.Controls.Add(this.txtReportCopy);
            this.grpExtract.Controls.Add(this.textBox1);
            this.grpExtract.Controls.Add(this.btnDecompress);
            this.grpExtract.Controls.Add(this.btnCompress);
            this.grpExtract.Controls.Add(this.btnExtractVideo);
            this.grpExtract.Location = new System.Drawing.Point(271, 66);
            this.grpExtract.Name = "grpExtract";
            this.grpExtract.Size = new System.Drawing.Size(267, 201);
            this.grpExtract.TabIndex = 11;
            this.grpExtract.TabStop = false;
            this.grpExtract.Text = "Read Video Stream";
// 
// btnExtractPart
// 
            this.btnExtractPart.Location = new System.Drawing.Point(7, 135);
            this.btnExtractPart.Name = "btnExtractPart";
            this.btnExtractPart.Size = new System.Drawing.Size(253, 20);
            this.btnExtractPart.TabIndex = 3;
            this.btnExtractPart.Text = "Extract a few Seconds to \"..\\..\\testdata\\video.avi\"";
            this.btnExtractPart.Click += new System.EventHandler(this.btnExtractPart_Click);
// 
// btnExtract
// 
            this.btnExtract.Location = new System.Drawing.Point(7, 82);
            this.btnExtract.Name = "btnExtract";
            this.btnExtract.Size = new System.Drawing.Size(253, 20);
            this.btnExtract.TabIndex = 2;
            this.btnExtract.Text = "Extract Bitmaps to \"..\\..\\testdata\\*.bmp\"";
            this.btnExtract.Click += new System.EventHandler(this.btnExtract_Click);
// 
// txtReportCopy
// 
            this.txtReportCopy.AutoSize = false;
            this.txtReportCopy.Location = new System.Drawing.Point(7, 160);
            this.txtReportCopy.Multiline = true;
            this.txtReportCopy.Name = "txtReportCopy";
            this.txtReportCopy.ReadOnly = true;
            this.txtReportCopy.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtReportCopy.Size = new System.Drawing.Size(253, 34);
            this.txtReportCopy.TabIndex = 0;
// 
// textBox1
// 
            this.textBox1.Location = new System.Drawing.Point(613, 367);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.ReadOnly = true;
            this.textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.textBox1.Size = new System.Drawing.Size(234, 132);
            this.textBox1.TabIndex = 0;
// 
// btnDecompress
// 
            this.btnDecompress.Location = new System.Drawing.Point(7, 28);
            this.btnDecompress.Name = "btnDecompress";
            this.btnDecompress.Size = new System.Drawing.Size(253, 20);
            this.btnDecompress.TabIndex = 2;
            this.btnDecompress.Text = "Decompress to \"..\\..\\testdata\\uncompressed.avi\"";
            this.btnDecompress.Click += new System.EventHandler(this.btnDecompress_Click);
// 
// btnCompress
// 
            this.btnCompress.Location = new System.Drawing.Point(7, 55);
            this.btnCompress.Name = "btnCompress";
            this.btnCompress.Size = new System.Drawing.Size(253, 20);
            this.btnCompress.TabIndex = 2;
            this.btnCompress.Text = "Compress to \"..\\..\\testdata\\compressed.avi\"";
            this.btnCompress.Click += new System.EventHandler(this.btnCompress_Click);
// 
// btnExtractVideo
// 
            this.btnExtractVideo.Location = new System.Drawing.Point(7, 110);
            this.btnExtractVideo.Name = "btnExtractVideo";
            this.btnExtractVideo.Size = new System.Drawing.Size(253, 20);
            this.btnExtractVideo.TabIndex = 2;
            this.btnExtractVideo.Text = "Extract Video to \"..\\..\\testdata\\video.avi\"";
            this.btnExtractVideo.Click += new System.EventHandler(this.btnExtractVideo_Click);
// 
// grpWrite
// 
            this.grpWrite.Controls.Add(this.btnWrite);
            this.grpWrite.Controls.Add(this.txtFileNames);
            this.grpWrite.Controls.Add(this.btnWriteCompress);
            this.grpWrite.Controls.Add(this.btnAppend);
            this.grpWrite.Location = new System.Drawing.Point(544, 66);
            this.grpWrite.Name = "grpWrite";
            this.grpWrite.Size = new System.Drawing.Size(207, 354);
            this.grpWrite.TabIndex = 12;
            this.grpWrite.TabStop = false;
            this.grpWrite.Text = "Create/Edit AVI from Bitmaps";
// 
// btnWrite
// 
            this.btnWrite.Location = new System.Drawing.Point(13, 208);
            this.btnWrite.Name = "btnWrite";
            this.btnWrite.Size = new System.Drawing.Size(180, 35);
            this.btnWrite.TabIndex = 2;
            this.btnWrite.Text = "Create uncompressed \"..\\..\\testdata\\new.avi\"";
            this.btnWrite.Click += new System.EventHandler(this.btnWrite_Click);
// 
// txtFileNames
// 
            this.txtFileNames.Location = new System.Drawing.Point(13, 28);
            this.txtFileNames.Multiline = true;
            this.txtFileNames.Name = "txtFileNames";
            this.txtFileNames.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtFileNames.Size = new System.Drawing.Size(180, 166);
            this.txtFileNames.TabIndex = 0;
            this.txtFileNames.Text = "..\\..\\testdata\\test.bmp";
// 
// btnWriteCompress
// 
            this.btnWriteCompress.Location = new System.Drawing.Point(13, 257);
            this.btnWriteCompress.Name = "btnWriteCompress";
            this.btnWriteCompress.Size = new System.Drawing.Size(180, 34);
            this.btnWriteCompress.TabIndex = 4;
            this.btnWriteCompress.Text = "Create and Compress \"..\\..\\testdata\\new.avi\"";
            this.btnWriteCompress.Click += new System.EventHandler(this.btnWriteCompress_Click);
// 
// btnAppend
// 
            this.btnAppend.Location = new System.Drawing.Point(13, 305);
            this.btnAppend.Name = "btnAppend";
            this.btnAppend.Size = new System.Drawing.Size(180, 35);
            this.btnAppend.TabIndex = 4;
            this.btnAppend.Text = "Add Frames";
            this.btnAppend.Click += new System.EventHandler(this.btnAppend_Click);
// 
// ExploreControl
// 
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.grpShow);
            this.Controls.Add(this.grpRead);
            this.Controls.Add(this.grpExtract);
            this.Controls.Add(this.grpWrite);
            this.Name = "ExploreControl";
            this.Size = new System.Drawing.Size(756, 423);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.grpShow.ResumeLayout(false);
            this.grpRead.ResumeLayout(false);
            this.grpRead.PerformLayout();
            this.grpExtract.ResumeLayout(false);
            this.grpExtract.PerformLayout();
            this.grpWrite.ResumeLayout(false);
            this.grpWrite.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion
        
        private void btnRead_Click(object sender, System.EventArgs e) {
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            VideoStream stream = aviManager.GetVideoStream();
            txtReportRead.Text = "Width: " + stream.Width;
            txtReportRead.Text += "\r\nHeight: " + stream.Height;
            txtReportRead.Text += "\r\nCount of Frames: " + stream.CountFrames;
            txtReportRead.Text += "\r\nFrame Rate: " + stream.FrameRate;

            txtReportRead.Text += "\r\nWave Sound:";

            try {
                AudioStream waveStream = aviManager.GetWaveStream();
                txtReportRead.Text += "\r\nSamples per Second: " + waveStream.CountSamplesPerSecond.ToString();
                txtReportRead.Text += "\r\nBits per Sample: " + waveStream.CountBitsPerSample.ToString();
                txtReportRead.Text += "\r\nChannels: " + waveStream.CountChannels.ToString();
            } catch {
                txtReportRead.Text += " None";
            }
        }

        private void btnExtract_Click(object sender, System.EventArgs e) {
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);

            VideoStream stream = aviManager.GetVideoStream();
            stream.GetFrameOpen();

            txtReportCopy.Text = txtFileNames.Text = String.Empty;
            String path = @"..\..\testdata\";
            for (int n = 0; n < stream.CountFrames; n++) {
                stream.ExportBitmap(n, path + n.ToString() + ".bmp");
                txtReportCopy.Text += n + ".bmp finished...\r\n";
                txtFileNames.Text += path + n + ".bmp\r\n";
            }

            stream.GetFrameClose();
            aviManager.Close();
        }

        private void btnWrite_Click(object sender, System.EventArgs e) {
            Bitmap bmp = (Bitmap)Image.FromFile(txtFileNames.Lines[0]);
            AviManager aviManager = new AviManager(@"..\..\testdata\new.avi", false);
            VideoStream aviStream = aviManager.AddVideoStream(false, 2, bmp);

            Bitmap bitmap;
            int count = 0;
            for (int n = 1; n < txtFileNames.Lines.Length; n++) {
                if (txtFileNames.Lines[n].Trim().Length > 0) {
                    bitmap = (Bitmap)Bitmap.FromFile(txtFileNames.Lines[n]);
                    aviStream.AddFrame(bitmap);
                    bitmap.Dispose();
                    count++;
                }
            }

            aviManager.Close();
        }

        private void btnWriteCompress_Click(object sender, System.EventArgs e) {
            //load the first image
            Bitmap bitmap = (Bitmap)Image.FromFile(txtFileNames.Lines[0]);
            //create a new AVI file
            AviManager aviManager = new AviManager(@"..\..\testdata\new.avi", false);
            //add a new video stream and one frame to the new file
            VideoStream aviStream = aviManager.AddVideoStream(true, 2, bitmap);

            int count = 0;
            for (int n = 1; n < txtFileNames.Lines.Length; n++) {
                if (txtFileNames.Lines[n].Trim().Length > 0) {
                    bitmap = (Bitmap)Bitmap.FromFile(txtFileNames.Lines[n]);
                    aviStream.AddFrame(bitmap);
                    bitmap.Dispose();
                    count++;
                }
            }

            aviManager.Close();
        }

        private void btnAppend_Click(object sender, System.EventArgs e) {
            //open file
            Bitmap bmp = (Bitmap)Image.FromFile(txtFileNames.Lines[0]);
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            VideoStream aviStream = aviManager.GetVideoStream();

            //streams cannot be edited - copy to a new file
            VideoStream newStream;
            AviManager newManager = aviStream.DecompressToNewFile(@"..\..\testdata\temp.avi", true, out newStream);
            aviStream = newStream; //newManager.GetOpenStream(0);

            //add images
            Bitmap bitmap;
            for (int n = 0; n < txtFileNames.Lines.Length; n++) {
                if (txtFileNames.Lines[n].Trim().Length > 0) {
                    bitmap = (Bitmap)Bitmap.FromFile(txtFileNames.Lines[n]);
                    aviStream.AddFrame(bitmap);
                    bitmap.Dispose();
                }
            }

            //close old file
            aviManager.Close();
            //save and close new file
            newManager.Close();

            //delete old file, replace with new file
            System.IO.File.Delete(txtAviFileName.Text);
            System.IO.File.Move(@"..\..\testdata\temp.avi", txtAviFileName.Text);
        }

        private void btnDecompress_Click(object sender, System.EventArgs e) {
            txtReportCopy.Text = "Decompressing " + txtAviFileName.Text + " to uncompressed.avi...\r\n";
            CopyFile(@"..\..\testdata\uncompressed.avi", false);
            txtReportCopy.Text += "...finished.";
        }

        private void btnCompress_Click(object sender, System.EventArgs e) {
            txtReportCopy.Text = "Compressing " + txtAviFileName.Text + " to compressed.avi...\r\n";
            CopyFile(@"..\..\testdata\compressed.avi", true);
            txtReportCopy.Text += "...finished.";
        }

        private void CopyFile(String newName, bool compress) {
            //open compressed file
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            VideoStream aviStream = aviManager.GetVideoStream();
            //create un-/re-compressed file
            VideoStream newStream;
            AviManager newManager = aviStream.DecompressToNewFile(newName, compress, out newStream);

            //close compressed file
            aviManager.Close();
            //save and close un-/re-compressed file
            newManager.Close();
        }


        private void numPosition_ValueChanged(object sender, System.EventArgs e) {
            ShowFrame();
        }

        private void ShowFrame() {
            if (System.IO.File.Exists(txtAviFileName.Text)) {
                try {
                    AviManager aviManager = new AviManager(txtAviFileName.Text, true);
                    VideoStream aviStream = aviManager.GetVideoStream();
                    aviStream.GetFrameOpen();

                    Bitmap bmp = aviStream.GetBitmap(Convert.ToInt32(numPosition.Value));
                    picFrame.Image = bmp;
                    aviStream.GetFrameClose();
                    aviManager.Close();
                } catch (Exception ex) {
                    MessageBox.Show(ex.ToString());
                }
            }
        }

        private void btnSelectFile_Click(object sender, System.EventArgs e) {
            String fileName = GetFileName("Videos (*.avi)|*.avi;*.mpe;*.mpeg");
            if (fileName != null) {
                txtAviFileName.Text = fileName;
                ShowFrame();
            }
        }

        private String GetCurrentFilePath() {
            return txtAviFileName.Text.Substring(0, txtAviFileName.Text.LastIndexOf("\\") + 1);
        }

        private void Form1_Load(object sender, System.EventArgs e) {
            ShowFrame();
        }

        private void btnExtractWave_Click(object sender, System.EventArgs e) {
            txtReportSound.Text = "Extracting " + txtAviFileName.Text + " to sound.wav...\r\n";
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            try {
                AudioStream audioStream = aviManager.GetWaveStream();
                audioStream.ExportStream(@"..\..\testdata\sound.wav");
                aviManager.Close();
                txtReportSound.Text += "...finished.";
            } catch (Exception ex) {
                MessageBox.Show(this, "The file does not contain a wave audio stream, or it cannot be opened.\r\n" + ex.ToString(), "No Stream Found");
            }
        }

        private String GetFileName(String filter) {
            OpenFileDialog dlg = new OpenFileDialog();
            dlg.Filter = filter;
            dlg.RestoreDirectory = true;
            if (txtAviFileName.Text.Length > 0) {
                dlg.InitialDirectory = GetCurrentFilePath();
            }
            if (dlg.ShowDialog(this) == DialogResult.OK) {
                return dlg.FileName;
            } else {
                return null;
            }
        }

        private void btnAddSound_Click(object sender, System.EventArgs e) {
            String fileName = GetFileName("Sounds (*.wav)|*.wav");
            if (fileName != null) {
                txtReportSound.Text = "Adding to sound.wav to " + txtAviFileName.Text + "...\r\n";
                AviManager aviManager = new AviManager(txtAviFileName.Text, true);
                try {
                    int countFrames = aviManager.GetVideoStream().CountFrames;
                    if (countFrames > numInsertWavePosition.Value) {
                        aviManager.AddAudioStream(fileName, (int)numInsertWavePosition.Value);
                    } else {
                        MessageBox.Show(this, "Frame " + numInsertWavePosition.Value + " does not exists. The video stream contains frame from 0 to " + (countFrames - 1) + ".");
                    }
                } catch (Exception ex) {
                    MessageBox.Show(this, "The file does not accept the new wave audio stream.\r\n" + ex.ToString(), "Error");
                }
                aviManager.Close();
                txtReportSound.Text += "...finished.";
            }
        }

        private void btnExtractVideo_Click(object sender, System.EventArgs e) {
            txtReportCopy.Text = "Extracting " + txtAviFileName.Text + " to video.avi...\r\n";
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            VideoStream videoStream = aviManager.GetVideoStream();
            videoStream.ExportStream(@"..\..\testdata\video.avi");
            aviManager.Close();
            txtReportCopy.Text += "...finished.";
        }

        private void btnExtractPart_Click(object sender, EventArgs e) {
            AviManager aviManager = new AviManager(txtAviFileName.Text, true);
            VideoStream aviStream = aviManager.GetVideoStream();

            CopyForm dialog = new CopyForm(0, (int)Math.Floor(aviStream.CountFrames / aviStream.FrameRate));
            if (dialog.ShowDialog() == DialogResult.OK) {
                int startSecond = dialog.Start;
                int stopSecond = dialog.Stop;

                txtReportCopy.Text = "Cutting seconds from " + txtAviFileName.Text + " to video.avi...\r\n";
                AviManager newFile = aviManager.CopyTo("..\\..\\testdata\\video.avi", startSecond, stopSecond);
                newFile.Close();
                txtReportCopy.Text += "...finished.";
            }
            aviManager.Close();
        }
    }
}
