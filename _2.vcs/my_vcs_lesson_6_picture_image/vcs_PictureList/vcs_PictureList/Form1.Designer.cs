namespace vcs_PictureList
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.mnuMoveLeft = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuMoveRight = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuDeletePicture = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuInsertPicture = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.panel1.AutoScroll = true;
            this.panel1.BackColor = System.Drawing.Color.White;
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel1.ContextMenuStrip = this.contextMenuStrip1;
            this.panel1.Location = new System.Drawing.Point(12, 11);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(832, 443);
            this.panel1.TabIndex = 1;
            this.panel1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.panel1_MouseDown);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuMoveLeft,
            this.mnuMoveRight,
            this.mnuDeletePicture,
            this.mnuInsertPicture});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(162, 114);
            // 
            // mnuMoveLeft
            // 
            this.mnuMoveLeft.Name = "mnuMoveLeft";
            this.mnuMoveLeft.Size = new System.Drawing.Size(161, 22);
            this.mnuMoveLeft.Text = "Move &Left";
            this.mnuMoveLeft.Click += new System.EventHandler(this.mnuMoveLeft_Click);
            // 
            // mnuMoveRight
            // 
            this.mnuMoveRight.Name = "mnuMoveRight";
            this.mnuMoveRight.Size = new System.Drawing.Size(161, 22);
            this.mnuMoveRight.Text = "Move &Right";
            this.mnuMoveRight.Click += new System.EventHandler(this.mnuMoveRight_Click);
            // 
            // mnuDeletePicture
            // 
            this.mnuDeletePicture.Name = "mnuDeletePicture";
            this.mnuDeletePicture.Size = new System.Drawing.Size(161, 22);
            this.mnuDeletePicture.Text = "&Delete Picture...";
            this.mnuDeletePicture.Click += new System.EventHandler(this.mnuDeletePicture_Click);
            // 
            // mnuInsertPicture
            // 
            this.mnuInsertPicture.Name = "mnuInsertPicture";
            this.mnuInsertPicture.Size = new System.Drawing.Size(161, 22);
            this.mnuInsertPicture.Text = "&Insert Picture...";
            this.mnuInsertPicture.Click += new System.EventHandler(this.mnuInsertPicture_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.DefaultExt = "png";
            this.openFileDialog1.Filter = "Image files|*.bmp;*.jpg;*.gif;*.png;*.tif|All FIles|*.*";
            this.openFileDialog1.Multiselect = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(850, 11);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(251, 442);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1113, 465);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.panel1);
            this.Name = "Form1";
            this.Text = "vcs_PictureList";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuMoveLeft;
        private System.Windows.Forms.ToolStripMenuItem mnuMoveRight;
        private System.Windows.Forms.ToolStripMenuItem mnuDeletePicture;
        private System.Windows.Forms.ToolStripMenuItem mnuInsertPicture;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

