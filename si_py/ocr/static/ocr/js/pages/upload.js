Dropzone.options.uploadWidget = {
  paramName: 'file',
  maxFilesize: 20, // MB
  maxFiles: 10,
  
  init: function() {
    this.on("error", function(file, message) { alert(message); });
    this.on('success', onUploadSuccess);
  }
};


function onUploadSuccess(file, res) {
  window.location.href = '/ocr/result';
}

