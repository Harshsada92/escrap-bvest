let card_list = document.querySelector(".card-list");
let children = card_list.children;
console.log(card_list);
let children_length = children.length;
let rev = Array.from(Array(children_length).keys());
rev = rev.reverse();
let prevMatch = false;
function handleResize() {
  console.clear();
  const eve1 = window.matchMedia("(max-width: 700px)");
  const eve2 = window.matchMedia("");
  if (prevMatch === false && eve1.matches) {
    prevMatch = true;
    for (let i = 0; i < children_length; i++) {
      for (let j = 0; j < children_length; j++) {
        if (i == rev[j]) {
          card_list.appendChild(children[j]);
          break;
        }
      }
    }
  } else if (!eve1.matches && prevMatch === true) {
    prevMatch = false;
    for (let i = 0; i < children_length; i++) {
      for (let j = 0; j < children_length; j++) {
        if (i == rev[j]) {
          card_list.appendChild(children[j]);
          break;
        }
      }
    }
  }
  // console.log(mQuery.matches);
  // console.log(window.innerHeight);
  // console.log(window.innerWidth);
}
window.onresize = handleResize;
