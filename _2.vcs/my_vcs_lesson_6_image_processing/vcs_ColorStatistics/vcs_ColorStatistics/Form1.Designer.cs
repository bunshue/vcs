namespace vcs_ColorStatistics
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
            this.LblDelta = new System.Windows.Forms.Label();
            this.SliderDelta = new System.Windows.Forms.TrackBar();
            this.label2 = new System.Windows.Forms.Label();
            this.LblAmount = new System.Windows.Forms.Label();
            this.SliderColorAmount = new System.Windows.Forms.TrackBar();
            this.Label = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.LblStatus = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.PicR = new System.Windows.Forms.PictureBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.button0 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.SliderDelta)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderColorAmount)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.PicR)).BeginInit();
            this.SuspendLayout();
            // 
            // LblDelta
            // 
            this.LblDelta.AutoSize = true;
            this.LblDelta.Location = new System.Drawing.Point(423, 124);
            this.LblDelta.Name = "LblDelta";
            this.LblDelta.Size = new System.Drawing.Size(17, 12);
            this.LblDelta.TabIndex = 24;
            this.LblDelta.Text = "24";
            // 
            // SliderDelta
            // 
            this.SliderDelta.Location = new System.Drawing.Point(116, 119);
            this.SliderDelta.Maximum = 128;
            this.SliderDelta.Minimum = 1;
            this.SliderDelta.Name = "SliderDelta";
            this.SliderDelta.Size = new System.Drawing.Size(301, 45);
            this.SliderDelta.TabIndex = 23;
            this.SliderDelta.TickStyle = System.Windows.Forms.TickStyle.None;
            this.SliderDelta.Value = 24;
            this.SliderDelta.Scroll += new System.EventHandler(this.SliderDelta_Scroll);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 124);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 22;
            this.label2.Text = "Delta：";
            // 
            // LblAmount
            // 
            this.LblAmount.AutoSize = true;
            this.LblAmount.Location = new System.Drawing.Point(423, 79);
            this.LblAmount.Name = "LblAmount";
            this.LblAmount.Size = new System.Drawing.Size(17, 12);
            this.LblAmount.TabIndex = 21;
            this.LblAmount.Text = "20";
            // 
            // SliderColorAmount
            // 
            this.SliderColorAmount.Location = new System.Drawing.Point(116, 74);
            this.SliderColorAmount.Maximum = 20;
            this.SliderColorAmount.Minimum = 1;
            this.SliderColorAmount.Name = "SliderColorAmount";
            this.SliderColorAmount.Size = new System.Drawing.Size(301, 45);
            this.SliderColorAmount.TabIndex = 20;
            this.SliderColorAmount.TickStyle = System.Windows.Forms.TickStyle.None;
            this.SliderColorAmount.Value = 20;
            this.SliderColorAmount.Scroll += new System.EventHandler(this.SliderColorAmount_Scroll);
            // 
            // Label
            // 
            this.Label.AutoSize = true;
            this.Label.Location = new System.Drawing.Point(12, 79);
            this.Label.Name = "Label";
            this.Label.Size = new System.Drawing.Size(89, 12);
            this.Label.TabIndex = 19;
            this.Label.Text = "主要顏色總數：";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1254, 31);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 36);
            this.bt_clear.TabIndex = 26;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1239, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(197, 643);
            this.richTextBox1.TabIndex = 25;
            this.richTextBox1.Text = "";
            // 
            // LblStatus
            // 
            this.LblStatus.AutoSize = true;
            this.LblStatus.Location = new System.Drawing.Point(200, 17);
            this.LblStatus.Name = "LblStatus";
            this.LblStatus.Size = new System.Drawing.Size(0, 12);
            this.LblStatus.TabIndex = 17;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(14, 175);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 16;
            this.pictureBox1.TabStop = false;
            // 
            // PicR
            // 
            this.PicR.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.PicR.Location = new System.Drawing.Point(658, 12);
            this.PicR.Name = "PicR";
            this.PicR.Size = new System.Drawing.Size(575, 643);
            this.PicR.TabIndex = 15;
            this.PicR.TabStop = false;
            this.PicR.Paint += new System.Windows.Forms.PaintEventHandler(this.PicR_Paint);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(518, 32);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(120, 60);
            this.button0.TabIndex = 131;
            this.button0.Text = "選擇圖像";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(518, 98);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(120, 60);
            this.button1.TabIndex = 130;
            this.button1.Text = "處理";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1447, 670);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.LblDelta);
            this.Controls.Add(this.SliderDelta);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.LblAmount);
            this.Controls.Add(this.SliderColorAmount);
            this.Controls.Add(this.Label);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.LblStatus);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.PicR);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.SliderDelta)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderColorAmount)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.PicR)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label LblDelta;
        private System.Windows.Forms.TrackBar SliderDelta;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label LblAmount;
        private System.Windows.Forms.TrackBar SliderColorAmount;
        private System.Windows.Forms.Label Label;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label LblStatus;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox PicR;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button1;
    }
}

