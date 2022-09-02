namespace howto_thumbnail_web_table
{
    partial class Form1
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.txtUrlPrefix = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtThumbHeight = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.txtThumbWidth = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.btnGo = new System.Windows.Forms.Button();
            this.txtWebPage = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.fbdDirectory = new System.Windows.Forms.FolderBrowserDialog();
            this.btnPickOutputDirectory = new System.Windows.Forms.Button();
            this.txtOutputDir = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnPickInputDirectory = new System.Windows.Forms.Button();
            this.txtInputDir = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtUrlPrefix
            // 
            this.txtUrlPrefix.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtUrlPrefix.Location = new System.Drawing.Point(105, 91);
            this.txtUrlPrefix.Name = "txtUrlPrefix";
            this.txtUrlPrefix.Size = new System.Drawing.Size(238, 20);
            this.txtUrlPrefix.TabIndex = 24;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 94);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(61, 13);
            this.label6.TabIndex = 32;
            this.label6.Text = "URL Prefix:";
            // 
            // txtThumbHeight
            // 
            this.txtThumbHeight.Location = new System.Drawing.Point(105, 144);
            this.txtThumbHeight.Name = "txtThumbHeight";
            this.txtThumbHeight.Size = new System.Drawing.Size(75, 20);
            this.txtThumbHeight.TabIndex = 26;
            this.txtThumbHeight.Text = "100";
            this.txtThumbHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 147);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(77, 13);
            this.label4.TabIndex = 31;
            this.label4.Text = "Thumb Height:";
            // 
            // txtThumbWidth
            // 
            this.txtThumbWidth.Location = new System.Drawing.Point(105, 117);
            this.txtThumbWidth.Name = "txtThumbWidth";
            this.txtThumbWidth.Size = new System.Drawing.Size(75, 20);
            this.txtThumbWidth.TabIndex = 25;
            this.txtThumbWidth.Text = "100";
            this.txtThumbWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 120);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(74, 13);
            this.label5.TabIndex = 30;
            this.label5.Text = "Thumb Width:";
            // 
            // btnGo
            // 
            this.btnGo.Location = new System.Drawing.Point(215, 129);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(75, 23);
            this.btnGo.TabIndex = 28;
            this.btnGo.Text = "Go";
            this.btnGo.UseVisualStyleBackColor = true;
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // txtWebPage
            // 
            this.txtWebPage.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtWebPage.Location = new System.Drawing.Point(105, 65);
            this.txtWebPage.Name = "txtWebPage";
            this.txtWebPage.Size = new System.Drawing.Size(238, 20);
            this.txtWebPage.TabIndex = 23;
            this.txtWebPage.Text = "Pictures.html";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 68);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(61, 13);
            this.label3.TabIndex = 29;
            this.label3.Text = "Web Page:";
            // 
            // btnPickOutputDirectory
            // 
            this.btnPickOutputDirectory.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnPickOutputDirectory.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnPickOutputDirectory.Image = ((System.Drawing.Image)(resources.GetObject("btnPickOutputDirectory.Image")));
            this.btnPickOutputDirectory.Location = new System.Drawing.Point(349, 36);
            this.btnPickOutputDirectory.Name = "btnPickOutputDirectory";
            this.btnPickOutputDirectory.Size = new System.Drawing.Size(23, 23);
            this.btnPickOutputDirectory.TabIndex = 22;
            this.btnPickOutputDirectory.UseVisualStyleBackColor = true;
            this.btnPickOutputDirectory.Click += new System.EventHandler(this.btnPickOutputDirectory_Click);
            // 
            // txtOutputDir
            // 
            this.txtOutputDir.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtOutputDir.Location = new System.Drawing.Point(105, 38);
            this.txtOutputDir.Name = "txtOutputDir";
            this.txtOutputDir.Size = new System.Drawing.Size(238, 20);
            this.txtOutputDir.TabIndex = 21;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(87, 13);
            this.label2.TabIndex = 27;
            this.label2.Text = "Output Directory:";
            // 
            // btnPickInputDirectory
            // 
            this.btnPickInputDirectory.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnPickInputDirectory.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnPickInputDirectory.Image = ((System.Drawing.Image)(resources.GetObject("btnPickInputDirectory.Image")));
            this.btnPickInputDirectory.Location = new System.Drawing.Point(349, 10);
            this.btnPickInputDirectory.Name = "btnPickInputDirectory";
            this.btnPickInputDirectory.Size = new System.Drawing.Size(23, 23);
            this.btnPickInputDirectory.TabIndex = 20;
            this.btnPickInputDirectory.UseVisualStyleBackColor = true;
            this.btnPickInputDirectory.Click += new System.EventHandler(this.btnPickInputDirectory_Click);
            // 
            // txtInputDir
            // 
            this.txtInputDir.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtInputDir.Location = new System.Drawing.Point(105, 12);
            this.txtInputDir.Name = "txtInputDir";
            this.txtInputDir.Size = new System.Drawing.Size(238, 20);
            this.txtInputDir.TabIndex = 18;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(79, 13);
            this.label1.TabIndex = 19;
            this.label1.Text = "Input Directory:";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGo;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(384, 175);
            this.Controls.Add(this.txtUrlPrefix);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.txtThumbHeight);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txtThumbWidth);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.txtWebPage);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.btnPickOutputDirectory);
            this.Controls.Add(this.txtOutputDir);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnPickInputDirectory);
            this.Controls.Add(this.txtInputDir);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_thumbnail_web_table";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtUrlPrefix;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtThumbHeight;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtThumbWidth;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button btnGo;
        private System.Windows.Forms.TextBox txtWebPage;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.FolderBrowserDialog fbdDirectory;
        private System.Windows.Forms.Button btnPickOutputDirectory;
        private System.Windows.Forms.TextBox txtOutputDir;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnPickInputDirectory;
        private System.Windows.Forms.TextBox txtInputDir;
        private System.Windows.Forms.Label label1;
    }
}

