using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 字符串工厂
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenStringFactory : TokenFactory
    {
        /// <summary>
        /// 词法分析
        /// </summary>
        /// <param name="TokenList">记号对象列表</param>
        /// <param name="Code">源表达式</param>
        /// <param name="Index">分析序号</param>
        /// <remarks>Author:Alex Leo</remarks>
        public new static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            string strQuotationMark = Code.Substring(Index, 1);//引号，可以是单引号，也可以是双引号
            int intIndexCurrent = Index + 1;//指向后一个字符
            string strTempChar = "";//临时字符
            StringBuilder strTempWord = new StringBuilder();//临时字符串
            bool blnContinue = true;

            while (blnContinue && intIndexCurrent < Code.Length)//循环直到标志位置False或超出长度
            {
                strTempChar = Code.Substring(intIndexCurrent, 1);

                if (strTempChar.Equals(strQuotationMark))//如果是字符串分隔符
                {
                    if ((intIndexCurrent < Code.Length - 1)
                        && Code.Substring(intIndexCurrent + 1, 1).Equals(strQuotationMark))//如果后面还是引号，则进行转义，将两个引号转义为一个引号字符
                    {
                        strTempWord.Append(strQuotationMark);//添加一个引号字符到临时字符串中
                        intIndexCurrent += 2;//向后移两位
                    }
                    else
                    {
                        blnContinue = false;//遇到字符串结束引号，退出
                    }
                }
                else
                {
                    strTempWord.Append(strTempChar);//添加当前字符到临时字符串中
                    intIndexCurrent += 1;//向后移一位
                }//if
            }//while

            TokenRecord Token = ProduceToken(strTempWord.ToString(), Index);
            TokenList.Add(Token);
            Index = intIndexCurrent;//指针移到当前指针，即字符串结束引号
        }//LexicalAnalysis

        /// <summary>
        /// 产生记号对象
        /// </summary>
        /// <param name="TokenWord">分析得到的单词</param>
        /// <param name="Index">当前序号</param>
        /// <returns>记号对象</returns>
        /// <remarks>Author:Alex Leo</remarks>
        public new static TokenRecord ProduceToken(string TokenWord, int Index)
        {
            TokenRecord Token = new TokenValue(Index, TokenWord.Length);
            Token.TokenValue = TokenWord;
            Token.TokenValueType = typeof(string);
            return Token;
        }
    }//class TokenStringFactory
}//namespace