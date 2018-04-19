
# customizing bulma following those steps :

cf : [link](https://medium.com/@mlars84/customizing-bulmas-sass-variables-725a9588cdd9)  
also : 
cf : [link](https://bulma.io/documentation/overview/customize/)
cf : [link](https://bulma.io/documentation/overview/variables/)

#### setup sass for bulma
- `$ mkdir bulma-custom && cd bulma-custom`
- `$ mkdir public public/styles public/vendors`

- `$ yarn init`
- `$ yarn add bulma font-awesome`
or : 
- `$ yarn upgrade bulma`

#### create the scss file overriding default bulma scss
- `$ touch public/index.html public/styles/bulma-custom.scss`
- customize import and vars


#### create custom css file with sass / from within bulma-custom folder
- `$ sass public/styles/bulma-custom.scss public/styles/bulma-custom.css`

or 
- `$ sass public/styles/bulma-custom.scss ../cis/app/static/css/bulma-custom.css`

