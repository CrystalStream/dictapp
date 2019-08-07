/**
 * Get the user selection of the current window he's looking at
 * and send a message to store it on localstorage of the chrome extension
 */
function broadcastSelection() {
  const userSelectedText = window.getSelection().toString()

  if (!userSelectedText) return;
  
  const eventTitle = `selection<-->${userSelectedText}`

  // Send the message with especial nomenclature
  chrome.runtime.sendMessage(chrome.runtime.id, eventTitle)
}

// Broadcast the user selection
broadcastSelection()
