using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.Reflection;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 关键字工厂
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    internal class TokenKeywordFactory : TokenFactory
    {
        private static SortedDictionary<string, string> m_DictionaryKeyword = new SortedDictionary<string, string>();
        /// <summary>
        /// 关键字字典
        /// </summary>
        /// <returns>关键字字典</returns>
        /// <remarks>Author:Alex Leo; Date:2008-5-19;</remarks>
        internal static SortedDictionary<string, string> KeywordDictionary
        {
            get
            {
                if (m_DictionaryKeyword.Count == 0)
                    TokenFactory.GetOperateTokenDictionary(m_DictionaryKeyword, m_DictionaryKeyWordRemark, OperateTokenTypeEnum.TokenKeyword);

                return m_DictionaryKeyword;
            }
        }

        private static SortedDictionary<string, string> m_DictionaryKeyWordRemark = new SortedDictionary<string, string>();
        /// <summary>
        /// 关键字注释字典
        /// </summary>
        public static SortedDictionary<string, string> KeyWordRemarkDictionary
        {
            get 
            {
                if(m_DictionaryKeyWordRemark.Count ==0)
                    TokenFactory.GetOperateTokenDictionary(m_DictionaryKeyword, m_DictionaryKeyWordRemark, OperateTokenTypeEnum.TokenKeyword);
                    
                return TokenKeywordFactory.m_DictionaryKeyWordRemark;
            }
        }


        /// <summary>
        /// 词法分析
        /// </summary>
        /// <param name="TokenList">记号对象列表</param>
        /// <param name="Code">源表达式</param>
        /// <param name="Index">分析序号</param>
        /// <remarks>Author:Alex Leo</remarks>
        public static new void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            int intIndexCurrent = Index;//当前序号
            bool blnContinue = true;
            //string strTempChar = "";//获取临时字符
            char chrTemp;
            string strTempWord = "";//获取临时字符串

            while (blnContinue && intIndexCurrent < Code.Length)
            {
                chrTemp = Code[intIndexCurrent];
                //关键字支持大小写字母及数字，但不允许以数字开头
                if (char.IsLetter(chrTemp) || char.IsDigit(chrTemp))
                {
                    intIndexCurrent += 1;//把当前序号后移
                }
                else
                {
                    blnContinue = false;
                }
            }

            strTempWord = Code.Substring(Index, intIndexCurrent - Index);//获取临时词
            TokenRecord Token = ProduceToken(strTempWord.ToLower(), Index);
            TokenList.Add(Token);

            Index = intIndexCurrent - 1;//设置指针到读取结束位置
        }

        /// <summary>
        /// 产生记号对象
        /// </summary>
        /// <param name="TokenWord">分析得到的单词</param>
        /// <param name="Index">当前序号</param>
        /// <returns>记号对象</returns>
        /// <remarks>Author:Alex Leo</remarks>
        protected static new TokenRecord ProduceToken(string TokenWord, int Index)
        {
            TokenRecord Token;

            if (KeywordDictionary.ContainsKey(TokenWord.ToLower()))
            {
                string strFullClassName = "ConExpress.Calculator." + KeywordDictionary[TokenWord];
                Type TokenType = Type.GetType(strFullClassName);
                Token = (TokenRecord)Activator.CreateInstance(TokenType, new object[] { Index, TokenWord.Length });
                //对常数的特殊处理
                switch (TokenWord.ToLower())
                {
                    case "pi"://以下为常量记号对象
                        Token.TokenValueType = typeof(double);
                        Token.TokenValue = Math.PI;
                        break;
                    case "e":
                        Token.TokenValueType = typeof(double);
                        Token.TokenValue = Math.E;
                        break;
                    case "true":
                        Token.TokenValueType = typeof(bool);
                        Token.TokenValue = true;
                        break;
                    case "false":
                        Token.TokenValueType = typeof(bool);
                        Token.TokenValue = false;
                        break;
                    default:
                        break;
                }
            }
            else
            {
                ////错误字符串，抛出错误，语法错误
                //throw new SyntaxException(Index, TokenWord.Length, "未知表达式：" + TokenWord);

                //改变以前的方法，将未知变量作为自动声明的变量
                if (!SyntaxAnalyse.DicVariable.ContainsKey(TokenWord))
                {
                    TokenValue temp = new TokenValue(Index, TokenWord.Length);
                    //temp.TokenValue = 0D;
                    //temp.TokenValueType = typeof(double);
                    SyntaxAnalyse.DicVariable.Add(TokenWord, temp);
                    Token = temp;
                }
                else
                {
                    Token = SyntaxAnalyse.DicVariable[TokenWord];
                }
            }

            return Token;
        }//ProduceToken
    }//class TokenKeywordFactory
}//namespace