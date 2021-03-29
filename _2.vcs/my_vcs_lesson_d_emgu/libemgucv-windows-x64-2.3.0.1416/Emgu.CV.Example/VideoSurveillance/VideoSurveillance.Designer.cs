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
          this.imageBox1 = new Emgu.CV.UI.ImageBox();
          this.label1 = new System.Windows.Forms.Label();
          this.imageBox2 = new Emgu.CV.UI.ImageBox();
          this.label2 = new System.Windows.Forms.Label();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).BeginInit();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox2)).BeginInit();
          this.SuspendLayout();
          // 
          // imageBox1
          // 
          this.imageBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
          this.imageBox1.Location = new System.Drawing.Point(12, 62);
          this.imageBox1.Name = "imageBox1";
          this.imageBox1.Size = new System.Drawing.Size(640, 480);
          this.imageBox1.TabIndex = 2;
          this.imageBox1.TabStop = false;
          // 
          // label1
          // 
          this.label1.AutoSize = true;
          this.label1.Location = new System.Drawing.Point(12, 30);
          this.label1.Name = "label1";
          this.label1.Size = new System.Drawing.Size(73, 12);
          this.label1.TabIndex = 0;
          this.label1.Text = "Camera Frame";
          // 
          // imageBox2
          // 
          this.imageBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
          this.imageBox2.Location = new System.Drawing.Point(675, 62);
          this.imageBox2.Name = "imageBox2";
          this.imageBox2.Size = new System.Drawing.Size(640, 480);
          this.imageBox2.TabIndex = 2;
          this.imageBox2.TabStop = false;
          // 
          // label2
          // 
          this.label2.AutoSize = true;
          this.label2.Location = new System.Drawing.Point(673, 30);
          this.label2.Name = "label2";
          this.label2.Size = new System.Drawing.Size(83, 12);
          this.label2.TabIndex = 0;
          this.label2.Text = "Forground Mask";
          // 
          // VideoSurveillance
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(1327, 556);
          this.Controls.Add(this.label2);
          this.Controls.Add(this.label1);
          this.Controls.Add(this.imageBox2);
          this.Controls.Add(this.imageBox1);
          this.Name = "VideoSurveillance";
          this.Text = "VideoSurveillance";
          ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).EndInit();
          ((System.ComponentModel.ISupportInitialize)(this.imageBox2)).EndInit();
          this.ResumeLayout(false);
          this.PerformLayout();

      }

      #endregion

      private Emgu.CV.UI.ImageBox imageBox1;
      private System.Windows.Forms.Label label1;
      private Emgu.CV.UI.ImageBox imageBox2;
      private System.Windows.Forms.Label label2;
   }
}