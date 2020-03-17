## Installation Steps :neutral_face:

#### Create virtual env in project dir
```console
 python3 -m venv env
 source env/bin/activate
```

#### Install django
```console
 pip3 install django
 pip3 install djangorestframework
```



#### Get set go...
```console
python3 manage.py runserver
```
#### No need to create virtual env


````javascript
  if (contentType) {
    data = form.find('[data-override="content"]').val() || ''

    if (contentType === 'multipart/form-data') {
      // We need to add a boundary parameter to the header
      // We assume the first valid-looking boundary line in the body is correct
      // regex is from RFC 2046 appendix A
      var boundaryCharNoSpace = "0-9A-Z'()+_,-./:=?";
      var boundaryChar = boundaryCharNoSpace + ' ';
      var re = new RegExp('^--([' + boundaryChar + ']{0,69}[' + boundaryCharNoSpace + '])[\\s]*?$', 'im');
      var boundary = data.match(re);
      if (boundary !== null) {
        contentType += '; boundary="' + boundary[1] + '"';
      }
      // Fix textarea.value EOL normalisation (multipart/form-data should use CR+NL, not NL)
      data = data.replace(/\n/g, '\r\n');
    }
  } else {
    contentType = form.attr('enctype') || form.attr('encoding')

    if (contentType === 'multipart/form-data') {
      if (!window.FormData) {
        alert('Your browser does not support AJAX multipart form submissions');
        return;
      }
````
