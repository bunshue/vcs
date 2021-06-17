using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;
using System.Drawing.Drawing2D;

namespace BootStrapBeatitude
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
                                                    GraphicsPath gp = new GraphicsPath();
                                                    Rectangle rect=new Rectangle(new Point(0,0),new Size(this.Width,this.Height));
                                                    gp.AddEllipse(rect);
                                                    this.Region = new Region(gp);

                                                    GraphicsPath gpstirng = new GraphicsPath();
                                                    FontFamily family = new FontFamily("細明體");
                                                    int fontStyle = (int)FontStyle.Italic;
                                                    int emSize = 25;
           
                                                    Point origin = new Point(0, 0);
                                                    StringFormat format = StringFormat.GenericDefault;

                                                    gpstirng.AddString("開開心心每一天", family, fontStyle, emSize, origin, format);
                                                    this.button1.Region = new Region(gpstirng);
                                                    //Registry.LocalMachine.CreateSubKey(@"SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN").SetValue("MyAngel", Application.StartupPath + "\\Ex05_13.exe", RegistryValueKind.String);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}