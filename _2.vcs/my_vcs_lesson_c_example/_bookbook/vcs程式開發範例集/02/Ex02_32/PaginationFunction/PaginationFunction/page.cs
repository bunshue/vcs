using System;
using System.Collections.Generic;
using System.Text;
using System.Data;

namespace PaginationFunction
{
    class page
    {
        private int RowsPerPage = 5;//表示ItemsPerPage屬性的默認值
        private DataSet TempSet = new DataSet();//定義一個存儲數據的對象
        private int CurrentPage = 0;//表示當前處於第一頁
        /// <summary>
        /// 表示每頁顯示多少條記錄
        /// </summary>
        public int ItemsPerPage
        {
            get
            {
                return RowsPerPage;//返回當前頁顯示的多少數據
            }
            set
            {
                RowsPerPage = value;//設置當前頁顯示的數據數目
            }
        }

        public void SetDataSet(DataSet dataSet, out DataTable dataTable)
        {
            TempSet = dataSet;//向數據集中填充內容
            GoToPageNumber(1, out dataTable);//跳轉到第一頁
        }

        /// <summary>
        /// 跳轉到最後一頁
        /// </summary>
        #region GoToLastPage
        public void GoToLastPage(out DataTable pageTable)
        {
            GoToPageNumber(GetTotalPages(), out pageTable);//跳轉到最後一頁
        }
        #endregion

        /// <summary>
        /// 顯示當前頁的下一頁記錄，如果該頁不存在，則不做任何操作
        /// </summary>
        #region GoToNextPage
        public void GoToNextPage(out DataTable pageTable)
        {
            GoToPageNumber(CurrentPage + 1, out pageTable);//跳轉到當前頁的下一頁
        }
        #endregion

        /// <summary>
        /// Displays the first page.
        /// </summary>
        #region GoToFirstPage
        public void GoToFirstPage(out DataTable pageTable)
        {
            pageTable = null;//清空數據表中pageTable的記錄
            DataSet TempSubSet = new DataSet();//初始化一個存儲數據的數據集
            DataRow[] Rows = new DataRow[RowsPerPage];//聲明一個DataRow數組

            if (TempSet.Tables[0].Rows.Count < RowsPerPage && CurrentPage != 1)//如果數據集中的記錄總數不足一行則在第一行中顯示全部
            {
                Rows = new DataRow[TempSet.Tables[0].Rows.Count];//重新定義DataRow數組的長度
                for (int i = 0; i < TempSet.Tables[0].Rows.Count; i++)//循環遍歷數據集中的每一條記錄
                {
                    Rows[i] = TempSet.Tables[0].Rows[i];//為DataRow數組賦值
                }
                TempSubSet.Merge(Rows);//將當前的數據記錄添加進數據集
                pageTable = TempSubSet.Tables[0];//設定當前數據表的內容
            }

            if (TempSet.Tables[0].Rows.Count >= RowsPerPage && CurrentPage != 1)//當數據集中的數據記錄大於每頁顯示記錄數時
            {
                for (int i = 0; i < RowsPerPage; i++)//循環遍歷每頁顯示的數據數
                {
                    Rows[i] = TempSet.Tables[0].Rows[i];//為DataRow數組賦值
                }
                TempSubSet.Merge(Rows);//將當前數據添加進數據集
                pageTable = TempSubSet.Tables[0];//設定當前數據表中的內容
            }
            CurrentPage = 1;//設定當前處於第1頁

        }
        #endregion

        /// <summary>
        /// 顯示上一條記錄
        /// </summary>
        #region GoToPreviousPage
        public void GoToPreviousPage(out DataTable pageTable)
        {

            if (CurrentPage != 1)//當當前頁沒有處於第1頁時
            {
                GoToPageNumber(CurrentPage - 1, out pageTable);//返回當前頁的上一頁

            }
            else//當處於第1頁時
            {
                pageTable = null;//清空數據表中的內容
            }
        }
        #endregion

        /// <summary>
        /// 跳轉到某一頁，如果該頁不存在則什麼也不做
        /// </summary>
        /// <param name="n">當前顯示的頁數</param>
        #region GoToPageNumber
        public void GoToPageNumber(int n, out DataTable pageTable)
        {
            DataSet TempSubSet = new DataSet();//初始化一個數據集對像
            DataRow[] Rows = new DataRow[RowsPerPage];//定義一個存儲數據行的數組
            int AllPages = 0;//該變量表示所有頁數
            AllPages = GetTotalPages();//為AllPages變量賦值

            if ((n > 0) && (n <= AllPages))//當變量n處於有效值範圍內時
            {
                int PageIndex = (n - 1) * RowsPerPage;//設置頁索引的值
                if (PageIndex >= TempSet.Tables[0].Rows.Count)//當頁索引的值大於等於數據集中的所有記錄總數時
                {
                    GoToFirstPage(out pageTable);//返回到第一頁
                }
                else//當頁索引的值小於數據集中的所有記錄總數時
                {
                    int WholePages = TempSet.Tables[0].Rows.Count / RowsPerPage;//記錄當前數據集按指定的分頁方式分為多少頁
                    if ((TempSet.Tables[0].Rows.Count % RowsPerPage) != 0 && n == AllPages)//當變量n為總頁數且有些頁的數據不足時
                    {
                        Rows = new DataRow[TempSet.Tables[0].Rows.Count - (WholePages * RowsPerPage)];//表示不足一頁的記錄數
                    }
                    for (int i = 0, j = PageIndex; i < Rows.Length && j < TempSet.Tables[0].Rows.Count; j++, i++)//循環遍歷數據集中每一條記錄
                    {
                        Rows[i] = TempSet.Tables[0].Rows[j];//為數組Rows賦值
                    }
                    TempSubSet.Merge(Rows);//將不足一頁的數據附加到數據集中

                    CurrentPage = n;//設定當前處於第幾頁
                    pageTable = TempSubSet.Tables[0];//為pageTable賦值
                }
            }
            else//當變量n處於無效數據範圍內時
            {
                pageTable = null;//清空數據表中的內容
            }
        }
        #endregion

        /// <summary>
        /// 該方法用來獲取數據集分頁後的頁的總數
        /// </summary>
        /// <returns>返回當前數據集中按指定的顯示方式所具有的頁數 </returns>
        public int GetTotalPages()
        {
            if ((TempSet.Tables[0].Rows.Count % RowsPerPage) != 0)//當數據表中的行數除以每頁顯示的行數的餘數不為0時
            {
                int x = TempSet.Tables[0].Rows.Count / RowsPerPage;//記錄數據表中的所有行數除以每頁顯示的數據數
                return (x + 1);//返回該數據集所包含的所有頁數
            }
            else//當數據表中的行數剛好能正處每頁顯示的頁數時
            {
                return TempSet.Tables[0].Rows.Count / RowsPerPage;//返回兩者相除後的值
            }
        }
    }
}
