using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace WindowsFormsApplication0223a
{
    public partial class LoadingControl : Form
    {
        public delegate void mydelegate();
        public mydelegate eventMethod;
        private static LoadingControl pLoading = new LoadingControl();
        delegate void SetTextCallback(string title, string caption, string description);
        delegate void CloseFormCallback();

        public LoadingControl()
        {
            InitializeComponent();
        }

        private void LoadingControl_Load(object sender, EventArgs e)
        {
            initLoadintForm();
            Thread t = new Thread(new ThreadStart(delegateEventMethod));
            t.IsBackground = true;
            t.Start();
        }

        private void LoadingControl_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (!this.IsDisposed)
            {
                this.Dispose(true);
            }
        }

        private void initLoadintForm()
        {
            this.ControlBox = false;   // 設置不出現關閉按鈕
            this.StartPosition = FormStartPosition.CenterParent;
        }

        private void delegateEventMethod()
        {
            eventMethod();
        }

        public static LoadingControl getLoading()
        {
            if (pLoading.IsDisposed)
            {
                pLoading = new LoadingControl();
                return pLoading;
            }
            else
            {
                return pLoading;
            }
        }

        //這種方法演示如何在線程安全的模式下調用Windows窗體上的控件。  
        /// <summary>
        /// 設置Loading 窗體的 標題title,標簽 caption 和描述 description
        /// </summary>
        /// <param name="title">窗口的標題[為空時，取默認值]</param>
        /// <param name="caption">標簽（例如:please wait）[為空時，取默認值]</param>
        /// <param name="description">描述(例如：正在加載資源...)[為空時，取默認值]</param>
        public void SetCaptionAndDescription(string title, string caption, string description)
        {
            if (this.InvokeRequired && lbl_caption.InvokeRequired && lbl_description.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(SetCaptionAndDescription);
                this.Invoke(d, new object[] { title, caption, description });
            }
            else
            {
                if (!title.Equals(""))
                {
                    this.Text = title;
                }
                if (!caption.Equals(""))
                {
                    lbl_caption.Text = caption;
                }
                if (!description.Equals(""))
                {
                    lbl_description.Text = description;
                }
            }
        }

        public void CloseLoadingForm()
        {
            if (this.InvokeRequired)
            {
                CloseFormCallback d = new CloseFormCallback(CloseLoadingForm);
                this.Invoke(d, new object[] { });
            }
            else
            {
                if (!this.IsDisposed)
                {
                    this.Dispose(true);
                }
            }
        }

        public void SetExecuteMethod(mydelegate method)
        {
            this.eventMethod += method;
        }
    }
}

