using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// �ַ�������
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenStringFactory : TokenFactory
    {
        /// <summary>
        /// �ʷ�����
        /// </summary>
        /// <param name="TokenList">�ǺŶ����б�</param>
        /// <param name="Code">Դ���ʽ</param>
        /// <param name="Index">�������</param>
        /// <remarks>Author:Alex Leo</remarks>
        public new static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            string strQuotationMark = Code.Substring(Index, 1);//���ţ������ǵ����ţ�Ҳ������˫����
            int intIndexCurrent = Index + 1;//ָ���һ���ַ�
            string strTempChar = "";//��ʱ�ַ�
            StringBuilder strTempWord = new StringBuilder();//��ʱ�ַ���
            bool blnContinue = true;

            while (blnContinue && intIndexCurrent < Code.Length)//ѭ��ֱ����־λ��False�򳬳�����
            {
                strTempChar = Code.Substring(intIndexCurrent, 1);

                if (strTempChar.Equals(strQuotationMark))//������ַ����ָ���
                {
                    if ((intIndexCurrent < Code.Length - 1)
                        && Code.Substring(intIndexCurrent + 1, 1).Equals(strQuotationMark))//������滹�����ţ������ת�壬����������ת��Ϊһ�������ַ�
                    {
                        strTempWord.Append(strQuotationMark);//���һ�������ַ�����ʱ�ַ�����
                        intIndexCurrent += 2;//�������λ
                    }
                    else
                    {
                        blnContinue = false;//�����ַ����������ţ��˳�
                    }
                }
                else
                {
                    strTempWord.Append(strTempChar);//��ӵ�ǰ�ַ�����ʱ�ַ�����
                    intIndexCurrent += 1;//�����һλ
                }//if
            }//while

            TokenRecord Token = ProduceToken(strTempWord.ToString(), Index);
            TokenList.Add(Token);
            Index = intIndexCurrent;//ָ���Ƶ���ǰָ�룬���ַ�����������
        }//LexicalAnalysis

        /// <summary>
        /// �����ǺŶ���
        /// </summary>
        /// <param name="TokenWord">�����õ��ĵ���</param>
        /// <param name="Index">��ǰ���</param>
        /// <returns>�ǺŶ���</returns>
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