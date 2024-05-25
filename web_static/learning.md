## `box-sizing`: the new CSS box model
When he `box-sizing` property is used, the padding and border of that element no longer increase its width. As a result, some authours want all elements on all their pages to always work this way. Such authors put the following CSS on their pages.
```css
* {
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}
```

## `position`
```css
{
	position; static;
}
{
        position: relative;
}
{
	position: fixed;
}
{
	position: absolute;
}
```
A fixed element is positioned relative to the viewport, which means it always stays in the same place even if the page is scrolled.

## `viewport`
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

## `float`
`float` is intended for wrapping text around images
```css
img {
  float: right;
  margin: 0 0 1em 1em;
}
```

## `clear`
`clear` is important for controlling the behaviour of floats.
```css
.box {
  float: left;
  width: 200px;
  height: 100px;
  margin: 1em;
}
.after-box {
  clear: left;
}
```
Using clear we have now moved this section down below the floated div. You use the value left to clear elements floated to the left. You can also clear right and both.

## percent width
Percent is the measurement unit relative to the containing block.
```css
article img {
  float: right;
  width: 50%;
}

nav {
  float: left;
  width: 25%;
}
section {
  margin-left: 25%;
}
```

## media queries
"Responsive Design" is the strategy of making a site that "responds" to the browser and device that it is being shouwn on... by lookin awesome no matter what. Media queries are the most powerful tool for doing this.
```css
@media (min-width:600px) {
  nav {
    float: left;
    width: 25%;
  }
  section {
    margin-left: 25%;
  }
}
@media (max-width:599px) {
  nav li {
    display: inline;
  }
}
```
There is a whole lot more you can detect than min-width and max-width: check out the MDN documentation to learn more.

## `inline-block`
This is used to create a grid of bexes that fills the browser width and wraps nicely. 

The hard way(using float):
```css
.box {
  float: left;
  width: 200px;
  height: 100px;
  margin: 1em;
}
.after-box {
  clear: left;
}
```
The easy way (using inline-block)
.box2 {
  display: inline-block;
  width: 200px;
  height: 100px;
  margin: 1em;
}
The `inline-block` property value can also be used for layouts.
```
nav {
  display: inline-block;
  vertical-align: top;
  width: 25%;
}
.column {
  display: inline-block;
  vertical-align: top;
  width: 75%;
}
```


## `column`
This is a new set of CSS properties that let you easily make multi-column text.
```css
.three-column {
  padding: 1em;
  -moz-column-count: 3;
  -moz-column-gap: 1em;
  -webkit-column-count: 3;
  -webkit-column-gap: 1em;
  column-count: 3;
  column-gap: 1em;
}
```
CSS columns are very new, so you need to use the prefixes, and it won't work through IE9 or in Opera Mini.

## `flexbox`
Simple Layout using Flexbox
```css
.container {
  display: -webkit-flex;
  display: flex;
}
nav {
  width: 200px;
}
.flex-column {
  -webkit-flex: 1;
          flex: 1;
}
```

## Frameworks
A list of CSS frameworks
- blueprint
- unsemantic
- bluetrip
- bootstrap
- susy
- Foundation
- kube
- groundworkCSS
- semantic UI
- pure.css
