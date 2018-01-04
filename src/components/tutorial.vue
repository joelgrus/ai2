<style scoped>
  #tutorial {
    z-index: 1000;
    background: rgba(0, 0, 0, 0.5);
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }
  #main {
    background: white;
    border-radius: 3px;
    position: absolute;
    top: 50px;
    left: 50px;
    bottom: 50px;
    right: 50px;
    box-shadow: 3px 3px 23px 0px rgba(47, 50, 50, 0.92);
  }
  .welcome {
    margin-top: 100px;
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
  .cake-enter-active {
    transition: opacity .5s;
  }
  .cake-enter {
    opacity: 0;
  }
  h4 {
    margin-top: 20px;
    font-weight: 100;
  }
  p {
    text-align: left;
    margin: 10px 100px;
  }
  .example {
    margin: 40px;
    font-style: italic;
    text-align: center;
  }
  .selected {
    font-weight: bold;
    font-style: underline;
    padding: 2px;
    border: none;
  }
  .button {
    padding: 5px;
    border: 1px solid grey;
    margin: 20px;
    display: inline-block;
    border-radius: 3px;
  }
  .button:hover {
    background-color: green;
    color: white;
  }
  .choseWord {
    border: none;
  }
  .choseWord:hover {
    border: 1px solid grey;
  }
  .wordSelected {
    border: 1px solid grey;
    background: orange;
  }
  .cake_lie {
    text-align: center;
    margin: 20px;
    /* font-size: 20px; */
    /* font-weight: bold; */
  }

</style>

<template>
  <div id="tutorial"  v-if="!hide">
    <div id="main">
      <!-- <h4> CoReference Tutorial </h4> -->
      <transition name="fade">
        <div class="welcome" v-if="page == 1">
          <p> Welcome {{user}}, </p>
          <p>In this short tutorial we'll be showing you how
          to pick out <b>coreferences</b>. Coreferences are two or more words which
          refer to the same thing. For example, in the sentence below, the coreferences are bolded.</p>
           
          <p class="example">"The <b>Golgi apparatus</b>, also known as the <b>Golgi complex</b>, <b>Golgi body</b>,
          or simply the <b>Golgi</b>, is an <b>organelle</b> found in most eukaryotic cells."</p>

          <p> Note: coreferences could occur across multiple sentences. For instance: </p>

          <p class="example">"The <b>project leader</b> is refusing to help. The <b>jerk</b> thinks only of himself."</p>

          <div class="button" @click="page = 2"> Got it! </div>
        </div>
      </transition>
      <transition name="fade">
        <div class="welcome" v-if="page == 2">
          <stopwatch id="stopwatch"></stopwatch>
          <p> Let's try an example. </p>
          <p> Can you find the coreferences in the sentence below?</p>
          <p class="example">
            <span v-for="(word, i) in words" class="choseWord"
            @click="words[i] = !words[i]"
            :class="{'wordSelected': words[i] == true}">{{i}}&nbsp;</span>.
          </p>
          <transition name="cake">
            <div v-if="words['that man'] && words['he']">
              <p class="cake_lie"> Great job! You may now click continue to start the task. </p>
              <div class="button" @click="hide = true">Continue</div>
            </div>
          </transition>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>

import stopwatch from './stopwatch'

export default {
  name: 'tutorial',
  components: {
    'stopwatch': stopwatch
  },
  data () {
    return {
      hide: false,
      user: 'Foo',
      page: 1,
      words: {
        "Look": false,
        "at": false,
        "that man": false,
        "over": false,
        "there,": false,
        "he": false,
        "is": false,
        "wearing": false,
        "a": false,
        "funny": false,
        "hat": false,
      }
    }
  },
  methods: {
    // validate: function(){
    //   if (this.words && this.words)
    // }
  }
}
</script>
