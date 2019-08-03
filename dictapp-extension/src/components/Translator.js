import React, { useEffect, useState } from 'react'
import Switcher from './ui/Switcher'
import Footer from './ui/Footer'
import Input from './DPInput'
import chrome from '../utils'

function Translator() {

  const [text, setSelection] = useState('')

  useEffect(() => {
    chrome.sendMessage('lplhnabkljkdpaellhdcmfgcnmkapjpb', 'getSelectedText', setSelection)
  }, [])


  return (
    <form>
      <Switcher />
      <hr />
      <div className="control">
        <div className="columns">
          <div className="column">
            <Input placeholder="Type your search and hit 'Enter'" suggestion="testing" value={text} onChange={(e) => { setSelection(e.target.value) }} />
          </div>
        </div>
        <div className="columns">
        <div className="column">
            <Input readOnly placeholder="Transalated text..."/>
          </div>
        </div>
      </div>
      <Footer />
    </form>
  )
}

export default Translator