namespace Snapshot_Maker
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose( bool disposing )
        {
            if ( disposing && ( components != null ) )
            {
                components.Dispose( );
            }
            base.Dispose( disposing );
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent( )
        {
            this.components = new System.ComponentModel.Container();
            this.label1 = new System.Windows.Forms.Label();
            this.devicesCombo = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.videoResolutionsCombo = new System.Windows.Forms.ComboBox();
            this.snapshotResolutionsCombo = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.connectButton = new System.Windows.Forms.Button();
            this.disconnectButton = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.videoSourcePlayer = new AForge.Controls.VideoSourcePlayer();
            this.toolTip = new System.Windows.Forms.ToolTip(this.components);
            this.triggerButton = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(10, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(73, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Video devices:";
            // 
            // devicesCombo
            // 
            this.devicesCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.devicesCombo.FormattingEnabled = true;
            this.devicesCombo.Location = new System.Drawing.Point(95, 14);
            this.devicesCombo.Name = "devicesCombo";
            this.devicesCombo.Size = new System.Drawing.Size(411, 20);
            this.devicesCombo.TabIndex = 1;
            this.devicesCombo.SelectedIndexChanged += new System.EventHandler(this.devicesCombo_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(10, 44);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(82, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Video resoluton:";
            // 
            // videoResolutionsCombo
            // 
            this.videoResolutionsCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.videoResolutionsCombo.FormattingEnabled = true;
            this.videoResolutionsCombo.Location = new System.Drawing.Point(95, 42);
            this.videoResolutionsCombo.Name = "videoResolutionsCombo";
            this.videoResolutionsCombo.Size = new System.Drawing.Size(100, 20);
            this.videoResolutionsCombo.TabIndex = 3;
            // 
            // snapshotResolutionsCombo
            // 
            this.snapshotResolutionsCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.snapshotResolutionsCombo.FormattingEnabled = true;
            this.snapshotResolutionsCombo.Location = new System.Drawing.Point(310, 42);
            this.snapshotResolutionsCombo.Name = "snapshotResolutionsCombo";
            this.snapshotResolutionsCombo.Size = new System.Drawing.Size(196, 20);
            this.snapshotResolutionsCombo.TabIndex = 4;
            this.toolTip.SetToolTip(this.snapshotResolutionsCombo, "Press shutter button on your camera to make snapshot");
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(205, 44);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(96, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "Snapshot resoluton:";
            this.toolTip.SetToolTip(this.label3, "Press shutter button on your camera to make snapshot");
            // 
            // connectButton
            // 
            this.connectButton.Location = new System.Drawing.Point(756, 6);
            this.connectButton.Name = "connectButton";
            this.connectButton.Size = new System.Drawing.Size(75, 21);
            this.connectButton.TabIndex = 6;
            this.connectButton.Text = "&Connect";
            this.connectButton.UseVisualStyleBackColor = true;
            this.connectButton.Click += new System.EventHandler(this.connectButton_Click);
            // 
            // disconnectButton
            // 
            this.disconnectButton.Location = new System.Drawing.Point(756, 34);
            this.disconnectButton.Name = "disconnectButton";
            this.disconnectButton.Size = new System.Drawing.Size(75, 21);
            this.disconnectButton.TabIndex = 7;
            this.disconnectButton.Text = "&Disconnect";
            this.disconnectButton.UseVisualStyleBackColor = true;
            this.disconnectButton.Click += new System.EventHandler(this.disconnectButton_Click);
            // 
            // panel1
            // 
            this.panel1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.panel1.Controls.Add(this.videoSourcePlayer);
            this.panel1.Location = new System.Drawing.Point(0, 97);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(853, 504);
            this.panel1.TabIndex = 8;
            // 
            // videoSourcePlayer
            // 
            this.videoSourcePlayer.AutoSizeControl = true;
            this.videoSourcePlayer.BackColor = System.Drawing.SystemColors.ControlDark;
            this.videoSourcePlayer.ForeColor = System.Drawing.Color.DarkRed;
            this.videoSourcePlayer.Location = new System.Drawing.Point(265, 131);
            this.videoSourcePlayer.Name = "videoSourcePlayer";
            this.videoSourcePlayer.Size = new System.Drawing.Size(322, 242);
            this.videoSourcePlayer.TabIndex = 0;
            this.videoSourcePlayer.VideoSource = null;
            // 
            // toolTip
            // 
            this.toolTip.AutoPopDelay = 5000;
            this.toolTip.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.toolTip.InitialDelay = 100;
            this.toolTip.ReshowDelay = 100;
            // 
            // triggerButton
            // 
            this.triggerButton.Location = new System.Drawing.Point(756, 61);
            this.triggerButton.Name = "triggerButton";
            this.triggerButton.Size = new System.Drawing.Size(75, 21);
            this.triggerButton.TabIndex = 9;
            this.triggerButton.Text = "&Trigger";
            this.triggerButton.UseVisualStyleBackColor = true;
            this.triggerButton.Click += new System.EventHandler(this.triggerButton_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(852, 599);
            this.Controls.Add(this.triggerButton);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.disconnectButton);
            this.Controls.Add(this.connectButton);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.snapshotResolutionsCombo);
            this.Controls.Add(this.videoResolutionsCombo);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.devicesCombo);
            this.Controls.Add(this.label1);
            this.MinimumSize = new System.Drawing.Size(535, 409);
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Snapshot Maker";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox devicesCombo;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox videoResolutionsCombo;
        private System.Windows.Forms.ComboBox snapshotResolutionsCombo;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button connectButton;
        private System.Windows.Forms.Button disconnectButton;
        private System.Windows.Forms.Panel panel1;
        private AForge.Controls.VideoSourcePlayer videoSourcePlayer;
        private System.Windows.Forms.ToolTip toolTip;
        private System.Windows.Forms.Button triggerButton;
    }
}

