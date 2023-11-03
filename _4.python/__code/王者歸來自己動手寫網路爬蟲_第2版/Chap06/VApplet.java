

import java.awt.BorderLayout;
import java.awt.Choice;
import java.awt.Component;
import java.util.Vector; // JMF相關的類
import javax.media.CaptureDeviceInfo;
import javax.media.CaptureDeviceManager;
import javax.media.Format;
import javax.media.Manager;
import javax.media.MediaLocator;
import javax.media.Player;
import javax.media.format.VideoFormat;
import javax.swing.JPanel;
import javax.swing.JApplet;

public class VApplet extends JApplet {
	private JPanel jContentPane = null;
	private Choice choice = null;

	public VApplet() {
		super();
	}

	public void init() {
		this.setSize(320, 240);
		this.setContentPane(getJContentPane());
		this.setName("VApplet");
	}

	// 取系統所有可採集的硬件裝置列表
	private CaptureDeviceInfo[] getDevices() {
		Vector devices = CaptureDeviceManager.getDeviceList(null);
		CaptureDeviceInfo[] info = new CaptureDeviceInfo[devices.size()];
		for (int i = 0; i < devices.size(); i++) {
			info[i] = (CaptureDeviceInfo) devices.get(i);
		}
		return info;
	}

	// 從已知裝置中取所有視訊裝置的列表
	private CaptureDeviceInfo[] getVideoDevices() {
		CaptureDeviceInfo[] info = getDevices();
		CaptureDeviceInfo[] videoDevInfo;
		Vector vc = new Vector();
		for (int i = 0; i < info.length; i++) {
			// 取裝置支援的格式，如果有一個是視訊格式，則認為此裝置為視訊裝置
			Format[] fmt = info[i].getFormats();
			for (int j = 0; j < fmt.length; j++) {
				if (fmt[j] instanceof VideoFormat) {
					vc.add(info[i]);
				}
				break;
			}
		}
		videoDevInfo = new CaptureDeviceInfo[vc.size()];
		for (int i = 0; i < vc.size(); i++) {
			videoDevInfo[i] = (CaptureDeviceInfo) vc.get(i);
		}
		return videoDevInfo;
	}

	private JPanel getJContentPane() {
		if (jContentPane == null) {
			BorderLayout borderLayout = new BorderLayout();
			jContentPane = new JPanel();
			jContentPane.setLayout(borderLayout);

			MediaLocator ml = null;
			Player player = null;
			try {
				// 這裡我只有一個視訊裝置，直接取第一個
				// 取得目前裝置的MediaLocator
				ml = getVideoDevices()[0].getLocator();
				// 用已經取得的MediaLocator得到一個Player
				player = Manager.createRealizedPlayer(ml);
				player.start();
				// 取得Player的AWT Component
				Component comp = player.getVisualComponent();
				// 如果是音頻裝置這個方法將傳回null,這裡要再判斷一次
				if (comp != null) {
					// 將Component加到窗體
					jContentPane.add(comp, BorderLayout.EAST);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return jContentPane;
	}
}
