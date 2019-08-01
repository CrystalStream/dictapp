import React from 'react'

function Suggestion(props) {
  return (
    <div className="suggestion-container">
      <div>
        <p>{props.text}</p>
      </div>
    </div>
  )
}

export default Suggestion
