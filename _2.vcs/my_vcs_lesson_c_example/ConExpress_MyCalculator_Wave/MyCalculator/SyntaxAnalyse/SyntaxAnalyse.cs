using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    //Author: Alex Leo
    //Email: alexleo321@hotmail.com
    //Blog: http://www.cnblogs.com/conexpress/


    //更新日志
    //Date:2008-4-24; Author:Alex Leo;
    //Remark:將語法分析的單個方法進行重構，提出多個方法
    //Remark:對字符串的處理更靈活，可以接受單引號和雙引號，和HTML一樣，同時對于兩個字符串標識符進行轉義
    //Date:2009-5-21; Author:Alex Leo;
    //Remark:實現變量，將min和max的操作數修改為不限制個數（但必須大于1）
    //Remark:新增Sum和Avg方法

    /// <summary>
    /// 表達式分析計算類，功能入口
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    public class SyntaxAnalyse
    {
        /// <summary>
        /// 構造函數
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2007-8-2</remarks>
        public SyntaxAnalyse()
        { }

        internal static Dictionary<string, TokenValue> DicVariable = new Dictionary<string, TokenValue>();//變量字典（新增）

        /// <summary>
        /// 分析語句并返回記號記錄對象
        /// </summary>
        /// <param name="Code">運算表達式</param>
        /// <returns>頂級TokenRecord對象</returns>
        public TokenRecord Analyse(string Code)
        {
            if (Code.Trim().Equals(string.Empty))
            {
                return new TokenValue(0, 1);
            }

            List<TokenRecord> ListToken = new List<TokenRecord>();//TokenRecord列表

            int intIndex = 0;
            TokenFactory.LexicalAnalysis(ListToken, Code, ref intIndex);//詞法分析，將代碼轉換為TokenRecord列表

            //語法樹分析，將Token列表按優先級轉換為樹
            TokenRecord TokenTop = SyntaxTreeAnalyse.SyntaxTreeGetTopTokenAnalyse(ListToken, 0, ListToken.Count - 1);
            TokenTop.Execute();
            return TokenTop;
        }
    }
}