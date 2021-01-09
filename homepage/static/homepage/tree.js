var SHOW_CLASS = 'show'
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
    buttonElements[i].removeEventListener('click', show)
    buttonElements[i].addEventListener('click', hide)
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
    buttonElements[i].removeEventListener('click', hide)
    buttonElements[i].addEventListener('click', show)
}