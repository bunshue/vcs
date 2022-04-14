using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;

namespace ConExpress.Calculator
{
    internal class TokenFactory
    {

        #region ���¼�¼
        //Date:2008-6-12; Author:Alex Leo;
        //Remark:����XML�ļ��м��ز����Ǻŵķ����ϲ�������

        #endregion

        /// <summary>
        /// �����ǺŶ���
        /// </summary>
        /// <param name="TokenWord">�ǺŶ�Ӧ���ַ���</param>
        /// <param name="Index">�Ǻſ�ʼ�������</param>
        /// <returns>�ǺŶ���</returns>
        protected static TokenRecord ProduceToken(string TokenWord, int Index)
        {
            throw new Exception("������������ʵ�ַ���");
        }

        /// <summary>
        /// �ʷ�����
        /// </summary>
        /// <param name="TokenList">�ǺŶ����б�</param>
        /// <param name="VariableDic">�����ֵ�</param>
        /// <param name="Code">���ʽ</param>
        /// <param name="Index">�����</param>
        public static void LexicalAnalysis(List<TokenRecord> TokenList, string Code, ref int Index)
        {
            char chrTemp;//��ʱ�ַ�

            for (int intIndex = 0; intIndex < Code.Length; intIndex++)
            {
                chrTemp = Code[intIndex];//��ȡ��ǰ�ַ�

                //�ؼ��ַ���
                if (char.IsLetter(chrTemp))//�����ǰ�ַ�Ϊ��ĸ�����йؼ��ִ���
                {
                     TokenKeywordFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (chrTemp.Equals('\'') || chrTemp.Equals('"'))//������ַ����ָ����������ַ�������
                {
                    TokenStringFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (char.IsDigit(chrTemp))//��ֵ����
                {
                    TokenNumberFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (TokenSymbolFactory.SymbolDictionary.ContainsKey(chrTemp.ToString()))//���������
                {
                    //��Щ�����Ϊ˫�ַ������������е�˫�ַ��������ǰһ���ַ����ж�Ӧ�ĵ��ַ������������ֻ����һ���ַ�
                    TokenSymbolFactory.LexicalAnalysis(TokenList, Code, ref intIndex);
                }
                else if (chrTemp.Equals(' '))
                {
                    //����ǿո�����Բ�����
                }
                else//������
                {
                    //�׳�����
                    throw new SyntaxException(intIndex, 1, "�������Ϸ��ַ���" + chrTemp.ToString());
                }
            }//for
        }//LexicalAnalysis

        /// <summary>
        /// ��ȡ�����Ǻ��ֵ�
        /// </summary>
        /// <param name="ClassDictionary">���ֵ䣬KeyΪ�ؼ��֣�ValueΪ����</param>
        /// <param name="RemarkDictionary">ע���ֵ䣬KeyΪ�ؼ��֣�ValueΪע����Ϣ</param>
        /// <param name="OperateTokenType">�����Ǻ�����</param>
        /// <returns>�����Ǻ��ֵ�</returns>
        /// <remarks>Author:Alex Leo; Date:2008-5-19; Remark:���ڱ����ļ�TokenRecord.xml;</remarks>
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
