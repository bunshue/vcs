/* This file contains the AudioMergeThread class, which helps to encapsulate the threading and
 * logic to run the audio merge operation in a separate thread so that the main GUI is not frozen.
 *
 * Date       Author         Description
 * 2009-03-24 erico          Created
 * 2009-03-31 erico          Fixed bugs in AudioMergeWorker() related to re-enabling the main GUI
 *                           after the audio merge is done.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using EricOulashin;

namespace AudioMerger
{
    class AudioMergeThread
    {
        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="pAppForm">The main application form</param>
        /// <param name="pAudioFilenames">An array of Strings containing the names of the WAV files to merge</param>
        /// <param name="pDestFilename">The name of the destination WAV file</param>
        /// <param name="pTempDir">The full path to the temporary directory to be used</param>
        public AudioMergeThread(AudioMerger.Form1 pAppForm, String[] pAudioFilenames, String pDestFilename, String pTempDir)
        {
            mAppForm = pAppForm;
            mAudioFilenames = pAudioFilenames;
            mDestFilename = pDestFilename;
            mTempDir = pTempDir;

            mThread = new Thread(AudioMergeWorker);
        }

        /// <summary>
        /// This is the function that actually performs the audio merging and runs as in a separate thread.
        /// </summary>
        private void AudioMergeWorker()
        {
            mAppForm.UseWaitCursor = true;

            try
            {
                // Disable the audio merge GUI elements on the main GUI
                mAppForm.DisableAudioMergeGUIElements();
                // Merge the audio files.  When done, set the status text in the GUI to say "Done.".
                WAVFile.MergeAudioFiles(mAudioFilenames, mDestFilename, mTempDir);

                // Clean and remove the temporary directory
                String retval = UtilityFunctions.DeleteDir(mTempDir);
                if (retval != "")
                {
                    MessageBox.Show(mAppForm, "Error removing temporary directory:\n" + mTempDir + "\n" + retval, "Error",
                                    MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (WAVFileAudioMergeException exc)
            {
                MessageBox.Show(mAppForm, "Audio merge exception: " + exc.Message, "Error", MessageBoxButtons.OK,
                                MessageBoxIcon.Error);
            }
            catch (WAVFileException exc)
            {
                MessageBox.Show(mAppForm, "WAV file exception: " + exc.Message, "Error", MessageBoxButtons.OK,
                                MessageBoxIcon.Error);
            }
            catch (Exception exc)
            {
                MessageBox.Show(mAppForm, exc.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            try
            {
                mAppForm.Show_Message("Done.");

                // Re-enable the audio merge GUI elements on the main GUI
                mAppForm.EnableAudioMergeGUIElements();
            }
            catch (Exception exc)
            {
                MessageBox.Show(mAppForm, exc.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            mAppForm.UseWaitCursor = false;
        }

        public Thread mThread;            // The thread to use for audio merging

        private AudioMerger.Form1 mAppForm;       // The main application form (to use for message boxes)
        private String[] mAudioFilenames; // Array of the names of the audio files to merge
        private String mDestFilename;     // The destination (merged) audio file name
        private String mTempDir;          // Directory to use for temporary work
    }
}
