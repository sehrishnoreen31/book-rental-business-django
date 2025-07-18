module.exports = {
  darkMode: 'class',   // Use class strategy (required for toggle)
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    './src/**/*.{html,js}',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
};
