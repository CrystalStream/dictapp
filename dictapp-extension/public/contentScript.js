function sendUserSelectedText() {
  const userSelectedText = window.getSelection().toString()

  if (!userSelectedText) return;
  
  const eventTitle = `selection<-->${userSelectedText}`

  // Send the message with especial nomenclature
  chrome.runtime.sendMessage('lplhnabkljkdpaellhdcmfgcnmkapjpb', eventTitle)
}

sendUserSelectedText()
