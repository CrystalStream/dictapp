import React from 'react'
import Logo from '../../assets/img/logo.png'

function Header(props) {

  return (
    <nav className="navbar app-navbar" role="navigation" aria-label="main navigation">
      <div className="navbar-brand">
        <a className="navbar-item" href="https://bulma.io">
          <img src={Logo} alt="Translate has never been so easy" width="112" height="50" />
        </a>
      </div>
      <div className="navbar-end">
        <div className="navbar-item">
          <button className="button config-button">
            <span className="icon-settings has-text-grey-darker is-size-5"></span>
          </button>
        </div>
      </div>
    </nav>
  )
}

export default Header
