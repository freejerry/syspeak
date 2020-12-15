
    /* simple scripts file for Themes.guide Bootstrap 4 theme templates */

    // init Bootstrap tooltips & popovers
    $("[data-toggle=popover]").popover();
    $("[data-toggle=tooltip]").tooltip();
    
    
    /* copy demo sources to clipboard */
    function copyTextToClipboard(text) {
      var textArea = document.createElement("textarea");
      textArea.style.position = 'fixed';
      textArea.style.top = 0;
      textArea.style.left = 0;
      textArea.style.width = '2em';
      textArea.style.height = '2em';
      textArea.style.padding = 0;
      textArea.style.border = 'none';
      textArea.style.outline = 'none';
      textArea.style.boxShadow = 'none';
      textArea.style.background = 'transparent';
      textArea.value = text;
      document.body.appendChild(textArea);
      textArea.select();
    
      try {
        var successful = document.execCommand('copy');
        var msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
      } catch (err) {
        console.log('Oops, unable to copy');
      }
    
      document.body.removeChild(textArea);
      return false;
    }
    
    var modalCode       = $('<div id="modalCode" class="modal fade" />');
    var modalDialog     = $('<div class="modal-dialog modal-dialog-centered modal-lg" />');
    var modalContent    = $('<div class="modal-content" />');
    var modalHeader     = $('<div class="modal-header align-items-center"><h3 class="mb-0">Source Code</h3><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button></div>');
    var modalBody       = $('<div class="modal-body d-block py-3"><span class="badge badge-dark font-weight-light mb-2">The following markup was copied to the clipboard...</span><textarea id="code" class="form-control" rows="10" wrap="off"></textarea></div>');
    modalHeader.appendTo(modalContent);
    modalBody.appendTo(modalContent);
    modalContent.appendTo(modalDialog);
    modalDialog.appendTo(modalCode);
    modalCode.appendTo('body');
    
    var css = ".copyable{position:relative}.copyable .copyable-trigger{color:#333;background-color:rgba(255,255,255,.8);border:1px #888 solid;border-radius:4px;position:absolute;padding:3px 6px;top:0;right:0;z-index:102;text-decoration:none;font-family:monospace;font-size:11px;cursor:pointer;display:none}.copyable:hover .copyable-trigger{display:inline-block}";
    
    $("head").append($(document.createElement("style"))
        .html(css)
    );
    
