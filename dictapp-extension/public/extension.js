/* global chrome */

function setupListeners() {
  chrome.runtime.onMessage.addListener(function(message) {

      if (message == "runContentScript"){
        chrome.tabs.executeScript({
          file: 'contentScript.js'
        })
      }

      else if (/<-->/.test(message)) {
        const [ _, selectedText ] = message.split('<-->')
        localStorage.setItem('selection', selectedText)
      }
   })
  
}

function init() {
  setupListeners()
}

init()
