using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UnilateralismChainTable;

namespace Alignment
{
    /// <summary>
    /// 隊列類
    /// </summary>

    public class CQueue
    {
        private Clist m_List;

        public CQueue()
        {
            //構造函數

            //這裡使用到前面編寫的List 
            m_List = new Clist();

        }
        /// <summary>
        /// 入隊
        /// </summary>
        public void EnQueue(int DataValue)
        {
            //功能：加入隊列，這裡使用List 類的Append 方法：

            //尾部新增數據，數據個數加1

            m_List.Append(DataValue);
        }

        /// <summary>
        /// 出隊
        /// </summary>

        public int DeQueue()
        {
            //功  能：出隊

            //傳回值： 2147483647 表示為空隊列無傳回

            int QueValue;

            if (!IsNull())
            {
                //不為空的隊列

                //移動到隊列的頭

                m_List.MoveFrist();

                //取得目前的值

                QueValue = m_List.GetCurrentValue();

                //刪除出隊的數據

                m_List.Delete();

                return QueValue;

            }
            return 2147483647;
        }

        /// <summary>
        /// 判斷隊列是否為空
        /// </summary>

        public bool IsNull()
        {
            //功能：判斷是否為空的隊列

            return m_List.IsNull();

        }

        /// <summary>
        /// 清空隊列
        /// </summary>

        public void Clear()
        {
            //清空鏈表
            m_List.Clear();
        }
        /// <summary>
        /// 取得隊列的數據個數
        /// </summary>
        public int QueueCount
        {
            get
            {
                //取得隊列的個數
                return m_List.ListCount;
            }
        }

    }
}
