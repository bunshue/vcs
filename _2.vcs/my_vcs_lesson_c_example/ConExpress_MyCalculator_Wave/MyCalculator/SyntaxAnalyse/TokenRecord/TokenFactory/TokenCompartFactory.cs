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

            //判断是否是关键字
            if (GetCompartList().Contains(TokenWord.ToLower()))
            {
                //是关键字
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
                        throw new Exception(string.Format("语法错误，列{0}，未知表达式：{1}。", Index.ToString(), TokenWord));
                }
            }
            else
            {
                //错误字符串，抛出错误，语法错误
                throw new Exception(string.Format("语法错误，列{0}，未知表达式：{1}。", Index.ToString(), TokenWord));
            }

            return Token;
        }//ProduceToken
    }
}