<template>
  <v-data-table
    dense
    :headers="headers"
    :items="teams"
    item-key="name"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
  export default {
    // dummy data for now
    data: () => ({
			headers: [
        {
          text: 'Team Name',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Shots: #', value: 'shots' },
        { text: 'Table Hits: #', value: 'table_hits' },
        { text: 'Points: #', value: 'points' },
        { text: 'Clinks: #', value: 'clinks' },
        { text: 'Dunks: #', value: 'dunks' },
				{ text: 'P. Points: #', value: 'p_points' },
				{ text: 'Catches: #', value: 'catches' },
				{ text: 'Drops: #', value: 'drops' },
				{ text: 'Table Hit %: #', value: 'table_hit_p' },
				{ text: 'PP %: #', value: 'p_point_p' },
      ],
      teams: [
        {
          name: 'Team 1',
          shots: 163,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 2',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 3',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 4',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 5',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 6',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 7',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 8',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
      ],
    }),
  }
</script>

