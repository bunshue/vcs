## Legacy Slidemode. 

This folder contains the legacy slidemode

Put the following in your custom.js


```
// Slidemode
require(['nbextensions/IPython-notebook-extensions/slidemode/main','base/js/events'], function(slidemode, events){
    events.on('app_initialized.NotebookApp', function(){
        slidemode.init();
    });
});
// end slidemode
```
