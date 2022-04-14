using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.Reflection;

namespace ConExpress.Calculator
{
    /// <summary>
    /// ���������
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenSymbolFactory : TokenFactory
    {

        private static SortedDictionary<string, string> m_DictionarySymbol = new SortedDictionary<string, string>();
        /// <summary>
        /// ������ֵ�
        /// </summary>
        /// <returns>������ֵ�</returns>
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
        /// �����ע���ֵ�
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
        /// �ʷ�����
        /// </summary>
        /// <param name="TokenList">�ǺŶ����б�</param>
        /// <param name="Code">Դ���ʽ</param>
        /// <param name="Index">�������</param>
        /// <remarks>Author:Alex Leo</remarks>
        public new static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            string strTempWord;
            if ((Index < Code.Length - 1) && SymbolDictionary.ContainsKey(Code.Substring(Index, 2)))//�����˫�ֽڲ�����
            {
                strTempWord = Code.Substring(Index, 2);
                Index += 1;//ָ�����һλ
            }
            else
            {
                strTempWord = Code.Substring(Index, 1);
            }

            TokenRecord Token = ProduceToken(strTempWord, Index);
            TokenList.Add(Token);
        }

        /// <summary>
        /// �����ǺŶ���
        /// </summary>
        /// <param name="TokenWord">�����õ��ĵ���</param>
        /// <param name="Index">��ǰ���</param>
        /// <returns>�ǺŶ���</returns>
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
                //�����ַ������׳������﷨����
                throw new SyntaxException(Index, TokenWord.Length, "δ֪���ʽ��" + TokenWord);
            }

            return Token;
        }//ProduceToken
    }//class TokenSymbolFactory
}//namespace
