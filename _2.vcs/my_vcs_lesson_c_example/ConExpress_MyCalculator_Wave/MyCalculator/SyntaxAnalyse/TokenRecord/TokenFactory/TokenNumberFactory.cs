using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// ��ֵ����
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    class TokenNumberFactory : TokenFactory
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
            int intIndexCurrent = Index;//ָ���һ���ַ�
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

            strTempWord = Code.Substring(Index, intIndexCurrent - Index);//ȡ����ʱ�ַ���
            TokenRecord Token = ProduceToken(strTempWord, Index);
            TokenList.Add(Token);

            Index = intIndexCurrent - 1;//ָ���Ƶ���ǰָ���ǰһλ��Ȼ��ֵ��ѭ��ָ��
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
            TokenRecord Token = new TokenValue(Index + 1, TokenWord.Length);
            Token.TokenValueType = typeof(double);
            double dblValue;

            if (double.TryParse(TokenWord, out dblValue))
            {
                Token.TokenValue = dblValue;
            }
            else
            {
                throw new SyntaxException(Index, TokenWord.Length, "���ʽ " + TokenWord + " �޷�ת������ֵ��");
            }

            return Token;
        }//ProduceToken
    }//class TokenNumberFactory
}//namespace


