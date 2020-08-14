using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

                            using System.IO;    //for Directory

using System.Reflection;    //for BindingFlags

using System.Net;   //for WebClient

using System.Xml.Linq;  //for XDocument
namespace WindowsFormsApplication1ffff
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static void CreateShortCut(string shortCutFile, string targetPath, string description = "")
        {
            var type = Type.GetTypeFromProgID("WScript.Shell");
            object instance = Activator.CreateInstance(type);
            var result = type.InvokeMember("CreateShortCut", BindingFlags.InvokeMethod, null, instance, new object[] { shortCutFile });

            type = result.GetType();
            type.InvokeMember("TargetPath", BindingFlags.SetProperty, null, result, new object[] { targetPath });
            type.InvokeMember("Description", BindingFlags.SetProperty, null, result, new object[] { description });
            type.InvokeMember("Save", BindingFlags.InvokeMethod, null, result, null);
        }

        private static void CreateSendToShortCut(string shortCutFileName, string targetPath, string description = "")
        {
            var sendToFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            var shortCutFile = Path.Combine(sendToFolderPath, shortCutFileName);
            CreateShortCut(shortCutFile, targetPath, description);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            CreateSendToShortCut("david test.lnk", @"C:\Program Files (x86)\WinMerge\WinMergeU.exe");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //DownloadStaticMap(40.714728, -73.998672, "map.jpg");





        }

        private void DownloadStaticMap(double latitude, double longitude, string file)
        {
            if (string.IsNullOrEmpty(file))
                throw new ArgumentNullException("file");

            if (File.Exists(file))
                return;


            var urlFormat = @"http://maps.google.com/maps/api/staticmap?center={0},{1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
            var url = String.Format(urlFormat, latitude.ToString(), longitude.ToString());

            using (var wc = new WebClient())
            {
                wc.DownloadFile(url, file);
            }
        }

    }
}
