namespace ShapeDetection
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
            this.fileNameTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.loadImageButton = new System.Windows.Forms.Button();
            this.originalImageBox = new Emgu.CV.UI.ImageBox();
            this.label1 = new System.Windows.Forms.Label();
            this.circleImageBox = new Emgu.CV.UI.ImageBox();
            this.label3 = new System.Windows.Forms.Label();
            this.triangleRectangleImageBox = new Emgu.CV.UI.ImageBox();
            this.label2 = new System.Windows.Forms.Label();
            this.lineImageBox = new Emgu.CV.UI.ImageBox();
            this.label4 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.imageBox1 = new Emgu.CV.UI.ImageBox();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.originalImageBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.circleImageBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.triangleRectangleImageBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.lineImageBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // fileNameTextBox
            // 
            this.fileNameTextBox.Location = new System.Drawing.Point(53, 12);
            this.fileNameTextBox.Name = "fileNameTextBox";
            this.fileNameTextBox.ReadOnly = true;
            this.fileNameTextBox.Size = new System.Drawing.Size(215, 22);
            this.fileNameTextBox.TabIndex = 2;
            this.fileNameTextBox.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 16);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(35, 12);
            this.label5.TabIndex = 1;
            this.label5.Text = "檔案 :";
            // 
            // loadImageButton
            // 
            this.loadImageButton.Location = new System.Drawing.Point(274, 11);
            this.loadImageButton.Name = "loadImageButton";
            this.loadImageButton.Size = new System.Drawing.Size(30, 21);
            this.loadImageButton.TabIndex = 0;
            this.loadImageButton.Text = "...";
            this.loadImageButton.UseVisualStyleBackColor = true;
            this.loadImageButton.Click += new System.EventHandler(this.loadImageButton_Click);
            // 
            // originalImageBox
            // 
            this.originalImageBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.originalImageBox.Cursor = System.Windows.Forms.Cursors.Cross;
            this.originalImageBox.Location = new System.Drawing.Point(0, 78);
            this.originalImageBox.Name = "originalImageBox";
            this.originalImageBox.Size = new System.Drawing.Size(487, 386);
            this.originalImageBox.TabIndex = 3;
            this.originalImageBox.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 54);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "原始影像";
            // 
            // circleImageBox
            // 
            this.circleImageBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.circleImageBox.Cursor = System.Windows.Forms.Cursors.Cross;
            this.circleImageBox.Location = new System.Drawing.Point(0, 485);
            this.circleImageBox.Name = "circleImageBox";
            this.circleImageBox.Size = new System.Drawing.Size(487, 363);
            this.circleImageBox.TabIndex = 4;
            this.circleImageBox.TabStop = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(0, 467);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 0;
            this.label3.Text = "偵測到圓形";
            // 
            // triangleRectangleImageBox
            // 
            this.triangleRectangleImageBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.triangleRectangleImageBox.Cursor = System.Windows.Forms.Cursors.Cross;
            this.triangleRectangleImageBox.Location = new System.Drawing.Point(493, 78);
            this.triangleRectangleImageBox.Name = "triangleRectangleImageBox";
            this.triangleRectangleImageBox.Size = new System.Drawing.Size(500, 386);
            this.triangleRectangleImageBox.TabIndex = 4;
            this.triangleRectangleImageBox.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(491, 54);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(113, 12);
            this.label2.TabIndex = 0;
            this.label2.Text = "偵測到三角形和矩形";
            // 
            // lineImageBox
            // 
            this.lineImageBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lineImageBox.Cursor = System.Windows.Forms.Cursors.Cross;
            this.lineImageBox.Location = new System.Drawing.Point(493, 485);
            this.lineImageBox.Name = "lineImageBox";
            this.lineImageBox.Size = new System.Drawing.Size(500, 363);
            this.lineImageBox.TabIndex = 4;
            this.lineImageBox.TabStop = false;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(491, 470);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(65, 12);
            this.label4.TabIndex = 0;
            this.label4.Text = "偵測到直線";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1010, 475);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(305, 431);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // imageBox1
            // 
            this.imageBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.imageBox1.Cursor = System.Windows.Forms.Cursors.Cross;
            this.imageBox1.Location = new System.Drawing.Point(1010, 16);
            this.imageBox1.Name = "imageBox1";
            this.imageBox1.Size = new System.Drawing.Size(305, 400);
            this.imageBox1.TabIndex = 6;
            this.imageBox1.TabStop = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1010, 432);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(123, 37);
            this.button1.TabIndex = 7;
            this.button1.Text = "Resize";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1335, 918);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.fileNameTextBox);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.imageBox1);
            this.Controls.Add(this.loadImageButton);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.circleImageBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.originalImageBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.lineImageBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.triangleRectangleImageBox);
            this.Name = "MainForm";
            this.Text = "Shape Detection";
            ((System.ComponentModel.ISupportInitialize)(this.originalImageBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.circleImageBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.triangleRectangleImageBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.lineImageBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private Emgu.CV.UI.ImageBox originalImageBox;
        private Emgu.CV.UI.ImageBox circleImageBox;
        private Emgu.CV.UI.ImageBox triangleRectangleImageBox;
        private Emgu.CV.UI.ImageBox lineImageBox;
        private System.Windows.Forms.TextBox fileNameTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button loadImageButton;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private Emgu.CV.UI.ImageBox imageBox1;
        private System.Windows.Forms.Button button1;

    }
}

