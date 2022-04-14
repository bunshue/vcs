using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.Reflection;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 运算符工厂
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenSymbolFactory : TokenFactory
    {

        private static SortedDictionary<string, string> m_DictionarySymbol = new SortedDictionary<string, string>();
        /// <summary>
        /// 运算符字典
        /// </summary>
        /// <returns>运算符字典</returns>
        /// <remarks>Author:Alex Leo; Date:2008-5-19;</remarks>
        internal static SortedDictionary<string, string> SymbolDictionary
        {
            get
            {
                if (m_DictionarySymbol.Count == 0)

                    TokenFactory.GetOperateTokenDictionary(m_DictionarySymbol, m_DictionarySymbolRemark, OperateTokenTypeEnum.TokenSymbol);
                return m_DictionarySymbol;
            }
        }

        private static SortedDictionary<string, string> m_DictionarySymbolRemark = new SortedDictionary<string, string>();
        /// <summary>
        /// 运算符注释字典
        /// </summary>
        internal static SortedDictionary<string, string> SymbolRemarkDictionary
        {
            get 
            {
                if (m_DictionarySymbolRemark.Count == 0)
                    TokenFactory.GetOperateTokenDictionary(m_DictionarySymbol, m_DictionarySymbolRemark, OperateTokenTypeEnum.TokenSymbol);
                return TokenSymbolFactory.m_DictionarySymbolRemark; 
            }
        }


        /// <summary>
        /// 词法分析
        /// </summary>
        /// <param name="TokenList">记号对象列表</param>
        /// <param name="Code">源表达式</param>
        /// <param name="Index">分析序号</param>
        /// <remarks>Author:Alex Leo</remarks>
        public new static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            string strTempWord;
            if ((Index < Code.Length - 1) && SymbolDictionary.ContainsKey(Code.Substring(Index, 2)))//如果是双字节操作符
            {
                strTempWord = Code.Substring(Index, 2);
                Index += 1;//指针后移一位
            }
            else
            {
                strTempWord = Code.Substring(Index, 1);
            }

            TokenRecord Token = ProduceToken(strTempWord, Index);
            TokenList.Add(Token);
        }

        /// <summary>
        /// 产生记号对象
        /// </summary>
        /// <param name="TokenWord">分析得到的单词</param>
        /// <param name="Index">当前序号</param>
        /// <returns>记号对象</returns>
        /// <remarks>Author:Alex Leo</remarks>
        protected new static TokenRecord ProduceToken(string TokenWord, int Index)
        {
            TokenRecord Token;

            if (SymbolDictionary.ContainsKey(TokenWord.ToLower()))
            {
                string strFullClassName = "ConExpress.Calculator." + SymbolDictionary[TokenWord.ToLower()];
                Type TokenType = Type.GetType(strFullClassName);
                Token = (TokenRecord)Activator.CreateInstance(TokenType, new object[] { Index, TokenWord.Length });
            }
            else
            {
                //错误字符串，抛出错误，语法错误
                throw new SyntaxException(Index, TokenWord.Length, "未知表达式：" + TokenWord);
            }

            return Token;
        }//ProduceToken
    }//class TokenSymbolFactory
}//namespace
