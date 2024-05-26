/**
 * @file Component Collection
 * @author Alexander Rose <alexander.rose@weirdbyte.de>
 * @private
 */

import RepresentationElement from './representation-element'
import Collection from './collection'
import { GenericColor } from '../types'

class RepresentationCollection extends Collection<RepresentationElement> {
  setParameters (params: any) {
    return this.forEach((repr) => repr.setParameters(params))
  }

  setVisibility (value: boolean) {
    return this.forEach((repr) => repr.setVisibility(value))
  }

  setSelection (string: string) {
    return this.forEach((repr) => repr.setSelection(string))
  }

  setColor (color: GenericColor) {
    return this.forEach((repr) => repr.setColor(color))
  }

  update (what: any) {
    return this.forEach((repr) => repr.update(what))
  }

  build (params?: any) {
    return this.forEach((repr) => repr.build(params))
  }

  dispose (params?: any) {
    return this.forEach((repr) => repr.dispose())
  }
}

export default RepresentationCollection
