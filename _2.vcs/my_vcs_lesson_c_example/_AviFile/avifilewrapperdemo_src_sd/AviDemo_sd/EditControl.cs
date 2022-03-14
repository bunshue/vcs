using System;
using System.IO;
using System.Drawing;
using System.ComponentModel;
using System.Windows.Forms;
using AviFile;

namespace AviDemo
{
	public class EditControl : System.Windows.Forms.UserControl
	{
		/// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

		private System.Windows.Forms.Panel panelEditor;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button btnSetStreamInfo;
        private System.Windows.Forms.NumericUpDown numFrameRate;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btnDelete;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown numPastePositionStream;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button btnCut;
        private System.Windows.Forms.Button btnCopy;
        private System.Windows.Forms.NumericUpDown numLast;
        private System.Windows.Forms.NumericUpDown numFirst;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.PictureBox picPreview;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblFrameIndex;
        private System.Windows.Forms.Button btnStop;
        private System.Windows.Forms.Button btnPlay;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.NumericUpDown numPastePositionBitmap;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button btnAddFrame;
        private System.Windows.Forms.Button btnSelectBitmap;
        private System.Windows.Forms.TextBox txtNewFrameFileName;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnOpen;
        private System.Windows.Forms.Button btnSelectFile;
        private System.Windows.Forms.TextBox txtAviFileName;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnClose;
		
		private delegate void SimpleDelegate();
		
        private AviPlayer player;
        private EditableVideoStream editableStream;

