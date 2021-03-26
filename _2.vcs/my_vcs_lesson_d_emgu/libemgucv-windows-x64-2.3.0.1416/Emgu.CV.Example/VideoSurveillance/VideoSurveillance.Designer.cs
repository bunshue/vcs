namespace VideoSurveillance
{
   partial class VideoSurveillance
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
          this.splitContainer1 = new System.Windows.Forms.SplitContainer();
          this.imageBox1 = new Emgu.CV.UI.ImageBox();
          this.panel1 = new System.Windows.Forms.Panel();
          this.label1 = new System.Windows.Forms.Label();
          this.imageBox2 = new Emgu.CV.UI.ImageBox();
          this.panel2 = new System.Windows.Forms.Panel();
          this.label2 = new System.Windows.Forms.Label();
          this.splitContainer1.Panel1.SuspendLayout();
          this.splitContainer1.Panel2.SuspendLayout();
          this.splitContainer1.SuspendLayout();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).BeginInit();
          this.panel1.SuspendLayout();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox2)).BeginInit();
          this.panel2.SuspendLayout();
          this.SuspendLayout();
          // 
          // splitContainer1
          // 
          this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
          this.splitContainer1.Location = new System.Drawing.Point(0, 0);
          this.splitContainer1.Name = "splitContainer1";
          // 
          // splitContainer1.Panel1
          // 
          this.splitContainer1.Panel1.Controls.Add(this.imageBox1);
          this.splitContainer1.Panel1.Controls.Add(this.panel1);
          // 
          // splitContainer1.Panel2
          // 
          this.splitContainer1.Panel2.Controls.Add(this.imageBox2);
          this.splitContainer1.Panel2.Controls.Add(this.panel2);
          this.splitContainer1.Size = new System.Drawing.Size(1392, 584);
          this.splitContainer1.SplitterDistance = 685;
          this.splitContainer1.TabIndex = 0;
          // 
          // imageBox1
          // 
          this.imageBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
          this.imageBox1.Location = new System.Drawing.Point(0, 44);
          this.imageBox1.Name = "imageBox1";
          this.imageBox1.Size = new System.Drawing.Size(640, 480);
          this.imageBox1.TabIndex = 2;
          this.imageBox1.TabStop = false;
          // 
          // panel1
          // 
          this.panel1.Controls.Add(this.label1);
          this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
          this.panel1.Location = new System.Drawing.Point(0, 0);
          this.panel1.Name = "panel1";
          this.panel1.Size = new System.Drawing.Size(685, 44);
          this.panel1.TabIndex = 0;
          // 
          // label1
          // 
          this.label1.AutoSize = true;
          this.label1.Location = new System.Drawing.Point(12, 12);
          this.label1.Name = "label1";
          this.label1.Size = new System.Drawing.Size(73, 12);
          this.label1.TabIndex = 0;
          this.label1.Text = "Camera Frame";
          // 
          // imageBox2
          // 
          this.imageBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
          this.imageBox2.Location = new System.Drawing.Point(0, 44);
          this.imageBox2.Name = "imageBox2";
          this.imageBox2.Size = new System.Drawing.Size(640, 480);
          this.imageBox2.TabIndex = 2;
          this.imageBox2.TabStop = false;
          // 
          // panel2
          // 
          this.panel2.Controls.Add(this.label2);
          this.panel2.Dock = System.Windows.Forms.DockStyle.Top;
          this.panel2.Location = new System.Drawing.Point(0, 0);
          this.panel2.Name = "panel2";
          this.panel2.Size = new System.Drawing.Size(703, 44);
          this.panel2.TabIndex = 0;
          // 
          // label2
          // 
          this.label2.AutoSize = true;
          this.label2.Location = new System.Drawing.Point(15, 12);
          this.label2.Name = "label2";
          this.label2.Size = new System.Drawing.Size(83, 12);
          this.label2.TabIndex = 0;
          this.label2.Text = "Forground Mask";
          // 
          // VideoSurveillance
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(1392, 584);
          this.Controls.Add(this.splitContainer1);
          this.Name = "VideoSurveillance";
          this.Text = "VideoSurveillance";
          this.splitContainer1.Panel1.ResumeLayout(false);
          this.splitContainer1.Panel2.ResumeLayout(false);
          this.splitContainer1.ResumeLayout(false);
          ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).EndInit();
          this.panel1.ResumeLayout(false);
          this.panel1.PerformLayout();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox2)).EndInit();
          this.panel2.ResumeLayout(false);
          this.panel2.PerformLayout();
          this.ResumeLayout(false);

      }

      #endregion

      private System.Windows.Forms.SplitContainer splitContainer1;
      private System.Windows.Forms.Panel panel1;
      private System.Windows.Forms.Panel panel2;
      private Emgu.CV.UI.ImageBox imageBox1;
      private System.Windows.Forms.Label label1;
      private Emgu.CV.UI.ImageBox imageBox2;
      private System.Windows.Forms.Label label2;
   }
}