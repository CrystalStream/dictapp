/* global chrome */

function setupListeners() {
  chrome.runtime.onMessage.addListener(function(message, _, sendResponse) {
      if (message == "runContentScript"){
        chrome.tabs.executeScript({
          file: 'contentScript.js'
        })
      }

      if (/<-->/.test(message)) {
        const [ _, selectedText ] = message.split('<-->')
        localStorage.setItem('selection', selectedText)
      }

      if (message === 'getSelectedText')  {
        let text = localStorage.getItem('selection')
        if (!text) text = ''
        localStorage.clear()
        sendResponse(text)
      }
   })
  
}

function init() {
  setupListeners()
}

init()
