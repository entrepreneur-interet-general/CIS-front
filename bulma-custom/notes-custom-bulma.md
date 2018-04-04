
# customizing bulma following those steps :
cf : https://medium.com/@mlars84/customizing-bulmas-sass-variables-725a9588cdd9 


#### setup sass for bulma
- `$ mkdir bulma-custom && cd bulma-custom`
- `$ mkdir public public/styles public/vendors`
- `$ yarn init`
- `$ yarn add bulma font-awesome`

#### create the scss file overriding default bulma scss
- `$ touch public/index.html public/styles/bulma-custom.scss`
- customize import and vars
 

#### create custom css file with sass
- `$ sass public/styles/bulma-custom.scss public/styles/bulma-custom.css`

