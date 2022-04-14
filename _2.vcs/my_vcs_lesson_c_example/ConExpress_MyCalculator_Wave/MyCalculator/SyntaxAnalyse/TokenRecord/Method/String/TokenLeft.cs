using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// Left�Ǻ��࣬�ַ�����������Ӧ�ؼ���left�������ִ�Сд
    /// </summary>
    /// <example>�÷�left("hello world",5)������hello��</example>
    /// <remarks>�����ȡ����С��1����Ĭ��Ϊ1�������ȡ���ȴ����ַ������ȣ���Ĭ��Ϊ�ַ������ȡ�</remarks>
    public class TokenLeft : TokenStringMethod
    {
        public TokenLeft(int Index, int Length)
            : base(Index, Length)
        {
            this.TokenValueType = typeof(string);
        }

        public override void Execute()
        {
            this.CheckChildCount("left��������Ԫ���������Ϸ�");//check child token

            string strMid = string.Empty;
            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            string strSource = TokenSource.ChangeTokenToString();

            TokenRecord TokenLength = this.ChildList[1];
            TokenLength.Execute();
            int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("left���Ľ�ȡ�������ǺϷ�����"));

            //��鳤�ȵĺϷ��ԣ���û��Խ����Χ
            intLength = Convert.ToInt32(intLength) < 1 ? 1 : intLength;
            intLength = Convert.ToInt32(intLength) > strSource.Length ? strSource.Length : intLength;

            this.TokenValue = strSource.Substring(0, intLength);
        }
    }
}
