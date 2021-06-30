using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using Microsoft.WindowsAPICodePack.Dialogs;
using Microsoft.WindowsAPICodePack.Taskbar;
using Microsoft.WindowsAPICodePack.Shell;

namespace player
{
    public partial class Form1 : Form
    {
        player player;
        int playState, songLength, timerCount;
        private ThumbnailToolbarButton buttonPlayPause;
        private ThumbnailToolbarButton buttonNext;
        private ThumbnailToolbarButton buttonPrevious;
        TaskbarManager tbManager = TaskbarManager.Instance;

        public Form1()
        {
            InitializeComponent();
            player = new player();
            playState = 1;
            songLength = 0;
            timerCount = 1;
        }

        private void playlist_DoubleClick(object sender, EventArgs e)
        {
            richTextBox1.Text += "playlist_DoubleClick\n"; 

            PlaySelectedSong();
        }

        private void btnPrevious_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "上一首\n"; 
            PlayPreviousSong(); 
        }

        private void PlayPreviousSong()
        {
            if ((playlist.SelectedIndex - 1) >= 0)
            {
                playlist.SelectedItem = playlist.Items[playlist.SelectedIndex - 1];
                PlaySelectedSong();
            }
        }

        private void btnNext_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "下一首\n";
            PlayNextSong(); 
           
        }

        private void PlayNextSong()
        {
            if ((playlist.SelectedIndex + 1) < playlist.Items.Count)
            {
                playlist.SelectedItem = playlist.Items[playlist.SelectedIndex + 1];
                PlaySelectedSong();
            }
        }

        private void btnAddSong_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "添加檔案\n";
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                playlist.Items.Add(openFileDialog.FileName);
            }
        }

        private void btnRemoveSong_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "移除檔案\n";
            playlist.Items.Remove(playlist.SelectedItem);
        }

        private void btnPlay_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "播放檔案\t";
            if (playState == 0)
            {
                richTextBox1.Text += "11111\n";
                player.PlaySong();
                playState = 1;
                SetTimerforPlay();
            }
            else
            {
                richTextBox1.Text += "22222\n";
                PlaySelectedSong();
            }
            buttonPlayPause.Icon = Properties.Resources.Pause;
        }

        private void btnPause_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "暫停\n";
            buttonPlayPause.Icon = Properties.Resources.play;
            player.PauseSong();
            playState = 0;
            SetTimerforPause();
        }
        
        private void SetTimerforPlay()
        {
            tbManager.SetProgressState(TaskbarProgressBarState.Normal);
            progressbarTimer.Enabled = true;
        }
        
        private void SetTimerforPause()
        {
            tbManager.SetProgressState(TaskbarProgressBarState.Error);
            progressbarTimer.Enabled = false;
        }

        private void PlaySelectedSong()
        {
            SetAlbumArt();
            SetTaskbarthumbnail();
            GetSongLength();
            timerCount = 1;
            SetTimerforPlay();

            if (playlist.SelectedItem != null)
            {
                buttonPlayPause.Icon = Properties.Resources.Pause;
                player.StopSong();
                player.LoadSong(playlist.SelectedItem.ToString());
                player.PlaySong();
                this.Text = playlist.SelectedItem.ToString().Substring(playlist.SelectedItem.ToString().LastIndexOf("\\") + 1, (playlist.SelectedItem.ToString().Length - (playlist.SelectedItem.ToString().LastIndexOf("\\") + 1)));            
            }   
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止播放\n";
            player.StopSong();
        }

        private void SetAlbumArt()
        {

            if (playlist.SelectedItem != null)
            {
                TagLib.File file = TagLib.File.Create(playlist.SelectedItem.ToString());
                if (file.Tag.Pictures.Length > 0)
                {
                    var bin = (byte[])(file.Tag.Pictures[0].Data.Data);
                    albumart.Image = Image.FromStream(new MemoryStream(bin)).GetThumbnailImage(100, 100, null, IntPtr.Zero);

                }
                else
                {
                    albumart.Image = Properties.Resources.gramophone;
                }
            }
            
        }
        private void GetSongLength()
        {
            if (playlist.SelectedItem != null)
            {
                TagLib.File f = TagLib.File.Create(playlist.SelectedItem.ToString());
                
                songLength = (int)f.Properties.Duration.TotalSeconds;
            }
            
        }

        private void SetTaskbarthumbnail()
        {
            TaskbarManager.Instance.TabbedThumbnail.SetThumbnailClip(this.Handle,new Rectangle(albumart.Location.X+4,albumart.Location.Y,albumart.Size.Width-1,albumart.Size.Height-4));
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            buttonPlayPause = new ThumbnailToolbarButton(Properties.Resources.play, "Play");
            buttonPlayPause.Enabled = true;
            buttonPlayPause.Click += new EventHandler<ThumbnailButtonClickedEventArgs>(buttonPlay_Click);

            buttonNext = new ThumbnailToolbarButton(Properties.Resources.nextArrow, "Next");
            buttonNext.Enabled = true;
            buttonNext.Click += new EventHandler<ThumbnailButtonClickedEventArgs>(buttonNext_Click);

            buttonPrevious = new ThumbnailToolbarButton(Properties.Resources.prevArrow, "Previous");
            buttonPrevious.Click += new EventHandler<ThumbnailButtonClickedEventArgs>(buttonPrevious_Click);
            TaskbarManager.Instance.ThumbnailToolbars.AddButtons(this.Handle, buttonPrevious, buttonPlayPause, buttonNext);
            TaskbarManager.Instance.TabbedThumbnail.SetThumbnailClip(this.Handle, new Rectangle(albumart.Location, albumart.Size));
        }

        void buttonPlay_Click(object sender, EventArgs e)
        {
            if (playState == 0)
            {
                player.PlaySong();
                playState = 1;
                buttonPlayPause.Icon = Properties.Resources.Pause;
                buttonPlayPause.Tooltip = "Pause";
                SetTimerforPlay();
            }
            else
            {
                player.PauseSong();
                playState = 0;
                buttonPlayPause.Icon = Properties.Resources.play;
                buttonPlayPause.Tooltip = "Play";
                SetTimerforPause();
            }
        }

        void buttonNext_Click(object sender, EventArgs e)
        {
            PlayNextSong();
        }

        void buttonPrevious_Click(object sender, EventArgs e)
        {
            PlayPreviousSong();
        }

        private void playlist_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void progressbarTimer_Tick(object sender, EventArgs e)
        {
            if (timerCount <= songLength)
            {
                tbManager.SetProgressValue(timerCount, songLength);
            }
            lblSeconds.Text = (songLength - timerCount).ToString() + " seconds";
            timerCount += 1;
        }

       

        
    }
}
