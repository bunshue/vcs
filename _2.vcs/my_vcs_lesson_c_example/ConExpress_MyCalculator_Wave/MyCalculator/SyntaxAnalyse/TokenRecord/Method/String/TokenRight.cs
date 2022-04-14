using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenRight : TokenStringMethod
    {
        public TokenRight(int Index, int Length)
            : base(Index, Length)
        { }
        public override void Execute()
        {
            this.CheckChildCount("right��������Ԫ���������Ϸ�");

            string strMid = string.Empty;
            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            TokenSource.ChangeTokenToString();

            TokenRecord TokenLength = this.ChildList[1];
            TokenLength.Execute();

            string strSource = TokenSource.ChangeTokenToString();
            int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("right���Ľ�ȡ�������ǺϷ�����"));

            //��鳤�ȵĺϷ��ԣ���û��Խ����Χ
            TokenLength.TokenValue = intLength < 1 ? 1 : intLength;
            TokenLength.TokenValue = intLength > strSource.Length ? strSource.Length : intLength;

            this.TokenValue = strSource.Substring(strSource.Length - intLength, intLength);

        }

    }
}
