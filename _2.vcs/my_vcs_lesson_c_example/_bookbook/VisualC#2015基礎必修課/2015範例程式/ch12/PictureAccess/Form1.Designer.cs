﻿namespace PictureAccess
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.btnEnd = new System.Windows.Forms.Button();
            this.btnCls = new System.Windows.Forms.Button();
            this.btnSave = new System.Windows.Forms.Button();
            this.btnOpen = new System.Windows.Forms.Button();
            this.picDraw = new System.Windows.Forms.PictureBox();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.picDraw)).BeginInit();
            this.SuspendLayout();
            // 
            // btnEnd
            // 
            this.btnEnd.Location = new System.Drawing.Point(273, 157);
            this.btnEnd.Name = "btnEnd";
            this.btnEnd.Size = new System.Drawing.Size(53, 21);
            this.btnEnd.TabIndex = 19;
            this.btnEnd.Text = "結束";
            this.btnEnd.UseVisualStyleBackColor = true;
            this.btnEnd.Click += new System.EventHandler(this.btnEnd_Click);
            // 
            // btnCls
            // 
            this.btnCls.Location = new System.Drawing.Point(273, 114);
            this.btnCls.Name = "btnCls";
            this.btnCls.Size = new System.Drawing.Size(53, 21);
            this.btnCls.TabIndex = 18;
            this.btnCls.Text = "清圖";
            this.btnCls.UseVisualStyleBackColor = true;
            this.btnCls.Click += new System.EventHandler(this.btnCls_Click);
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(273, 69);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(54, 20);
            this.btnSave.TabIndex = 17;
            this.btnSave.Text = "存檔";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // btnOpen
            // 
            this.btnOpen.Location = new System.Drawing.Point(272, 23);
            this.btnOpen.Name = "btnOpen";
            this.btnOpen.Size = new System.Drawing.Size(54, 22);
            this.btnOpen.TabIndex = 16;
            this.btnOpen.Text = "開檔";
            this.btnOpen.UseVisualStyleBackColor = true;
            this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
            // 
            // picDraw
            // 
            this.picDraw.Location = new System.Drawing.Point(12, 23);
            this.picDraw.Name = "picDraw";
            this.picDraw.Size = new System.Drawing.Size(231, 157);
            this.picDraw.TabIndex = 15;
            this.picDraw.TabStop = false;
            this.picDraw.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picDraw_MouseDown);
            this.picDraw.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picDraw_MouseMove);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(353, 199);
            this.Controls.Add(this.btnEnd);
            this.Controls.Add(this.btnCls);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.btnOpen);
            this.Controls.Add(this.picDraw);
            this.Name = "Form1";
            this.Text = "小小畫家";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picDraw)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.Button btnEnd;
        internal System.Windows.Forms.Button btnCls;
        internal System.Windows.Forms.Button btnSave;
        internal System.Windows.Forms.Button btnOpen;
        internal System.Windows.Forms.PictureBox picDraw;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}

