import React, { useState } from 'react'

function Switcher(props) {

  const [ enToEs, setLang ] = useState(true)

  return (
    <div className="switcher-button-container has-text-centered">
      <div className="columns is-flex is-centered is-vcentered">
        <div className="column is-5">
          <button className={`button is-normal is-fullwidth flip-button ${enToEs ? '' : 'es'}`} onClick={(e) => { e.preventDefault(); setLang(!enToEs) } }>
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
