import React, { useEffect, useState, useCallback } from 'react'
import Switcher from './ui/Switcher'
import Footer from './ui/Footer'
import Input from './DPInput'
import chrome from '../utils'

function Translator() {

  const [text, setText] = useState('')
  const [translation, setTranslation] = useState({})
  const [isLoading, setLoading] = useState(false)

  useEffect(() => {
    // Get the user selection of the active window's tab
    chrome.sendMessage(chrome.extensionID, 'getSelection', setText)
  }, [])

  const searchPhrase = useCallback((e) => {

    // Clean up if the user input is null
    if (!text) {
      setText('')
      setTranslation({})
      return
    }

    // Capture only the enter, but without the combination with the shift key
    if (e.key !== 'Enter' || (e.key === 'Enter' && e.shiftKey)) return

    // Do the actual search
    setLoading(true)

    setTimeout(() => {

      const translate = {
        text: text + ' traducido',
        suggestion: text + ' <- asi escribelo'
      }
      
      setTranslation(translate)
      setLoading(false)
    }, 1000)
  }, [text])

  const onChangeText = useCallback((e) => {
    let uText = e.target.value

    if (!e.target.value.trim().length) uText = ''
    setText(uText)
  },  [setText])

  const preventEnter = function(e){
    if (e.key === 'Enter' && !(e.key === 'Enter' && e.shiftKey)) e.preventDefault()
  }

  return (
    <>
      <Switcher />
      <hr />
      <div className="control">
        <div className="columns">
          <div className="column">
            <Input
              placeholder="Type your search and hit 'Enter'"
              suggestion={text && translation.suggestion}
              loading={isLoading}
              value={text}
              onChange={onChangeText}
              onKeyDown={preventEnter}
              onKeyUp={searchPhrase} />
          </div>
        </div>
        <div className="columns">
        <div className="column">
            <Input
              readOnly
              placeholder="Transalated text..."
              value={translation.text || ''}
            />
          </div>
        </div>
      </div>
      <Footer />
    </>
  )
}

export default Translator
