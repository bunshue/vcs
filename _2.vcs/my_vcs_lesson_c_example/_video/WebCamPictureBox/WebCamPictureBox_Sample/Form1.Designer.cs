﻿using System;
namespace WebCamPictureBox_Sample
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
        /// <param name="disposing">如果應該公開 Managed 資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.webCamPictureBox2 = new WebCamPictureBox.WebCamPictureBox();
            this.webCamPictureBox1 = new WebCamPictureBox.WebCamPictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.webCamPictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.webCamPictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 611);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(98, 51);
            this.button1.TabIndex = 1;
            this.button1.Text = "Test Connect";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(132, 611);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(98, 51);
            this.button2.TabIndex = 2;
            this.button2.Text = "Start";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(252, 611);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(98, 51);
            this.button3.TabIndex = 3;
            this.button3.Text = "Stop";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(362, 95);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(64, 74);
            this.button4.TabIndex = 5;
            this.button4.Text = ">> 截圖";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(372, 611);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(98, 51);
            this.button5.TabIndex = 6;
            this.button5.Text = "Save";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // webCamPictureBox2
            // 
            this.webCamPictureBox2.Image = global::WebCamPictureBox_Sample.Properties.Resources.WebPictureBox;
            this.webCamPictureBox2.Location = new System.Drawing.Point(449, 12);
            this.webCamPictureBox2.Name = "webCamPictureBox2";
            this.webCamPictureBox2.Size = new System.Drawing.Size(320, 240);
            this.webCamPictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.webCamPictureBox2.TabIndex = 4;
            this.webCamPictureBox2.TabStop = false;
            // 
            // webCamPictureBox1
            // 
            this.webCamPictureBox1.Image = global::WebCamPictureBox_Sample.Properties.Resources.WebPictureBox;
            this.webCamPictureBox1.Location = new System.Drawing.Point(12, 12);
            this.webCamPictureBox1.Name = "webCamPictureBox1";
            this.webCamPictureBox1.Size = new System.Drawing.Size(320, 240);
            this.webCamPictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.webCamPictureBox1.TabIndex = 0;
            this.webCamPictureBox1.TabStop = false;
            this.webCamPictureBox1.ConnectStateChanged += new System.EventHandler(this.webCamPictureBox1_WebCamConnectStateChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(868, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(364, 507);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1244, 696);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.webCamPictureBox2);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.webCamPictureBox1);
            this.Name = "Form1";
            this.Text = "WebCam PictureBox Sample";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.webCamPictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.webCamPictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private WebCamPictureBox.WebCamPictureBox webCamPictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private WebCamPictureBox.WebCamPictureBox webCamPictureBox2;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

