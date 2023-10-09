let ele = document.getElementById("count-el")
let saveEl = document.getElementById("save-el")
let count = 0
function increment() {
    count += 1
    ele.textContent = count
}
function save() {
    let countStr = count + " - "
    saveEl.textContent += countStr
    ele.textContent = 0
    count = 0
}