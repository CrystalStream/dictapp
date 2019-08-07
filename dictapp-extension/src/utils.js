/* global chrome */

/**
 * Return the background page for the react extension
 */
function getBackgroundPage() {
  if (chrome.extension) {
    return chrome.extension.getBackgroundPage()
  }
  return null
}

/**
 * Debug purposes
 * console log to the react extension debug page
 */
function consoleLog() {
  const page = getBackgroundPage()

  if (!page) return;

  return page.console.log(...arguments)
    
}

/**
 * Send messages to the chrome api listeners
 */
function sendMessage() {
  if (chrome && chrome.runtime && chrome.runtime.sendMessage) {
    return chrome.runtime.sendMessage(...arguments)

  }
}

export default {
  extensionID: chrome.runtime.id || 'lplhnabkljkdpaellhdcmfgcnmkapjpb',
  consoleLog,
  sendMessage
}
