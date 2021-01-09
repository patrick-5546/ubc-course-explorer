var SHOW_CLASS = 'show'
var CLICKED_CLASS = 'clicked'
var treeElements = document.querySelectorAll('[tree-node]')
var buttonElements = document.querySelectorAll('[button]')
var dropdownElements = document.querySelectorAll('[dropdown]')

buttonElements.forEach(button => {
    button.addEventListener('click', show)
})

function show(e) {
    console.log("click")
    const buttonClicked = e.target
    var buttonIndex
    for (i = 0; i < 999999; i++) {
        if (buttonElements[i] == buttonClicked) {
            buttonIndex = i
            break
        }
    }
    dropdownElements[i].classList.add(SHOW_CLASS)
    buttonClicked.classList.add(CLICKED_CLASS)
    buttonClicked.removeEventListener('click', show)
    buttonClicked.addEventListener('click', hide)
    buttonClicked.innerText = '▲'
}

function hide(e) {
    console.log("click")
    const buttonClicked = e.target
    var buttonIndex
    for (i = 0; i < 999999; i++) {
        if (buttonElements[i] == buttonClicked) {
            buttonIndex = i
            break
        }
    }
    dropdownElements[i].classList.remove(SHOW_CLASS)
    buttonClicked.classList.remove(CLICKED_CLASS)
    buttonClicked.removeEventListener('click', hide)
    buttonClicked.addEventListener('click', show)
    buttonClicked.innerText = '▼'
}