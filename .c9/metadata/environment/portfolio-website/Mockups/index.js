{"filter":false,"title":"index.js","tooltip":"/portfolio-website/Mockups/index.js","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":39,"column":5},"action":"insert","lines":["anime.timeline({loop: true})","  .add({","    targets: '.ml5 .line',","    opacity: [0.5,1],","    scaleX: [0, 1],","    easing: \"easeInOutExpo\",","    duration: 700","  }).add({","    targets: '.ml5 .line',","    duration: 600,","    easing: \"easeOutExpo\",","    translateY: (el, i) => (-0.625 + 0.625*2*i) + \"em\"","  }).add({","    targets: '.ml5 .ampersand',","    opacity: [0,1],","    scaleY: [0.5, 1],","    easing: \"easeOutExpo\",","    duration: 600,","    offset: '-=600'","  }).add({","    targets: '.ml5 .letters-left',","    opacity: [0,1],","    translateX: [\"0.5em\", 0],","    easing: \"easeOutExpo\",","    duration: 600,","    offset: '-=300'","  }).add({","    targets: '.ml5 .letters-right',","    opacity: [0,1],","    translateX: [\"-0.5em\", 0],","    easing: \"easeOutExpo\",","    duration: 600,","    offset: '-=600'","  }).add({","    targets: '.ml5',","    opacity: 0,","    duration: 1000,","    easing: \"easeOutExpo\",","    delay: 1000","  });"],"id":1}]]},"ace":{"folds":[],"scrolltop":87,"scrollleft":0,"selection":{"start":{"row":39,"column":5},"end":{"row":39,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583816396709,"hash":"fc87fe9dd0ce0133d4473e16b924a2484aaada43"}