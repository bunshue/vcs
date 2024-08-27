using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Thread_Example3
{
    class ChangeTime
    {

        private Form1 form;

        private Boolean state = true;


        private int h;
        private int m;
        private int s;

        public ChangeTime(Form1 form1)
        {
            this.form = form1;
            //設定預設的起始時間
            DateTime date = DateTime.Now;
            h = date.Hour;
            m = date.Minute;
            s = date.Second;
        }

        //停止thread,在fomr Dispose時要把thread也設定關掉
        public void stop()
        {
            state = false;
        }

        public void run()
        {
            while (state)
            {
                s++;
                if (s / 60 == 1)
                {
                    s = s - 60;
                    m++;
                    if (m / 60 == 1)
                    {
                        m = m - 60;
                        h++;
                        if (h / 24 == 1)
                        {
                            h = h - 24;
                        }
                    }
                }

                //一定要使用form裡的thread才可以變動form上的元件內容，其它thread更動時會有問題
                //利用invoke來執行form的thread
                if (state)//如果已經Dispose掉了就不再invoke了
                {
                    form.Invoke(new Form1.InvokeFunction(form.setTime), new object[] { h, m, s });
                }
                //一秒執行一次
                System.Threading.Thread.Sleep(1000);//停一秒
            }
        }
    }
}

