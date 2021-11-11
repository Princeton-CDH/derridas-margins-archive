function deactivate(el) { el.setAttribute('disabled', 'disabled') }


// OPTION 1: Allows for drop downs, you just can't click the inside checkboxes.

document.addEventListener("DOMContentLoaded", function(event) {
  var filter_section = document.querySelectorAll('.filter__section')
  filter_section.forEach(section => {
    if (section.classList.contains("filter__section--toggles")) {
      section.querySelectorAll('input').forEach(deactivate);  
    }
    section.querySelectorAll('fieldset').forEach(deactivate);
  })
});

/*
// OPTION 2: Is very clear with deactivation, but hard to read. No drop downs.


document.addEventListener("DOMContentLoaded", function(event) {
  var filter_section = document.querySelectorAll('.filter__section')
  filter_section.forEach(section => {
    section.querySelectorAll('input').forEach(deactivate);
    section.querySelectorAll('fieldset').forEach(deactivate);
  })
});
*/


// DISABLE SEARCH BUTTON

document.addEventListener("DOMContentLoaded", function(event) {
  document.getElementsByClassName('header__search-button')[0].setAttribute('data-action', '')
});
