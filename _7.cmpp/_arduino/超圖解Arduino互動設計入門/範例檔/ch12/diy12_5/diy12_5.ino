// 動手做12-5：遙控照相機拍攝縮時影片
// 詳細的程式說明，請參閱第十二章，12-20頁。

#include <multiCameraIrControl.h>

Sony NEX(3);

void setup(){
}

void loop(){
  NEX.shutterNow();
  delay(5000);
}
