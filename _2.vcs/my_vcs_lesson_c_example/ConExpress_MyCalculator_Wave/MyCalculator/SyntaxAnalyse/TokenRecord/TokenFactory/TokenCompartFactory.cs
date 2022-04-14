using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    class TokenCompartFactory : TokenFactory
    {
        private static string[] c_ArrayCompart = new string[] { "(", ")", "," };
        private static List<string> c_ListCompart = new List<string>();

        public static List<string> GetCompartList()
        { 
            if (c_ListCompart.Count == 0)
            {
                c_ListCompart.AddRange(c_ArrayCompart);
            }

            return c_ListCompart;
        }

        public new static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            TokenRecord Token = ProduceToken(Code.Substring(Index, 1), Index);
            TokenList.Add(Token);
        }

        public new static TokenRecord ProduceToken(string TokenWord, int Index)
        {
            TokenRecord Token;

            //�ж��Ƿ��ǹؼ���
            if (GetCompartList().Contains(TokenWord.ToLower()))
            {
                //�ǹؼ���
                switch (TokenWord.ToLower())
                {
                    case "(":
                        Token = new TokenLeftBracket(Index + 1);
                        break;
                    case ")":
                        Token = new TokenRightBracket(Index + 1);
                        break;
                    case ",":
                        Token = new TokenComma(Index + 1);
                        break;
                    default:
                        throw new Exception(string.Format("�﷨������{0}��δ֪���ʽ��{1}��", Index.ToString(), TokenWord));
                }
            }
            else
            {
                //�����ַ������׳������﷨����
                throw new Exception(string.Format("�﷨������{0}��δ֪���ʽ��{1}��", Index.ToString(), TokenWord));
            }

            return Token;
        }//ProduceToken
    }
}