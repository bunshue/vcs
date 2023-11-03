// Allow drag&drop of images into a notebook
// Tested with Firefox and Chrome

define([
    'base/js/namespace',
    'jquery',
    "base/js/events"
], function(IPython, $, events) {
    "use strict";

        /* http://stackoverflow.com/questions/3231459/create-unique-id-with-javascript */
        function uniqueid(){
            // always start with a letter (for DOM friendlyness)
            var idstr=String.fromCharCode(Math.floor((Math.random()*25)+65));
            do {                
                // between numbers and characters (48 is 0 and 90 is Z (42-48 = 90)
                var ascicode=Math.floor((Math.random()*42)+48);
                if (ascicode<58 || ascicode>64){
                    // exclude all chars between : (58) and @ (64)
                    idstr+=String.fromCharCode(ascicode);    
                }                
            } while (idstr.length<32);

            return (idstr);
        }
        
        var send_to_server = function(name,path,msg) {
            if (name == '') {
                name = uniqueid() + '.' + msg.match(/data:image\/(\S+);/)[1];
                }
            path = path.substring(0, path.lastIndexOf('/')) + '/';
            if (path === '/') path = '';
            var url = '//' + location.host + '/api/contents/' + path + name;
            var img = msg.replace(/(^\S+,)/, ''); // strip header
            //console.log("send_to_server:", url, img);
            var data = {'name': name, 'format':'base64', 'content': img, 'type': 'file'};
            var settings = {
                processData : false,
                cache : false,
                type : "PUT",
                dataType : "json",
                data : JSON.stringify(data),
                headers : {'Content-Type': 'text/plain'},
                async : false,
                success : function (data, status, xhr) {
                    var new_cell = IPython.notebook.insert_cell_below('markdown');
                    var str = '<img  src="' + name + '"/>';
                    new_cell.set_text(str);
                    new_cell.execute();
                    },
                error : function() {console.log('Data transfer for drag-and-drop failed.'); }
            };
            $.ajax(url, settings);
        };
        
        /* the dragover event needs to be canceled to allow firing the drop event */
        window.addEventListener('dragover', function(event){
            if (event.preventDefault) {
                event.preventDefault();
            }
        });
        
        /* allow dropping an image in notebook */
        window.addEventListener('drop', function(event){
            var cell = IPython.notebook.get_selected_cell();
            event.preventDefault();
            if(event.stopPropagation) {event.stopPropagation();}
                if (event.dataTransfer.items != undefined) {
                    /* Chrome here */
                    var items = event.dataTransfer.items;
                    for (var i = 0; i < items.length; i++) {
                        /* data coming from local file system, must be an image to allow dropping*/
                        if (items[i].kind == 'file' && items[i].type.indexOf('image/') !== -1) {

                            var blob = items[i].getAsFile();
                            var filename = blob.name;
                            var reader = new FileReader();
                            reader.onload = ( function(evt) {
                                send_to_server(filename, IPython.notebook.notebook_path, evt.target.result);
                                if(event.stopPropagation) {event.stopPropagation();}
                             } );
                            reader.readAsDataURL(blob);
                        } else {
                            console.log("Unsupported type:", items[i].kind); 
                        }
                    }
                } else { 
                    /* Firefox here */
                    var files = event.dataTransfer.files;
                    if (files.length == 0) {
                        var filename = event.dataTransfer.getData('application/x-moz-file-promise-dest-filename');
                        var data = event.dataTransfer.getData('text/plain');
                        if (filename.length == 0) {
                            url = "";
                            filename = '';
                        } else {
                            url = data;
                            data = "";
                        }   
                        /* data coming from browser:
                         *   url  - image is given as an url
                         *   data - image is a base64 blob
                         */
                        //console.log("type:",url," name:", filename," path:", IPython.notebook.notebook_path," url:", url);
                        send_to_server(filename, IPython.notebook.notebook_path, data);                        
                        return;
                        }
                    /* data coming from local file system, must be an image to allow dropping*/
                    for (var i=0; i < files.length; i++) {
                        var blob = event.dataTransfer.files[0];
                        if (blob.type.indexOf('image/') !== -1) {
                            var filename = blob.name;
                            var url = event.view.location.origin;
                            var reader = new FileReader();
                                reader.onload = ( function(evt) {
                                    //console.log("file"," name:", filename," path:", IPython.notebook.notebook_path," url:", url);
                                    send_to_server(filename, IPython.notebook.notebook_path, evt.target.result);
                                    event.preventDefault();
                                    } );
                            reader.readAsDataURL(blob);
                        } else {
                            console.log("Unsupported type:", blob.type); 
                        }
                        
                    }   
            }
        });

        /* 
         * make sure we do not drop images into a codemirror text field 
         */
        var checktype = function(cm,event) {
            if (event.dataTransfer.items != undefined)  
                {
                event.codemirrorIgnore = true;
                }
            var blob = event.dataTransfer.files[0];

            if (event.dataTransfer.files.length > 0 && blob.type.indexOf('image/') !== -1) {
                event.codemirrorIgnore = true;
                }
        };

        var create_cell = function (event,nbcell,nbindex) {
            var cell = nbcell.cell;
            if ((cell instanceof IPython.CodeCell)) {
                cell.code_mirror.on('drop', checktype);
            }
        }; 
        
        var cells = IPython.notebook.get_cells();
        for(var i in cells){
            var cell = cells[i];
            if ((cell instanceof IPython.CodeCell)) {
                cell.code_mirror.on('drop', checktype);
            }
        }

        events.on('create.Cell',create_cell);     
});

   

