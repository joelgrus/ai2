<style>
  #stopwatch {
    position: absolute;
    top: 20px;
    right: 20px;
  }
  .text {
    display: inline-block;
    width: 80%;
    margin: 20px;
  }
  .word {
    display: inline-block;
    margin: 2px;
    padding: 2px;
    border: 1px solid white;
  }
  .word:hover, .clicked {
    border-radius: 4px;
    border: 1px solid grey;
    background: orange;
  }
  .button {
    width: 100px;
    padding: 5px;
    border: 1px solid grey;
    margin: 20px auto;
    display: block;
    border-radius: 3px;
  }
  .button:hover {
    background: green;
    color: white;
  }
  #controls {
    position: absolute;
    top: 50px;
    left: 50px;
    width: 60px;
  }
  .color {
    padding: 4px;
    width: 100%;
    height: 40px;
  }
  .fade-enter-active {
    transition: opacity .5s;
    transition-delay: .5s;
  }
  .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>

<template>
  <div class="body">
    <transition name="fade">
      <div v-if="!hideAll">
        <stopwatch id="stopwatch"></stopwatch>
        <tutorial></tutorial>
        <div><b> Find the coreferences in the paragraphs below.</b></div>
        <div class="text">
          <div class="word"
            @click="wordSelected(d)"
            :class="{'clicked': d.clicked}"
            :style="{background: d.clicked ? d.background : 'white'}"
            v-for="d in text">{{d.name}}
          </div>
        </div>

        <div class="text">
          <div class="word"
            @click="wordSelected(d2)"
            :class="{'clicked': d2.clicked}"
            :style="{background: d2.clicked ? d2.background : 'white'}"
            v-for="d2 in text2">{{d2.name}}
          </div>
        </div>

        <div class="text">
          <div class="word"
            @click="wordSelected(d3)"
            :class="{'clicked': d3.clicked}"
            :style="{background: d3.clicked ? d3.background : 'white'}"
            v-for="d3 in text3">{{d3.name}}
          </div>
        </div>

        <div class="button" @click="hideAll = true"> Finished! </div>

        <div id="controls">
          <div v-once class="color"
            v-for="(color,i) in getColors()"
            :style="{'background': color}"
            @click="currentColor = color ">
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="hideAll">
        Thanks for your participation!
      </div>
    </transition>


  </div>
</template>

<script>

import stopwatch from './stopwatch'
import tutorial from './tutorial'
import text from './data.json'
import text2 from './data.json'
import text3 from './data.json'
import _ from 'lodash'

export default {
  name: 'dash',
  components: {
    'stopwatch': stopwatch,
    'tutorial': tutorial
  },
  data () {
    return {
      text: _.cloneDeep(text),
      text2: _.cloneDeep(text2),
      text3: _.cloneDeep(text3),
      currentColor: 0,
      hideAll: false
    }
  },
  methods: {
    getColors: function(){
      var colors = []
      for (var i in [0,1,2,3,4,5,6,7,8,9]){
        colors.push(this.getColor())
      }
      this.currentColor = colors[0]
      return colors
    },
    getColor: function(){
      var rgb = [];
      for(var i = 0; i < 3; i++)
          rgb.push(Math.floor(Math.random() * 255));
      return 'rgb('+ rgb.join(',') +')';
    },
    wordSelected: function(d){
      d.clicked = !d.clicked;
      d.background = this.currentColor
    }
  }
}
</script>
