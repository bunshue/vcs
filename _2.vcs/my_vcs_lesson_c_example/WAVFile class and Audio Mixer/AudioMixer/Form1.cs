/* This file contains the Form1 class, which is the main GUI for the AudioMerger application.
 *
 * Date       Author         Description
 * 2009-03-09 erico          Created
 * 2009-03-24 erico          Updated to perform the audio merging in a separate thread
 *                           so that the GUI is not frozen during the process.
 * 2009-03-31 erico          Updated so that only the filename (without the full directory) shows up
 *                           on the GUI.  The full pathes are stored in a member ArrayList.
 * 2009-04-01 erico          Fixed bugs related to adding & removing audio files to the GUI.
 *                           Setting the AllowUserToAddRows property of FilenameGrid helped a lot
 *                           with that and allowed simpler code for adding an audio file to the GUI.
 *                           Changed the first File menu option to "Add audio file(s)" to allow
 *                           the user to add 1 or more WAV files to the GUI.  Also, added a Help
 *                           menu with an "About" option.  Also, renamed the program from Audio
 *                           Merger to Audio Mixer.
 */

using System;
using System.Windows.Forms;
using System.IO;
using System.Threading;
using System.Collections;

using EricOulashin;

namespace AudioMerger
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// Stores the paths to the audio files (without trailing backslash).
        /// </summary>
        private ArrayList mSoundFilePaths;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            mSoundFilePaths = new ArrayList();

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\_wav\1.wav";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\_wav\2.wav";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\_wav\3.wav";
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\_wav\4.wav";
            AddAudioFilename(filename1);
            AddAudioFilename(filename2);
            AddAudioFilename(filename3);
            AddAudioFilename(filename4);

        }

        /// <summary>
        /// Sets the text of the first status label.
        /// </summary>
        /// <param name="pText">The text to set in the status label</param>
        public void Show_Message(String pText)
        {
            richTextBox1.Text += "message : " + pText + "\n";
        }

        /// <summary>
        /// Enables the GUI elements related to audio merging.
        /// </summary>
        public void EnableAudioMergeGUIElements()
        {
            FilenameGrid.Enabled = true;
            MixAudioButton.Enabled = true;
            ClearListButton.Enabled = true;
        }

        /// <summary>
        /// Disables the GUI elements related to audio merging.
        /// </summary>
        public void DisableAudioMergeGUIElements()
        {
            FilenameGrid.Enabled = false;
            MixAudioButton.Enabled = false;
            ClearListButton.Enabled = false;
        }

        private void FilenameGrid_DragEnter(object sender, System.Windows.Forms.DragEventArgs e)
        {
            // make sure they're actually dropping files (not text or anything else)
            if (e.Data.GetDataPresent(DataFormats.FileDrop, false))
            {
                // allow them to continue
                // (without this, the cursor stays a "NO" symbol
                e.Effect = DragDropEffects.All;
            }
        }

        private void FilenameGrid_DragDrop(object sender, System.Windows.Forms.DragEventArgs e)
        {
            // transfer the filenames to a string array
            string[] files = (string[])e.Data.GetData(DataFormats.FileDrop);

            // loop through the string array, adding each filename to the ListBox
            foreach (string filename in files)
            {
                // Make sure the file is a WAV audio file before adding it.
                if (WAVFile.IsWaveFile(filename))
                {
                    AddAudioFilename(filename);
                }
            }
        }

        ///////////////////
        // Private stuff //
        //////////////////

        /// <summary>
        /// Adds a filename to the GUI and related data members.
        /// </summary>
        /// <param name="pFilename">The name of the audio file to add (fully pathed)</param>
        private void AddAudioFilename(String pFilename)
        {
            // Add a new row for the filename, and store the new row number.
            // Note: This works properly because the AllowUserToAddRows property
            // of FilenameGrid is set to false.
            FilenameGrid.Rows.Add(1);
            int rowNum = FilenameGrid.Rows.Count - 1;

            // Add the filename to the row (just the filename, without the full path).  Also, add the text to
            // the row's "Remove" button.
            FilenameGrid.Rows[rowNum].Cells[0].Value = Path.GetFileName(pFilename);
            FilenameGrid.Rows[rowNum].Cells[1].Value = "Remove";

            // Add the full sound file path to mSoundFilePaths.
            mSoundFilePaths.Add(Path.GetDirectoryName(pFilename));

            // The grid automatically selects the last row added.  Make sure the last row added is not selected.
            if (rowNum > 0)
            {
                FilenameGrid.Rows[rowNum - 1].Selected = false;
            }
        }

        /// <summary>
        /// Returns the fully-pathed filename for one of the audio files from a given index.  If the
        /// index is not valid, this will return a blank string.
        /// </summary>
        /// <param name="pIndex">The index of the filename to return</param>
        /// <returns>The fully-pathed audio filename, or a blank string if the given index is not valid.</returns>
        private String GetFullyPathedAudioFilename(int pIndex)
        {
            String filename = "";

            if ((pIndex >= 0) && (pIndex < mSoundFilePaths.Count) && (pIndex < FilenameGrid.Rows.Count))
            {
                // Note: The filename is in cell 0 of the row, and its path (without trailing separator
                // character) is in mSoundFilePaths.
                filename = ((String)(mSoundFilePaths[pIndex]) + Path.DirectorySeparatorChar
                         + (String)(FilenameGrid.Rows[pIndex].Cells[0].Value));
            }

            return filename;
        }

        // Merge button event function - Merges the WAV files together.
        private void MergeAudioButton_Click(object sender, EventArgs e)
        {
            try
            {
                // If there are less than 2 audio files, then there is nothing to do.
                if (FilenameGrid.Rows.Count < 2)
                {
                    String message = "Nothing to do.";
                    if ((FilenameGrid.Rows.Count == 1) && ((String)FilenameGrid.Rows[0].Cells[0].Value != null))
                    {
                        message += "  There is only 1 audio file.";
                    }
                    //MessageBox.Show(this, message, "Message");
                    richTextBox1.Text += "XXXXX1 " + message + "\n";
                    return;
                }

                string mixOutputFilename = DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

                richTextBox1.Text += "Working...\n";

                // Create an array of filenames for the WAVFile class
                String[] audioFilenames = new String[FilenameGrid.Rows.Count];
                for (int row = 0; row < FilenameGrid.Rows.Count; ++row)
                {
                    audioFilenames[row] = GetFullyPathedAudioFilename(row);
                }

                // Perform the audio mix
                AudioMergeThread mergeThread = new AudioMergeThread(this, audioFilenames, mixOutputFilename, Application.StartupPath);
                mergeThread.mThread.Start();
            }
            catch (Exception exc)
            {
                //MessageBox.Show(this, exc.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                richTextBox1.Text += "XXXXX2 " + exc.Message + "\n";
                EnableAudioMergeGUIElements();
            }
        }

        /// <summary>
        /// Clears the audio file list.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void ClearListButton_Click(object sender, EventArgs e)
        {
            FilenameGrid.Rows.Clear();
            mSoundFilePaths.Clear();
        }

        /// <summary>
        /// This is an event function that is called when a user clicks on one of the "Remove" buttons
        /// in the filename grid.  This will remove the filename from the GUI and mSoundFilePaths.
        /// </summary>
        /// <param name="sender">The sending object</param>
        /// <param name="e">Contains information for the data grid click event</param>
        private void FilenameGrid_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            richTextBox1.Text += "你按了 ColumnIndex = " + e.ColumnIndex.ToString() + "\n";

            // If the user clicked on the button (column 1), then remove the audio file from the list.
            if (e.ColumnIndex == 1)
            {
                try
                {
                    richTextBox1.Text += "你按了第 " + e.RowIndex.ToString() + " 項\n";
                    FilenameGrid.Rows.RemoveAt(e.RowIndex);
                    mSoundFilePaths.RemoveAt(e.RowIndex);
                }
                catch (Exception exc)
                {
                    MessageBox.Show(this, exc.Message, "Error removing audio file", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    richTextBox1.Text += "XXXXX3 " + exc.Message + "\n";
                }
            }
        }
    }
}

