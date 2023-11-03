

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import org.mozilla.javascript.Context;
import org.mozilla.javascript.Scriptable;


public class RhinoTest
{
    public static void main(String[] args)
    {
        /* 建立一個Javascript的上下文環境，用來儲存Javascript的環境資訊 */
        Context cx = Context.enter();
        try {
            /* 初始化Javascript標準對像（例如Object, Function, Array等） */
            Scriptable scope = cx.initStandardObjects();
 
            /* 讀取一個.js檔案 */
            String script = "";
            File file = null;
            if(args.length > 0)
            {
                file = new File(args[0]);  // 如果有參數，則讀入第一個參數中指定的js檔案
            }
            else
            {
                file = new File("script.js"); // 如果沒有參數，則讀入script.js
            }
            BufferedReader in = new BufferedReader(new FileReader(file));
            String s = "";
            while((s = in.readLine()) != null)
            {
                script += s + "\n";
            }
 
            /* 執行程式碼 */
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

