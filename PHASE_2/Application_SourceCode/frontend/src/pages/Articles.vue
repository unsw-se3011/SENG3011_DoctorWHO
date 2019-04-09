<template>
  <div class="row">
  <card type="plain" title="Articles">
  </card>
  <card type="plain">
  <p>
    Filter articles by date of publication, key terms and location.
  </p>
    <div class="col-md-8">
      <form>
        <p>
          Start date: <datetime type="datetime" v-model="datetime"></datetime>
        </p>
        <p>
          End date: <datetime type="datetime" v-model="datetime"></datetime>
        </p>
        <p>
          Key terms (optional): <br> <input type="text"> <br>
        </p>
        <p>
          Location (optional): <br> <input type="text"> <br>
        </p>
        <button class="btn"> Submit </button> 
      </form>
    </div>
  </card>
  </div>
</template>

<script>
// https://github.com/mariomka/vue-datetime
</script>

<style>
</style>
