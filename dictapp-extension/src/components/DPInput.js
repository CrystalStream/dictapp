import React from 'react'
import Suggestion from './ui/Suggestion'

function DPInput({suggestion, loading, ...props}) {
  const classes = ['textarea', 'has-fixed-size']

  return (
    <div className={`control ${loading ? 'is-loading' : ''}`}>
      <textarea className={classes.join(' ')} {...props} disabled={loading}></textarea>
      {suggestion && <Suggestion text={suggestion} />}
    </div>
  )

}

export default DPInput
