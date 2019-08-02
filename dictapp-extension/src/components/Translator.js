import React from 'react'
import Switcher from './ui/Switcher'
import Footer from './ui/Footer'
import Input from './DPInput'

function Translator(props) {
  const selectedText = localStorage.getItem('selection')
  localStorage.clear()

  return (
    <form>
      <Switcher />
      <hr />
      <div className="control">
        <div className="columns">
          <div className="column">
            <Input placeholder="Type your search and hit 'Enter'" suggestion="testing" text={selectedText} />
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
