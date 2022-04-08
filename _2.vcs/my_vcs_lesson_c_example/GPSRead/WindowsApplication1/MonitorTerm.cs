using System;
using System.Windows.Forms;
using System.IO;
using JH.CommBase; 
using System.Text;
using System.Threading;

namespace WinBaseTerm
{
     public   class MonitorTerm : CommBase
    {

         public static GPSReadForm form;
        public static MonitorTerm term;
        public static CommBaseTermSettings settings;
        public static string settingsFileName = "";

        private int lineCount = 0;
         public static int messgeCount = 0;
        public class CommBaseTermSettings : CommBaseSettings
        {
            public bool showAsHex = false;
            public bool breakLineOnChar = false;
            public ASCII lineBreakChar = 0;
            public int charsInLine = 0;

            public static new CommBaseTermSettings LoadFromXML(Stream s)
            {
                return (CommBaseTermSettings)LoadFromXML(s, typeof(CommBaseTermSettings));
            }
        }

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static int Main(string[] args)
        {
            if (args.Length == 1)
            {
                FileInfo f = new FileInfo(args[0]);
                if (f.Exists)
                {
                    settingsFileName = f.Name;
                    settings = CommBaseTermSettings.LoadFromXML(f.OpenRead());
                    if (settings == null)
                    {
                        MessageBox.Show("Bad settings file", "CommBase Terminal", MessageBoxButtons.OK);
                        return 0;
                    }
                }
            }
            else
            {
                settings = new CommBaseTermSettings();
            }
            settings.baudRate = 115200;
            settings.txWhenRxXoff = false;
            term = new MonitorTerm();
            form = new GPSReadForm();
            Application.Run(form);
            return 0;
        }
        public bool Immediate = false;       

        protected override CommBaseSettings CommSettings()
        {
            return settings;
        }

         string message = "";
         bool isNoend=true;
        protected override void OnRxChar(byte c)
        {
            string s; bool nl = false;
            ASCII v = (ASCII)c;
            if (settings.charsInLine > 0)
            {
                nl = (++lineCount >= settings.charsInLine);
            }
            if (settings.breakLineOnChar) if (v == settings.lineBreakChar) nl = true;
            if (nl) lineCount = 0;
            if (settings.showAsHex)
            {
                s = c.ToString("X2");
                if (!nl) s += " ";
            }
            else
            {
                if ((c < 0x20) || (c > 0x7E))
                {
                    s = "<" + v.ToString() + ">";
                }
                else
                {
                    s = new string((char)c, 1);
                }
            }
            lock(message)
            {
                message += s;
                if (s.ToLower() == "<lf>")
                {
                    messgeCount = messgeCount + 1;
                    form.ShowRevMsg(message, messgeCount);
               

                    message = "";
                }
            }

         
        }
  
     
       
    }
}
