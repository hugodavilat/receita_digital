function download(filename, data) {
  let a = document.createElement("a");
  document.body.appendChild(a);
  a.style = "display: none";
  blob = new Blob([data]);
  url = window.URL.createObjectURL(blob);
  a.href = url;
  a.download = filename;
  a.click();
  window.URL.revokeObjectURL(url);
}
function formSubmission() {
  let a = nacl.box.keyPair();
  $("#public-key").val(toHexString(a.publicKey));

  console.log(toHexString(a.publicKey));
  console.log( $("#public-key").val());
  download('my.id',a.secretKey);
}

const fromHexString = hexString =>
new Uint8Array(hexString.match(/.{1,2}/g).map(byte => parseInt(byte, 16)));

const toHexString = bytes =>
bytes.reduce((str, byte) => str + byte.toString(16).padStart(2, '0'), '');

$( document ).ready( function() {

  $("#criar-medico-form").submit(formSubmission);

});


