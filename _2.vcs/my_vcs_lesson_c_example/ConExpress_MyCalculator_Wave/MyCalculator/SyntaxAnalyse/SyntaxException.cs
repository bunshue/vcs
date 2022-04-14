using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// �﷨�����࣬���ڷ�������ʱ��ʾ�û���ѡ�д���Ĳ�����
    /// </summary>
    /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
    public class SyntaxException : Exception
    {
        private int m_Index;
        /// <summary>
        /// �����к�
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
        public int Index
        {
            get { return m_Index; }
        }

        private int m_Length;
        /// <summary>
        /// �������������
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-5-21;</remarks>
        public int Length
        {
            get { return m_Length; }
        }

        private string m_Message;
        /// <summary>
        /// ������Ϣ
        /// </summary>
        public override string Message
        {
            get { return m_Message; }
        }

        /// <summary>
        /// ���캯��
        /// </summary>
        /// <param name="Index">���󴦵��кţ����ڴ���ʱȷ�������������ʼλ�ã�</param>
        /// <param name="Length">������������ȣ����ڴ���ʱѡ�����������ĳ��ȣ�</param>
        /// <param name="ErrorInformation">������Ϣ</param>
        public SyntaxException(int Index, int Length, string ErrorInformation)
        {
            this.m_Index = Index;
            this.m_Length = Length;
            this.m_Message = ErrorInformation;
        }

    }
}
