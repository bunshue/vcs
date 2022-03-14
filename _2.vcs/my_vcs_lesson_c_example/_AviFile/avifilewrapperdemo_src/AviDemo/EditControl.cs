#region Using directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Text;
using System.IO;
using System.Windows.Forms;
using AviFile;

#endregion

namespace AviDemo {
    public partial class EditControl : UserControl {

        private delegate void SimpleDelegate();

        private AviPlayer player;
        private EditableVideoStream editableStream;

        public EditControl() {
            InitializeComponent();
            panelEditor.Enabled = false;
        }

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

        private void btnClose_Click(object sender, EventArgs e)
        {
            editableStream.Close();
            editableStream = null;
            panelEditor.Enabled = false;
        }
    }
}
