<template>
  <!-- <v-card height="400px"> -->
    <v-footer
      :absolute="false"
      :padless="true"
    >
      <v-card
        flat
        tile
        width="100%"
        class="text-center"
      >
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4"
            icon
          >
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text >
          {{ new Date().getFullYear() }} — <strong>Pizzapp</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  <!-- </v-card> -->
</template>
<script>
export default {
    data: () => ({
      icons: [
        'fab fa-facebook-f',
        'fab fa-instagram',
        'fab fa-twitter',
        'fa-map-marker-alt',
      ],
    }),
}
</script>