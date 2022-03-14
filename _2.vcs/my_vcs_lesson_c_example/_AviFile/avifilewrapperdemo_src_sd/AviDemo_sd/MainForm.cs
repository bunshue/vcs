using System;
using System.Windows.Forms;

namespace AviDemo
{
	/// <summary>
	/// Description of MainForm.	
	/// </summary>
	public class MainForm : System.Windows.Forms.Form
	{
		 /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;


        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabExplore;
        private System.Windows.Forms.TabPage tabEdit;
        private EditControl editControl1;
        private ExploreControl exploreControl1;
		
        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabExplore = new System.Windows.Forms.TabPage();
            this.exploreControl1 = new AviDemo.ExploreControl();
            this.tabEdit = new System.Windows.Forms.TabPage();
            this.editControl1 = new AviDemo.EditControl();
            this.SuspendLayout();
// 
// tabControl1
// 
            this.tabControl1.Controls.Add(this.tabExplore);
            this.tabControl1.Controls.Add(this.tabEdit);
            this.tabControl1.Location = new System.Drawing.Point(0, 13);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(770, 484);
            this.tabControl1.TabIndex = 0;
// 
// tabExplore
// 
            this.tabExplore.Controls.Add(this.exploreControl1);
            this.tabExplore.Location = new System.Drawing.Point(4, 22);
            this.tabExplore.Name = "tabExplore";
            this.tabExplore.Size = new System.Drawing.Size(762, 458);
            this.tabExplore.TabIndex = 0;
            this.tabExplore.Text = "Explore";
// 
// exploreControl1
// 
            this.exploreControl1.Location = new System.Drawing.Point(4, 4);
            this.exploreControl1.Name = "exploreControl1";
            this.exploreControl1.Size = new System.Drawing.Size(756, 423);
            this.exploreControl1.TabIndex = 0;
// 
// tabEdit
// 
            this.tabEdit.Controls.Add(this.editControl1);
            this.tabEdit.Location = new System.Drawing.Point(4, 22);
            this.tabEdit.Name = "tabEdit";
            this.tabEdit.Size = new System.Drawing.Size(762, 458);
            this.tabEdit.TabIndex = 1;
            this.tabEdit.Text = "Edit";
// 
// editControl1
// 
            this.editControl1.Location = new System.Drawing.Point(9, 17);
            this.editControl1.Name = "editControl1";
            this.editControl1.Size = new System.Drawing.Size(752, 438);
            this.editControl1.TabIndex = 0;
// 
// MainForm
// 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
            this.ClientSize = new System.Drawing.Size(770, 498);
            this.Controls.Add(this.tabControl1);
            this.Name = "MainForm";
            this.Text = "Basics of AVI Files";
            this.ResumeLayout(false);

        }

        #endregion

		[STAThread]
        public static void Main() {
            Application.Run(new MainForm());
        }
        
        public MainForm() {
            InitializeComponent();
        }
	}
}
