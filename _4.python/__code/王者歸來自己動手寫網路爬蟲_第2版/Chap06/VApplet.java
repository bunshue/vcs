

import java.awt.BorderLayout;
import java.awt.Choice;
import java.awt.Component;
import java.util.Vector; // JMF��������
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

	// ���t�ΩҦ��i�Ķ����w��˸m�C��
	private CaptureDeviceInfo[] getDevices() {
		Vector devices = CaptureDeviceManager.getDeviceList(null);
		CaptureDeviceInfo[] info = new CaptureDeviceInfo[devices.size()];
		for (int i = 0; i < devices.size(); i++) {
			info[i] = (CaptureDeviceInfo) devices.get(i);
		}
		return info;
	}

	// �q�w���˸m�����Ҧ����T�˸m���C��
	private CaptureDeviceInfo[] getVideoDevices() {
		CaptureDeviceInfo[] info = getDevices();
		CaptureDeviceInfo[] videoDevInfo;
		Vector vc = new Vector();
		for (int i = 0; i < info.length; i++) {
			// ���˸m�䴩���榡�A�p�G���@�ӬO���T�榡�A�h�{�����˸m�����T�˸m
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
				// �o�̧ڥu���@�ӵ��T�˸m�A�������Ĥ@��
				// ���o�ثe�˸m��MediaLocator
				ml = getVideoDevices()[0].getLocator();
				// �Τw�g���o��MediaLocator�o��@��Player
				player = Manager.createRealizedPlayer(ml);
				player.start();
				// ���oPlayer��AWT Component
				Component comp = player.getVisualComponent();
				// �p�G�O���W�˸m�o�Ӥ�k�N�Ǧ^null,�o�̭n�A�P�_�@��
				if (comp != null) {
					// �NComponent�[�쵡��
					jContentPane.add(comp, BorderLayout.EAST);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return jContentPane;
	}
}
