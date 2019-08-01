import React from 'react'
import Suggestion from './ui/Suggestion'

function DPInput({suggestion, ...props}) {
  const classes = ['textarea', 'has-fixed-size']

  return (
    <>
      <textarea className={classes.join(' ')} {...props}></textarea>
      {suggestion && <Suggestion text="testing"/>}
    </>
  )

}

export default DPInput
