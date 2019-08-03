/* global chrome */

function getBackgroundPage() {
  if (chrome.extension) {
    return chrome.extension.getBackgroundPage()
  }
  return null
}

function consoleLog() {
  const page = getBackgroundPage()

  if (!page) return;

  return page.console.log(...arguments)
    
}

function sendMessage() {
  if (chrome && chrome.runtime && chrome.runtime.sendMessage) {
    return chrome.runtime.sendMessage(...arguments)

  }
}

export default {
  consoleLog,
  sendMessage
}
