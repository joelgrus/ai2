<template>
    <span  v-if="show">{{currentTime}}</span>
</template>

<style>
 span {
   border: 1px solid grey;
   border-radius: 3px;
   padding: 10px;
 }
</style>

<script>
export default {
  name: 'stopwatch',
  data () {
    return {
      currentTime: this.formatTime(Date.now() - this.startTime),
      show: false
    }
  },
  mounted: function() {
    this.startTime = Date.now();
    this.interval = setInterval(this.updateCurrentTime, 1000);
  },
  methods: {
      updateCurrentTime: function() {
          this.currentTime = this.formatTime(Date.now() - this.startTime)
          this.show = true
      },
      formatTime: function(time){
        var sec_num = parseInt(time / 1000, 10); // don't forget the second param
        var hours   = Math.floor(sec_num / 3600);
        var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
        var seconds = sec_num - (hours * 3600) - (minutes * 60);

        if (hours   < 10) {hours   = "0"+hours;}
        if (minutes < 10) {minutes = "0"+minutes;}
        if (seconds < 10) {seconds = "0"+seconds;}
        return hours+':'+minutes+':'+seconds;
      }
  }
}
</script>
