Dropzone.options.uploadWidget({
  init: function() {
    this.on("error", function(file, message) { alert(message); });    
  }
});

