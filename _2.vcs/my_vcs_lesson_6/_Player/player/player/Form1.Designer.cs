namespace player
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.playlist = new System.Windows.Forms.ListBox();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lblSeconds = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.btnRemoveSong = new System.Windows.Forms.Button();
            this.albumart = new System.Windows.Forms.PictureBox();
            this.btnAddSong = new System.Windows.Forms.Button();
            this.btnPlay = new System.Windows.Forms.Button();
            this.btnStop = new System.Windows.Forms.Button();
            this.btnPause = new System.Windows.Forms.Button();
            this.btnNext = new System.Windows.Forms.Button();
            this.btnPrevious = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.progressbarTimer = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.albumart)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // playlist
            // 
            this.playlist.BackColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.playlist.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.playlist.ForeColor = System.Drawing.Color.Transparent;
            this.playlist.FormattingEnabled = true;
            this.playlist.Location = new System.Drawing.Point(6, 13);
            this.playlist.Name = "playlist";
            this.playlist.Size = new System.Drawing.Size(204, 208);
            this.playlist.TabIndex = 0;
            this.playlist.SelectedIndexChanged += new System.EventHandler(this.playlist_SelectedIndexChanged);
            this.playlist.DoubleClick += new System.EventHandler(this.playlist_DoubleClick);
            // 
            // openFileDialog
            // 
            this.openFileDialog.FileName = "openFileDialog";
            this.openFileDialog.Filter = "Songs|*.mp3";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lblSeconds);
            this.groupBox1.Controls.Add(this.pictureBox1);
            this.groupBox1.Controls.Add(this.btnRemoveSong);
            this.groupBox1.Controls.Add(this.albumart);
            this.groupBox1.Controls.Add(this.btnAddSong);
            this.groupBox1.Controls.Add(this.btnPlay);
            this.groupBox1.Controls.Add(this.btnStop);
            this.groupBox1.Controls.Add(this.btnPause);
            this.groupBox1.Controls.Add(this.btnNext);
            this.groupBox1.Controls.Add(this.btnPrevious);
            this.groupBox1.Location = new System.Drawing.Point(4, -3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(216, 160);
            this.groupBox1.TabIndex = 8;
            this.groupBox1.TabStop = false;
            // 
            // lblSeconds
            // 
            this.lblSeconds.AutoSize = true;
            this.lblSeconds.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblSeconds.ForeColor = System.Drawing.Color.Teal;
            this.lblSeconds.Location = new System.Drawing.Point(138, 143);
            this.lblSeconds.Name = "lblSeconds";
            this.lblSeconds.Size = new System.Drawing.Size(0, 13);
            this.lblSeconds.TabIndex = 9;
            this.lblSeconds.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::player.Properties.Resources.treble_staff_with_notes_01;
            this.pictureBox1.Location = new System.Drawing.Point(119, 105);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(91, 50);
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // btnRemoveSong
            // 
            this.btnRemoveSong.Image = global::player.Properties.Resources.edit_remove;
            this.btnRemoveSong.Location = new System.Drawing.Point(170, 58);
            this.btnRemoveSong.Name = "btnRemoveSong";
            this.btnRemoveSong.Size = new System.Drawing.Size(40, 40);
            this.btnRemoveSong.TabIndex = 6;
            this.btnRemoveSong.UseVisualStyleBackColor = true;
            this.btnRemoveSong.Click += new System.EventHandler(this.btnRemoveSong_Click);
            // 
            // albumart
            // 
            this.albumart.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.albumart.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.albumart.Image = global::player.Properties.Resources.gramophone;
            this.albumart.Location = new System.Drawing.Point(8, 55);
            this.albumart.Name = "albumart";
            this.albumart.Size = new System.Drawing.Size(100, 100);
            this.albumart.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.albumart.TabIndex = 7;
            this.albumart.TabStop = false;
            // 
            // btnAddSong
            // 
            this.btnAddSong.Image = global::player.Properties.Resources.edit_add;
            this.btnAddSong.Location = new System.Drawing.Point(119, 58);
            this.btnAddSong.Name = "btnAddSong";
            this.btnAddSong.Size = new System.Drawing.Size(40, 40);
            this.btnAddSong.TabIndex = 5;
            this.btnAddSong.UseVisualStyleBackColor = true;
            this.btnAddSong.Click += new System.EventHandler(this.btnAddSong_Click);
            // 
            // btnPlay
            // 
            this.btnPlay.Image = global::player.Properties.Resources.player_play;
            this.btnPlay.Location = new System.Drawing.Point(6, 12);
            this.btnPlay.Name = "btnPlay";
            this.btnPlay.Size = new System.Drawing.Size(40, 40);
            this.btnPlay.TabIndex = 1;
            this.btnPlay.UseVisualStyleBackColor = true;
            this.btnPlay.Click += new System.EventHandler(this.btnPlay_Click);
            // 
            // btnStop
            // 
            this.btnStop.Image = global::player.Properties.Resources.player_stop;
            this.btnStop.Location = new System.Drawing.Point(170, 12);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(40, 40);
            this.btnStop.TabIndex = 7;
            this.btnStop.UseVisualStyleBackColor = true;
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
            // 
            // btnPause
            // 
            this.btnPause.Image = global::player.Properties.Resources.player_pause1;
            this.btnPause.Location = new System.Drawing.Point(47, 12);
            this.btnPause.Name = "btnPause";
            this.btnPause.Size = new System.Drawing.Size(40, 40);
            this.btnPause.TabIndex = 2;
            this.btnPause.UseVisualStyleBackColor = true;
            this.btnPause.Click += new System.EventHandler(this.btnPause_Click);
            // 
            // btnNext
            // 
            this.btnNext.Image = global::player.Properties.Resources.player_end;
            this.btnNext.Location = new System.Drawing.Point(129, 12);
            this.btnNext.Name = "btnNext";
            this.btnNext.Size = new System.Drawing.Size(40, 40);
            this.btnNext.TabIndex = 3;
            this.btnNext.UseVisualStyleBackColor = true;
            this.btnNext.Click += new System.EventHandler(this.btnNext_Click);
            // 
            // btnPrevious
            // 
            this.btnPrevious.Image = global::player.Properties.Resources.player_start;
            this.btnPrevious.Location = new System.Drawing.Point(88, 12);
            this.btnPrevious.Name = "btnPrevious";
            this.btnPrevious.Size = new System.Drawing.Size(40, 40);
            this.btnPrevious.TabIndex = 4;
            this.btnPrevious.UseVisualStyleBackColor = true;
            this.btnPrevious.Click += new System.EventHandler(this.btnPrevious_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.playlist);
            this.groupBox2.Location = new System.Drawing.Point(4, 155);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(216, 228);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            // 
            // progressbarTimer
            // 
            this.progressbarTimer.Interval = 1000;
            this.progressbarTimer.Tick += new System.EventHandler(this.progressbarTimer_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(226, 9);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(593, 374);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(831, 406);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.Text = "MP3 Player";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Shown += new System.EventHandler(this.Form1_Shown);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.albumart)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox playlist;
        private System.Windows.Forms.Button btnPlay;
        private System.Windows.Forms.Button btnPause;
        private System.Windows.Forms.Button btnNext;
        private System.Windows.Forms.Button btnPrevious;
        private System.Windows.Forms.Button btnAddSong;
        private System.Windows.Forms.Button btnRemoveSong;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.Windows.Forms.Button btnStop;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.PictureBox albumart;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer progressbarTimer;
        private System.Windows.Forms.Label lblSeconds;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

