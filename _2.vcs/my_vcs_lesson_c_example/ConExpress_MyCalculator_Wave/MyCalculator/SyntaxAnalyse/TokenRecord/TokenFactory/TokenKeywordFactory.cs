using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.Reflection;

namespace ConExpress.Calculator
{
    /// <summary>
    /// �ؼ��ֹ���
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    internal class TokenKeywordFactory : TokenFactory
    {
        private static SortedDictionary<string, string> m_DictionaryKeyword = new SortedDictionary<string, string>();
        /// <summary>
        /// �ؼ����ֵ�
        /// </summary>
        /// <returns>�ؼ����ֵ�</returns>
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
        /// �ؼ���ע���ֵ�
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
        /// �ʷ�����
        /// </summary>
        /// <param name="TokenList">�ǺŶ����б�</param>
        /// <param name="Code">Դ���ʽ</param>
        /// <param name="Index">�������</param>
        /// <remarks>Author:Alex Leo</remarks>
        public static new void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            int intIndexCurrent = Index;//��ǰ���
            bool blnContinue = true;
            //string strTempChar = "";//��ȡ��ʱ�ַ�
            char chrTemp;
            string strTempWord = "";//��ȡ��ʱ�ַ���

            while (blnContinue && intIndexCurrent < Code.Length)
            {
                chrTemp = Code[intIndexCurrent];
                //�ؼ���֧�ִ�Сд��ĸ�����֣��������������ֿ�ͷ
                if (char.IsLetter(chrTemp) || char.IsDigit(chrTemp))
                {
                    intIndexCurrent += 1;//�ѵ�ǰ��ź���
                }
                else
                {
                    blnContinue = false;
                }
            }

            strTempWord = Code.Substring(Index, intIndexCurrent - Index);//��ȡ��ʱ��
            TokenRecord Token = ProduceToken(strTempWord.ToLower(), Index);
            TokenList.Add(Token);

            Index = intIndexCurrent - 1;//����ָ�뵽��ȡ����λ��
        }

        /// <summary>
        /// �����ǺŶ���
        /// </summary>
        /// <param name="TokenWord">�����õ��ĵ���</param>
        /// <param name="Index">��ǰ���</param>
        /// <returns>�ǺŶ���</returns>
        /// <remarks>Author:Alex Leo</remarks>
        protected static new TokenRecord ProduceToken(string TokenWord, int Index)
        {
            TokenRecord Token;

            if (KeywordDictionary.ContainsKey(TokenWord.ToLower()))
            {
                string strFullClassName = "ConExpress.Calculator." + KeywordDictionary[TokenWord];
                Type TokenType = Type.GetType(strFullClassName);
                Token = (TokenRecord)Activator.CreateInstance(TokenType, new object[] { Index, TokenWord.Length });
                //�Գ��������⴦��
                switch (TokenWord.ToLower())
                {
                    case "pi"://����Ϊ�����ǺŶ���
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
                ////�����ַ������׳������﷨����
                //throw new SyntaxException(Index, TokenWord.Length, "δ֪���ʽ��" + TokenWord);

                //�ı���ǰ�ķ�������δ֪������Ϊ�Զ������ı���
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