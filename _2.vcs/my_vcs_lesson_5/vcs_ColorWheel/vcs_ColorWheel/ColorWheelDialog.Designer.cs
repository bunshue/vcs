namespace vcs_ColorWheel
{
    partial class ColorWheelDialog
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
            this.txtAlpha = new System.Windows.Forms.TextBox();
            this.txtSaturation = new System.Windows.Forms.TextBox();
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnOk = new System.Windows.Forms.Button();
            this.picSelection = new System.Windows.Forms.PictureBox();
            this.label4 = new System.Windows.Forms.Label();
            this.picWheel = new System.Windows.Forms.PictureBox();
            this.picSample = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.hscrSaturation = new System.Windows.Forms.HScrollBar();
            this.hscrAlpha = new System.Windows.Forms.HScrollBar();
            ((System.ComponentModel.ISupportInitialize)(this.picSelection)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWheel)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            this.SuspendLayout();
            // 
            // txtAlpha
            // 
            this.txtAlpha.Location = new System.Drawing.Point(248, 205);
            this.txtAlpha.Name = "txtAlpha";
            this.txtAlpha.ReadOnly = true;
            this.txtAlpha.Size = new System.Drawing.Size(39, 22);
            this.txtAlpha.TabIndex = 35;
            this.txtAlpha.TabStop = false;
            this.txtAlpha.Text = "255";
            this.txtAlpha.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtSaturation
            // 
            this.txtSaturation.Location = new System.Drawing.Point(248, 229);
            this.txtSaturation.Name = "txtSaturation";
            this.txtSaturation.ReadOnly = true;
            this.txtSaturation.Size = new System.Drawing.Size(39, 22);
            this.txtSaturation.TabIndex = 34;
            this.txtSaturation.TabStop = false;
            this.txtSaturation.Text = "255";
            this.txtSaturation.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnCancel
            // 
            this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnCancel.Location = new System.Drawing.Point(212, 253);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(75, 21);
            this.btnCancel.TabIndex = 33;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = true;
            // 
            // btnOk
            // 
            this.btnOk.DialogResult = System.Windows.Forms.DialogResult.OK;
            this.btnOk.Location = new System.Drawing.Point(131, 253);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(75, 21);
            this.btnOk.TabIndex = 32;
            this.btnOk.Text = "OK";
            this.btnOk.UseVisualStyleBackColor = true;
            // 
            // picSelection
            // 
            this.picSelection.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSelection.Location = new System.Drawing.Point(225, 121);
            this.picSelection.Name = "picSelection";
            this.picSelection.Size = new System.Drawing.Size(64, 59);
            this.picSelection.TabIndex = 31;
            this.picSelection.TabStop = false;
            // 
            // label4
            // 
            this.label4.AutoEllipsis = true;
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(224, 106);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(50, 12);
            this.label4.TabIndex = 30;
            this.label4.Text = "Selection:";
            // 
            // picWheel
            // 
            this.picWheel.Location = new System.Drawing.Point(12, 12);
            this.picWheel.Name = "picWheel";
            this.picWheel.Size = new System.Drawing.Size(200, 185);
            this.picWheel.TabIndex = 29;
            this.picWheel.TabStop = false;
            this.picWheel.MouseClick += new System.Windows.Forms.MouseEventHandler(this.picWheel_MouseClick);
            this.picWheel.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picWheel_MouseMove);
            // 
            // picSample
            // 
            this.picSample.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSample.Location = new System.Drawing.Point(225, 24);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(64, 59);
            this.picSample.TabIndex = 28;
            this.picSample.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(9, 232);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 12);
            this.label2.TabIndex = 27;
            this.label2.Text = "Saturation:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 208);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(36, 12);
            this.label1.TabIndex = 26;
            this.label1.Text = "Alpha:";
            // 
            // hscrSaturation
            // 
            this.hscrSaturation.Location = new System.Drawing.Point(70, 229);
            this.hscrSaturation.Maximum = 264;
            this.hscrSaturation.Name = "hscrSaturation";
            this.hscrSaturation.Size = new System.Drawing.Size(175, 20);
            this.hscrSaturation.TabIndex = 25;
            this.hscrSaturation.Value = 255;
            this.hscrSaturation.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hscrSaturation_Scroll);
            // 
            // hscrAlpha
            // 
            this.hscrAlpha.Location = new System.Drawing.Point(70, 205);
            this.hscrAlpha.Maximum = 264;
            this.hscrAlpha.Name = "hscrAlpha";
            this.hscrAlpha.Size = new System.Drawing.Size(175, 20);
            this.hscrAlpha.TabIndex = 24;
            this.hscrAlpha.Value = 255;
            this.hscrAlpha.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hscrAlpha_Scroll);
            // 
            // ColorWheelDialog
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(461, 433);
            this.Controls.Add(this.txtAlpha);
            this.Controls.Add(this.txtSaturation);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.picSelection);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.picWheel);
            this.Controls.Add(this.picSample);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.hscrSaturation);
            this.Controls.Add(this.hscrAlpha);
            this.Name = "ColorWheelDialog";
            this.Text = "ColorWheelDialog";
            this.Load += new System.EventHandler(this.ColorWheelDialog_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picSelection)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWheel)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtAlpha;
        private System.Windows.Forms.TextBox txtSaturation;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.Button btnOk;
        private System.Windows.Forms.PictureBox picSelection;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.PictureBox picWheel;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.HScrollBar hscrSaturation;
        private System.Windows.Forms.HScrollBar hscrAlpha;
    }
}