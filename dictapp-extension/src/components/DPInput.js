import React from 'react'
import Suggestion from './ui/Suggestion'

function DPInput({suggestion, text, ...props}) {
  const classes = ['textarea', 'has-fixed-size']

  return (
    <>
      <textarea className={classes.join(' ')} {...props}>
        {text}
      </textarea>
      {suggestion && <Suggestion text={suggestion} />}
    </>
  )

}

export default DPInput
