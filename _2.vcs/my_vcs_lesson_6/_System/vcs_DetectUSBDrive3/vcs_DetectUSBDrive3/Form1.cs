using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_DetectUSBDrive3
{
    public partial class Form1 : Form
    {
        [StructLayout(LayoutKind.Sequential)]
        struct DEV_BROADCAST_HDR
        {
            public UInt32 dbch_size;
            public UInt32 dbch_devicetype;
            public UInt32 dbch_reserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        struct DEV_BROADCAST_VOLUME
        {
            public UInt32 dbcv_size;
            public UInt32 dbcv_devicetype;
            public UInt32 dbcv_reserved;
            public UInt32 dbcv_unitmask;
            public UInt16 dbcv_flags;
        }

        protected override void DefWndProc(ref Message m)
        {
            if (m.Msg == 0x0219)//WM_DEVICECHANGE
            {
                switch (m.WParam.ToInt32())
                {
                    case 0x8000://DBT_DEVICEARRIVAL
                        {
                            DEV_BROADCAST_HDR dbhdr = (DEV_BROADCAST_HDR)Marshal.PtrToStructure(m.LParam, typeof(DEV_BROADCAST_HDR));

                            if (dbhdr.dbch_devicetype == 0x00000002)//DBT_DEVTYP_VOLUME
                            {
                                DEV_BROADCAST_VOLUME dbv = (DEV_BROADCAST_VOLUME)Marshal.PtrToStructure(m.LParam, typeof(DEV_BROADCAST_VOLUME));
                                if (dbv.dbcv_flags == 0)
                                    AddVolumes(GetVolumes(dbv.dbcv_unitmask));
                            }
                            break;
                        }
                    case 0x8004://DBT_DEVICEREMOVECOMPLETE
                        {
                            DEV_BROADCAST_HDR dbhdr = (DEV_BROADCAST_HDR)Marshal.PtrToStructure(m.LParam, typeof(DEV_BROADCAST_HDR));

                            if (dbhdr.dbch_devicetype == 0x00000002)//DBT_DEVTYP_VOLUME
                            {
                                DEV_BROADCAST_VOLUME dbv = (DEV_BROADCAST_VOLUME)Marshal.PtrToStructure(m.LParam, typeof(DEV_BROADCAST_VOLUME));
                                if (dbv.dbcv_flags == 0)
                                    RemoveVolumes(GetVolumes(dbv.dbcv_unitmask));
                            }
                            break;
                        }
                }
            }
            base.DefWndProc(ref m);
        }

        /**/
        /// <summary>
        /// 根據驅動器掩碼返回驅動器號數組
        /// </summary>
        /// <param name="Mask">掩碼</param>
        /// <returns>返回驅動器號數組</returns>
        public static char[] GetVolumes(UInt32 Mask)
        {
            List<char> Volumes = new List<char>();

            for (int i = 0; i < 32; i++)
            {
                uint p = (uint)Math.Pow(2, i);
                if ((p | Mask) == p)
                {
                    Volumes.Add((char)('A' + i));
                }
            }
            return Volumes.ToArray();
        }

        public void AddVolumes(char[] Volumes)
        {
            foreach (char volume in Volumes)
            {
                richTextBox1.Text += "增加磁碟 : \t" + volume + "\n";
            }
        }

        public void RemoveVolumes(char[] Volumes)
        {
            foreach (char volume in Volumes)
            {
                richTextBox1.Text += "移除磁碟 : \t" + volume + "\n";
            }
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}

