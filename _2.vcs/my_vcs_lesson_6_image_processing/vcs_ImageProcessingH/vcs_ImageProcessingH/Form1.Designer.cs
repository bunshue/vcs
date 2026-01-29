namespace vcs_ImageProcessingH
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.scrBright = new System.Windows.Forms.HScrollBar();
            this.lb_bright = new System.Windows.Forms.Label();
            this.scrBlue = new System.Windows.Forms.HScrollBar();
            this.lb_blue = new System.Windows.Forms.Label();
            this.scrGreen = new System.Windows.Forms.HScrollBar();
            this.lb_green = new System.Windows.Forms.Label();
            this.scrRed = new System.Windows.Forms.HScrollBar();
            this.picColor = new System.Windows.Forms.PictureBox();
            this.lb_red = new System.Windows.Forms.Label();
            this.picToned = new System.Windows.Forms.PictureBox();
            this.picOriginal = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.scrBright);
            this.groupBox1.Controls.Add(this.lb_bright);
            this.groupBox1.Controls.Add(this.scrBlue);
            this.groupBox1.Controls.Add(this.lb_blue);
            this.groupBox1.Controls.Add(this.scrGreen);
            this.groupBox1.Controls.Add(this.lb_green);
            this.groupBox1.Controls.Add(this.scrRed);
            this.groupBox1.Controls.Add(this.picColor);
            this.groupBox1.Controls.Add(this.lb_red);
            this.groupBox1.Controls.Add(this.picToned);
            this.groupBox1.Controls.Add(this.picOriginal);
            this.groupBox1.Location = new System.Drawing.Point(12, 118);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(644, 512);
            this.groupBox1.TabIndex = 21;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "改變色調";
            // 
            // scrBright
            // 
            this.scrBright.Location = new System.Drawing.Point(62, 81);
            this.scrBright.Maximum = 264;
            this.scrBright.Name = "scrBright";
            this.scrBright.Size = new System.Drawing.Size(258, 14);
            this.scrBright.TabIndex = 24;
            // 
            // lb_bright
            // 
            this.lb_bright.AutoSize = true;
            this.lb_bright.Location = new System.Drawing.Point(20, 81);
            this.lb_bright.Name = "lb_bright";
            this.lb_bright.Size = new System.Drawing.Size(38, 12);
            this.lb_bright.TabIndex = 23;
            this.lb_bright.Text = "Bright:";
            // 
            // scrBlue
            // 
            this.scrBlue.Location = new System.Drawing.Point(62, 65);
            this.scrBlue.Maximum = 264;
            this.scrBlue.Name = "scrBlue";
            this.scrBlue.Size = new System.Drawing.Size(258, 14);
            this.scrBlue.TabIndex = 22;
            // 
            // lb_blue
            // 
            this.lb_blue.AutoSize = true;
            this.lb_blue.Location = new System.Drawing.Point(20, 65);
            this.lb_blue.Name = "lb_blue";
            this.lb_blue.Size = new System.Drawing.Size(30, 12);
            this.lb_blue.TabIndex = 21;
            this.lb_blue.Text = "Blue:";
            // 
            // scrGreen
            // 
            this.scrGreen.Location = new System.Drawing.Point(62, 48);
            this.scrGreen.Maximum = 264;
            this.scrGreen.Name = "scrGreen";
            this.scrGreen.Size = new System.Drawing.Size(258, 14);
            this.scrGreen.TabIndex = 20;
            // 
            // lb_green
            // 
            this.lb_green.AutoSize = true;
            this.lb_green.Location = new System.Drawing.Point(20, 48);
            this.lb_green.Name = "lb_green";
            this.lb_green.Size = new System.Drawing.Size(36, 12);
            this.lb_green.TabIndex = 19;
            this.lb_green.Text = "Green:";
            // 
            // scrRed
            // 
            this.scrRed.Location = new System.Drawing.Point(62, 30);
            this.scrRed.Maximum = 264;
            this.scrRed.Name = "scrRed";
            this.scrRed.Size = new System.Drawing.Size(258, 14);
            this.scrRed.TabIndex = 18;
            // 
            // picColor
            // 
            this.picColor.BackColor = System.Drawing.Color.LightBlue;
            this.picColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.picColor.Location = new System.Drawing.Point(326, 30);
            this.picColor.Name = "picColor";
            this.picColor.Size = new System.Drawing.Size(68, 63);
            this.picColor.TabIndex = 17;
            this.picColor.TabStop = false;
            // 
            // lb_red
            // 
            this.lb_red.AutoSize = true;
            this.lb_red.Location = new System.Drawing.Point(20, 30);
            this.lb_red.Name = "lb_red";
            this.lb_red.Size = new System.Drawing.Size(27, 12);
            this.lb_red.TabIndex = 16;
            this.lb_red.Text = "Red:";
            // 
            // picToned
            // 
            this.picToned.Location = new System.Drawing.Point(326, 97);
            this.picToned.Name = "picToned";
            this.picToned.Size = new System.Drawing.Size(300, 400);
            this.picToned.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picToned.TabIndex = 15;
            this.picToned.TabStop = false;
            // 
            // picOriginal
            // 
            this.picOriginal.Image = ((System.Drawing.Image)(resources.GetObject("picOriginal.Image")));
            this.picOriginal.Location = new System.Drawing.Point(20, 97);
            this.picOriginal.Name = "picOriginal";
            this.picOriginal.Size = new System.Drawing.Size(305, 400);
            this.picOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picOriginal.TabIndex = 14;
            this.picOriginal.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(426, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 29;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(442, 68);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 36;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(984, 661);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "10,10";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.HScrollBar scrBright;
        private System.Windows.Forms.Label lb_bright;
        private System.Windows.Forms.HScrollBar scrBlue;
        private System.Windows.Forms.Label lb_blue;
        private System.Windows.Forms.HScrollBar scrGreen;
        private System.Windows.Forms.Label lb_green;
        private System.Windows.Forms.HScrollBar scrRed;
        private System.Windows.Forms.PictureBox picColor;
        private System.Windows.Forms.Label lb_red;
        private System.Windows.Forms.PictureBox picToned;
        private System.Windows.Forms.PictureBox picOriginal;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
    }
}

