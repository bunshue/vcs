namespace vcs_WordArt
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
            this.label1 = new System.Windows.Forms.Label();
            this.wordArt1 = new vcs_WordArt.WordArt();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(12, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(154, 24);
            this.label1.TabIndex = 0;
            this.label1.Text = "使用者控制項";
            // 
            // wordArt1
            // 
            this.wordArt1.Caption = "艺术字的控件";
            this.wordArt1.Location = new System.Drawing.Point(16, 147);
            this.wordArt1.Name = "wordArt1";
            this.wordArt1.Size = new System.Drawing.Size(391, 150);
            this.wordArt1.TabIndex = 1;
            this.wordArt1.WordArtBackColor = System.Drawing.Color.Gray;
            this.wordArt1.WordArtEffect = vcs_WordArt.WordArtEffectStyle.projection;
            this.wordArt1.WordArtFont = new System.Drawing.Font("標楷體", 24F);
            this.wordArt1.WordArtForeColor = System.Drawing.Color.BlueViolet;
            this.wordArt1.WordArtSmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            this.wordArt1.WordArtTextRenderingHint = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(560, 323);
            this.Controls.Add(this.wordArt1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private WordArt wordArt1;
    }
}

