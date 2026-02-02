// 動畫的類別
// 用來求出 關鍵格數 中間的 對應值
// 主程式要這樣使用
/*
G2D_Anim ani;
ani = new Anim(3, 5000, true, AnimType.AT_Step); // 三個關鍵值 總時間五秒 要重複播放 階層式的取值
ani = new Anim(3, 5000, true, AnimType.AT_Linear); // 或 三個關鍵值 總時間五秒 要重複播放 線性式的取值
ani.SetKeyValue(0, 0.0f, 0.0f); //第 0 個關鍵值  在 0.0f 比例時間的位置 值是 0
ani.SetKeyValue(1, 0.5f, 3.0f); //第 1 個關鍵值  在 0.5f 比例時間的位置 值是 3
ani.SetKeyValue(2, 1.0f, 0.0f); //第 2 個關鍵值  在 1.0f 比例時間的位置 值是 0 
ani.BeginAnimation();  // 開始計時
ani.GetValue()         // 依據目前的時間 取回 對應值
 * */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace vcs_Draw5_Image_ImageAttributes
{
    enum AnimType { AT_Step, AT_Linear} ; // 動畫種類  階層、線性
    class G2D_Anim  
    {
        int m_duration; // 動畫的長度(千分秒數)
        bool m_isLoop = true;  // 是否要重複播放
        PointF[] m_pt;  // 關鍵影格陣列 (X, Y) = (keyPos, KeyValue)
        DateTime m_start = DateTime.MinValue; // 開始的時間
        AnimType m_AT; // 動畫種類
        bool m_pause =  false;		// 是否暫停 中
        DateTime m_pauseTime;    // 暫停 當下的時間

        // KeyCount 關鍵格數，duration 動畫的長度(千分秒數)，isLoop 是否要重複播放
        public G2D_Anim(int KeyCount, int duration, bool isLoop, AnimType AT)  // 建構子
        {
            m_pt = new PointF[KeyCount]; // 關鍵影格陣列

            this.m_duration = duration;  // 總千分秒數
            this.m_isLoop = isLoop;
            this.m_AT = AT;
        }

        // 設定關鍵格數的比例位置與值： 關鍵格數 總長度的比例數 傳回值
        public void SetKeyValue(int keyNo, float keyPos, float KeyValue) 
        {
            if (keyNo < 0 || keyNo >= m_pt.Length) return;

            m_pt[keyNo].X = keyPos;
            m_pt[keyNo].Y = KeyValue;
        }

        public void BeginAnimation() // 動畫開始 儲存開始的時間 
        {
            m_start = DateTime.Now;
        }

        public float GetValue() // 依據當下的時間 計算出 對應的值 KeyValue
        {
            DateTime dt = DateTime.Now; // 當下的時間
            TimeSpan ts = dt - m_start; // 經過的時間
            double tm = ts.TotalMilliseconds; // 經過的時間的總千分秒數

            // 如果 不重複播放 而且 當下時刻又 大於 結束時刻，則傳回最後值
            if (!m_isLoop && tm > m_duration)
                return m_pt[m_pt.Length - 1].Y;

            tm = tm % m_duration; // 過濾掉 重複的週期

            float keyPos = (float)tm / (float)m_duration; // 計算出比例 0.0 ~ 1.0

            if ((1.0f - keyPos) < 0.001f) return m_pt[m_pt.Length - 1].Y; // 很接近 最後的時間
            if (keyPos < 0.001f) return m_pt[0].Y; // 很接近 最初的時間

            int index = 0;
            while (m_pt[index].X < keyPos)  // 找到比 keyPos 大的 pt[index].X
                index++;

            if (m_AT == AnimType.AT_Step) return m_pt[index - 1].Y; // 如果是階層式動畫種類 就傳回 比較小 的關鍵畫格的對應的值

            // 求出傾斜度(全體為1.0時的增減量)
            float diffValue = m_pt[index].Y - m_pt[index - 1].Y;// 關鍵畫格間的相減
            float diffPos = m_pt[index].X - m_pt[index - 1].X;	// 關鍵畫格之間的持續時間
            float slope = diffValue / diffPos;

            // 求出現在值
            float fPastFromPrev = keyPos - m_pt[index - 1].X;	 // 在這個區間經過的時間
            return slope * fPastFromPrev + m_pt[index - 1].Y;  // 在這個區間估計的現值
        }

        // 是否已經結束
        public bool isTimeup()
        {
            if (m_pause) return false;
            if (m_start == DateTime.MinValue) return false;

            DateTime dt = DateTime.Now; // 當下的時間
            TimeSpan ts = dt - m_start; // 經過的時間
            return (ts.TotalMilliseconds >= m_duration);
        }

        // 是否已經開始計時
        public bool isStarted()
        {
            return (m_start != DateTime.MinValue);
        }

        public void pause()         // 暫停
        {
            if (m_pause) return;

            m_pauseTime = DateTime.Now; // 當下的時間
            m_pause = true;
        }

        public void resume()        // 再繼續
        {
            if (!m_pause) return;
            DateTime dt = DateTime.Now; // 當下的時間 
            m_start = m_start + (dt - m_pauseTime);   // 調整開始的時間
            m_pause = false;
        }
    }
}
