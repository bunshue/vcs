using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StartupScreen
{
    /// <summary>  
    /// 啟動畫面  
    /// </summary>  
    public partial class StartupScreen : Form
    {
        /// <summary>  
        /// 啟動畫面本身  
        /// </summary>  
        static StartupScreen instance;

        /// <summary>  
        /// 顯示的圖片  
        /// </summary>  
        Bitmap bitmap;

        public static StartupScreen Instance
        {
            get
            {
                return instance;
            }
            set
            {
                instance = value;
            }
        }

        public StartupScreen()
        {
            InitializeComponent();

            // 設置窗體的類型  
            const string showInfo = "程式啟動中，請稍候...";
            FormBorderStyle = FormBorderStyle.None;
            StartPosition = FormStartPosition.CenterScreen;
            ShowInTaskbar = false;
            bitmap = new Bitmap(Properties.Resources.elephant);
            ClientSize = bitmap.Size;

            using (Font font = new Font("Consoles", 40))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                {
                    g.DrawString(showInfo, font, Brushes.Red, 15, 15);
                }
            }

            BackgroundImage = bitmap;
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                if (bitmap != null)
                {
                    bitmap.Dispose();
                    bitmap = null;
                }
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        public static void ShowSplashScreen()
        {
            instance = new StartupScreen();
            instance.Show();
        }
    }
}
