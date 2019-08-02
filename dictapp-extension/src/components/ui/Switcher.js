import React from 'react'

function Switcher(props) {

  return (
    <div className="switcher-button-container has-text-centered">
      <div className="columns is-flex is-centered is-vcentered">
        <div className="column is-5">
          <button className="button is-normal is-fullwidth">Spanish &nbsp;&nbsp;<span className="icon-repeat"></span>&nbsp;&nbsp; English</button>
        </div>
      </div>
    </div>
  )
}

export default Switcher
