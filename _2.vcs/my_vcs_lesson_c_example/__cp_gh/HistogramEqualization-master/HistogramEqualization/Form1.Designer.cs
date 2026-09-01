namespace HistogramEqualization
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
      this.BottomToolStripPanel = new System.Windows.Forms.ToolStripPanel();
      this.TopToolStripPanel = new System.Windows.Forms.ToolStripPanel();
      this.RightToolStripPanel = new System.Windows.Forms.ToolStripPanel();
      this.LeftToolStripPanel = new System.Windows.Forms.ToolStripPanel();
      this.ContentPanel = new System.Windows.Forms.ToolStripContentPanel();
      this.menuStrip1 = new System.Windows.Forms.MenuStrip();
      this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.stretchToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.linear0255ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.linearToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.linear2ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.equalizationToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
      this.splitContainer1 = new System.Windows.Forms.SplitContainer();
      this.panel2 = new System.Windows.Forms.Panel();
      this.histogramPanel2 = new CustomControls.HistogramPanel();
      this.panel1 = new System.Windows.Forms.Panel();
      this.histogramPanel1 = new CustomControls.HistogramPanel();
      this.pictureBox1 = new System.Windows.Forms.PictureBox();
      this.panel3 = new System.Windows.Forms.Panel();
      this.menuStrip1.SuspendLayout();
      this.splitContainer1.Panel1.SuspendLayout();
      this.splitContainer1.Panel2.SuspendLayout();
      this.splitContainer1.SuspendLayout();
      this.panel2.SuspendLayout();
      this.panel1.SuspendLayout();
      ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
      this.SuspendLayout();
      // 
      // BottomToolStripPanel
      // 
      this.BottomToolStripPanel.Location = new System.Drawing.Point(0, 0);
      this.BottomToolStripPanel.Name = "BottomToolStripPanel";
      this.BottomToolStripPanel.Orientation = System.Windows.Forms.Orientation.Horizontal;
      this.BottomToolStripPanel.RowMargin = new System.Windows.Forms.Padding(3, 0, 0, 0);
      this.BottomToolStripPanel.Size = new System.Drawing.Size(0, 0);
      // 
      // TopToolStripPanel
      // 
      this.TopToolStripPanel.Location = new System.Drawing.Point(0, 0);
      this.TopToolStripPanel.Name = "TopToolStripPanel";
      this.TopToolStripPanel.Orientation = System.Windows.Forms.Orientation.Horizontal;
      this.TopToolStripPanel.RowMargin = new System.Windows.Forms.Padding(3, 0, 0, 0);
      this.TopToolStripPanel.Size = new System.Drawing.Size(0, 0);
      // 
      // RightToolStripPanel
      // 
      this.RightToolStripPanel.Location = new System.Drawing.Point(0, 0);
      this.RightToolStripPanel.Name = "RightToolStripPanel";
      this.RightToolStripPanel.Orientation = System.Windows.Forms.Orientation.Horizontal;
      this.RightToolStripPanel.RowMargin = new System.Windows.Forms.Padding(3, 0, 0, 0);
      this.RightToolStripPanel.Size = new System.Drawing.Size(0, 0);
      // 
      // LeftToolStripPanel
      // 
      this.LeftToolStripPanel.Location = new System.Drawing.Point(0, 0);
      this.LeftToolStripPanel.Name = "LeftToolStripPanel";
      this.LeftToolStripPanel.Orientation = System.Windows.Forms.Orientation.Horizontal;
      this.LeftToolStripPanel.RowMargin = new System.Windows.Forms.Padding(3, 0, 0, 0);
      this.LeftToolStripPanel.Size = new System.Drawing.Size(0, 0);
      // 
      // ContentPanel
      // 
      this.ContentPanel.AutoScroll = true;
      this.ContentPanel.Size = new System.Drawing.Size(872, 530);
      // 
      // menuStrip1
      // 
      this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.stretchToolStripMenuItem});
      this.menuStrip1.Location = new System.Drawing.Point(0, 0);
      this.menuStrip1.Name = "menuStrip1";
      this.menuStrip1.Size = new System.Drawing.Size(1010, 24);
      this.menuStrip1.TabIndex = 0;
      this.menuStrip1.Text = "menuStrip1";
      // 
      // fileToolStripMenuItem
      // 
      this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openToolStripMenuItem});
      this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
      this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
      this.fileToolStripMenuItem.Text = "File";
      // 
      // openToolStripMenuItem
      // 
      this.openToolStripMenuItem.Name = "openToolStripMenuItem";
      this.openToolStripMenuItem.Size = new System.Drawing.Size(103, 22);
      this.openToolStripMenuItem.Text = "Open";
      this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click_1);
      // 
      // stretchToolStripMenuItem
      // 
      this.stretchToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.linear0255ToolStripMenuItem,
            this.linearToolStripMenuItem,
            this.linear2ToolStripMenuItem,
            this.equalizationToolStripMenuItem});
      this.stretchToolStripMenuItem.Name = "stretchToolStripMenuItem";
      this.stretchToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
      this.stretchToolStripMenuItem.Text = "Stretch";
      // 
      // linear0255ToolStripMenuItem
      // 
      this.linear0255ToolStripMenuItem.Name = "linear0255ToolStripMenuItem";
      this.linear0255ToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
      this.linear0255ToolStripMenuItem.Text = "Linear 0-255";
      this.linear0255ToolStripMenuItem.Click += new System.EventHandler(this.linear0255ToolStripMenuItem_Click);
      // 
      // linearToolStripMenuItem
      // 
      this.linearToolStripMenuItem.Name = "linearToolStripMenuItem";
      this.linearToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
      this.linearToolStripMenuItem.Text = "Linear";
      this.linearToolStripMenuItem.Click += new System.EventHandler(this.linearToolStripMenuItem_Click);
      // 
      // linear2ToolStripMenuItem
      // 
      this.linear2ToolStripMenuItem.Name = "linear2ToolStripMenuItem";
      this.linear2ToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
      this.linear2ToolStripMenuItem.Text = "Linear 2%";
      this.linear2ToolStripMenuItem.Click += new System.EventHandler(this.linear2ToolStripMenuItem_Click);
      // 
      // equalizationToolStripMenuItem
      // 
      this.equalizationToolStripMenuItem.Name = "equalizationToolStripMenuItem";
      this.equalizationToolStripMenuItem.Size = new System.Drawing.Size(138, 22);
      this.equalizationToolStripMenuItem.Text = "Equalization";
      this.equalizationToolStripMenuItem.Click += new System.EventHandler(this.equalizationToolStripMenuItem_Click);
      // 
      // splitContainer1
      // 
      this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
      this.splitContainer1.Location = new System.Drawing.Point(0, 72);
      this.splitContainer1.Name = "splitContainer1";
      this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
      // 
      // splitContainer1.Panel1
      // 
      this.splitContainer1.Panel1.Controls.Add(this.panel2);
      this.splitContainer1.Panel1.Controls.Add(this.panel1);
      // 
      // splitContainer1.Panel2
      // 
      this.splitContainer1.Panel2.Controls.Add(this.pictureBox1);
      this.splitContainer1.Size = new System.Drawing.Size(1010, 757);
      this.splitContainer1.SplitterDistance = 265;
      this.splitContainer1.TabIndex = 1;
      // 
      // panel2
      // 
      this.panel2.Controls.Add(this.histogramPanel2);
      this.panel2.Dock = System.Windows.Forms.DockStyle.Fill;
      this.panel2.Location = new System.Drawing.Point(501, 0);
      this.panel2.Name = "panel2";
      this.panel2.Padding = new System.Windows.Forms.Padding(2, 4, 4, 4);
      this.panel2.Size = new System.Drawing.Size(509, 265);
      this.panel2.TabIndex = 2;
      // 
      // histogramPanel2
      // 
      this.histogramPanel2.Dock = System.Windows.Forms.DockStyle.Fill;
      this.histogramPanel2.Location = new System.Drawing.Point(2, 4);
      this.histogramPanel2.Name = "histogramPanel2";
      this.histogramPanel2.Size = new System.Drawing.Size(503, 257);
      this.histogramPanel2.TabIndex = 0;
      this.histogramPanel2.Title = "Output Histogram";
      // 
      // panel1
      // 
      this.panel1.Controls.Add(this.histogramPanel1);
      this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
      this.panel1.Location = new System.Drawing.Point(0, 0);
      this.panel1.Name = "panel1";
      this.panel1.Padding = new System.Windows.Forms.Padding(4, 4, 2, 4);
      this.panel1.Size = new System.Drawing.Size(501, 265);
      this.panel1.TabIndex = 1;
      // 
      // histogramPanel1
      // 
      this.histogramPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
      this.histogramPanel1.Location = new System.Drawing.Point(4, 4);
      this.histogramPanel1.Name = "histogramPanel1";
      this.histogramPanel1.Size = new System.Drawing.Size(495, 257);
      this.histogramPanel1.TabIndex = 0;
      this.histogramPanel1.Title = "Input Histogram";
      // 
      // pictureBox1
      // 
      this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
      this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Fill;
      this.pictureBox1.Location = new System.Drawing.Point(0, 0);
      this.pictureBox1.Name = "pictureBox1";
      this.pictureBox1.Size = new System.Drawing.Size(1010, 488);
      this.pictureBox1.TabIndex = 0;
      this.pictureBox1.TabStop = false;
      // 
      // panel3
      // 
      this.panel3.Dock = System.Windows.Forms.DockStyle.Top;
      this.panel3.Location = new System.Drawing.Point(0, 24);
      this.panel3.Name = "panel3";
      this.panel3.Size = new System.Drawing.Size(1010, 48);
      this.panel3.TabIndex = 2;
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(1010, 829);
      this.Controls.Add(this.splitContainer1);
      this.Controls.Add(this.panel3);
      this.Controls.Add(this.menuStrip1);
      this.Name = "Form1";
      this.Text = "Form1";
      this.SizeChanged += new System.EventHandler(this.Form1_SizeChanged);
      this.menuStrip1.ResumeLayout(false);
      this.menuStrip1.PerformLayout();
      this.splitContainer1.Panel1.ResumeLayout(false);
      this.splitContainer1.Panel2.ResumeLayout(false);
      this.splitContainer1.ResumeLayout(false);
      this.panel2.ResumeLayout(false);
      this.panel1.ResumeLayout(false);
      ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.ToolStripPanel BottomToolStripPanel;
    private System.Windows.Forms.ToolStripPanel TopToolStripPanel;
    private System.Windows.Forms.ToolStripPanel RightToolStripPanel;
    private System.Windows.Forms.ToolStripPanel LeftToolStripPanel;
    private System.Windows.Forms.ToolStripContentPanel ContentPanel;
    private System.Windows.Forms.MenuStrip menuStrip1;
    private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
    private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
    private System.Windows.Forms.SplitContainer splitContainer1;
    private System.Windows.Forms.PictureBox pictureBox1;
    private System.Windows.Forms.Panel panel2;
    private CustomControls.HistogramPanel histogramPanel2;
    private System.Windows.Forms.Panel panel1;
    private CustomControls.HistogramPanel histogramPanel1;
    private System.Windows.Forms.Panel panel3;
    private System.Windows.Forms.ToolStripMenuItem stretchToolStripMenuItem;
    private System.Windows.Forms.ToolStripMenuItem linear0255ToolStripMenuItem;
    private System.Windows.Forms.ToolStripMenuItem linearToolStripMenuItem;
    private System.Windows.Forms.ToolStripMenuItem linear2ToolStripMenuItem;
    private System.Windows.Forms.ToolStripMenuItem equalizationToolStripMenuItem;


  }
}