		public EditControl() {
            InitializeComponent();
            panelEditor.Enabled = false;
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
            this.panelEditor = new System.Windows.Forms.Panel();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.btnSetStreamInfo = new System.Windows.Forms.Button();
            this.numFrameRate = new System.Windows.Forms.NumericUpDown();
            this.label8 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnDelete = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.numPastePositionStream = new System.Windows.Forms.NumericUpDown();
            this.label5 = new System.Windows.Forms.Label();
            this.btnCut = new System.Windows.Forms.Button();
            this.btnCopy = new System.Windows.Forms.Button();
            this.numLast = new System.Windows.Forms.NumericUpDown();
            this.numFirst = new System.Windows.Forms.NumericUpDown();
            this.label4 = new System.Windows.Forms.Label();
            this.btnSave = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.picPreview = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblFrameIndex = new System.Windows.Forms.Label();
            this.btnStop = new System.Windows.Forms.Button();
            this.btnPlay = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.label6 = new System.Windows.Forms.Label();
            this.numPastePositionBitmap = new System.Windows.Forms.NumericUpDown();
            this.label7 = new System.Windows.Forms.Label();
            this.btnAddFrame = new System.Windows.Forms.Button();
            this.btnSelectBitmap = new System.Windows.Forms.Button();
            this.txtNewFrameFileName = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnOpen = new System.Windows.Forms.Button();
            this.btnSelectFile = new System.Windows.Forms.Button();
            this.txtAviFileName = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnClose = new System.Windows.Forms.Button();
            this.panelEditor.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
// 
// panelEditor
// 
            this.panelEditor.Controls.Add(this.btnClose);
            this.panelEditor.Controls.Add(this.groupBox4);
            this.panelEditor.Controls.Add(this.groupBox1);
            this.panelEditor.Controls.Add(this.btnSave);
            this.panelEditor.Controls.Add(this.groupBox2);
            this.panelEditor.Controls.Add(this.groupBox3);
            this.panelEditor.Location = new System.Drawing.Point(4, 89);
            this.panelEditor.Name = "panelEditor";
            this.panelEditor.Size = new System.Drawing.Size(742, 349);
            this.panelEditor.TabIndex = 34;
// 
// groupBox4
// 
            this.groupBox4.Controls.Add(this.btnSetStreamInfo);
            this.groupBox4.Controls.Add(this.numFrameRate);
            this.groupBox4.Controls.Add(this.label8);
            this.groupBox4.Location = new System.Drawing.Point(233, 195);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(251, 98);
            this.groupBox4.TabIndex = 32;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Stream Info";
// 
// btnSetStreamInfo
// 
            this.btnSetStreamInfo.Location = new System.Drawing.Point(19, 60);
            this.btnSetStreamInfo.Name = "btnSetStreamInfo";
            this.btnSetStreamInfo.Size = new System.Drawing.Size(165, 23);
            this.btnSetStreamInfo.TabIndex = 2;
            this.btnSetStreamInfo.Text = "Change Frame Rate";
            this.btnSetStreamInfo.Click += new System.EventHandler(this.btnSetStreamInfo_Click);
// 
// numFrameRate
// 
            this.numFrameRate.DecimalPlaces = 4;
            this.numFrameRate.Location = new System.Drawing.Point(120, 24);
            this.numFrameRate.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numFrameRate.Name = "numFrameRate";
            this.numFrameRate.Size = new System.Drawing.Size(64, 20);
            this.numFrameRate.TabIndex = 1;
// 
// label8
// 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(19, 30);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(64, 14);
            this.label8.TabIndex = 0;
            this.label8.Text = "Frame Rate";
// 
// groupBox1
// 
            this.groupBox1.Controls.Add(this.btnDelete);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.numPastePositionStream);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.btnCut);
            this.groupBox1.Controls.Add(this.btnCopy);
            this.groupBox1.Controls.Add(this.numLast);
            this.groupBox1.Controls.Add(this.numFirst);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Location = new System.Drawing.Point(8, 4);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(207, 289);
            this.groupBox1.TabIndex = 22;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Copy, Cut, Paste";
// 
// btnDelete
// 
            this.btnDelete.Location = new System.Drawing.Point(17, 177);
            this.btnDelete.Name = "btnDelete";
            this.btnDelete.Size = new System.Drawing.Size(142, 23);
            this.btnDelete.TabIndex = 22;
            this.btnDelete.Text = "Delete, no Paste";
            this.btnDelete.Click += new System.EventHandler(this.btnDelete_Click);
// 
// label3
// 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(17, 29);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(62, 14);
            this.label3.TabIndex = 14;
            this.label3.Text = "First Frame";
// 
// numPastePositionStream
// 
            this.numPastePositionStream.Location = new System.Drawing.Point(107, 77);
            this.numPastePositionStream.Name = "numPastePositionStream";
            this.numPastePositionStream.Size = new System.Drawing.Size(52, 20);
            this.numPastePositionStream.TabIndex = 21;
// 
// label5
// 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(18, 83);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(89, 14);
            this.label5.TabIndex = 20;
            this.label5.Text = "Paste at Position";
// 
// btnCut
// 
            this.btnCut.Location = new System.Drawing.Point(17, 147);
            this.btnCut.Name = "btnCut";
            this.btnCut.Size = new System.Drawing.Size(142, 23);
            this.btnCut.TabIndex = 19;
            this.btnCut.Text = "Cut and Paste";
            this.btnCut.Click += new System.EventHandler(this.btnCut_Click);
// 
// btnCopy
// 
            this.btnCopy.Location = new System.Drawing.Point(18, 117);
            this.btnCopy.Name = "btnCopy";
            this.btnCopy.Size = new System.Drawing.Size(141, 23);
            this.btnCopy.TabIndex = 18;
            this.btnCopy.Text = "Copy and Paste";
            this.btnCopy.Click += new System.EventHandler(this.btnCopy_Click);
// 
// numLast
// 
            this.numLast.Location = new System.Drawing.Point(107, 50);
            this.numLast.Name = "numLast";
            this.numLast.Size = new System.Drawing.Size(52, 20);
            this.numLast.TabIndex = 17;
// 
// numFirst
// 
            this.numFirst.Location = new System.Drawing.Point(107, 23);
            this.numFirst.Name = "numFirst";
            this.numFirst.Size = new System.Drawing.Size(52, 20);
            this.numFirst.TabIndex = 16;
// 
// label4
// 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(18, 56);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(61, 14);
            this.label4.TabIndex = 15;
            this.label4.Text = "Last Frame";
// 
// btnSave
// 
            this.btnSave.Location = new System.Drawing.Point(421, 319);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(155, 23);
            this.btnSave.TabIndex = 31;
            this.btnSave.Text = "Save new Video Stream";
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
// 
// groupBox2
// 
            this.groupBox2.Controls.Add(this.picPreview);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Controls.Add(this.lblFrameIndex);
            this.groupBox2.Controls.Add(this.btnStop);
            this.groupBox2.Controls.Add(this.btnPlay);
            this.groupBox2.Location = new System.Drawing.Point(504, 4);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(234, 289);
            this.groupBox2.TabIndex = 23;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Play Video";
// 
// picPreview
// 
            this.picPreview.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.picPreview.Location = new System.Drawing.Point(16, 20);
            this.picPreview.Name = "picPreview";
            this.picPreview.Size = new System.Drawing.Size(202, 173);
            this.picPreview.TabIndex = 0;
            this.picPreview.TabStop = false;
// 
// label1
// 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 200);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 14);
            this.label1.TabIndex = 12;
            this.label1.Text = "Frame Index";
// 
// lblFrameIndex
// 
            this.lblFrameIndex.AutoSize = true;
            this.lblFrameIndex.Location = new System.Drawing.Point(84, 200);
            this.lblFrameIndex.Name = "lblFrameIndex";
            this.lblFrameIndex.Size = new System.Drawing.Size(10, 14);
            this.lblFrameIndex.TabIndex = 13;
            this.lblFrameIndex.Text = "0";
// 
// btnStop
// 
            this.btnStop.Enabled = false;
            this.btnStop.Location = new System.Drawing.Point(16, 251);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(202, 23);
            this.btnStop.TabIndex = 11;
            this.btnStop.Text = "Stop Preview";
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
// 
// btnPlay
// 
            this.btnPlay.Location = new System.Drawing.Point(16, 221);
            this.btnPlay.Name = "btnPlay";
            this.btnPlay.Size = new System.Drawing.Size(202, 23);
            this.btnPlay.TabIndex = 10;
            this.btnPlay.Text = "Play Preview";
            this.btnPlay.Click += new System.EventHandler(this.btnPlay_Click);
// 
// groupBox3
// 
            this.groupBox3.Controls.Add(this.label6);
            this.groupBox3.Controls.Add(this.numPastePositionBitmap);
            this.groupBox3.Controls.Add(this.label7);
            this.groupBox3.Controls.Add(this.btnAddFrame);
            this.groupBox3.Controls.Add(this.btnSelectBitmap);
            this.groupBox3.Controls.Add(this.txtNewFrameFileName);
            this.groupBox3.Location = new System.Drawing.Point(233, 4);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(251, 184);
            this.groupBox3.TabIndex = 30;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Insert Frames";
// 
// label6
// 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(19, 31);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(45, 14);
            this.label6.TabIndex = 25;
            this.label6.Text = "Pictures";
// 
// numPastePositionBitmap
// 
            this.numPastePositionBitmap.Location = new System.Drawing.Point(132, 107);
            this.numPastePositionBitmap.Name = "numPastePositionBitmap";
            this.numPastePositionBitmap.Size = new System.Drawing.Size(52, 20);
            this.numPastePositionBitmap.TabIndex = 29;
// 
// label7
// 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(19, 113);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(89, 14);
            this.label7.TabIndex = 28;
            this.label7.Text = "Paste at Position";
// 
// btnAddFrame
// 
            this.btnAddFrame.Location = new System.Drawing.Point(19, 143);
            this.btnAddFrame.Name = "btnAddFrame";
            this.btnAddFrame.Size = new System.Drawing.Size(165, 23);
            this.btnAddFrame.TabIndex = 27;
            this.btnAddFrame.Text = "Add Frame";
            this.btnAddFrame.Click += new System.EventHandler(this.btnAddFrame_Click);
// 
// btnSelectBitmap
// 
            this.btnSelectBitmap.Location = new System.Drawing.Point(188, 44);
            this.btnSelectBitmap.Name = "btnSelectBitmap";
            this.btnSelectBitmap.Size = new System.Drawing.Size(58, 20);
            this.btnSelectBitmap.TabIndex = 26;
            this.btnSelectBitmap.Text = "Browse...";
            this.btnSelectBitmap.Click += new System.EventHandler(this.btnSelectBitmap_Click);
// 
// txtNewFrameFileName
// 
            this.txtNewFrameFileName.AutoSize = false;
            this.txtNewFrameFileName.Location = new System.Drawing.Point(19, 45);
            this.txtNewFrameFileName.Multiline = true;
            this.txtNewFrameFileName.Name = "txtNewFrameFileName";
            this.txtNewFrameFileName.Size = new System.Drawing.Size(165, 52);
            this.txtNewFrameFileName.TabIndex = 24;
// 
// panel1
// 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.btnOpen);
            this.panel1.Controls.Add(this.btnSelectFile);
            this.panel1.Controls.Add(this.txtAviFileName);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Location = new System.Drawing.Point(4, 4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(732, 69);
            this.panel1.TabIndex = 33;
// 
// btnOpen
// 
            this.btnOpen.Location = new System.Drawing.Point(489, 36);
            this.btnOpen.Name = "btnOpen";
            this.btnOpen.Size = new System.Drawing.Size(155, 23);
            this.btnOpen.TabIndex = 8;
            this.btnOpen.Text = "Edit Selected File";
            this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
// 
// btnSelectFile
// 
            this.btnSelectFile.Location = new System.Drawing.Point(651, 9);
            this.btnSelectFile.Name = "btnSelectFile";
            this.btnSelectFile.Size = new System.Drawing.Size(62, 20);
            this.btnSelectFile.TabIndex = 7;
            this.btnSelectFile.Text = "Browse...";
            this.btnSelectFile.Click += new System.EventHandler(this.btnSelectFile_Click);
// 
// txtAviFileName
// 
            this.txtAviFileName.Location = new System.Drawing.Point(107, 9);
            this.txtAviFileName.Name = "txtAviFileName";
            this.txtAviFileName.Size = new System.Drawing.Size(537, 20);
            this.txtAviFileName.TabIndex = 5;
            this.txtAviFileName.Text = "..\\..\\testdata\\test.avi";
// 
// label2
// 
            this.label2.Location = new System.Drawing.Point(7, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Edit AVI File";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
// 
// btnClose
// 
            this.btnClose.Location = new System.Drawing.Point(583, 319);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(155, 23);
            this.btnClose.TabIndex = 33;
            this.btnClose.Text = "Discard new Video Stream";
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
// 
// EditControl
// 
            this.Controls.Add(this.panelEditor);
            this.Controls.Add(this.panel1);
            this.Name = "EditControl";
            this.Size = new System.Drawing.Size(752, 443);
            this.panelEditor.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

		private void btnOpen_Click(object sender, EventArgs e) {
            if (editableStream != null) {
                editableStream.Close();
            }

            AviManager file = new AviManager(txtAviFileName.Text, true);
            VideoStream stream = file.GetVideoStream();
            editableStream = new EditableVideoStream(stream);
            file.Close();

            numFirst.Maximum = editableStream.CountFrames - 1;
            numFirst.Value = 0;

            numPastePositionStream.Maximum = editableStream.CountFrames - 1;
            numPastePositionStream.Value = 0;

            numLast.Maximum = editableStream.CountFrames - 1;
            numLast.Value = editableStream.CountFrames - 1;

            if (numFrameRate.Maximum < (decimal)editableStream.FrameRate) {
                numFrameRate.Maximum = (decimal)editableStream.FrameRate;
            }
            numFrameRate.Value = (decimal)editableStream.FrameRate;

            panelEditor.Enabled = true;
        }

        private String GetFileName(String filter) {
            OpenFileDialog dlg = new OpenFileDialog();
            dlg.Filter = filter;
            dlg.RestoreDirectory = true;
            if (txtAviFileName.Text.Length > 0) {
                dlg.InitialDirectory = txtAviFileName.Text.Substring(0, txtAviFileName.Text.LastIndexOf("\\") + 1);
            }
            if (dlg.ShowDialog(this) == DialogResult.OK) {
                return dlg.FileName;
            } else {
                return null;
            }
        }

        private void btnSelectFile_Click(object sender, EventArgs e) {
            String fileName = GetFileName("Videos (*.avi)|*.avi;*.mpe;*.mpeg");
            if (fileName != null) {
                txtAviFileName.Text = fileName;
            }
        }

        private void btnPlay_Click(object sender, EventArgs e) {
            player = new AviPlayer(editableStream, picPreview, lblFrameIndex);
            player.Stopped += new System.EventHandler(player_Stopped);
            player.Start();
            SetPreviewButtonsState();
        }

        private void player_Stopped(object sender, EventArgs e) {
            btnPlay.Invoke(new SimpleDelegate(SetPreviewButtonsState));
        }

        private void SetPreviewButtonsState() {
            btnPlay.Enabled = ! player.IsRunning;
            btnStop.Enabled = player.IsRunning;
        }

        private void btnStop_Click(object sender, EventArgs e) {
            player.Stop();
        }

        private void btnCopy_Click(object sender, EventArgs e) {
            int start = (int)numFirst.Value;
            int length = 1 + (int)numLast.Value - start;
            int position = (int)numPastePositionStream.Value;

            //copy frames
            IntPtr copiedData = editableStream.Copy(start, length);

            //insert frames
            editableStream.Paste(copiedData, 0, position, length);
        }

        private void btnCut_Click(object sender, EventArgs e) {
            int start = (int)numFirst.Value;
            int length = 1 + (int)numLast.Value - start;
            int position = (int)numPastePositionStream.Value;

            //cut frames
            IntPtr copiedData = editableStream.Cut(start, length);

            //insert frames
            editableStream.Paste(copiedData, 0, position, length);
        }

        private void btnDelete_Click(object sender, EventArgs e) {
            int start = (int)numFirst.Value;
            int length = 1 + (int)numLast.Value - start;

            //cut frames
            IntPtr copiedData = editableStream.Cut(start, length);
        }

        private void btnAddFrame_Click(object sender, EventArgs e) {
            String tempFileName = System.IO.Path.GetTempFileName() + ".avi";
            AviManager tempFile = new AviManager(tempFileName, false);

            Bitmap bitmap = (Bitmap)Image.FromFile(txtNewFrameFileName.Lines[0].Trim());
            tempFile.AddVideoStream(false, 1, bitmap);
            VideoStream stream = tempFile.GetVideoStream();

            for (int n = 1; n < txtNewFrameFileName.Lines.Length; n++) {
                if (txtNewFrameFileName.Lines[n].Trim().Length > 0) {
                    stream.AddFrame((Bitmap)Image.FromFile(txtNewFrameFileName.Lines[n]));
                }
            }

            editableStream.Paste(stream, 0, (int)numPastePositionBitmap.Value, stream.CountFrames);

            tempFile.Close();
            try { File.Delete(tempFileName); } catch (IOException) { }
        }

        private void btnSelectBitmap_Click(object sender, EventArgs e) {
            String fileName = GetFileName("Images (*.bmp; *.jpg; *.tif; *.png; *.gif)|*.bmp;*.jpg;*.tif;*.png;*.gif");
            if (fileName != null) {
                txtNewFrameFileName.Text += fileName + "\r\n";
            }
        }

        private void btnSave_Click(object sender, EventArgs e) {
            SaveFileDialog dlg = new SaveFileDialog();
            dlg.Filter = "Videos (*.avi)|*.avi;";
            if (dlg.ShowDialog() == DialogResult.OK) {
                AviManager.MakeFileFromStream(dlg.FileName, editableStream);
                editableStream.Close();
                editableStream = null;
                panelEditor.Enabled = false;
            }
        }

        private void btnSetStreamInfo_Click(object sender, EventArgs e) {
            Avi.AVISTREAMINFO info = editableStream.StreamInfo;
            info.dwRate = (int)(numFrameRate.Value * 10000);
            info.dwScale = 10000;
            editableStream.SetInfo(info);
        }

        private void btnClose_Click(object sender, EventArgs e) {
            editableStream.Close();
            editableStream = null;
            panelEditor.Enabled = false;
        }
	}
}
