using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 数值工厂
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenNumberFactory : TokenFactory
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
            int intIndexCurrent = Index;//指向后一个字符
            bool blnContinue = true;
            char chrTemp;
            string strTempWord;

            while (blnContinue && intIndexCurrent < Code.Length)
            {
                chrTemp = Code[intIndexCurrent];
                if (char.IsDigit(chrTemp) || chrTemp.Equals('.'))
                {
                    intIndexCurrent += 1;
                }
                else
                {
                    blnContinue = false;
                }
            }//while

            strTempWord = Code.Substring(Index, intIndexCurrent - Index);//取得临时字符串
            TokenRecord Token = ProduceToken(strTempWord, Index);
            TokenList.Add(Token);

            Index = intIndexCurrent - 1;//指针移到当前指针的前一位，然后赋值给循环指针
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
            TokenRecord Token = new TokenValue(Index + 1, TokenWord.Length);
            Token.TokenValueType = typeof(double);
            double dblValue;

            if (double.TryParse(TokenWord, out dblValue))
            {
                Token.TokenValue = dblValue;
            }
            else
            {
                throw new SyntaxException(Index, TokenWord.Length, "表达式 " + TokenWord + " 无法转换成数值。");
            }

            return Token;
        }//ProduceToken
    }//class TokenNumberFactory
}//namespace


