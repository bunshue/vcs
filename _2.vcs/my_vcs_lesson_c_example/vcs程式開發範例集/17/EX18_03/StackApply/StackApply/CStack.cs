using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UnilateralismChainTable;

namespace StackApply
{
    public class CStack
    {
        //呼叫鏈表類
        private Clist m_List;

        public CStack()
        {
            //構造函數
            m_List = new Clist();

        }
        /// <summary>
        /// 壓入堆棧
        /// </summary>
        public void Push(int PushValue)
        {
            //參數： int PushValue 壓入堆棧的數據
            m_List.Append(PushValue);

        }
        /// <summary>
        /// 彈出堆棧數據,如果為空，則取得 2147483647 為 int 的最大值；
        /// </summary>

        public int Pop()
        {
            //功能：彈出堆棧數據 
            int PopValue;

            if (!IsNullStack())
            {
                //不為空堆棧
                //移動到頂
                MoveTop();
                //取得彈出的數據
                PopValue = GetCurrentValue();
                //刪除
                Delete();
                return PopValue;
            }
            //  空的時候為 int 類型的最大值
            return 2147483647;
        }
        /// <summary>
        /// 判斷是否為空的堆棧
        /// </summary>
        public bool IsNullStack()
        {
            if (m_List.IsNull())
                return true;
            return false;
        }
        /// <summary>
        /// 堆棧的個數
        /// </summary>
        public int StackListCount
        {
            get
            {
                return m_List.ListCount;
            }

        }

        /// <summary>
        /// 移動到堆棧的底部
        /// </summary>
        public void MoveBottom()
        {
            m_List.MoveFrist();
        }

        /// <summary>
        /// 移動到堆棧的Top
        /// </summary>
        public void MoveTop()
        {
            m_List.MoveLast();
        }
        /// <summary>
        /// 向上移動
        /// </summary>

        public void MoveUp()
        {
            m_List.MoveNext();
        }
        /// <summary>
        /// 向上移動
        /// </summary>

        public void MoveDown()
        {
            m_List.MovePrevious();
        }
        /// <summary>
        /// 取得目前的值
        /// </summary>

        public int GetCurrentValue()
        {
            return m_List.GetCurrentValue();
        }
        /// <summary>
        /// 刪除取得目前的結點
        /// </summary>

        public void Delete()
        {
            m_List.Delete();
        }
        /// <summary>
        /// 清空堆棧
        /// </summary>
        public void Clear()
        {
            m_List.Clear();
        }
    }
}
