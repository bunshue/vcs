

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import org.mozilla.javascript.Context;
import org.mozilla.javascript.Scriptable;


public class RhinoTest
{
    public static void main(String[] args)
    {
        /* �إߤ@��Javascript���W�U�����ҡA�Ψ��x�sJavascript�����Ҹ�T */
        Context cx = Context.enter();
        try {
            /* ��l��Javascript�зǹﹳ�]�ҦpObject, Function, Array���^ */
            Scriptable scope = cx.initStandardObjects();
 
            /* Ū���@��.js�ɮ� */
            String script = "";
            File file = null;
            if(args.length > 0)
            {
                file = new File(args[0]);  // �p�G���ѼơA�hŪ�J�Ĥ@�ӰѼƤ����w��js�ɮ�
            }
            else
            {
                file = new File("script.js"); // �p�G�S���ѼơA�hŪ�Jscript.js
            }
            BufferedReader in = new BufferedReader(new FileReader(file));
            String s = "";
            while((s = in.readLine()) != null)
            {
                script += s + "\n";
            }
 
            /* ����{���X */
            cx.evaluateString(scope, script, "[" + file.getName() + "]", 1, null);
        }
        catch (Exception ex)
        {
            ex.printStackTrace();
        }
        finally
        {
            Context.exit();
        }
    }
}

