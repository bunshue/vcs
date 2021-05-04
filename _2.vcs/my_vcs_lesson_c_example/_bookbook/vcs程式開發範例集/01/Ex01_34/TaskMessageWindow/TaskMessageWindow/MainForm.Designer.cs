namespace TaskMessageWindow
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
        protected override void Dispose(bool disposing)
        {
            if(disposing && (components != null))
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.Counter = new System.Windows.Forms.Timer(this.components);
            this.titleInform = new System.Windows.Forms.Label();
            this.contentInform = new System.Windows.Forms.Label();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.taskBarIcon = new System.Windows.Forms.NotifyIcon(this.components);
            this.iconCounter = new System.Windows.Forms.Timer(this.components);
            this.displayCounter = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // titleInform
            // 
            this.titleInform.AutoSize = true;
            this.titleInform.BackColor = System.Drawing.Color.White;
            this.titleInform.Location = new System.Drawing.Point(89, 54);
            this.titleInform.Name = "titleInform";
            this.titleInform.Size = new System.Drawing.Size(33, 12);
            this.titleInform.TabIndex = 0;
            this.titleInform.Text = "label1";
            // 
            // contentInform
            // 
            this.contentInform.AutoSize = true;
            this.contentInform.BackColor = System.Drawing.Color.White;
            this.contentInform.Location = new System.Drawing.Point(141, 81);
            this.contentInform.Name = "contentInform";
            this.contentInform.Size = new System.Drawing.Size(33, 12);
            this.contentInform.TabIndex = 1;
            this.contentInform.Text = "label2";
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "Close2.bmp");
            this.imageList1.Images.SetKeyName(1, "Close1.bmp");
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::TaskMessageWindow.Properties.Resources.Close2;
            this.pictureBox1.Location = new System.Drawing.Point(242, 6);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(17, 17);
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseLeave += new System.EventHandler(this.pictureBox1_MouseLeave);
            this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click);
            this.pictureBox1.MouseEnter += new System.EventHandler(this.pictureBox1_MouseEnter);
            // 
            // taskBarIcon
            // 
            this.taskBarIcon.Text = "任务栏通知窗口";
            this.taskBarIcon.Visible = true;
            this.taskBarIcon.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.taskBarIcon_MouseDoubleClick);
            // 
            // iconCounter
            // 
            this.iconCounter.Interval = 400;
            this.iconCounter.Tick += new System.EventHandler(this.iconCounter_Tick);
            // 
            // displayCounter
            // 
            this.displayCounter.Interval = 1000;
            this.displayCounter.Tick += new System.EventHandler(this.displayCounter_Tick);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::TaskMessageWindow.Properties.Resources.提醒;
            this.ClientSize = new System.Drawing.Size(268, 161);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.contentInform);
            this.Controls.Add(this.titleInform);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "MainForm";
            this.ShowInTaskbar = false;
            this.Text = "MainForm";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.MouseEnter += new System.EventHandler(this.MainForm_MouseEnter);
            this.MouseLeave += new System.EventHandler(this.MainForm_MouseLeave);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer Counter;
        private System.Windows.Forms.Label titleInform;
        private System.Windows.Forms.Label contentInform;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.NotifyIcon taskBarIcon;
        private System.Windows.Forms.Timer iconCounter;
        private System.Windows.Forms.Timer displayCounter;
    }
}