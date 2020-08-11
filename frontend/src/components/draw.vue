<template>
<v-row class="justify-space-around">
  <div style="margin: 1em auto">
    <div ref="container">
      <canvas
        :width="width"
        :height="height"
        ref="canvas"
        style="background-color:white; padding:5px">
      </canvas>
    </div>
    <v-row class="my-2 justify-space-around">
      <v-btn @click="sendImage">実行</v-btn>
      <v-btn @click="onClearCanvas">リセット</v-btn>
    </v-row>
    <p style="margin: 10px; font-weight: 300; font-size:20px">予測：{{ answer }}</p>
  </div>
</v-row>
</template>

<script>
import Konva from 'konva';
import axios from 'axios';

export default {
  name: 'FreeDrawing',
  // propsは親の「CallCanvas.vue」から値を受け取るためのプロパティ
  data: function(){
    return {
      answer: null,
      width: window.innerWidth,
      height: window.innerHeight,
      distance: 0,
      stage: null,
      canvas: null,
      context: null,
      drawingLayer: null,
      backgroundLayer: null,
      backgroundRect: null,
      drawingScope: null,
      lastPointerPosition: {},
      localPos: {
        x: 0,
        y: 0
      },
      pos: null,
      isPaint: false
    }
  },
  mounted: function () {
    var container = this.$refs.container;
    this.distance = Math.min(this.width, this.height) / 2
    this.stage = new Konva.Stage({
      container,
      width: this.distance,
      height: this.distance
    })
    this.backgroundRect = new Konva.Rect({
      x: 0,
      y: 0,
      width: this.distance,
      height: this.distance,
      fill: 'white'
    })
    this.backgroundLayer = new Konva.Layer()
    this.drawingLayer = new Konva.Layer()
    this.backgroundLayer.add(this.backgroundRect)
    this.stage.add(this.backgroundLayer)
    this.stage.add(this.drawingLayer)
    this.canvas = this.$refs.canvas
    this.drawingScope = new Konva.Image({
      image: this.canvas,
      x: 0,
      y: 0,
      stroke: 'black'
    })
    this.drawingLayer.add(this.drawingScope)
    this.stage.draw()

    this.context = this.canvas.getContext('2d')
    this.context.strokeStyle = ''
    this.context.lineJoin = 'round'
    this.context.lineWidth = 15

    // イベント追加
    this.drawingScope.on('mousedown', this.mousedown)
    this.stage.addEventListener('mouseup', this.mouseup)
    this.stage.addEventListener('mousemove', this.mousemove)
    this.drawingScope.on('touchstart', this.mousedown)
    this.stage.addEventListener('touchend', this.mouseup)
    this.stage.addEventListener('touchmove', this.mousemove)
  },
  methods: {
    mousedown: function () {
      this.isPaint = true

      // マウスダウン時の座標を取得しておく
      this.lastPointerPosition = this.stage.getPointerPosition()
    },
    mouseup: function () {
      this.isPaint = false
    },
    mousemove: function () {
      if (!this.isPaint) {
        return;
      }
      this.context.globalCompositeOperation = 'source-over';

      this.context.beginPath()

      this.localPos.x = this.lastPointerPosition.x - this.drawingScope.x()
      this.localPos.y = this.lastPointerPosition.y - this.drawingScope.y()

      // 描画開始座標を指定する
      this.context.moveTo(this.localPos.x, this.localPos.y)

      this.pos = this.stage.getPointerPosition()
      this.localPos.x = this.pos.x - this.drawingScope.x()
      this.localPos.y = this.pos.y - this.drawingScope.y()

      // 描画開始座標から、lineToに指定された座標まで描画する
      this.context.lineTo(this.localPos.x, this.localPos.y)
      this.context.closePath()
      this.context.stroke()
      this.drawingLayer.draw()

      this.lastPointerPosition = this.pos
    },
    onClearCanvas: function () {
      this.context.globalCompositeOperation = 'destination-out'
      this.context.fillRect(0, 0, this.width, this.height)
      this.drawingLayer.draw()

      
    },
    // 現在のモードが指定されたモードと一致するかどうか
    isTargetMode: function (targetMode) {
      return this.mode === targetMode
    },
    sendImage: async function(){
      var image = this.stage.toDataURL({
        mimetype: 'image/jpeg',
        quality: 1
      })
      var data = null
      await axios.post('/predict', {img: image}).then((response) => {
        data = response['data']
      })
      this.answer = data['ans']
    }
  }
}
</script>