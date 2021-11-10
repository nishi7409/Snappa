<template>
    <div class="Preview">
        <h1>Preview page!</h1>
        <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card-title class="white--text orange darken-4">
      Participant List

    </v-card-title>

    <v-card-text class="pt-4">
    These players have joined the Snappa league. Feel free to check out other players before team selection!
    </v-card-text>

    <v-divider></v-divider>

    <v-virtual-scroll
      :items="items"
      :item-height="50"
      height="400"
    >
      <template v-slot:default="{ item }">
        <v-list-item>
          <v-list-item-avatar>
            <v-avatar
              :color="item.color"
              size="56"
              class="white--text"
            >
              {{ item.initials }}
            </v-avatar>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>{{ item.fullName }}</v-list-item-title>
          </v-list-item-content>

          <v-list-item-action>
            <v-btn href="google.com" target="_blank"
              depressed
              small
            >
              View User

              <v-icon
                color="orange darken-4"
                right
              >
                mdi-open-in-new
              </v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </template>
    </v-virtual-scroll>
  </v-card>
    </div>
</template>

<script>
  export default {
    data: () => ({
      names: ['Joseph Xiao', 'Soorya Pari','Nishant Srivastava','Vincent Chen','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng']
    }),

    computed: {
      items () {

        return Array.from({ length: this.names.length }, (k, v) => {
          const name = this.names[v]

          return {
            color: '#2196F3',
            fullName: `${name}`,
            initials: v+1,
          }
        })
      },
    },

    methods: {
      genRandomIndex (length) {
        return Math.ceil(Math.random() * (length - 1))
      },
    },
  }
</script>