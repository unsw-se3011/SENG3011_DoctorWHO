<template>
  <div class="profile-dropdown">
    <span class="profile-dropdown__avatar-container">
      <slot/>
    </span>
    <vuestic-dropdown
      v-model="isShown"
      position="bottom"
    >
      <div
        v-for="option in options"
        :key="option.name"
        class="dropdown-item plain-link-item"
      >
      
        <router-link :to="{name: option.redirectTo}" class="plain-link" href="#">
          {{ $t(`user.${option.name}`) }}
        </router-link>
      </div>
      <div class="dropdown-item plain-link-item"><a class="plain-link" @click="logout">Logout</a></div>
    </vuestic-dropdown>
  </div>
</template>

<script>
export default {
  name: 'profile-section',
  data () {
    return {
      isShown: false,
    }
  },
  props: {
    options: {
      type: Array,
      default: () => [
        {
          name: 'profile',
          redirectTo: 'cards',
        }
      ],
    },
  },
  methods: {
    logout () {
      document.cookie = 'session=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;'
      window.location.replace('/')
    }
  }
}
</script>

<style lang="scss">
@import '../../../../../vuestic-theme/vuestic-sass/resources/resources';

.profile-dropdown {
  @include flex-center();
  cursor: pointer;

  &__avatar-container {
    display: inline-block;
    width: 50px;
    height: 50px;
    background-color: white;
    border-radius: 50%;
    border: 2px solid $lighter-gray;
    overflow: hidden;

    img {
      height: 100%;
      width: 100%;
    }
  }
}
</style>
