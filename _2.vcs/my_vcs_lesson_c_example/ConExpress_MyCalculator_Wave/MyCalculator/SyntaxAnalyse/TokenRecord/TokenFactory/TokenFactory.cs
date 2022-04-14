using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;

namespace ConExpress.Calculator
{
    internal class TokenFactory
    {

        #region 更新记录
        //Date:2008-6-12; Author:Alex Leo;
        //Remark:将从XML文件中加载操作记号的方法合并到这里

        #endregion

        /// <summary>
        /// 产生记号对象
        /// </summary>
        /// <param name="TokenWord">记号对应的字符串</param>
        /// <param name="Index">记号开始的列序号</param>
        /// <returns>记号对象</returns>
        protected static TokenRecord ProduceToken(string TokenWord, int Index)
        {
            throw new Exception("必须在子类中实现方法");
        }

        /// <summary>
        /// 词法分析
        /// </summary>
        /// <param name="TokenList">记号对象列表</param>
        /// <param name="VariableDic">变量字典</param>
        /// <param name="Code">表达式</param>
        /// <param name="Index">列序号</param>
        public static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            char chrTemp;//临时字符

            for (int intIndex = 0; intIndex < Code.Length; intIndex++)
            {
                chrTemp = Code[intIndex];//获取当前字符

                //关键字分析
                if (char.IsLetter(chrTemp))//如果当前字符为字母，进行关键字处理
                {
                     TokenKeywordFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (chrTemp.Equals('\'') || chrTemp.Equals('"'))//如果是字符串分隔符，进行字符串处理
                {
                    TokenStringFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (char.IsDigit(chrTemp))//数值处理
                {
                    TokenNumberFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (TokenSymbolFactory.SymbolDictionary.ContainsKey(chrTemp.ToString()))//运算符处理
                {
                    //有些运算符为双字符，但这里所有的双字符运算符的前一个字符都有对应的单字符运算符，可以只考虑一个字符
                    TokenSymbolFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (chrTemp.Equals(' '))
                {
                    //如果是空格，则忽略不处理
                }
                else//错误处理
                {
                    //抛出错误
                    throw new SyntaxException(intIndex, 1, "包含不合法字符：" + chrTemp.ToString());
                }
            }//for
        }//LexicalAnalysis

        /// <summary>
        /// 获取操作记号字典
        /// </summary>
        /// <param name="ClassDictionary">类字典，Key为关键字，Value为类名</param>
        /// <param name="RemarkDictionary">注释字典，Key为关键字，Value为注释信息</param>
        /// <param name="OperateTokenType">操作记号类型</param>
        /// <returns>操作记号字典</returns>
        /// <remarks>Author:Alex Leo; Date:2008-5-19; Remark:基于本地文件TokenRecord.xml;</remarks>
        internal static void GetOperateTokenDictionary(SortedDictionary<string, string> ClassDictionary, SortedDictionary<string, string> RemarkDictionary, OperateTokenTypeEnum OperateTokenType)
        {
            //SortedDictionary<string, string> myDictionary = new SortedDictionary<string, string>();
            ClassDictionary = ClassDictionary == null ? new SortedDictionary<string,string>() :ClassDictionary;
            RemarkDictionary = RemarkDictionary==null?new SortedDictionary<string,string>() : RemarkDictionary;

            if (ClassDictionary.Count == 0)
            {
                XmlDocument myDoc = new XmlDocument();
                myDoc.Load("../../xml/TokenRecord.xml");
                XmlNodeList KeywordList = myDoc.SelectNodes(string.Format("TokenRecord/{0}/Token", 
                    Enum.GetName(typeof(OperateTokenTypeEnum),OperateTokenType)));

                foreach (XmlNode Node in KeywordList)
                {
                    ClassDictionary.Add(Node.Attributes["Word"].Value, Node.Attributes["Class"].Value);
                    RemarkDictionary.Add(Node.Attributes["Word"].Value, Node.Attributes["Example"].Value);
                }
            }

            //return myDictionary;
        }//GetOperateTokenDictionary

    }//class TokenFactory
}//namespace
