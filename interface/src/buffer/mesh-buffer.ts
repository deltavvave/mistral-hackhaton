/**
 * @file Mesh Buffer
 * @author Alexander Rose <alexander.rose@weirdbyte.de>
 * @private
 */

import '../shader/Mesh.vert'
import '../shader/Mesh.frag'

import Buffer, { BufferParameters, BufferData } from './buffer'

/**
 * Mesh buffer. Draws a triangle mesh.
 *
 * @example
 * var meshBuffer = new MeshBuffer({
 *   position: new Float32Array(
 *     [ 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1 ]
 *   ),
 *   color: new Float32Array(
 *     [ 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0 ]
 *   )
 * });
 */
class MeshBuffer extends Buffer {
  vertexShader = 'Mesh.vert'
  fragmentShader = 'Mesh.frag'

  /**
   * @param  {Object} data - attribute object
   * @param  {Float32Array} data.position - positions
   * @param  {Float32Array} data.color - colors
   * @param  {Float32Array} [data.index] - triangle indices
   * @param  {Float32Array} [data.normal] - radii
   * @param  {BufferParameters} params - parameter object
   */
  constructor (data: BufferData, params: Partial<BufferParameters> = {}) {
    super(data, params)

    this.addAttributes({
      'normal': { type: 'v3', value: data.normal }
    })

    if (data.normal === undefined) {
      this.geometry.computeVertexNormals()
    }
  }
}

export default MeshBuffer
