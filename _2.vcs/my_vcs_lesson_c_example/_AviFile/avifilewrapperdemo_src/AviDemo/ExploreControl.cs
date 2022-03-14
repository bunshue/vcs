#region Using directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Text;
using System.Windows.Forms;
using AviFile;

#endregion

namespace AviDemo {
    public partial class ExploreControl : UserControl {
        public ExploreControl() {
            InitializeComponent();
        }

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
			FrameRateForm dlg = new FrameRateForm();
			if(dlg.ShowDialog() == DialogResult.OK){
				Bitmap bmp = (Bitmap)Image.FromFile(txtFileNames.Lines[0]);
		        AviManager aviManager = new AviManager(@"..\..\testdata\new.avi", false);
			    VideoStream aviStream = aviManager.AddVideoStream(false, dlg.Rate, bmp);

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
		}

        private void btnWriteCompress_Click(object sender, System.EventArgs e) {
			FrameRateForm dlg = new FrameRateForm();
			if(dlg.ShowDialog() == DialogResult.OK){
				//load the first image
				Bitmap bitmap = (Bitmap)Image.FromFile(txtFileNames.Lines[0]);
				//create a new AVI file
				AviManager aviManager = new AviManager(@"..\..\testdata\new.avi", false);
				//add a new video stream and one frame to the new file
				VideoStream aviStream = aviManager.AddVideoStream(true, dlg.Rate, bitmap);

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
