<template>
      <card type="plain">
      <p> Specify the range of data you wish to use: </p> <br>
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
            <button class="btn"> Create Graphs  </button>
          </form>
        </div>
      </card>
</template>

<script>
</script>

<style>
</style>
