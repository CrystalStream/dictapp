import React, { useState } from 'react'

function Switcher(props) {

  const [ enToEs, setLang ] = useState(true)

  const onClick = e => {
    /* global chrome */

    e.preventDefault();
    var bkg = chrome.extension.getBackgroundPage()
    bkg.console.log('local', bkg.localStorage.getItem('selection'))
    setLang(!enToEs)
  };

  return (
    <div className="switcher-button-container has-text-centered">
      <div className="columns is-flex is-centered is-vcentered">
        <div className="column is-4">
        <button className={`button is-normal flip-button ${enToEs ? '' : 'es'}`} onClick={onClick}>
            <div className={`front-button ${ enToEs ? 'active': ''}`}>
              <p>
                English &nbsp;&nbsp;<span className="icon-repeat"></span>&nbsp;&nbsp; Spanish
              </p>
            </div>
            <div className={`back-button ${ !enToEs ? 'active': ''}`}>
              <p>
                Spanish &nbsp;&nbsp;<span className="icon-repeat"></span>&nbsp;&nbsp; English
              </p>
            </div>
          </button>
        </div>
      </div>
    </div>
  )
}

export default Switcher
