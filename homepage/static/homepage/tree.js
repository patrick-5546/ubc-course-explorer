var SHOW_CLASS = 'show'
var treeElements = document.querySelectorAll('[tree-node]')
var buttonElements = document.querySelectorAll('[button]')
var dropdownElements = document.querySelectorAll('[dropdown]')

buttonElements.forEach(button => {
    button.addEventListener('click', handleClick)
})

function handleClick(e) {
    console.log("click")
    const buttonClicked = e.target
    var buttonIndex
    for (i = 0; i < 999999; i++) {
        if (buttonElements[i] == buttonClicked) {
            buttonIndex = i
            break
        }
    }
    if (dropdownElements[i].classList.contains(SHOW_CLASS)) {
        dropdownElements[i].classList.remove(SHOW_CLASS)
    } else {
    dropdownElements[i].classList.add(SHOW_CLASS)
    }
}