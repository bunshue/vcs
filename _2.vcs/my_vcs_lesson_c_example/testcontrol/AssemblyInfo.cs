using System.Reflection;
using System.Runtime.CompilerServices;

//
// �����{�Ƕ����`�W�H���O�q�L�U�C
// �ݩʶ�����C���o���ݩʭȥi�ק�P�{�Ƕ�
// ���p���H���C
//
[assembly: AssemblyTitle("")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("")]
[assembly: AssemblyProduct("")]
[assembly: AssemblyCopyright("")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]

//
// �{�Ƕ��������H���ѤU�C 4 �ӭȲզ�:
//
//      �D����
//      ������ 
//      ����������
//      �׭q��
//
// �z�i�H���w�Ҧ��o�ǭȡA�]�i�H�ϥΡ��׭q�����M�����������������q�{�ȡA��k�O��
// �p�U�ҥܨϥ� '*':

[assembly: AssemblyVersion("1.0.*")]

//
// �n��{�Ƕ��i��ñ�W�A�������w�n�ϥΪ��K�_�C�����{�Ƕ�ñ�W����h�H���A�аѦ� 
// Microsoft .NET Framework ���ɡC
//
// �ϥΤU�����ݩʱ���Ω�ñ�W���K�_�C
//
// �`�N:
//   (*) �p�G�����w�K�_�A�h�{�Ƕ����|�Qñ�W�C
//   (*) KeyName �O���w�g�w�˦b�p����W��
//      �[�K�A�ȴ��ѵ{��(CSP)�����K�_�CKeyFile �O���]�t
//       �K�_�����C
//   (*) �p�G KeyFile �M KeyName �ȳ��w���w�A�h 
//       �o�ͤU�C�B�z:
//       (1) �p�G�b CSP ���i�H��� KeyName�A�h�ϥθӱK�_�C
//       (2) �p�G KeyName ���s�b�� KeyFile �s�b�A�h 
//           KeyFile �����K�_�w�˨� CSP ���åB�ϥθӱK�_�C
//   (*) �n�Ы� KeyFile�A�i�H�ϥ� sn.exe(�j�W��)��Τu��C
//       �b���w KeyFile �ɡAKeyFile ����m���Ӭ۹��
//       ���ؿ�X�ؿ��A�Y
//       %Project Directory%\obj\<configuration>�C�Ҧp�A�p�G KeyFile ���
//       �Ӷ��إؿ��A���N AssemblyKeyFile 
//       �ݩʫ��w�� [assembly: AssemblyKeyFile("..\\..\\mykey.snk")]
//   (*) ������ñ�W���O�@�Ӱ��ſﶵ - ����������h�H���A�аѾ\ Microsoft .NET Framework
//       ���ɡC
//
[assembly: AssemblyDelaySign(false)]
[assembly: AssemblyKeyFile("")]
[assembly: AssemblyKeyName("")]

