import React from 'react'
import './App.scss'

import { Header, Translator } from './components'

function App() {
  return (
    <div className="dictapp">
      <Header />
      <div className="container">
        <section className="section main-section">
          <Translator />
        </section>
      </div>
    </div>
  )
}

export default App
