﻿namespace howto_corona_diagnoser
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
            this.chkFever = new System.Windows.Forms.CheckBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lblNone = new System.Windows.Forms.Label();
            this.lblAll = new System.Windows.Forms.Label();
            this.chkAdult = new System.Windows.Forms.CheckBox();
            this.chkSneezing = new System.Windows.Forms.CheckBox();
            this.chkRunnyNose = new System.Windows.Forms.CheckBox();
            this.chkDiarrhea = new System.Windows.Forms.CheckBox();
            this.chkFatigue = new System.Windows.Forms.CheckBox();
            this.chkSoreThroat = new System.Windows.Forms.CheckBox();
            this.chkAchesAndPains = new System.Windows.Forms.CheckBox();
            this.chkHeadaches = new System.Windows.Forms.CheckBox();
            this.chkShortnessOfBreath = new System.Windows.Forms.CheckBox();
            this.chkDryCough = new System.Windows.Forms.CheckBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.lblAllergies = new System.Windows.Forms.Label();
            this.lblFlu = new System.Windows.Forms.Label();
            this.lblCold = new System.Windows.Forms.Label();
            this.lblCoronaVirus = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // chkFever
            // 
            this.chkFever.AutoSize = true;
            this.chkFever.Location = new System.Drawing.Point(23, 42);
            this.chkFever.Name = "chkFever";
            this.chkFever.Size = new System.Drawing.Size(50, 16);
            this.chkFever.TabIndex = 0;
            this.chkFever.Text = "Fever";
            this.chkFever.UseVisualStyleBackColor = true;
            this.chkFever.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.groupBox1.Controls.Add(this.lblNone);
            this.groupBox1.Controls.Add(this.lblAll);
            this.groupBox1.Controls.Add(this.chkAdult);
            this.groupBox1.Controls.Add(this.chkSneezing);
            this.groupBox1.Controls.Add(this.chkRunnyNose);
            this.groupBox1.Controls.Add(this.chkDiarrhea);
            this.groupBox1.Controls.Add(this.chkFatigue);
            this.groupBox1.Controls.Add(this.chkSoreThroat);
            this.groupBox1.Controls.Add(this.chkAchesAndPains);
            this.groupBox1.Controls.Add(this.chkHeadaches);
            this.groupBox1.Controls.Add(this.chkShortnessOfBreath);
            this.groupBox1.Controls.Add(this.chkDryCough);
            this.groupBox1.Controls.Add(this.chkFever);
            this.groupBox1.Location = new System.Drawing.Point(12, 11);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(164, 578);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Symptoms";
            // 
            // lblNone
            // 
            this.lblNone.BackColor = System.Drawing.Color.LightBlue;
            this.lblNone.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblNone.Location = new System.Drawing.Point(92, 15);
            this.lblNone.Name = "lblNone";
            this.lblNone.Size = new System.Drawing.Size(35, 18);
            this.lblNone.TabIndex = 12;
            this.lblNone.Text = "None";
            this.lblNone.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.lblNone.Click += new System.EventHandler(this.lblNone_Click);
            // 
            // lblAll
            // 
            this.lblAll.BackColor = System.Drawing.Color.LightBlue;
            this.lblAll.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblAll.Location = new System.Drawing.Point(51, 15);
            this.lblAll.Name = "lblAll";
            this.lblAll.Size = new System.Drawing.Size(35, 18);
            this.lblAll.TabIndex = 11;
            this.lblAll.Text = "All";
            this.lblAll.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.lblAll.Click += new System.EventHandler(this.lblAll_Click);
            // 
            // chkAdult
            // 
            this.chkAdult.AutoSize = true;
            this.chkAdult.Location = new System.Drawing.Point(23, 271);
            this.chkAdult.Name = "chkAdult";
            this.chkAdult.Size = new System.Drawing.Size(50, 16);
            this.chkAdult.TabIndex = 10;
            this.chkAdult.Text = "Adult";
            this.chkAdult.UseVisualStyleBackColor = true;
            this.chkAdult.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkSneezing
            // 
            this.chkSneezing.AutoSize = true;
            this.chkSneezing.Location = new System.Drawing.Point(23, 233);
            this.chkSneezing.Name = "chkSneezing";
            this.chkSneezing.Size = new System.Drawing.Size(66, 16);
            this.chkSneezing.TabIndex = 9;
            this.chkSneezing.Text = "Sneezing";
            this.chkSneezing.UseVisualStyleBackColor = true;
            this.chkSneezing.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkRunnyNose
            // 
            this.chkRunnyNose.AutoSize = true;
            this.chkRunnyNose.Location = new System.Drawing.Point(23, 211);
            this.chkRunnyNose.Name = "chkRunnyNose";
            this.chkRunnyNose.Size = new System.Drawing.Size(82, 16);
            this.chkRunnyNose.TabIndex = 8;
            this.chkRunnyNose.Text = "Runny Nose";
            this.chkRunnyNose.UseVisualStyleBackColor = true;
            this.chkRunnyNose.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkDiarrhea
            // 
            this.chkDiarrhea.AutoSize = true;
            this.chkDiarrhea.Location = new System.Drawing.Point(23, 190);
            this.chkDiarrhea.Name = "chkDiarrhea";
            this.chkDiarrhea.Size = new System.Drawing.Size(64, 16);
            this.chkDiarrhea.TabIndex = 7;
            this.chkDiarrhea.Text = "Diarrhea";
            this.chkDiarrhea.UseVisualStyleBackColor = true;
            this.chkDiarrhea.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkFatigue
            // 
            this.chkFatigue.AutoSize = true;
            this.chkFatigue.Location = new System.Drawing.Point(23, 169);
            this.chkFatigue.Name = "chkFatigue";
            this.chkFatigue.Size = new System.Drawing.Size(58, 16);
            this.chkFatigue.TabIndex = 6;
            this.chkFatigue.Text = "Fatigue";
            this.chkFatigue.UseVisualStyleBackColor = true;
            this.chkFatigue.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkSoreThroat
            // 
            this.chkSoreThroat.AutoSize = true;
            this.chkSoreThroat.Location = new System.Drawing.Point(23, 148);
            this.chkSoreThroat.Name = "chkSoreThroat";
            this.chkSoreThroat.Size = new System.Drawing.Size(79, 16);
            this.chkSoreThroat.TabIndex = 5;
            this.chkSoreThroat.Text = "Sore Throat";
            this.chkSoreThroat.UseVisualStyleBackColor = true;
            this.chkSoreThroat.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkAchesAndPains
            // 
            this.chkAchesAndPains.AutoSize = true;
            this.chkAchesAndPains.Location = new System.Drawing.Point(23, 126);
            this.chkAchesAndPains.Name = "chkAchesAndPains";
            this.chkAchesAndPains.Size = new System.Drawing.Size(99, 16);
            this.chkAchesAndPains.TabIndex = 4;
            this.chkAchesAndPains.Text = "Aches and Pains";
            this.chkAchesAndPains.UseVisualStyleBackColor = true;
            this.chkAchesAndPains.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkHeadaches
            // 
            this.chkHeadaches.AutoSize = true;
            this.chkHeadaches.Location = new System.Drawing.Point(23, 105);
            this.chkHeadaches.Name = "chkHeadaches";
            this.chkHeadaches.Size = new System.Drawing.Size(73, 16);
            this.chkHeadaches.TabIndex = 3;
            this.chkHeadaches.Text = "Headaches";
            this.chkHeadaches.UseVisualStyleBackColor = true;
            this.chkHeadaches.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkShortnessOfBreath
            // 
            this.chkShortnessOfBreath.AutoSize = true;
            this.chkShortnessOfBreath.Location = new System.Drawing.Point(23, 84);
            this.chkShortnessOfBreath.Name = "chkShortnessOfBreath";
            this.chkShortnessOfBreath.Size = new System.Drawing.Size(115, 16);
            this.chkShortnessOfBreath.TabIndex = 2;
            this.chkShortnessOfBreath.Text = "Shortness of Breath";
            this.chkShortnessOfBreath.UseVisualStyleBackColor = true;
            this.chkShortnessOfBreath.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // chkDryCough
            // 
            this.chkDryCough.AutoSize = true;
            this.chkDryCough.Location = new System.Drawing.Point(23, 63);
            this.chkDryCough.Name = "chkDryCough";
            this.chkDryCough.Size = new System.Drawing.Size(77, 16);
            this.chkDryCough.TabIndex = 1;
            this.chkDryCough.Text = "Dry Cough";
            this.chkDryCough.UseVisualStyleBackColor = true;
            this.chkDryCough.CheckedChanged += new System.EventHandler(this.chkSymptom_CheckedChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox2.Controls.Add(this.lblAllergies);
            this.groupBox2.Controls.Add(this.lblFlu);
            this.groupBox2.Controls.Add(this.lblCold);
            this.groupBox2.Controls.Add(this.lblCoronaVirus);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(182, 11);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(410, 578);
            this.groupBox2.TabIndex = 10;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Possible Causes";
            // 
            // lblAllergies
            // 
            this.lblAllergies.BackColor = System.Drawing.Color.LightGreen;
            this.lblAllergies.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblAllergies.Location = new System.Drawing.Point(112, 81);
            this.lblAllergies.Name = "lblAllergies";
            this.lblAllergies.Size = new System.Drawing.Size(125, 16);
            this.lblAllergies.TabIndex = 7;
            this.lblAllergies.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblFlu
            // 
            this.lblFlu.BackColor = System.Drawing.Color.LightGreen;
            this.lblFlu.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblFlu.Location = new System.Drawing.Point(112, 59);
            this.lblFlu.Name = "lblFlu";
            this.lblFlu.Size = new System.Drawing.Size(125, 16);
            this.lblFlu.TabIndex = 6;
            this.lblFlu.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblCold
            // 
            this.lblCold.BackColor = System.Drawing.Color.LightGreen;
            this.lblCold.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCold.Location = new System.Drawing.Point(112, 38);
            this.lblCold.Name = "lblCold";
            this.lblCold.Size = new System.Drawing.Size(125, 16);
            this.lblCold.TabIndex = 5;
            this.lblCold.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblCoronaVirus
            // 
            this.lblCoronaVirus.BackColor = System.Drawing.Color.LightGreen;
            this.lblCoronaVirus.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCoronaVirus.Location = new System.Drawing.Point(112, 18);
            this.lblCoronaVirus.Name = "lblCoronaVirus";
            this.lblCoronaVirus.Size = new System.Drawing.Size(125, 16);
            this.lblCoronaVirus.TabIndex = 4;
            this.lblCoronaVirus.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(23, 82);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(46, 12);
            this.label4.TabIndex = 3;
            this.label4.Text = "Allergies";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(23, 61);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 12);
            this.label3.TabIndex = 2;
            this.label3.Text = "Flu";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(23, 40);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(75, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "Common Cold";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 18);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(57, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "COVID-19";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(598, 15);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(486, 574);
            this.richTextBox1.TabIndex = 11;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1096, 601);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "howto_corona_diagnoser";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.CheckBox chkFever;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox chkDiarrhea;
        private System.Windows.Forms.CheckBox chkFatigue;
        private System.Windows.Forms.CheckBox chkSoreThroat;
        private System.Windows.Forms.CheckBox chkAchesAndPains;
        private System.Windows.Forms.CheckBox chkHeadaches;
        private System.Windows.Forms.CheckBox chkShortnessOfBreath;
        private System.Windows.Forms.CheckBox chkDryCough;
        private System.Windows.Forms.CheckBox chkSneezing;
        private System.Windows.Forms.CheckBox chkRunnyNose;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label lblCoronaVirus;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblAllergies;
        private System.Windows.Forms.Label lblFlu;
        private System.Windows.Forms.Label lblCold;
        private System.Windows.Forms.CheckBox chkAdult;
        private System.Windows.Forms.Label lblNone;
        private System.Windows.Forms.Label lblAll;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

