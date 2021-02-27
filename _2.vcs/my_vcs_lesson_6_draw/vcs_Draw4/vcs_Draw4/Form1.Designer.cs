namespace vcs_Draw4
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button13 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button34 = new System.Windows.Forms.Button();
            this.button42 = new System.Windows.Forms.Button();
            this.button44 = new System.Windows.Forms.Button();
            this.button45 = new System.Windows.Forms.Button();
            this.button46 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(146, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(601, 601);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 748);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(128, 48);
            this.button2.TabIndex = 2;
            this.button2.Text = "clear";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 120);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(120, 30);
            this.button3.TabIndex = 3;
            this.button3.Text = "DrawLine";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(146, 619);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(601, 177);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // button13
            // 
            this.button13.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button13.Location = new System.Drawing.Point(12, 374);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(120, 30);
            this.button13.TabIndex = 14;
            this.button13.Text = "DrawArc";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button15
            // 
            this.button15.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button15.Location = new System.Drawing.Point(12, 192);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(120, 30);
            this.button15.TabIndex = 16;
            this.button15.Text = "DrawCurve";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // button17
            // 
            this.button17.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button17.Location = new System.Drawing.Point(12, 410);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(120, 30);
            this.button17.TabIndex = 18;
            this.button17.Text = "DrawBezier";
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // button34
            // 
            this.button34.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button34.Location = new System.Drawing.Point(12, 156);
            this.button34.Name = "button34";
            this.button34.Size = new System.Drawing.Size(120, 30);
            this.button34.TabIndex = 36;
            this.button34.Text = "DrawLines";
            this.button34.UseVisualStyleBackColor = true;
            this.button34.Click += new System.EventHandler(this.button34_Click);
            // 
            // button42
            // 
            this.button42.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button42.Location = new System.Drawing.Point(778, 338);
            this.button42.Name = "button42";
            this.button42.Size = new System.Drawing.Size(120, 30);
            this.button42.TabIndex = 44;
            this.button42.Text = "Eraser";
            this.button42.UseVisualStyleBackColor = true;
            this.button42.Click += new System.EventHandler(this.button42_Click);
            // 
            // button44
            // 
            this.button44.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button44.Location = new System.Drawing.Point(915, 302);
            this.button44.Name = "button44";
            this.button44.Size = new System.Drawing.Size(120, 30);
            this.button44.TabIndex = 48;
            this.button44.Text = "GraphicsPath";
            this.button44.UseVisualStyleBackColor = true;
            this.button44.Click += new System.EventHandler(this.button44_Click);
            // 
            // button45
            // 
            this.button45.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button45.Location = new System.Drawing.Point(915, 338);
            this.button45.Name = "button45";
            this.button45.Size = new System.Drawing.Size(120, 30);
            this.button45.TabIndex = 49;
            this.button45.Text = "GraphicsPath";
            this.button45.UseVisualStyleBackColor = true;
            this.button45.Click += new System.EventHandler(this.button45_Click);
            // 
            // button46
            // 
            this.button46.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button46.Location = new System.Drawing.Point(915, 389);
            this.button46.Name = "button46";
            this.button46.Size = new System.Drawing.Size(120, 30);
            this.button46.TabIndex = 50;
            this.button46.Text = "GraphicsPath";
            this.button46.UseVisualStyleBackColor = true;
            this.button46.Click += new System.EventHandler(this.button46_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1047, 808);
            this.Controls.Add(this.button46);
            this.Controls.Add(this.button45);
            this.Controls.Add(this.button44);
            this.Controls.Add(this.button42);
            this.Controls.Add(this.button34);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button34;
        private System.Windows.Forms.Button button42;
        private System.Windows.Forms.Button button44;
        private System.Windows.Forms.Button button45;
        private System.Windows.Forms.Button button46;
    }
}

