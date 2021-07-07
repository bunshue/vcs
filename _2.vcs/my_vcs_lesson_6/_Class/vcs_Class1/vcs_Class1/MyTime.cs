using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class1
{
    class MyTime
    {
        private int Hour;
        private int Minute;
        private int Second;

        // constructor
        public MyTime(int h, int m, int s)
        {
            setTime(h, m, s);
        }

        public MyTime(int h, int m)
        {
            setTime(h, m);
        }

        // default constructor
        public MyTime() { }

        public void setTime(int h, int m, int s)
        {
            // 假設超出範圍，則不處理 
            /*
            if (h < 0 || h > 23) return;
            if (m < 0 || m > 59) return;
            if (s < 0 || s > 59) return;
            Hour = h; Minute = m; Second = s;
            */
            if (validTime(h, m, s))
            {
                Hour = h; Minute = m; Second = s;
            }
        }

        public void setTime(int h, int m)
        {
            /*
            if (h < 0 || h > 23) return;
            if (m < 0 || m > 59) return;
            Hour = h; Minute = m; Second = 0;
            */
            if (validTime(h, m, 0))
            {
                Hour = h; Minute = m; Second = 0;
            }
        }

        private bool validTime(int h, int m, int s)
        {
            if (h < 0 || h > 23) return false;
            if (m < 0 || m > 59) return false;
            if (s < 0 || s > 59) return false;
            return true;  // 合法資料 
        }

        public string getTime()
        {
            return Hour + ":" + Minute + ":" + Second;
        }

        // property
        public int mHour
        {
            get { return Hour; }
            set
            {
                if (value < 0 || value > 23) return;
                Hour = value;
            }
        }
        public int mMinute
        {
            get { return Minute; }
            set
            {
                if (value < 0 || value > 59) return;
                Minute = value;
            }
        }
        public int mSecond
        {
            get { return Second; }
            set
            {
                if (value < 0 || value > 59) return;
                Second = value;
            }
        }

        ~MyTime()
        { //不可加上public
            //MessageBox.Show("*** 物件已釋放 ***"); //測試用
        } // 必須Using System.Windows.Forms;

    }
}
