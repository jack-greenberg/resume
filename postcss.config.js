module.exports = {    
  plugins: [
    require('postcss-import')({
      path: ["assets/css"],
    }),         
    require('tailwindcss')('./tailwind.config.js'),       
    require('autoprefixer')({
      grid: true,
      overrideBrowserslist: ['>1%']
    }),    
  ]
}
