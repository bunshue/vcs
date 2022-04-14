using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// Max�Ǻ��࣬���������нϴ��һ������Ӧ�ؼ���max�������ִ�Сд��
    /// </summary>
    /// <example>�÷�max(15,20)������20��</example>
    public class TokenMax : TokenArithmeticMethod
    {
        public TokenMax(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// ����¼�����
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (this.ChildList.Count < 2)
            {
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        private const string c_IsNotNumber = "Max�����Ĳ�������������";
        public override void Execute()
        {
            this.CheckChildCount("Max����������Ԫ���������Ϸ�");

            List<double> myList = new List<double>();
            foreach (TokenRecord item in this.ChildList)
            {
                item.Execute();
                myList.Add(item.ChangeTokenToDouble(c_IsNotNumber));
            }
            myList.Sort();

            this.TokenValue = myList[myList.Count - 1];
        }
    }
}
